import numpy as np
import math

def find_class_case_1(inv_cov_matrix,mean1,mean2,mean3,x) :
	g1=0.0;g2=0.0;g3=0.0;
	arr=np.zeros(3)
	'''
	det=np.linalg.det(inv_cov_matrix)
	sigma=inv_cov_matrix[0][0]
	g1=((-1)/2.00)*(((x[0]-mean1[0])*(x[0]-mean1[0]))+((x[1]-mean1[1])*(x[1]-mean1[1]))) -(2.00/2)*math.log(2*3.14)-(1.00/2)*(math.log(det))+(1.00/3)

	g2=((-1)/2.00)*(((x[0]-mean2[0])*(x[0]-mean2[0]))+((x[1]-mean2[1])*(x[1]-mean2[1]))) -(2.00/2)*math.log(2*3.14)-(1.00/2)*(math.log(det))+(1.00/3)

	g3=((-1)/2.00)*(((x[0]-mean3[0])*(x[0]-mean3[0]))+((x[1]-mean3[1])*(x[1]-mean3[1]))) -(2.00/2)*math.log(2*3.14)-(1.00/2)*(math.log(det))+(1.00/3)
    '''
	_x1=np.zeros(2);
	_x2=np.zeros(2);
	_x3=np.zeros(2);
	_y1=np.zeros(2);
	_y2=np.zeros(2);
	_y3=np.zeros(2);

	_x1[0]=x[0]-mean1[0]
	_x1[1]=x[1]-mean1[1]

	_x2[0]=x[0]-mean2[0]
	_x2[1]=x[1]-mean2[1]

	_x3[0]=x[0]-mean3[0]
	_x3[1]=x[1]-mean3[1]

	_y1=_x1.transpose()
	_y2=_x2.transpose()
	_y3=_x3.transpose()

	_x1=np.matmul(_x1,inv_cov_matrix)
	_x2=np.matmul(_x2,inv_cov_matrix)
	_x3=np.matmul(_x3,inv_cov_matrix)

	g1=(-0.5)*np.matmul(_x1,_y1)
	g2=(-0.5)*np.matmul(_x2,_y2)
	g3=(-0.5)*np.matmul(_x3,_y3)    
	arr[0]=g1
	arr[1]=g2
	arr[2]=g3
	return(np.argmax(arr))

def find_class_case_2(inv_cov_matrix,mean1,mean2,mean3,x) :
	g1=0.0;g2=0.0;g3=0.0;
	arr=np.zeros(3)
	_x1=np.zeros(2);
	_x2=np.zeros(2);
	_x3=np.zeros(2);
	_y1=np.zeros(2);
	_y2=np.zeros(2);
	_y3=np.zeros(2);

	_x1[0]=x[0]-mean1[0]
	_x1[1]=x[1]-mean1[1]

	_x2[0]=x[0]-mean2[0]
	_x2[1]=x[1]-mean2[1]

	_x3[0]=x[0]-mean3[0]
	_x3[1]=x[1]-mean3[1]

	_y1=_x1.transpose()
	_y2=_x2.transpose()
	_y3=_x3.transpose()

	_x1=np.matmul(_x1,inv_cov_matrix)
	_x2=np.matmul(_x2,inv_cov_matrix)
	_x3=np.matmul(_x3,inv_cov_matrix)

	g1=(-0.5)*np.matmul(_x1,_y1)
	g2=(-0.5)*np.matmul(_x2,_y2)
	g3=(-0.5)*np.matmul(_x3,_y3)

	arr[0]=g1
	arr[1]=g2
	arr[2]=g3
	return(np.argmax(arr))


def find_class_case_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x) :

	g1=0.0;g2=0.0;g3=0.0;
	arr=np.zeros(3)
	_x1=np.zeros(2);
	_x2=np.zeros(2);
	_x3=np.zeros(2);
	_y1=np.zeros(2);
	_y2=np.zeros(2);
	_y3=np.zeros(2);

	_x1[0]=x[0]-mean1[0]
	_x1[1]=x[1]-mean1[1]

	_x2[0]=x[0]-mean2[0]
	_x2[1]=x[1]-mean2[1]

	_x3[0]=x[0]-mean3[0]
	_x3[1]=x[1]-mean3[1]

	_y1=_x1.transpose()
	_y2=_x2.transpose()
	_y3=_x3.transpose()

	_x1=np.matmul(_x1,inv_cov_matrix1)
	_x2=np.matmul(_x2,inv_cov_matrix2)
	_x3=np.matmul(_x3,inv_cov_matrix3)
	g1=(-0.5)*np.matmul(_x1,_y1)-(0.5)*math.log(np.linalg.det(np.linalg.inv(inv_cov_matrix1)))
	g2=(-0.5)*np.matmul(_x2,_y2)-(0.5)*math.log(np.linalg.det(np.linalg.inv(inv_cov_matrix2)))
	g3=(-0.5)*np.matmul(_x3,_y3)-(0.5)*math.log(np.linalg.det(np.linalg.inv(inv_cov_matrix3)))

	arr[0]=g1
	arr[1]=g2
	arr[2]=g3
	return(np.argmax(arr))


