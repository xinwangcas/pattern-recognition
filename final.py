# !usr/bin/python
# Filename: HW6.py

import re
import os
import string
import math
import numpy as np
from random import randint
from numpy.linalg import inv

f = open('results.txt','a+')

def handlefile(s):
    for i in ['B', 'C', 'D', 'E', 'I', 'J', 'O', 'R', 'U', 'V']:
        s1 = './C-II/%s-%s.txt'%(s, i)
        s2 = './C-II/%s-%s_new.txt'%(s, i)
        
        f1 = file(s1, 'r')
        f2 = open(s2, 'w')
        
        h = 0 
        h_up = 0
        h_down = 0
        w = 0
        w_left = 0
        w_right = 0
        
        while True:
            line1 = f1.readline()
            if(len(line1) == 0):
                break;
            m = line1.split(' ')

            if m[0] == 'C':
                sh = re.findall(r'\d+', m[1])
                h = int(sh[0])
                h_up = int((16-h)/2)
                h_down = 16-h_up-h
		if(h_down < 0):
			h_down = 0
			h = 16
                sw = re.findall(r'\d+', m[2])
                w = int(sw[0])
                w_left = (16-w)/2
                w_right = 16-w_left-w
		if w_right < 0 :
			w_right = 0
			w = 16
                line2 = m[0] + ' w16 h16 ' + m[3];
                f2.write(line2)
            else:
                while (h_up > 0):
                    line2 = ''
                    for i in range (0,16):
                        line2 += '.'
                    line2 += '\n'
                    h_up -= 1
                    f2.write(line2)
                
		if (h_up == 0 and h > 0):
                    line2 = ''
		    if w_left >= 0:
               	    	for i in range (0,w_left):
                	        line2 += '.'
			line2 += line1
			line2 = line2.rstrip('\n')
       			for i in range (0, w_right):
				line2 += '.'
		    else:
		    	t = -w_left
		    	line2 = line1[t:16+t]
			line2 = line2.rstrip('\n')
       			for i in range (0, w_right):
				line2 += '.'
                    line2 += '\n'
		    h -= 1
		    f2.write(line2)
                    
                while (h_up == 0 and h == 0 and h_down > 0 ):
			line2 = ''
			for i in range (0,16):
                            line2 += '.'
                        line2 += '\n'
                        h_down -= 1
                        f2.write(line2)
	f1.close();
	f2.close();
#######################################################################

