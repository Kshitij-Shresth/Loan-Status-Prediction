#encoding
data.replace({'Loan_Status': {'Y': 1, 'N': 0}}, inplace=True)
data.replace({'Dependents': {'3+': 4}}, inplace=True)
data.replace({'Married': {'Yes': 1, 'No': 0}}, inplace=True)
data.replace({'Gender': {'Male': 1, 'Female': 0}}, inplace=True)
data.replace({'Education': {'Graduate': 1, 'Not Graduate': 0}}, inplace=True)
data.replace({'Self_Employed': {'No': 0, 'Yes': 1}}, inplace=True)
data.replace({'Property_Area': {'Urban': 2, 'Rural': 0, 'Semiurban':1}}, inplace=True)
