import numpy as np  
import math
#import find_class

def find_cov_matrix(mean1,x1,y1,file) :

	x1_sum=0.0000000;y1_sum=0.000000;xy_sum=0.0000000;
	x1_square_sum=0.000000;y1_square_sum=0.00000000;
	cov_matrix=np.zeros((2,2))
	file1=open(file,"r")                # taking input from file
	i=0;
	for line in file1:
		a=line.split()
		x1[i]= float(a[0])
		y1[i]= float(a[1])

		x1_sum =x1_sum + x1[i]	
		y1_sum = y1_sum + y1[i]
		xy_sum += x1[i]*y1[i]
		x1_square_sum += x1[i]*x1[i]
		y1_square_sum += y1[i]*y1[i]

		i=i+1
		if i > 374 :
		   break;   
	#file1.close()	
	mean_x1=x1_sum/375
	mean_y1=y1_sum/375
	cov_xx=x1_square_sum/375 - mean_x1*mean_x1
	cov_yy=y1_square_sum/375 - mean_y1*mean_y1
	cov_xy=(xy_sum)/375 - mean_x1*mean_y1
	cov_yx=cov_xy
	cov_matrix[0][0]=cov_xx
	cov_matrix[0][1]=cov_xy
	cov_matrix[1][0]=cov_yx
	cov_matrix[1][1]=cov_yy 
	mean1[0]=mean_x1
	mean1[1]=mean_y1
	return(cov_matrix)   
