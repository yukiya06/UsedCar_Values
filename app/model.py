import pdb
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

import pickle
import psycopg2


# connect DB, create df
conn = psycopg2.connect(
    host="**.com",
    database="**",
    user="**",
    password="**")

cur = conn.cursor()
cur.execute('SELECT * FROM used_cars;')
conn.commit()
tmp = cur.fetchall()

col_names = []
for elt in cur.description:
    col_names.append(elt[0])

cur.close()
conn.close()

df = pd.DataFrame(tmp, columns=col_names)

# df
X = df.drop(['price','vin','state', 'title_status',	'paint_color'], axis=1)
y = np.log1p(df['price'])

# preprocessing
trans_all = Pipeline([("encoder", OrdinalEncoder(cols=['model', 'manufacturer', 'fuel', 'cylinders',
                                                       'transmission', 'type', 'drive'])),                                             
                    # ("scaler", RobustScaler()),
                      ("imputer", SimpleImputer())])
scaled = trans_all.fit_transform(X)
X_enc = pd.DataFrame(scaled, index=X.index, columns=X.columns)

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X_enc, y, random_state=66, train_size=0.7, test_size=0.3)

# Instantiate the model
model= LinearRegression()

# Model fit
model.fit(X_train, y_train)
y_pred = model.predict(X_train)

# Make pickle file of model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(trans_all.named_steps['encoder'], open("encoder.pkl", "wb"))
model_c_name = X.columns
pickle.dump(model_c_name, open("columns_name.pkl", "wb"))