def CentralMoment(s):

    Mat_11 = []	
    Mat_21 = []
    Mat_12 = []
    Mat_31 = []
    Mat_22 = []
    Mat_13 = []
    Mat_41 = []
    Mat_32 = []
    Mat_23 = []
    Mat_14 = []
    Mat_51 = []
    Mat_42 = []
    Mat_33 = []
    Mat_24 = []
    Mat_15 = []
    Mat_61 = []
    Mat_52 = []
    Mat_43 = []
    Mat_34 = []
    Mat_25 = []

    for i in ['B', 'C', 'D', 'E', 'I', 'J', 'O', 'R', 'U', 'V']:
        s1 = './C-II/%s-%s_new.txt'%(s, i)
        
        f1 = file(s1, 'r')
        
        h = 0 
        w = 0
       
	area = []
	li = []
 
        while True:
            line1 = f1.readline()
            if(len(line1) == 0):
                break;
            m = line1.split(' ')

            if m[0] == 'C':
		li = []
		area.append(li)

	    else:
		li.append(line1[0:len(line1)-1])

	f1.close()
	M_11 = []
	M_21 = []
	M_12 = []
	M_31 = []
	M_22 = []
	M_13 = []
	M_41 = []
	M_32 = []
	M_23 = []
	M_14 = []
	M_51 = []
	M_42 = []
	M_33 = []
	M_24 = []
	M_15 = []
	M_61 = []
	M_52 = []
	M_43 = []
	M_34 = []
	M_25 = []

	Mat_11.append(M_11)
	Mat_21.append(M_21)
	Mat_12.append(M_12)
	Mat_31.append(M_31)
	Mat_22.append(M_22)
	Mat_13.append(M_13)
	Mat_41.append(M_41)
	Mat_32.append(M_32)
	Mat_23.append(M_23)
	Mat_14.append(M_14)
	Mat_51.append(M_51)
	Mat_42.append(M_42)
	Mat_33.append(M_33)
	Mat_24.append(M_24)
	Mat_15.append(M_15)
	Mat_61.append(M_61)
	Mat_52.append(M_52)
	Mat_43.append(M_43)
	Mat_34.append(M_34)
	Mat_25.append(M_25)
	for a in area:
		m_00 = 0.0000
		m_10 = 0.0000
		m_01 = 0.0000
		x_c = 0.0000
		y_c = 0.0000
		l = 0
		w = 0
		I = np.zeros(256).reshape(16,16)
		for l in range(0,16):
			for w in range(0,16):
			    if a[l][w] == 'x':
				m_00 += 1
				m_10 += w+1
				m_01 += l+1
				I[l][w] = 1
		xc = m_10/m_00
		x_c = float("%0.5f" % xc)
		yc = m_01/m_00
		y_c = float("%0.5f" % yc)
		M11 = CalcMoment(x_c, y_c, 1, 1, I)
		M_11.append(M11)
		M21 = CalcMoment(x_c, y_c, 2, 1, I)
		M_21.append(M21)
		M12 = CalcMoment(x_c, y_c, 1, 2, I)
		M_12.append(M12)
		M31 = CalcMoment(x_c, y_c, 3, 1, I)
		M_31.append(M31)
		M22 = CalcMoment(x_c, y_c, 2, 2, I)
		M_22.append(M22)
		M13 = CalcMoment(x_c, y_c, 1, 3, I)
		M_13.append(M13)
		M41 = CalcMoment(x_c, y_c, 4, 1, I)
		M_41.append(M41)
		M32 = CalcMoment(x_c, y_c, 3, 2, I)
		M_32.append(M32)
		M23 = CalcMoment(x_c, y_c, 2, 3, I)
		M_23.append(M23)
		M14 = CalcMoment(x_c, y_c, 1, 4, I)
		M_14.append(M14)
		M51 = CalcMoment(x_c, y_c, 5, 1, I)
		M_51.append(M51)
		M42 = CalcMoment(x_c, y_c, 4, 2, I)
		M_42.append(M42)
		M33 = CalcMoment(x_c, y_c, 3, 3, I)
		M_33.append(M33)
		M24 = CalcMoment(x_c, y_c, 2, 4, I)
		M_24.append(M24)
		M15 = CalcMoment(x_c, y_c, 1, 5, I)
		M_15.append(M15)
		M61 = CalcMoment(x_c, y_c, 6, 1, I)
		M_61.append(M61)
		M52 = CalcMoment(x_c, y_c, 5, 2, I)
		M_52.append(M52)
		M43 = CalcMoment(x_c, y_c, 4, 3, I)
		M_43.append(M43)
		M34 = CalcMoment(x_c, y_c, 3, 4, I)
		M_34.append(M34)
		M25 = CalcMoment(x_c, y_c, 2, 5, I)
		M_25.append(M25)
    
    Mat_11 = Normalize(Mat_11)
    Mat_21 = Normalize(Mat_21)
    Mat_12 = Normalize(Mat_12)
    Mat_31 = Normalize(Mat_31)
    Mat_22 = Normalize(Mat_22)
    Mat_13 = Normalize(Mat_13)
    Mat_41 = Normalize(Mat_41)
    Mat_32 = Normalize(Mat_32)
    Mat_23 = Normalize(Mat_23)
    Mat_14 = Normalize(Mat_14)
    Mat_51 = Normalize(Mat_51)
    Mat_42 = Normalize(Mat_42)
    Mat_33 = Normalize(Mat_33)
    Mat_24 = Normalize(Mat_24)
    Mat_15 = Normalize(Mat_15)
    Mat_61 = Normalize(Mat_61)
    Mat_52 = Normalize(Mat_52)
    Mat_43 = Normalize(Mat_43)
    Mat_34 = Normalize(Mat_34)
    Mat_25 = Normalize(Mat_25)
    M = np.zeros(20000).reshape(20, 10, 100)
    M[0] = Mat_11
    M[1] = Mat_21
    M[2] = Mat_12
    M[3] = Mat_31
    M[4] = Mat_22
    M[5] = Mat_13
    M[6] = Mat_41
    M[7] = Mat_32
    M[8] = Mat_23
    M[9] = Mat_14
    M[10] = Mat_51
    M[11] = Mat_42
    M[12] = Mat_33
    M[13] = Mat_24
    M[14] = Mat_15
    M[15] = Mat_61
    M[16] = Mat_52
    M[17] = Mat_43
    M[18] = Mat_34
    M[19] = Mat_25
    return M

