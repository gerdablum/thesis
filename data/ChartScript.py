import pandas
import matplotlib.pyplot as plt
import numpy as np

testData = pandas.read_csv('C:/Users/L30603/Documents/SurveyData/data_experience-it.csv', sep = ';')
print(testData.head())
xData = testData['IN04_01']
minAge = 5#min(xData)
maxAge = max(xData)
quantity = [0] * (maxAge + 1 - minAge)
ages = range(minAge, maxAge + 1)

for age in xData:
    quantity[int(age) - minAge] = quantity[int(age) - minAge] + 1

print(quantity)
plt.plot(ages, quantity)
plt.title('Age of participants')
plt.axis([5, 60, 0, 10])
plt.xticks(np.arange(5, 60, 1)) 
plt.yticks(np.arange(0, 10, 1)) 
plt.xlabel('Quantity')
plt.ylabel("Age")
plt.show()


