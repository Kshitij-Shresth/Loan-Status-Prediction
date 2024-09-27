# Loan-Status-Prediction

Support Vector Machine classifier to predict loan approval status using a dataset with various socio-economic and loan-related features. 

## Code Workflow

### Data Preprocessing
Heatmap Generation: The numerical columns in the dataset are selected, and a heatmap is created to visualize the correlation between the features using seaborn.
```
numeric_data = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
```

![image](https://github.com/user-attachments/assets/49d5286e-12ce-4090-a22d-662d33761ba0)

![image](https://github.com/user-attachments/assets/5cf04f7e-5bd1-420a-b3f3-b8a7df18ec6d)

![image](https://github.com/user-attachments/assets/bc6ffe57-7ade-415a-ae49-2b28e785edc7)

![image](https://github.com/user-attachments/assets/dba90b33-a7c2-4962-85af-90bc7050d87b)

![image](https://github.com/user-attachments/assets/9bb1f8d9-2ddb-4b82-8a35-cd9990e4dd0a)
