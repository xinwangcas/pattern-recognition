# !usr/bin/python
# Filename: HW6.py

import re
import os
import string
import sys
import math
import numpy as np
from random import randint
from numpy.linalg import inv

f = open('hw6.txt','a+')

def handlefile(s):
    for i in range (0,10):
        s1 = '../../hw5_data/%s-%d.txt'%(s, i)
        s2 = '../../hw5_data/%s-%d_new.txt'%(s, i)
        
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
                sw = re.findall(r'\d+', m[2])
                w = int(sw[0])
                w_left = (16-w)/2
                w_right = 16-w_left-w
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
                    for i in range (0,w_left):
                        line2 += '.'
                    line2 += line1
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
    Mat_11 = Normalize(s, 0, Mat_11)
    Mat_21 = Normalize(s, 1, Mat_21)
    Mat_12 = Normalize(s, 2, Mat_12)
    Mat_31 = Normalize(s, 3, Mat_31)
    Mat_22 = Normalize(s, 4, Mat_22)
    Mat_13 = Normalize(s, 5, Mat_13)
    Mat_41 = Normalize(s, 6, Mat_41)
    Mat_32 = Normalize(s, 7, Mat_32)
    Mat_23 = Normalize(s, 8, Mat_23)
    Mat_14 = Normalize(s, 9, Mat_14)
    M = np.zeros(10000).reshape(10, 10, 100)
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
    return M

def Normalize(s, k, mat):
	sum = 0
	n = len(mat)*len(mat[0])
	if s == 'A':
		for i in range(0, len(mat)):
		    for j in range(0, len(mat[0])):
			sum += math.pow(mat[i][j], 2)
			rms[k] = math.sqrt(sum/n)
	for i in range(0, len(mat)):
	    for j in range(0, len(mat[0])):
		mat[i][j] /= rms[k]
	return mat	

def Moment1NNL2():
	MA = CentralMoment('A')
	MB = CentralMoment('B')
	u = np.zeros(100).reshape(10, 10)
	for i in range (0, 10):
		for j in range (0, 10):
			sum = 0
			for k in range (0, 100):
				sum += MA[i][j][k]
			sum /= 100
			u[i][j] = sum
	errorsB = 0
	cost = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 10):
						dist += pow((MB[i][j][k] - MA[i][n][m]),2)
						cost += 1
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
	cost /= 1000.0
	print >> f, cost


def Moment1NNL4():
	MA = CentralMoment('A')
	MB = CentralMoment('B')
	u = np.zeros(100).reshape(10, 10)
	for i in range (0, 10):
		for j in range (0, 10):
			sum = 0
			for k in range (0, 100):
				sum += MA[i][j][k]
			sum /= 100
			u[i][j] = sum
	errorsB = 0
	cost = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = 1000000
			min_n = 0
			for n in range(0, 10):
				for m in range(0, 100):
					dist = 0
					for i in range(0, 10):
						dist += pow((MB[i][j][k] - MA[i][n][m]),2)
						cost += 1
						dist += pow(dist, 2)
						cost += 1
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
	cost /= 1000.0
	print >> f, cost


