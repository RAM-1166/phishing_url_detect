import pandas as pd
legitimate_urls = pd.read_csv(r"Phishing-URL-Detection\Phishing-URL-detection\extracted_csv_files\legitimate-urls.csv")
phishing_urls = pd.read_csv(r"Phishing-URL-Detection\Phishing-URL-detection\extracted_csv_files\phishing-urls.csv")
legitimate_urls.head(10)
phishing_urls.head(10)
urls = legitimate_urls.append(phishing_urls)
urls.head(5)
urls.columns


# Removing Unnecessary columns

urls = urls.drop(urls.columns[[0,3,5]],axis=1)
# Since we merged two dataframes top 1000 rows will have legitimate urls and bottom 1000 rows will have phishing urls. So if we split the data now and create a model for it will overfit or underfit so we need to shuffle the rows before splitting the data into training set and test set

# shuffling the rows in the dataset so that when splitting the train and test set are equally distributed
urls = urls.sample(frac=1).reset_index(drop=True)
urls_without_labels = urls.drop('label',axis=1)
urls_without_labels.columns
labels = urls['label']
from sklearn.model_selection import train_test_split
data_train, data_test, labels_train, labels_test = train_test_split(urls_without_labels, labels, test_size=0.30, random_state=100)
print(len(data_train),len(data_test),len(labels_train),len(labels_test))
print(labels_train.value_counts())
print(labels_test.value_counts())

train_0_dist = 711/1410
print(train_0_dist)
train_1_dist = 699/1410
print(train_1_dist)
test_0_dist = 306/605
print(test_0_dist)
test_1_dist = 299/605
print(test_1_dist)
from sklearn.tree import DecisionTreeClassifier
DTmodel = DecisionTreeClassifier(random_state=0)
DTmodel.fit(data_train,labels_train)
pred_label = DTmodel.predict(data_test)
print(pred_label),print(list(labels_test))


# #### creating confusion matrix and checking the accuracy

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labels_test,pred_label)
print(cm)
accuracy_score(labels_test,pred_label)


# ## Random Forest

from sklearn.ensemble import RandomForestClassifier
RFmodel = RandomForestClassifier()
RFmodel.fit(data_train,labels_train)
rf_pred_label = RFmodel.predict(data_test)
print(list(labels_test)),print(list(rf_pred_label))
cm2 = confusion_matrix(labels_test,rf_pred_label)
cm2
accuracy_score(labels_test,rf_pred_label)
imp_rf_model = RandomForestClassifier(n_estimators=100,max_depth=30,max_leaf_nodes=10000)
imp_rf_model.fit(data_train,labels_train)
imp_pred_label = imp_rf_model.predict(data_test)
cm3 = confusion_matrix(labels_test,imp_pred_label)
cm3
accuracy_score(labels_test,imp_pred_label)
