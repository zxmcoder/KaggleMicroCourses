import pandas as pd
from sklearn.tree import DecisionTreeRegressor

test_data=pd.read_csv('D:/PanDownload/data_format2/train_format2.csv')
print("Making predictions for the following 5:")
print(test_data.head())
# print(test_data.describe())
# print(test_data.columns)
# test_data=test_data.dropna(axis=0)
y=test_data.label
test_data_features=['age_range', 'gender']
X=test_data[test_data_features]
# print(X.describe())
# print(X.head())
test_model=DecisionTreeRegressor(random_state=1)
test_model.fit(X,y)
# print(X.head())
print("The predictions are")
print(test_model.predict(X.head()))
