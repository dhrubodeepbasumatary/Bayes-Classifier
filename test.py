import numpy as np
import math
import find_class


def test_1(c1,c2,c3,inv_cov_matrix,mean1,mean2,mean3) :

	confusion_matrix=np.zeros((3,3))
	x=np.zeros(2)
	file1=open(c1,"r")
	i=0;
	for line in file1:
		a=line.split()
		i=i+1
		if (i>375) :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_1(inv_cov_matrix,mean1,mean2,mean3,x)
			confusion_matrix[0][clas]+=1

	file2=open(c2,"r")
	i=0;
	for line in file2:
		a=line.split()
		i=i+1
		if i>375 :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_1(inv_cov_matrix,mean1,mean2,mean3,x)
			confusion_matrix[1][clas]+=1	

	file3=open(c3,"r")
	i=0;
	for line in file3:
		a=line.split()
		i=i+1
		if i>375 :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_1(inv_cov_matrix,mean1,mean2,mean3,x)
			confusion_matrix[2][clas]+=1


	return(confusion_matrix)



def test_2(c1,c2,c3,inv_cov_matrix,mean1,mean2,mean3) :

	confusion_matrix=np.zeros((3,3))
	x=np.zeros(2)
	file1=open(c1,"r")
	i=0;
	for line in file1:
		a=line.split()
		i=i+1
		if (i>375) :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_2(inv_cov_matrix,mean1,mean2,mean3,x)
			confusion_matrix[0][clas]+=1

	file2=open(c2,"r")
	i=0;
	for line in file2:
		a=line.split()
		i=i+1
		if i>375 :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_2(inv_cov_matrix,mean1,mean2,mean3,x)
			confusion_matrix[1][clas]+=1	

	file3=open(c3,"r")
	i=0;
	for line in file3:
		a=line.split()
		i=i+1
		if i>375 :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_2(inv_cov_matrix,mean1,mean2,mean3,x)
			confusion_matrix[2][clas]+=1


	return(confusion_matrix)


def test_3(c1,c2,c3,inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3) :

	confusion_matrix=np.zeros((3,3))
	x=np.zeros(2)
	file1=open(c1,"r")
	i=0;
	for line in file1:
		a=line.split()
		i=i+1
		if (i>375) :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x)
			confusion_matrix[0][clas]+=1

	file2=open(c2,"r")
	i=0;
	for line in file2:
		a=line.split()
		i=i+1
		if i>375 :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x)
			confusion_matrix[1][clas]+=1	

	file3=open(c3,"r")
	i=0;
	for line in file3:
		a=line.split()
		i=i+1
		if i>375 :
			x[0]= float(a[0])
			x[1]=float(a[1])
			clas=find_class.find_class_case_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x)
			confusion_matrix[2][clas]+=1


	return(confusion_matrix)	


