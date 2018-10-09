import numpy as np
import matplotlib.pyplot as plt
import math
import find_class

def plot_1(inv_cov_matrix,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	x=np.zeros(2)
	x11=np.zeros(1000000)
	x22=np.zeros(1000000)
	x33=np.zeros(1000000)
	y11=np.zeros(1000000)
	y22=np.zeros(1000000)
	y33=np.zeros(1000000)
	l1=0
	l2=0
	l3=0
	for i in range(-60,250):
		for j in range(-150,200):
			x[0]=i*0.1
			x[1]=j*0.1
			clas=find_class.find_class_case_1(inv_cov_matrix,mean1,mean2,mean3,x)
			if clas==0:
				x11[l1]=i*0.1
				y11[l1]=j*0.1
				l1=l1+1
			elif clas==1:	
				x22[l2]=i*0.1
				y22[l2]=j*0.1
				l2=l2+1
			elif clas==2:
				x33[l3]=i*0.1
				y33[l3]=j*0.1
				l3=l3+1

	plt.plot(x11,y11,'#DEB887')
	plt.plot(x22,y22,'#53868B')
	plt.plot(x33,y33,'#458B00')

	plt.plot(x1,y1,'ro')
	plt.plot(x2,y2,'bo')
	plt.plot(x3,y3,'go')

	plt.show()


def plot_2(inv_cov_matrix,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	x=np.zeros(2)
	x11=np.zeros(1000000)
	x22=np.zeros(1000000)
	x33=np.zeros(1000000)
	y11=np.zeros(1000000)
	y22=np.zeros(1000000)
	y33=np.zeros(1000000)
	l1=0
	l2=0
	l3=0
	for i in range(-60,250):
		for j in range(-150,200):
			x[0]=i*0.1
			x[1]=j*0.1
			clas=find_class.find_class_case_2(inv_cov_matrix,mean1,mean2,mean3,x)
			if clas==0:
				x11[l1]=i*0.1
				y11[l1]=j*0.1
				l1=l1+1
			elif clas==1:	
				x22[l2]=i*0.1
				y22[l2]=j*0.1
				l2=l2+1
			elif clas==2:
				x33[l3]=i*0.1
				y33[l3]=j*0.1
				l3=l3+1

	plt.plot(x11,y11,'#DEB887')
	plt.plot(x22,y22,'#53868B')
	plt.plot(x33,y33,'#458B00')

	plt.plot(x1,y1,'ro')
	plt.plot(x2,y2,'bo')
	plt.plot(x3,y3,'go')

	plt.show()

def plot_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x1,x2,x3,y1,y2,y3):
    
	x=np.zeros(2)
	x11=np.zeros(1000000)
	x22=np.zeros(1000000)
	x33=np.zeros(1000000)
	y11=np.zeros(1000000)
	y22=np.zeros(1000000)
	y33=np.zeros(1000000)
	l1=0
	l2=0
	l3=0
	for i in range(-60,250):
		for j in range(-150,200):
			x[0]=i*0.1
			x[1]=j*0.1
			clas=find_class.find_class_case_3(inv_cov_matrix1,inv_cov_matrix2,inv_cov_matrix3,mean1,mean2,mean3,x)
			if clas==0:
				x11[l1]=i*0.1
				y11[l1]=j*0.1
				l1=l1+1
			elif clas==1:	
				x22[l2]=i*0.1
				y22[l2]=j*0.1
				l2=l2+1
			elif clas==2:
				x33[l3]=i*0.1
				y33[l3]=j*0.1
				l3=l3+1

	plt.plot(x11,y11,'#DEB887')
	plt.plot(x22,y22,'#53868B')
	plt.plot(x33,y33,'#458B00')

	plt.plot(x1,y1,'ro')
	plt.plot(x2,y2,'bo')
	plt.plot(x3,y3,'go')

	plt.show()