def Moment1NNL2():
	MA = CentralMoment('A')
	MB = CentralMoment('B')
	MC = CentralMoment('C')
	MD = CentralMoment('D')
	errorsA = 0
	cA = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 20):
						dist += pow((MA[i][j][k] - MA[i][n][m]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cA[j][min_n] += 1
				errorsA += 1
			else:
				cA[j][j] += 1

	errorsB = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 20):
						dist += pow((MB[i][j][k] - MA[i][n][m]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cB[j][min_n] += 1
				errorsB += 1
			else:
				cB[j][j] += 1

	errorsC = 0
	cC = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 20):
						dist += pow((MC[i][j][k] - MA[i][n][m]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cC[j][min_n] += 1
				errorsC += 1
			else:
				cC[j][j] += 1

	errorsD = 0
	cD = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 20):
						dist += pow((MD[i][j][k] - MA[i][n][m]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cD[j][min_n] += 1
				errorsD += 1
			else:
				cD[j][j] += 1

	print >> f, "Moment1NNL2:"
	print >> f, "Testing set A"
	print_mat(cA)
	print >> f, errorsA

	print >> f, "Testing set B"
	print_mat(cB)
	print >> f, errorsB

	print >> f, "Testing set C"
	print_mat(cC)
	print >> f, errorsC

	print >> f, "Testing set D"
	print_mat(cD)
	print >> f, errorsD

	print >> f, "Average error:"
	errorsAverage = (errorsB+errorsC+errorsD)/3
	print >> f, errorsAverage

def Moment5NNL2():
	MA = CentralMoment('A')
	MB = CentralMoment('B')
	MC = CentralMoment('C')
	MD = CentralMoment('D')
	errorsA = 0
	cA = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 20):
						dist += pow((MA[i][j][k] - MA[i][n][m]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cA[j][classNum] += 1
				errorsA += 1
			else:
				cA[j][j] += 1
	errorsB = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 20):
						dist += pow((MB[i][j][k] - MA[i][n][m]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cB[j][classNum] += 1
				errorsB += 1
			else:
				cB[j][j] += 1

	errorsC = 0
	cC = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 10):
						dist += pow((MB[i][j][k] - MA[i][n][m]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cC[j][classNum] += 1
				errorsC += 1
			else:
				cC[j][j] += 1
	errorsD = 0
	cD = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 10):
						dist += pow((MB[i][j][k] - MA[i][n][m]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cD[j][classNum] += 1
				errorsD += 1
			else:
				cD[j][j] += 1
	print >> f, "Moment1NNL2:"
	print >> f, "Testing set A"
	print_mat(cA)
	print >> f, errorsA

	print >> f, "Testing set B"
	print_mat(cB)
	print >> f, errorsB

	print >> f, "Testing set C"
	print_mat(cC)
	print >> f, errorsC

	print >> f, "Testing set D"
	print_mat(cD)
	print >> f, errorsD

	print >> f, "Average error:"
	errorsAverage = (errorsB+errorsC+errorsD)/3
	print >> f, errorsAverage

def print_mat(mat):
	f = open('results.txt','a+')
	print >> f, "CONFUSION TABLE"
	print >> f, "True class",
	print >> f, "\t",
	for i in range (0, 10):
		print >> f, i,
		print >> f, "\t",
	print >> f, "ErrorTypeI"
	for i in range (len(mat)):
		print >> f, i,
		print >> f, "\t\t",
		for j in range (len(mat[0])):
			if(mat[i][j] != 0):
				print >> f, mat[i][j],
				print >> f, "\t",
			else:
				print >> f, "\t",
		print >> f, 100-mat[i][i],
		print >> f, "\n"
	print >> f, "ErrorTypeII",
	b = 0
	for i in range (10):
		a = 0
		for j in range(10):
			if(i != j):
				a += mat[j][i]
		print >> f, a,
		print >> f, "\t",
		b += a
	print >> f, b

def Normalize(mat):
	rms = 0
	sum = 0
	n = len(mat)*len(mat[0])
	for i in range(0, len(mat)):
	    for j in range(0, len(mat[0])):
		sum += math.pow(mat[i][j], 2)
	rms = math.sqrt(sum/n)
	for i in range(0, len(mat)):
	    for j in range(0, len(mat[0])):
		mat[i][j] /= rms
	return mat	
	
def CalcMoment(x_c, y_c, p, q, I):
	M = 0
	for x in range(0, 16):
	    for y in range(0, 16):
		M += math.pow((x + 1 - x_c), p)*math.pow((y + 1 - y_c), q)*I[y][x]
	return M

def MinDistance():
	MA = CentralMoment('A')
	MB = CentralMoment('B')
	MC = CentralMoment('C')
	MD = CentralMoment('D')
	u = np.zeros(200).reshape(20, 10)
	errorsA = 0
	for i in range (0, 20):
		for j in range (0, 10):
			sum = 0
			for k in range (0, 100):
				sum += MA[i][j][k]
			sum /= 100
			u[i][j] = sum
	cA = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				dist = 0
				for i in range(0, 20):
					dist += pow((MA[i][j][k] - u[i][n]),2)
				if (dist < min_dist):
					min_dist = dist
					min_n = n
			if (j != min_n):
				cA[j][min_n] += 1
				errorsA += 1
			else:
				cA[j][j] += 1
	print_mat(cA)
	print >> f, errorsA
	errorsB = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				dist = 0
				for i in range(0, 20):
					dist += pow((MB[i][j][k] - u[i][n]),2)
				if (dist < min_dist):
					min_dist = dist
					min_n = n
			if (j != min_n):
				cB[j][min_n] += 1
				errorsB += 1
			else:
				cB[j][j] += 1
	print_mat(cB)
	print >> f, errorsB

	errorsC = 0
	cC = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				dist = 0
				for i in range(0, 20):
					dist += pow((MC[i][j][k] - u[i][n]),2)
				if (dist < min_dist):
					min_dist = dist
					min_n = n
			if (j != min_n):
				cC[j][min_n] += 1
				errorsC += 1
			else:
				cC[j][j] += 1
	print_mat(cC)
	print >> f, errorsC

	errorsD = 0
	cD = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				dist = 0
				for i in range(0, 20):
					dist += pow((MD[i][j][k] - u[i][n]),2)
				if (dist < min_dist):
					min_dist = dist
					min_n = n
			if (j != min_n):
				cD[j][min_n] += 1
				errorsD += 1
			else:
				cD[j][j] += 1
	print_mat(cD)
	print >> f, errorsD

def IdenticalCovariance():
	MA = CentralMoment('A')
	MatA = np.zeros(20000).reshape(10, 100, 20)
	MB = CentralMoment('B')
	MatB = np.zeros(20000).reshape(10, 100, 20)
	MC = CentralMoment('C')
	MatC = np.zeros(20000).reshape(10, 100, 20)
	MD = CentralMoment('D')
	MatD = np.zeros(20000).reshape(10, 100, 20)
	for i in range (0, 20):
		for j in range(0, 10):
			for k in range(0, 100):
				MatA[j][k][i] = MA[i][j][k]
				MatB[j][k][i] = MB[i][j][k]
				MatC[j][k][i] = MC[i][j][k]
				MatD[j][k][i] = MD[i][j][k]
	sigma = np.zeros(400).reshape(20, 20)
	for i in range (0, 10):
		sigma += np.cov(MatA[i], rowvar = 0)
	sigma /= 10
	sigma_inv = inv(sigma)
	errorsA = 0
	errorsB = 0
	errorsC = 0
	errorsD = 0
	cA = np.zeros(100).reshape(10, 10)
	cB = np.zeros(100).reshape(10, 10)
	cC = np.zeros(100).reshape(10, 10)
	cD = np.zeros(100).reshape(10, 10)

	u = np.zeros(200).reshape(10, 20)
	for i in range (0, 10):
		for j in range(0, 20):
			u[i][j] = 0
			for k in range (0, 100):
				u[i][j] += MatA[i][k][j]
			u[i][j] /= 100
	for i in range (0, 10):
		for j in range (0, 100):
			min_g_x = 1000000
			min_n = 0
			for n in range (0, 10):
				g_x = np.dot( np.dot((MatA[i][j] - u[n]).T , sigma_inv) , (MatA[i][j] - u[n]) )
				if (g_x < min_g_x):
					min_g_x = g_x
					min_n = n
			if (i != min_n):
				cA[i][min_n] += 1
				errorsA += 1
			else:
				cA[i][i] += 1
	print_mat(cA)
	print >> f, errorsA
	
	for i in range (0, 10):
		for j in range (0, 100):
			min_g_x = 1000000
			min_n = 0
			for n in range (0, 10):
				g_x = np.dot( np.dot((MatB[i][j] - u[n]).T , sigma_inv) , (MatB[i][j] - u[n]) )
				if (g_x < min_g_x):
					min_g_x = g_x
					min_n = n
			if (i != min_n):
				cB[i][min_n] += 1
				errorsB += 1
			else:
				cB[i][i] += 1
	print_mat(cB)
	print >> f, errorsB
	
	for i in range (0, 10):
		for j in range (0, 100):
			min_g_x = 1000000
			min_n = 0
			for n in range (0, 10):
				g_x = np.dot( np.dot((MatC[i][j] - u[n]).T , sigma_inv) , (MatC[i][j] - u[n]) )
				if (g_x < min_g_x):
					min_g_x = g_x
					min_n = n
			if (i != min_n):
				cC[i][min_n] += 1
				errorsC += 1
			else:
				cC[i][i] += 1
	print_mat(cC)
	print >> f, errorsC
	
	for i in range (0, 10):
		for j in range (0, 100):
			min_g_x = 1000000
			min_n = 0
			for n in range (0, 10):
				g_x = np.dot( np.dot((MatD[i][j] - u[n]).T , sigma_inv) , (MatD[i][j] - u[n]) )
				if (g_x < min_g_x):
					min_g_x = g_x
					min_n = n
			if (i != min_n):
				cD[i][min_n] += 1
				errorsD += 1
			else:
				cD[i][i] += 1
	print_mat(cD)
	print >> f, errorsD

def PixelIndependent():
	MA = PixelSpace('A')
	MB = PixelSpace('B')
	P = np.zeros(2560).reshape(10, 256)
	Q = np.zeros(2560).reshape(10, 256)
	for i in range (0, 10):
		for k in range(0, 256):
			for j in range(0, 100):
				P[i][k] += MA[i][j][k]
			P[i][k] /= 100
			if (P[i][k] == 0):
				P[i][k] += 1.0/(3*100)
			if (P[i][k] == 1):
				P[i][k] = (3*100-1.0)/(3*100)
			Q[i][k] = 1-P[i][k]
	errorsA = 0
	errorsB = 0
	cA = np.zeros(100).reshape(10, 10)
	cB = np.zeros(100).reshape(10, 10)
	
	for i in range(0, 10):
		for j in range(0, 100):
			max_dist = -1000000
			max_n = 0
			for n in range(0, 10):
				dist = 0
				for k in range (0, 256):
					dist += np.dot(MA[i][j][k], (math.log(P[n][k]))) + np.dot(1-MA[i][j][k], (math.log(Q[n][k])))
					print dist
				if (dist > max_dist):
					max_dist = dist
					max_n = n
			if(i != max_n):
				cA[i][max_n] += 1
				errorsA += 1
			else:
				cA[i][i] += 1
	print_mat(cA)
	print >> f, errorsA
	
	for i in range(0, 10):
		for j in range(0, 100):
			max_dist = -1000000
			max_n = 0
			for n in range(0, 10):
				dist = 0
				for k in range (0, 256):
					dist += np.dot(MB[i][j][k], (math.log(P[n][k]))) + np.dot(1-MB[i][j][k], (math.log(Q[n][k])))
				if (dist > max_dist):
					max_dist = dist
					max_n = n
			if(i != max_n):
				cB[i][max_n] += 1
				errorsB += 1
			else:
				cB[i][i] += 1
	print_mat(cB)
	print >> f, errorsB

def Pixel1NNL2():
	MA = PixelSpace('A')
	MB = PixelSpace('B')
	MC = PixelSpace('C')
	MD = PixelSpace('D')
	errorsB = 0
	errorsC = 0
	errorsD = 0
	
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 256):
						dist += pow((MB[j][k][i] - MA[n][m][i]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cB[j][min_n] += 1
				errorsB += 1
			else:
				cB[j][j] += 1
	print_mat(cB)
	print >> f, errorsB
	
	cC = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 256):
						dist += pow((MC[j][k][i] - MA[n][m][i]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cC[j][min_n] += 1
				errorsC += 1
			else:
				cC[j][j] += 1
	print_mat(cC)
	print >> f, errorsC

	cD = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 256):
						dist += pow((MD[j][k][i] - MA[n][m][i]),2)
					if (dist < min_dist):
						min_dist = dist
						min_n = n
					if (dist == min_dist):
						r = randint(1,2)
						if(r == 1):
							min_dist = dist
							min_n = n
			if (j != min_n):
				cD[j][min_n] += 1
				errorsD += 1
			else:
				cD[j][j] += 1
	print_mat(cD)
	print >> f, errorsD

def Pixel5NNL2():
	MA = PixelSpace('A')
	MB = PixelSpace('B')
	MC = PixelSpace('C')
	MD = PixelSpace('D')
	
	errorsB = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 256):
						dist += pow((MB[j][k][i] - MA[n][m][i]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cB[j][classNum] += 1
				errorsB += 1
			else:
				cB[j][j] += 1
	print_mat(cB)
	print >> f, errorsB

	errorsC = 0
	cC = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 256):
						dist += pow((MC[j][k][i] - MA[n][m][i]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cC[j][classNum] += 1
				errorsC += 1
			else:
				cC[j][j] += 1
	print_mat(cC)
	print >> f, errorsC

	errorsD = 0
	cD = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = np.zeros(5);
			min_n = np.zeros(5);
			for x in range(0, 5):
				min_dist[x] = 1000000
				min_n[x] = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 256):
						dist += pow((MD[j][k][i] - MA[n][m][i]),2)
					if (dist < max(min_dist)):
						for cnt in range (0, 5):
							if min_dist[cnt] == max(min_dist):
								min_dist[cnt] = dist
								min_n[cnt] = n
					if (dist == max(min_dist)):
						r = randint(1,2)
						if(r == 1):
							for cnt in range (0, 5):
								if min_dist[cnt] == max(min_dist):
									min_dist[cnt] = dist
									min_n[cnt] = n
			classes = np.zeros(10)
			classNum = -1
			n = 0
			for cnt in range(0, 10):
				classes[cnt] = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			for cnt in range(0, 10):
				if(classes[min_n[cnt]] >= 3):
					classNum = min_n[cnt]
					n = 3
					break
				elif(classes[min_n[cnt]] >= 2):
					if(classNum != -1):
						r = randint(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 2
				elif(n <= 1 and classes[min_n[cnt]] >= 1):
					if(classNum != -1):
						r = randin(1,2)
						if(r == 1):
							classNum = min_n[cnt]
					else:
						classNum = min_n[cnt]
					n = 1
			if (j != classNum):
				cD[j][classNum] += 1
				errorsD += 1
			else:
				cD[j][j] += 1
	print_mat(cD)
	print >> f, errorsD


def PixelMinDistance():
	MA = PixelSpace('A')
	MB = PixelSpace('B')
	MC = PixelSpace('C')
	MD = PixelSpace('D')
	u = np.zeros(2560).reshape(10, 256)
	
	for i in range(0, 10):
		for k in range(0, 256):
			for j in range(0, 100):
				u[i][k] += MA[i][j][k]
			u[i][k] /= 100
	errorsB = 0
	errorsC = 0
	errorsD = 0
	cA = np.zeros(100).reshape(10, 10)
	cB = np.zeros(100).reshape(10, 10)
	cC = np.zeros(100).reshape(10, 10)
	cD = np.zeros(100).reshape(10, 10)
	
	for i in range(0, 10):
		for j in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range (0, 10):
				dist = 0
				for k in range (0, 256):
					dist += math.pow((MA[i][j][k] - u[n][k]), 2)
				if (dist < min_dist):
					min_dist = dist
					min_n = n
			if(i != min_n):
				cA[i][min_n] += 1
				errorsA += 1
			else:
				cA[i][i] += 1
	print_mat(cA)
	print >> f, errorsA

	for i in range(0, 10):
		for j in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range (0, 10):
				dist = 0
				for k in range (0, 256):
					dist += math.pow((MB[i][j][k] - u[n][k]), 2)
				if (dist < min_dist):
					min_dist = dist
					min_n = n
			if(i != min_n):
				cB[i][min_n] += 1
				errorsB += 1
			else:
				cB[i][i] += 1
	print_mat(cB)
	print >> f, errorsB

def PixelSpace(s):

    M = np.zeros(256000).reshape(10, 100, 256)
    for i in range (0,10):
        s1 = '../../hw5_data/%s-%d_new.txt'%(s, i)
        
        f1 = file(s1, 'r')
        
        h = 0 
        w = 0
       
	area = []
	li = []
 
        while True:
            line1 = f1.readline()
            if(len(line1) == 0):
                break;
            m = line1.split(' ')

            if m[0] == 'C':
		li = []
		area.append(li)

	    else:
		li.append(line1[0:len(line1)-1])

	f1.close()
	
	j = 0
	for a in area:
		I = np.zeros(256)
		for l in range(0,16):
			for w in range(0,16):
			    if a[l][w] == 'x':
				I[l*16+w] = 1
			    else:
				I[l*16+w] = 0
		M[i][j] = I
		j += 1
    return M


#handlefile('A')
#handlefile('B')
#handlefile('C')
#handlefile('D')
#Moment1NNL2()
#Moment5NNL2()
MinDistance()
IdenticalCovariance()
#Pixel1NNL2()
#Pixel5NNL2()
#PixelMinDistance()
