#Creating a svm backed model

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.1, stratify = Y, random_state = 7)
#choosing randomm state 7 here because Train mean = 0.688 and Test mean = 0.683

#Training using svm
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train,Y_train)
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

#Approx 80% accuracy
