'''
Pattern recognition cs669

lab 1 

Group10

'''
import numpy as np
import matplotlib.pyplot as plt         # for plotting

#local file

#print matrix.confusion_matrix[0]

def parameter(mean,c1) :

	x1=np.zeros(1000)
	y1=np.zeros(1000)
	x1_sum=0.0;y1_sum=0.0;xy_sum=0.0;
	x1_square_sum=0.0;y1_square_sum=0.0
	cov_matrix=np.zeros((2,2))
	#c1=raw_input("enter file name \n")
	file1= open(c1,"r")                # taking input from file
	i=0;
	for line in file1:
		a=line.split()
		x1[i]= float(a[0])
		y1[i]= float(a[1])

		x1_sum =x1_sum + x1[i]	
		y1_sum = y1_sum + y1[i]
		xy_sum += x1_sum*y1_sum
		x1_square_sum += x1_sum*x1_sum
		y1_square_sum += y1_sum*y1_sum
		#print arr[i]
		i=i+1
		if i > 374 :
		   break;   
	file1.close()	
	mean_x1= x1_sum/375
	mean_y1=y1_sum/375
	cov_xx=x1_square_sum/375 - mean_x1*mean_x1
	cov_yy=y1_square_sum/375 - mean_y1*mean_y1
	cov_xy=(xy_sum)/375 - mean_x1*mean_y1
	cov_yx=cov_xy
	cov_matrix[0][0]=cov_xx
	cov_matrix[0][1]=cov_xy
	cov_matrix[1][0]=cov_yx
	cov_matrix[1][1]=cov_yy 
	return(cov_matrix)   



cov_matrix1=np.zeros((2,2))
mean1=np.zeros(2)
c1=raw_input("enter file name \n")
cov_matrix1=parameter(mean1,c1)

for i in range(2):
	for j in range(2):
		print inv_cov_matrix[i][j]

for	i in range(2):
    	



'''
cov_matrix2=np.zeros((2,2))
cov_matrix3=np.zeros((2,2))
cov_matrix=np.zeros((2,2))
inv_cov_matrix=np.zeros((2,2))
cov_matrix1=parameter()
cov_matrix2=parameter()
cov_matrix3=parameter()

for i in range(2):
	for j in range(2):
		if (i+j) %2==0:
			cov_matrix[i][j]=(cov_matrix1[i][j]+cov_matrix2[i][j]+cov_matrix3[i][j])/3
		else:
		    cov_matrix[i][j]=0;	


inv_cov_matrix=np.linalg.inv(cov_matrix)

for i in range(2):
	for j in range(2):
		print inv_cov_matrix[i][j]

#when the covarinace matrix is duagonal and same for all the class
'''
'''
c1=raw_input("enter file name \n")
c2=raw_input("enter file name \n")
c3=raw_input("enter file name \n")

confusion_matrix=np.zeros((3,3))

file1=open(c1,"r")
i=0;
for line in file1:
	a=line.split()
	i++;
	if(i>375):



'''
