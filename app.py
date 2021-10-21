from flask import *
import pickle

app = Flask(__name__)
model = pickle.load(open("loan_approval_model.pkl", "rb"))

@app.route("/", methods = ["GET"])

def home():
    return render_template("loanapproval.html")

@app.route("/predict", methods = ["GET", "POST"])

def predict():
    if request.method == "POST":
        gender = request.form["Gender"]
        if gender == "Male":
            gender_male = 1
        else:
            gender_male = 0

        married = request.form["Married"]
        if married == "Yes":
            married_yes = 1
        else:
            married_yes = 0

        dependents = float(request.form["Dependents"])
        if dependents == 1:
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif dependents == 2:
            dependents_2 = 1
            dependents_1 = 0
            dependents_3 = 0
        elif dependents == 3:
            dependents_3 = 1
            dependents_1 = 0
            dependents_2 = 0
        else:
            dependents_2 = 0
            dependents_1 = 0
            dependents_3 = 0

        education = request.form["Education"]
        if education == "Not Graduate":
            not_graduate = 1
        else:
            not_graduate = 0

        employment = request.form["Self_Employed"]
        if employment == "Yes":
            employment_yes = 1
        else:
            employment_yes = 0

        income = int(request.form["ApplicantIncome"])

        side_income = int(request.form["CoapplicantIncome"])

        loan_amount = int(request.form["LoanAmount"])

        loan_amount_term = float(request.form["Loan_Amount_Term"])
        if loan_amount_term == 36:
            term_36 = 1
            term_60 = 0
            term_84 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 60:
            term_60 = 1
            term_36 = 0
            term_84 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 84:
            term_84 = 1
            term_60 = 0
            term_36 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 120:
            term_120 = 1
            term_84 = 0
            term_60 = 0
            term_36 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 180:
            term_180 = 1
            term_84 = 0
            term_60 = 0
            term_36 = 0
            term_120 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 240:
            term_240 = 1
            term_84 = 0
            term_60 = 0
            term_36 = 0
            term_120 = 0
            term_180 = 0
            term_300 = 0
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 300:
            term_300 = 1
            term_84 = 0
            term_60 = 0
            term_36 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_360 = 0 
            term_480 = 0
        elif loan_amount_term == 360:
            term_360 = 1
            term_60 = 0
            term_480 = 0
            term_84 = 0
            term_36 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
        elif loan_amount_term == 480:
            term_480 = 1
            term_84 = 0
            term_60 = 0
            term_36 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
        else:
            term_84 = 0
            term_60 = 0
            term_36 = 0
            term_120 = 0
            term_180 = 0
            term_240 = 0 
            term_300 = 0
            term_360 = 0 
            term_480 = 0

        credit_history = float(request.form["Credit_History"])
        if credit_history == 1:
            credit_1 = 1
        else:
            credit_1 = 0


        area = request.form["Property_Area"]
        if area == "Semiurban":
            urban = 0
            semiurban = 1
        elif area == "Urban":
            semiurban = 0
            urban= 1
        else:
            urban = 0
            semiurban = 0

        prediction = model.predict([[gender_male, married_yes, dependents_1, dependents_2, dependents_3, 
        not_graduate, employment_yes, income, side_income, loan_amount, 
        term_84, term_60, term_36, term_120, term_180, term_240, term_300, term_360, term_480,credit_1, semiurban, urban]])

        output = prediction
        if output == 0:
            output = "No"
            return render_template ("loanapproval1.html", prediction_text = "Loan Status: {}".format(output))
        else:
            output = "Yes"
            return render_template ("loanapproval1.html", prediction_text = "Loan Status: {}".format(output))
                
    else:
        return render_template("loanapproval1.html")

if __name__ == "__main__":
    app.run(debug = True)