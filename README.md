# Loan-Status-Prediction

The pipeline includes preprocessing steps for categorical feature encoding, generating a correlation heatmap for feature interaction analysis, and training a linear SVM to assess the likelihood of loan approval (binary classification). In a market context, this project mimics the decision-making process used by financial institutions for loan risk assessment. By encoding categorical variables such as employment status, property area, and education level, the model transforms qualitative data into quantitative insights. The SVM algorithm is particularly suitable due to its effectiveness in high-dimensional spaces, making it a strong candidate for binary classification problems in finance where margins between approved and denied loans may be subtle.

This framework serves as a prototype for building scalable loan approval models that financial institutions can use to automate risk evaluation, improve accuracy in decision-making, and minimize default rates.

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
### Model Training
A Support Vector Classifier (SVC) with a linear kernel is trained on the dataset.

```
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)
```
### Model Evaluation
After training the model, predictions are made on the training set. The accuracy score is calculated, which achieves approximately 80% accuracy.

```
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
```
![image](https://github.com/user-attachments/assets/49d5286e-12ce-4090-a22d-662d33761ba0)

![image](https://github.com/user-attachments/assets/5cf04f7e-5bd1-420a-b3f3-b8a7df18ec6d)

![image](https://github.com/user-attachments/assets/bc6ffe57-7ade-415a-ae49-2b28e785edc7)

![image](https://github.com/user-attachments/assets/dba90b33-a7c2-4962-85af-90bc7050d87b)

![image](https://github.com/user-attachments/assets/9bb1f8d9-2ddb-4b82-8a35-cd9990e4dd0a)
