
from my_lambdata_1.my_classes import MyDataSplitter
# from my_lambdata_1.my_classes import train_validation_test_split

df = {'col1': [1, 5, 3, 100, 8], 'col2': [3, 4, 7, 5, 6]}


if __name__ == "__main__":
    dt = MyDataSplitter(df)
        
    X_train, X_val, X_test, y_train, y_val, y_test = dt.train_validation_test_split('col1','col2',random_state=42)

    print(X_val)
    print(y_val)