# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:30:43 2021

@author: ASUS
"""

import pandas
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

#baca csv
d = pandas.read_csv("phishing.csv", sep = ',')

#acak data csv
d = d.sample(frac=1)

#membagi kolom atribute dan label dalam csv    
d_train = d[:5250]
d_test = d[5250:]

d_train_att = d_train.drop(['class'], axis=1)
d_train_pass = d_train['class']

d_test_att = d_test.drop(['class'], axis=1)
d_test_pass = d_test['class']

d_att = d.drop(['class'], axis=1)
d_pass = d['class']

gnb = modelnb = GaussianNB()

# membuat model trainning
gnb.fit(d_train_att, d_train_pass)

# memprediksi data test atribute dari model prediksi
Prediksi = gnb.predict(d_test_att) 

# akurasi prediksi yang dijalankan menggunakan gnb
Akurasi = gnb.score(d_test_att, d_test_pass)

# memprediksi probabilitas
Prediksi_Probabilitas = gnb.predict_proba(d_test_att)

# visualisasi hasil prediksi menggunakan convusion matriks
pred_pass = gnb.predict(d_test_att)
cm = confusion_matrix(d_test_pass, pred_pass)