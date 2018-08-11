import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib 
import pdb
import nltk
from sklearn.tree import export_graphviz
import os
 
# File Paths
INPUT_PATH = "datainal.csv"
OUTPUT_PATH = "final/final_test.csv"
 

 
def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier(n_estimators=1000)
    clf.fit(features, target)
    joblib.dump(clf, 'trained_model.pkl') 
    return clf
 
 
def dataset_statistics(dataset):
    """
    Basic statistics of the dataset
    :param dataset: Pandas dataframe
    :return: None, print the basic statistics of the dataset
    """
    print(dataset.describe())
 
 
def main():
    """
    Main function
    :return:
    """
    #nltk.download()
    # Load the csv file into pandas dataframe
    #data_file_to_csv()
    dataset = pd.read_csv(OUTPUT_PATH)
    # Get basic statistics of the loaded dataset
    dataset_statistics(dataset)
    test_x=dataset.iloc[:, :342]
    #train_y=dataset.iloc[:, 342: ]
    # Filter missing values
    #train_x, test_x, train_y, test_y = split_dataset(datas, 0.7, HEADERS[1:-1], HEADERS[-1])
    #train_x=float(train_x)
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3) 
     #Train and Test dataset size details
    print ("Train_x Shape :: ", train_x.shape)
    print ("Train_y Shape :: ", train_y.shape)
    print ("Test_x Shape :: ", test_x.shape)
    print ("Test_y Shape :: ", test_y.shape)
 
    # Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y.values.ravel())
    joblib.dump(trained_model,'trained_model.pkl')
    trained_model=joblib.load('trained_model.pkl')
    print ("Trained model :: ", trained_model)
    predictions = trained_model.predict(test_x)
    print(predictions)
    #test_matrix_y=test_y.as_matrix
    #prediction_matrix=predictions.as_matrix
   # i=0
   # for tree_in_forest in trained_model.estimators_:
        #if i<1:
            #export_graphviz(tree_in_forest,feature_names=X.columns,filled=True,rounded=True)
            #os.system('dot -Tpng tree.dot -o tree.png')
            #i+=1
   # print("AUC-ROC",roc_auc_score(y,trained_model.oob_prediction))
    print ("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print ("Test Accuracy  :: ", accuracy_score(test_y, predictions))
    print (" Confusion matrix \n", confusion_matrix(test_y, predictions))
 
 
if __name__ == "__main__":
    main()