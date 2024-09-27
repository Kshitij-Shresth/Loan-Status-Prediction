# Loan-Status-Prediction

Support Vector Machine classifier to predict loan approval status using a dataset with various socio-economic and loan-related features. 

## Code Workflow

### Data Preprocessing
Heatmap Generation: The numerical columns in the dataset are selected, and a heatmap is created to visualize the correlation between the features using seaborn.
```
numeric_data = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
```
Encoding: Categorical features are encoded into numerical values for use in machine learning

```Loan_Status```: Y (1), N (0)

```Dependents```: 3+ (4)

```Married```: Yes (1), No (0)

```Gender```: Male (1), Female (0)

```Education```: Graduate (1), Not Graduate (0)

```Self_Employed```: Yes (1), No (0)

```Property_Area```: Urban (2), Rural (0), Semiurban (1)

### Data Splitting
The dataset is split into training and test sets using an 90-10 split. Stratified sampling is used to maintain the proportion of labels in both sets. The random seed is set to 7 based on the observed training and test mean values.

```
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=7)
```

![image](https://github.com/user-attachments/assets/49d5286e-12ce-4090-a22d-662d33761ba0)

![image](https://github.com/user-attachments/assets/5cf04f7e-5bd1-420a-b3f3-b8a7df18ec6d)

![image](https://github.com/user-attachments/assets/bc6ffe57-7ade-415a-ae49-2b28e785edc7)

![image](https://github.com/user-attachments/assets/dba90b33-a7c2-4962-85af-90bc7050d87b)

![image](https://github.com/user-attachments/assets/9bb1f8d9-2ddb-4b82-8a35-cd9990e4dd0a)
