import requests
import re
import pickle
import time
import datetime

requests.packages.urllib3.disable_warnings() 

pattern = re.compile('<tr id.*?</tr>',re.DOTALL)
pattern2 = re.compile('class="price" data-usd=\".*?\"')
pattern3 = re.compile('\d+.\d+')
pattern4 = re.compile('[-|\d]+\.\d+%')

def getTop100():
    response = requests.get('https://coinmarketcap.com/', verify=False)
    result = pattern4.findall(response.text)
    average100 = 0
    
    for i in result:
        average100 += float(i[:-1])

    average100 /= len(result)
    
    return format(float(average100),'.2f')

def getTop10():
    response = requests.get('https://coinmarketcap.com/', verify=False)
    result = pattern4.findall(response.text)
    average10 = 0
    
    for i in range(10):
        average10 += float(result[i][:-1])

    average10 /= 10
    
    return format(float(average10),'.2f')

def getAll():
    response = requests.get('https://coinmarketcap.com/all/views/all/', verify=False)
    result = pattern4.findall(response.text)
    average = 0
    for i in result:
        average += float(i[:-1])

    average /= len(result)
    return format(float(average),'.2f'), len(result)

def getBTC():
    response = requests.get('https://coinmarketcap.com/', verify=False)
    result = pattern4.findall(response.text)
    
    return format(float(result[0][:-1]),'.2f')

def writeToFile(inputList):
    with open('changeData.data', 'wb') as filehandle:  
        pickle.dump(inputList, filehandle)

def readFile():
    with open('changeData.data', 'rb') as filehandle:  
        outputList = pickle.load(filehandle)
    return outputList

'''
print("BitCoin Change: " + str(getBTC()) + '%')
print("Top 100 coins average: " + str(getTop100()) + '%')
print(str(getAll()[1]) + " coins average: " + str(getAll()[0]) + '%')
'''

try:
    changeList = readFile()

except:
    changeList = []

temp = 0
while(True): 
    try:
        changeList.append((getBTC(),getTop10(),getTop100(), getAll(), datetime.datetime.now()))
        temp += 1
        print(str(temp))
    except:
        print("Some error, probably no response from server")
        
    writeToFile(changeList)
    time.sleep(15)

