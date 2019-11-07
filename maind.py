'''
Pattern recognition cs669
Instructor : Dr. Dileep A.D
IIT Mandi

5th sem
lab 1 
Group10

'''
import numpy as np
import matplotlib.pyplot as plt        # for plotting
import math
import find_class
import find_cov_matrix
import test
import plot
import bayes_classifier


confusion_matrix1=np.zeros((3,3))
confusion_matrix2=np.zeros((3,3))
confusion_matrix3=np.zeros((3,3))
confusion_matrix4=np.zeros((3,3))
inv_cov_matrix1=np.zeros((2,2))
inv_cov_matrix2=np.zeros((2,2))
inv_cov_matrix3=np.zeros((2,2))
inv_cov_matrix4=np.zeros((2,2))
cov_matrix=np.zeros((2,2))
cov_matrix1=np.zeros((2,2))
cov_matrix2=np.zeros((2,2))
cov_matrix3=np.zeros((2,2))
mean1=np.zeros(2)
mean2=np.zeros(2)
mean3=np.zeros(2)
x=np.zeros(2)
x1=np.zeros(375)
x2=np.zeros(375)
x3=np.zeros(375)
y1=np.zeros(375)
y2=np.zeros(375)
y3=np.zeros(375)

c1=raw_input("enter file name \n")
c2=raw_input("enter file name \n")
c3=raw_input("enter file name \n")

cov_matrix1=find_cov_matrix.find_cov_matrix(mean1,x1,y1,c1)
cov_matrix2=find_cov_matrix.find_cov_matrix(mean2,x2,y2,c2)
cov_matrix3=find_cov_matrix.find_cov_matrix(mean3,x3,y3,c3)


#case1:when covariance matrix is same diagonal and all the covariances are same


confusion_matrix1=bayes_classifier.case_4(c1,c2,c3,cov_matrix1,cov_matrix2,cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3)


for i in range(3):
	for j in range(3):
		print confusion_matrix1[i][j]





