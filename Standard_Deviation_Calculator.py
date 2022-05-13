print("Welcome to Standard Deviation Calculator")

import numpy as np
dataset = []
size = int(input("Please enter size of dataset or the number of values within the set: "))
print("Please enter dataset values: ")
for x in range(size):
  values = int(input())
  dataset.append(values)

print ("Dataset is: ",dataset)

mean = sum(dataset)/size
print ("Mean is: ",mean)

print("Standard Deviation is the sum of each dataset value subtracted from the mean\ndivided the total number of values within the dataset\n")
standDev = np.std(dataset)
print("Standard Deviation of above dataset is:",standDev)

