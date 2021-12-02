from flask import Flask, escape, request , render_template
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
  return render_template("index.html")



@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['Gender']
        married = request.form['married']
        Dependents = request.form['Dependents']
        Education = request.form['Education']
        Self_Employed = request.form['Self_Employed']
        Property_Area = request.form['Property_Area']
    
        
         # gender
        if (Gender == "Male"):
            Male = 1
        else:
            Male = 0
        
        # married
        if(married == "Yes"):
            married_yes = 1
        else:
            married_yes = 0

        # dependents
        if(Dependents =='1'):
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif(Dependents == '2'):
            dependents_1 = 0
            dependents_2 = 1
            dependents_3 = 0
        elif(Dependents == "3+"):
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 1
        else:
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 0  

        # education
        if (Education=="Not Graduate"):
            not_graduate = 1
        else:
            not_graduate = 0

        # employed
        if (Self_Employed == "Yes"):
            employed_yes  = 1
        else:
            employed_yes = 0


        # property area

        if(Property_Area=="Semiurban"):
            semiurban = 1
            urban = 0
        elif(Property_Area=="Urban"):
            semiurban = 0
            urban = 1
        else:
            semiurban = 0
            urban = 0
        

        prediction = model.predict([[ Male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes,semiurban, urban ]])

        # print(prediction)

        if(prediction=="N"):
            prediction  ="No"
        else:
            prediction ="Yes"
        
        return render_template("prediction.html",prediction_text ="loan status is {}".format(prediction))

    else:
        return render_template("prediction.html")

@app.route("/devloper",methods=['GET', 'POST'])
def about():
    return render_template("devloper.html")
        
if __name__ == "__main__":
    app.run(debug=True)
    
