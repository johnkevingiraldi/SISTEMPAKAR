# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:31:27 2021

@author: ASUS
"""

Pengumpulan tugas mengenai materi NaiveBayesClassifier atas nama John Kevin Giraldi (1184049)

#Untuk membaca file csv
d = pandas.read_csv("phishing.csv", sep = ',')

#Proses pengacakan data pada file csv
d = d.sample(frac=1)

#Proses pembagian label dan atribut dalam file csv  
d_train = d[:5250]
d_test = d[5250:]

d_train_att = d_train.drop(['class'], axis=1)
d_train_pass = d_train['class']

d_test_att = d_test.drop(['class'], axis=1)
d_test_pass = d_test['class']

d_att = d.drop(['class'], axis=1)
d_pass = d['class']

gnb = modelnb = GaussianNB()

#Melakukan proses training model
gnb.fit(d_train_att, d_train_pass)

#Melakukan prediksi dengan data test att dari model prediksi
Prediksi = gnb.predict(d_test_att) 

#Melakukan akurasi prediksi yang diproses menggunakan gnd
Akurasi = gnb.score(d_test_att, d_test_pass)

#Langkah untuk memprediksi probabilitas data
Prediksi_Probabilitas = gnb.predict_proba(d_test_att)

#Langkah untuk melakukan gambaran dari hasil prediksi menggunakan convusion matriks
pred_pass = gnb.predict(d_test_att)
cm = confusion_matrix(d_test_pass, pred_pass)