def Moment5NNL2():
	MA = CentralMoment('A')
	MB = CentralMoment('B')
	u = np.zeros(100).reshape(10, 10)
	for i in range (0, 10):
		for j in range (0, 10):
			sum = 0
			for k in range (0, 100):
				sum += MA[i][j][k]
			sum /= 100
			u[i][j] = sum
	errorsB = 0
	cost = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = [sys.maxint]*6;
			min_n = [0]*6;
			for n in range(0, 10):
				for m in range(0, 100):
					min_dist[5] = 0
					for i in range(0, 10):
						min_dist[5] += pow((MB[i][j][k] - MA[i][n][m]),2)
						cost += 1
					min_dist[5] = np.sqrt(min_dist[5])
					min_n[5] = n
					p = 5
					while(p >= 1):
						if(min_dist[p] < min_dist[p-1]):
							min_dist[p], min_dist[p-1] = min_dist[p-1], min_dist[p]
							min_n[p], min_n[p-1] = min_n[p-1], min_n[p]
							p -= 1
						elif(min_dist[p] == min_dist[p-1]):
							q = randint(1,2)
							if(q == 1):
								min_dist[p], min_dist[p-1] = min_dist[p-1], min_dist[p]
								min_n[p], min_n[p-1] = min_n[p-1], min_n[p]
								p -= 1
						else:
							break
						
			classes = np.zeros(10)
			classNum = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			max_value = max(classes)
			max_list = []
			for cnt in range(0, 10):
				if classes[cnt] == max_value:
					max_list.append(cnt)
			classNum = max_list[randint(0, len(max_list)-1)]
				
			if (j != classNum):
				cB[j][classNum] += 1
				errorsB += 1
			else:
				cB[j][j] += 1
	print_mat(cB)
	print >> f, errorsB
	cost /= 1000.0
	print >> f, cost


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

	
def CalcMoment(x_c, y_c, p, q, I):
	M = 0
	for x in range(0, 16):
	    for y in range(0, 16):
		M += math.pow((x + 1 - x_c), p)*math.pow((y + 1 - y_c), q)*I[y][x]
	return M

def Pixel1NNL2():
	MA = PixelSpace('A')
	MB = PixelSpace('B')
	u = np.zeros(2560).reshape(10, 256)
	
	errorsA = 0
	errorsB = 0
	
	cost = 0
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
						cost += 1
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
	cost /= 1000.0
	print >> f, cost


def Pixel5NNL2():
	MA = PixelSpace('A')
	MB = PixelSpace('B')
	u = np.zeros(2560).reshape(10, 256)
	
	errorsB = 0
	cost = 0
	cB = np.zeros(100).reshape(10, 10) # class i to class j; class j to class i
	for j in range (0, 10):
		for k in range (0, 100):
			min_dist = [sys.maxint]*6;
			min_n = [0]*6;
			for n in range(0, 10):
				for m in range(0, 100):
					min_dist[5] = 0
					for i in range(0, 256):
						min_dist[5] += pow((MB[j][k][i] - MA[n][m][i]),2)
						cost += 1
					min_dist[5] = np.sqrt(min_dist[5])
					min_n[5] = n
					p = 5
					while(p >= 1):
						if(min_dist[p] < min_dist[p-1]):
							min_dist[p], min_dist[p-1] = min_dist[p-1], min_dist[p]
							min_n[p], min_n[p-1] = min_n[p-1], min_n[p]
							p -= 1
						elif(min_dist[p] == min_dist[p-1]):
							q = randint(1,2)
							if(q == 1):
								min_dist[p], min_dist[p-1] = min_dist[p-1], min_dist[p]
								min_n[p], min_n[p-1] = min_n[p-1], min_n[p]
								p -= 1
						else:
							break
						
			classes = np.zeros(10)
			classNum = 0
			for cnt in range(0, 5):
				classes[min_n[cnt]] += 1
			max_value = max(classes)
			max_list = []
			for cnt in range(0, 10):
				if classes[cnt] == max_value:
					max_list.append(cnt)
			classNum = max_list[randint(0, len(max_list)-1)]
				
			if (j != classNum):
				cB[j][classNum] += 1
				errorsB += 1
			else:
				cB[j][j] += 1
	print_mat(cB)
	print >> f, errorsB
	cost /= 1000.0
	print >> f, cost

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


handlefile('A')
handlefile('B')
rms = np.zeros(10)
#Moment1NNL2()
rms = np.zeros(10)
#Moment1NNL4()
rms = np.zeros(10)
#Moment5NNL2()
rms = np.zeros(10)
Pixel1NNL2()
rms = np.zeros(10)
#Pixel5NNL2()
rms = np.zeros(10)
#CentralMoment('A')
#CentralMoment('B')
