import math
import numpy as np
import argparse

# begin PROVIDED section - do NOT modify ##################################

count = 0

def getArgs() :
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type = str, help = 'File containing terrain')
    
    parser.add_argument('h', type = float, help = 'h value')
    
    parser.add_argument('theta', type = float, help = 'Angle of elevation for Sun')
    parser.add_argument('algorithm', type = str, help = 'naive | early | fast')
    return parser.parse_args()

def compare(x,y):
    global count
    count += 1
    if abs(x-y) < .000000000001 :
        return False
    if x < y :
        return True
    else:
        return False

def print_shade(boolean_array):
    for row in boolean_array:
        for column in row:
            if column == True:
                print ('*    ', end = '')
            elif column == False:
                print ('0    ', end = '')
        print('\n')
        
def read2Dfloat(fileName) : # read CSV of floats into 2D array
    array2D = []
    # Read input file
    f = open(fileName, "r")
    data = f.read().split('\n')
    
    # Get 2-D array
    for row in data[0:-1]:
        float_list = list(map(float, row.split(',')[0:-1]))
        array2D.append(float_list)
    
    return array2D

def runTest(args, terrain = None) :

    
    # Initialize counter
    global count
    count = 0
    result = ''

    theta = np.deg2rad(args.theta)
    
    if terrain == None :
      terrain = read2Dfloat(args.input_file)

    N     = len(terrain)
    shade = [[False] * N for i in range(N)]

    if args.algorithm == 'naive':
        result = naive(terrain, args.h, theta, N, shade)
    elif args.algorithm == 'early':
        result = earlyexit(terrain, args.h, theta, N, shade)
    elif args.algorithm == 'fast':
        result = fast(terrain, args.h, theta, N, shade)

    return result

# end PROVIDED section ##################################

# Fritz Sieker 

def naive(image,h,angle,N,shade):
    # go through every row
    for row in range(N):
        # go through every column
        for col in range(1, N):
            # go through every column in the same row up until the column that the upper loop is on
            for k in range(col):
                lhs = (image[row][k] - image[row][col])/(h*(col-k))
                tan = math.tan(angle)
                # compare lhs and tangent
                if compare(tan, lhs):
                    # it is in the shade
                    shade[row][col] = True
    
###### Complete this function

    return shade

def earlyexit(image,h,angle, N, shade):
    # go through every row
    for row in range(N):
        # go through every column
        for col in range(1, N):
            # go through every column in the same row up until the column that the upper loop is on
            for k in range(col):
                lhs = (image[row][k] - image[row][col])/(h*(col-k))
                tan = math.tan(angle)
                # compare lhs and tangent
                if compare(tan, lhs):
                    # it is in the shade
                    shade[row][col] = True
                    # move on. you already know this one is in the shade
                    break
                    
    
###### Complete this function

    return shade



def fast(image,h,angle, N, shade):
    # walk through every row
    for row in range(N):
        # keep a running max of the max height in this row. Starting with the first column
        max = image[row][0]
        k = 0
        # walk through every column
        for col in range(1,N):
            lhs = (image[row][k] - image[row][col])/(h*(col-k))
            tan = math.tan(angle)
            # if in the sun update new max 
            if not compare(tan, lhs):
                max = image[row][col]
                k = col
            # if in the shade update shade array
            if compare(tan, lhs):
                shade[row][col] = True   
###### Complete this function
    
    return shade


    
if __name__ == '__main__':
    

    answer = runTest(getArgs())
    print_shade(answer)
    print('Number of comparisons: ' + str(count))