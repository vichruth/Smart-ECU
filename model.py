import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from micromlgen import port

# load dataset
normal_data = pd.read_csv('C:/Users/vichr/OneDrive/Documents/GitHub/Smart-ECU/normal.csv')
anomaly_data = pd.read_csv('C:/Users/vichr/OneDrive/Documents/GitHub/Smart-ECU/anomaly.csv')
data = pd.concat([normal_data,anomaly_data])
X = data[['rpm']]
y = data['label']

# split  dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

# export model to C++ code
c_code = port(model)

# save the model
with open('model.h', 'w') as f:
    f.write(c_code)

print("Model exported to model.h")

