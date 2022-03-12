#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 09:04:35 2022

@author: konstantinos
"""

from numpy import median,mean,std

'''
This class will provide a set of statistical values for an array of double values. 
More specifically, the statistical metrics that are being implemented are:
    
1.Minimun vlaue, 
2. Maximum value, 
3. Median value, 
4. Mean value, 
5. Standard deviation    
'''

class StatisticUtilsArray:
    
    # The initialization method of the class
    def __init__(self, arr):
        
        self.arr = arr
        
        if arr == []:
            raise ValueError("The array is empty")
        
    # This method gives the minimun value of an array
    def minValue(self):
        return min(self.arr)
    
    # This method gives the maximum value of an array
    def maxValue(self):
        return max(self.arr)
    
    # This method gives the median of an array
    def medianValue(self):
        return median(self.arr)
    
    # This method gives the mean of an array
    def meanValue(self):
        return mean(self.arr)
    
    # This method gives the standard deviation of an array
    def standardDeviation(self):
        return format(std(self.arr),".4f")
        

'''
This class implements the Ascending Minima algorithm 
In brief this algorithm for a given array of size n returns the n-k+1 minimum values
where k corresponds to the size of a sliding windows size.  
For example :
Assume that the array is 5,1,3,2,6,8,4,6, and the window size is 3.
The algorithm returns the array 1,1,2,2,4,4
'''


'''
Note:
The implementation of StatisticUtilsArrayList in Python is same as StatisticUtilsArray
because:
    
A list in Python is a collection of items which can contain elements of multiple data types
, which may be either numeric, character logical values, etc

An array is a vector containing homogeneous elements i.e. belonging to the same data type. 

The task refers to double numerical values so in this case list is coincide with array

'''

class AscendingMinima:
     
    # The initialization method of the class 
    def __init__(self,arr,k):
        self.arr = arr  # arr is the target array
        self.k   = k    # k corresponds to the size of a sliding windows size
        
        
    # This method implement the asxending minima algorithm    
    def ascendingMinima(self):
        
        minima    = []
        start_pos = 0
        
        
        for i in range( len(self.arr) - (self.k-1) ):
            minima.append(min(arr[start_pos:self.k]))
            start_pos += 1
            self.k    += 1
        
        return minima
         
    
    
arr = [5,1,3,2,6,8,4,6]



# e1 is an example instance of the StatisticUtilsArray class
# If we put an empty array it throws ValueError

e1 = StatisticUtilsArray(arr)   

print("Below are represented metrics for the array: ",arr)
print("The minimum value is: ",e1.minValue())
print("The maximum value is: ",e1.maxValue()) 
print("The median is: ",e1.medianValue())
print("The mean value is: ",e1.meanValue())
print("The standard deviation is: ",e1.standardDeviation())


# e2 is an example instance of the AscendingMinima class

# k is the sliding window's size
k = 3


# Exaple_1 If the arr = [5,1,3,2,6,8,4,6] with window size 3 we take  [1, 1, 2, 2, 4, 4]

e2 = AscendingMinima(arr,k) 
print("The ascending minima for the array",arr,"with window size", k, "is \n",  e2.ascendingMinima())
    

# Example_2 If the arr = [] empty we take empty ascending minima 
    
arr3 = []
e3 = AscendingMinima(arr3,k) 
print("The ascending minima for the array",arr3,"with window size", k, "is \n",  e3.ascendingMinima())    
    
# Example_3 If the arr  = [5,1,3,2,6,8,4,6] with window size 7 we take  [1, 1]
    
arr4 = [5,1,3,2,6,8,4,6]
k4   = 7
e4 = AscendingMinima(arr4,k4) 
print("The ascending minima for the array",arr3,"with window size", k4, "is \n",  e4.ascendingMinima())        
    
    
    