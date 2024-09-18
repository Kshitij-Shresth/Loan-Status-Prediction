#encoding
data.replace({'Loan_Status': {'Y': 1, 'N': 0}}, inplace=True)
data.replace({'Dependents': {'3+': 4}}, inplace=True)
