from app import model_pred

new_data = {'Credit_line_outstanding': 5,
            'Loan_amt_outstanding': 1958.92,
            'Total_debt_outstanding': 8228.75,
            'Income': 26648.71,
            'Years_employed': 2,
            'Fico_score': 572,
            }


def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1, "incorrect prediction"
