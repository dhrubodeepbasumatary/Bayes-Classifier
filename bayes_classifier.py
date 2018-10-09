import numpy as np
import test
import plot
import math

def case_1(c1,c2,c3,cov_matrix1,cov_matrix2,cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	cov_matrix=np.zeros((2,2))
	inv_cov_matrix=np.zeros((2,2))
	confusion_matrix=np.zeros((3,3))
	for i in range(2):
		for j in range(2):
			if (i+j) %2==0:
				cov_matrix[i][j]=(cov_matrix1[i][j]+cov_matrix2[i][j]+cov_matrix3[i][j])/3;

			else:
			    cov_matrix[i][j]=0;	

	inv_cov_matrix=np.linalg.inv(cov_matrix)
	confusion_matrix=test.test_1(c1,c2,c3,inv_cov_matrix,mean1,mean2,mean3)

	plot.plot_1(inv_cov_matrix,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3)
	return(confusion_matrix)

def case_2(c1,c2,c3,cov_matrix1,cov_matrix2,cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	cov_matrix=np.zeros((2,2))
	inv_cov_matrix=np.zeros((2,2))
	confusion_matrix=np.zeros((3,3))
	for i in range(2):
		for j in range(2):
			cov_matrix[i][j]=(cov_matrix1[i][j]+cov_matrix2[i][j]+cov_matrix3[i][j])/3;


	inv_cov_matrix=np.linalg.inv(cov_matrix)
	confusion_matrix=test.test_2(c1,c2,c3,inv_cov_matrix,mean1,mean2,mean3)

	plot.plot_2(inv_cov_matrix,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3)
	return(confusion_matrix)	

def case_3(c1,c2,c3,cov_matrix1,cov_matrix2,cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	cov_matrix=np.zeros((2,2))
	inv_cov_matrix1=np.zeros((2,2))
	inv_cov_matrix2=np.zeros((2,2))
	inv_cov_matrix3=np.zeros((2,2))
	confusion_matrix=np.zeros((3,3))
	for i in range(2):
		for j in range(2):
			if(i+j)%2!=0:
				cov_matrix1[i][j]=0;
				cov_matrix2[i][j]=0;
				cov_matrix3[i][j]=0;


	inv_cov_matrix1=np.linalg.inv(cov_matrix1)
	inv_cov_matrix2=np.linalg.inv(cov_matrix2)
	inv_cov_matrix3=np.linalg.inv(cov_matrix3)
	confusion_matrix=test.test_3(c1,c2,c3,inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3)

	plot.plot_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3)
	return(confusion_matrix)

def case_4(c1,c2,c3,cov_matrix1,cov_matrix2,cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	cov_matrix=np.zeros((2,2))
	inv_cov_matrix1=np.zeros((2,2))
	inv_cov_matrix2=np.zeros((2,2))
	inv_cov_matrix3=np.zeros((2,2))
	confusion_matrix=np.zeros((3,3))

	inv_cov_matrix1=np.linalg.inv(cov_matrix1)
	inv_cov_matrix2=np.linalg.inv(cov_matrix2)
	inv_cov_matrix3=np.linalg.inv(cov_matrix3)
	confusion_matrix=test.test_3(c1,c2,c3,inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3)

	plot.plot_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3)
	return(confusion_matrix)	

