import sklearn.ensemble.GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd 

seed = 7 
test_size = 0.3

data = pd.read_csv("C:\\Users\\Priyanka.chandran\\Documents\\Datasets\\German credit\\german_credit_data.csv")
print(data.head(10))