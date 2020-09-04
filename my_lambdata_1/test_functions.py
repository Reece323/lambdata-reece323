#coming back to work on

from my_lambdata_1.my_utilities import train_validation_test_split
from my_lambdata_1.my_utilities import MyDataSplitter

# #numeric
# numeric_features = train_features.select_dtypes(include='number').columns.tolist()

# #series with cardinality of nonnumeric features
# cardinality = train_features.select_dtypes(exclude='number').nunique()

# #categorical features with cardinality <= 50
# categorical_features = cardinality[cardinality <= 110].index.tolist()

# #combining lists
# features = numeric_features + categorical_features