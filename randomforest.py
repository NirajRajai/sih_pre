import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
 
import pdb
 
# File Paths
INPUT_PATH = "datainal.csv"
OUTPUT_PATH = "finaldataset.csv"
 
# Headers
#HEADERS = ['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','ill','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filthy','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac','tte','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','bed','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','type'] 
def read_data(path):
    """
    Read the data into pandas dataframe
    :param path:
    :return:
    """
    data = pd.read_csv(path)
    return data
 
 
def get_headers(dataset):
    """
    dataset headers
    :param dataset:
    :return:
    """
    return dataset.columns.values
 
 
def add_headers(dataset, headers):
    """
    Add the headers to the dataset
    :param dataset:
    :param headers:
    :return:
    """
    dataset.columns = headers
    return dataset
 
 
def data_file_to_csv():
    """
 
    :return:
    """
 
    # Headers
    headers = ['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','ill','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filthy','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac','tte','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','bed','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','type']    # Load the dataset into Pandas data frame
    dataset = read_data(INPUT_PATH)
    # Add the headers to the loaded dataset
    dataset = add_headers(dataset, headers)
    # Save the loaded dataset into csv format
    dataset.to_csv(OUTPUT_PATH, index=False)
    print("File saved ...!")
 
 
def split_dataset(dataset, train_percentage, feature_headers, target_header):
    """
    Split the dataset with train_percentage
    :param dataset:
    :param train_percentage:
    :param feature_headers:
    :param target_header:
    :return: train_x, test_x, train_y, test_y
    """
 
    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header],
                                                        train_size=train_percentage)
    return train_x, test_x, train_y, test_y
 
 
def handel_missing_values(dataset, missing_values_header, missing_label):
    """
    Filter missing values from the dataset
    :param dataset:
    :param missing_values_header:
    :param missing_label:
    :return:
    """
 
    return dataset[dataset[missing_values_header] != missing_label]
 
 
def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier()
    clf.fit(features, target)
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
    # Load the csv file into pandas dataframe
    #data_file_to_csv()
    dataset = pd.read_csv(OUTPUT_PATH)
    # Get basic statistics of the loaded dataset
    dataset_statistics(dataset)
    X=dataset.iloc[:, :136]
    y=dataset.iloc[:, 136: ]
    # Filter missing values
    #train_x, test_x, train_y, test_y = split_dataset(datas, 0.7, HEADERS[1:-1], HEADERS[-1])
    #train_x=float(train_x)
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.33) 
    # Train and Test dataset size details
    print ("Train_x Shape :: ", train_x.shape)
    print ("Train_y Shape :: ", train_y.shape)
    print ("Test_x Shape :: ", test_x.shape)
    print ("Test_y Shape :: ", test_y.shape)
 
    # Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y.values.ravel())
    print ("Trained model :: ", trained_model)
    predictions = trained_model.predict(test_x)
    #test_matrix_y=test_y.as_matrix
    #prediction_matrix=predictions.as_matrix
    
    
    
 
    print ("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print ("Test Accuracy  :: ", accuracy_score(test_y, predictions))
    print (" Confusion matrix \n", confusion_matrix(test_y, predictions))
 
 
if __name__ == "__main__":
    main()