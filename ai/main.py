# Imports
import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

# Docs are here:
# http://tiny.cc/c9etez
URL = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets'
dataframe = pd.read_csv(URL)
dataframe.head()

defaults = {
  "pl_hostname": "",
  "pl_letter": "",
  "pl_name": "",
  "pl_discmethod": "",
  "pl_controvflag": 0,
  "pl_pnum": 0,
  "pl_orbper": 0,
  "pl_orbpererr1": 0,
  "pl_orbpererr2": 0,
  "pl_orbperlim": 0,
  "pl_orbpern": 0,
  "pl_orbsmax": 0,
  "pl_orbsmaxerr1": 0,
  "pl_orbsmaxerr2": 0,
  "pl_orbsmaxlim": 0,
  "pl_orbsmaxn": 0,
  "pl_orbeccen": 0,
  "pl_orbeccenerr1": 0,
  "pl_orbeccenerr2": 0,
  "pl_orbeccenlim": 0,
  "pl_orbeccenn": 0,
  "pl_orbincl": 0,
  "pl_orbinclerr1": 0,
  "pl_orbinclerr2": 0,
  "pl_orbincllim": 0,
  "pl_orbincln": 0,
  "pl_bmassj": 0,
  "pl_bmassjerr1": 0,
  "pl_bmassjerr2": 0,
  "pl_bmassjlim": 0,
  "pl_bmassn": 0,
  "pl_bmassprov": "",
  "pl_radj": 0,
  "pl_radjerr1": 0,
  "pl_radjerr2": 0,
  "pl_radjlim": 0,
  "pl_radn": 0,
  "pl_dens": 0,
  "pl_denserr1": 0,
  "pl_denserr2": 0,
  "pl_denslim": 0,
  "pl_densn": 0,
  "pl_ttvflag": 0,
  "pl_kepflag": 0,
  "pl_k2flag": 0,
  "ra_str": "",
  "dec_str": "",
  "ra": 0,
  "st_raerr": 0,
  "dec": 0,
  "st_decerr": 0,
  "st_posn": 0,
  "st_dist": 0,
  "st_disterr1": 0,
  "st_disterr2": 0,
  "st_distlim": 0,
  "st_distn": 0,
  "st_optmag": 0,
  "st_optmagerr": 0,
  "st_optmaglim": 0,
  "st_optband": "",
  "gaia_gmag": 0,
  "gaia_gmagerr": 0,
  "gaia_gmaglim": 0,
  "st_teff": 0,
  "st_tefferr1": 0,
  "st_tefferr2": 0,
  "st_tefflim": 0,
  "st_teffn": 0,
  "st_mass": 0,
  "st_masserr1": 0,
  "st_masserr2": 0,
  "st_masslim": 0,
  "st_massn": 0,
  "st_rad": 0,
  "st_raderr1": 0,
  "st_raderr2": 0,
  "st_radlim": 0,
  "st_radn": 0,
  "pl_nnotes": 0,
  "rowupdate": "",
  "pl_facility": "",
  'Kepler-40': '',
  'b': ''
}

# Replace na values with defaults stored in `defaults`
dataframe.fillna(value=defaults, inplace=True)

train, test = train_test_split(dataframe, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)
print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')

def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('pl_orbper')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds


# Define which features we want
feature_columns = []

for header in ['st_mass', 'pl_radj', 'pl_bmassj']:
  feature_columns.append(feature_column.numeric_column(header))

# Create the feature layer
feature_layer = tf.keras.layers.DenseFeatures(feature_columns)

batch_size = 50
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)

model = tf.keras.Sequential([
  feature_layer,
  layers.Dense(128, activation='relu'),
  layers.Dense(128, activation='relu'),
  layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_ds,
          validation_data=val_ds,
          epochs=30)

loss, accuracy = model.evaluate(test_ds)
print("Accuracy", accuracy)