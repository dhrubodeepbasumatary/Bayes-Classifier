	'''
	Pattern recognition cs669

	lab 1 

	Group10

	'''
	import numpy as np
	import matplotlib.pyplot as plt         # for plotting

	#import matrix  #local file

	#print matrix.confusion_matrix[0]

	arr = np.zeros(1000, dtype='float32,float32')
	x1=np.zeros(1000)
	y1=np.zeros(1000)
	x2=np.zeros(1000)
	y2=np.zeros(1000)
	x3=np.zeros(1000)
	y3=np.zeros(1000)
  
	x1_sum=0.0;  x2_sum=0; x3_sum=0.0

	y1_sum=0.0; y2_sum=0.0;y3_sum=0.0

	c1=raw_input("enter file name \n")


	file1= open(c1,"r")                # taking input from file
	i=0;
	for line in file1:
		a=line.split()
		arr[i]=(a[0],a[1])
		x1[i]= float(a[0])
		y1[i]= float(a[1])

		x1_sum =x1_sum + x1[i]	
		y1_sum = y1_sum + y1[i]
		#print arr[i]
		i=i+1
		if i > 374 :
			break;
	file1.close()	
	mean_x1= x1_sum/375
	mean_y1=y1_sum/375

	x2_sum=0.0
	y2_sum=0.0

	c2=raw_input("enter file name of another class\n")
	file2= open(c2,"r")          #taking input from file
	i=0;
	for line in file2:
		a=line.split()
		x2[i]=float(a[0])
		y2[i]=float(a[1])
		x2_sum = x2_sum + x2[i]
		y2_sum = y2_sum + y2[i]
		i=i+1
		if(i > 375):
			break

	file2.close()

	mean_x2= x2_sum/375
	mean_y2=y2_sum/375

	x3_sum=0.0
	y3_sum=0.0

	c3=raw_input("enter file name of another class\n")
	file3= open(c3,"r")         #taking input from file
	i=0;
	for line in file3:
		a=line.split()
		x3[i]= float(a[0])
		y3[i]= float(a[1])
		x3_sum = x3_sum + x3[i]
		y3_sum +=y3_sum + y3[i]
		i=i+1
		if(i > 374):
			break
	file3.close()

	mean_x3= x3_sum/375
	mean_y3=y3_sum/375




	plt.plot(x1,y1,'ro')
	plt.plot(x2,y2,'go')
	plt.plot(x3,y3,'bo')
	plt.show()
	
