import matplotlib.pyplot as plt
import pickle

def readFile():
    with open('changeData.data', 'rb') as filehandle:  
        outputList = pickle.load(filehandle)
    
    return outputList

testList = readFile()

def side_values(num_list):
    results_list = sorted(num_list)
    return results_list[0], results_list[-1]

def min_max(inputList):
    minimum = 999999
    maximum = -999999
    
    for x in inputList:
        if(float(x[0]) > maximum):
            maximum = float(x[0])
            
        if(float(x[1]) > maximum):
            maximum = float(x[1])
            
        if(float(x[2][0]) > maximum):
            maximum = float(x[2][0])
            
        if(float(x[0]) < minimum):
            minimum = float(x[0])
        
        if(float(x[1]) < minimum):
            minimum = float(x[1])
            
        if(float(x[2][0]) < minimum):
            minimum = float(x[2][0])
    
    return minimum,maximum

x1_val = [float(x[0]) for x in testList]
x2_val = [float(x[1]) for x in testList]
x3_val = [float(x[2]) for x in testList]
x4_val = [float(x[3][0]) for x in testList]
y_val = []

for i in range(len(testList)):
    y_val.append(i)

plt.plot(y_val,x1_val, label = "BTC")

plt.plot(y_val,x2_val, label = "Top 10 Coins by MarketCap")

plt.plot(y_val,x3_val, label = "Top 100 Coins by MarketCap")

name = str(testList[0][3][1]) + " Coins"
plt.plot(y_val,x4_val, label = name)

plt.suptitle('24 hr Percent Change Over Time', fontsize=20)
plt.xlabel('Time (15 * x seconds)', fontsize=18)
plt.ylabel('Percent Change', fontsize=16)

plt.legend()
plt.savefig('differences.png')


