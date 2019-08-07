import pandas
import matplotlib.pyplot as plt
import numpy as np

def calcQuantity(rng, values):
    outputValues = [0] * rng
    for val in values:
        outputValues[int(val)-1] = outputValues[int(val)-1] + 1
    return outputValues

testData = pandas.read_csv('C:/Users/L30603/Documents/SurveyData/data_experience-it.csv', sep = ';')

scale = [1,2,3,4,5,6,7]
#before testing VR
question1Before = testData['IN07_01'].tolist()
question2Before = testData['IN07_02'].tolist()
question3Before = testData['IN07_03'].tolist()

#after testing VR
question1After = testData['AF02_01'].tolist()
question2After = testData['AF02_02'].tolist()
question3After = testData['AF02_03'].tolist()

plt.plot(
range(1, len(question1Before) + 1), question1Before, 'r--',
#range(1,len(question1Before) + 1), question2Before, 'g--',
#range(1,len(question1Before) + 1), question3Before, 'b--',
range(1,len(question1Before) + 1), question1After, 'r'
#range(1,len(question1Before) + 1), question2After, 'g',
#range(1,len(question1Before) + 1), question3After, 'b',
)
plt.xlabel("Answer")
plt.ylabel("Quantity")
plt.show()

