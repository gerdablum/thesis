import pandas
import matplotlib.pyplot as plt
import numpy as np
import chartcalc as calc

testData = pandas.read_csv('C:/Users/L30603/Documents/SurveyData/data_experience-it.csv', sep = ';')
vrExperience = testData['IN06']


noExperience = calc.percentage(vrExperience, 1)
aLittle  = calc.percentage(vrExperience, 2)
sometimes = calc.percentage(vrExperience, 3)
print ('VR usage: never', noExperience)
print ('VR usage: 1-3 times', aLittle)
print('VR usage: sometimes', sometimes)

quantities = calc.quantity(vrExperience, [1, 2, 3, 4, 5])
print(quantities)

plt.bar(['never', 'yes, 1-3 times before', 'yes, sometimes', 'yes, often', 'yes, very often'], quantities, width=0.5)
plt.xticks(rotation='vertical')
plt.title('Have you used virtual reality (VR) technologies before?')
plt.show()