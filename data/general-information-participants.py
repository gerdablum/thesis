import pandas
import matplotlib.pyplot as plt
import numpy as np

testData = pandas.read_csv('C:/Users/L30603/Documents/SurveyData/data_experience-it.csv', sep = ';')
ageData = testData['IN04_01']
schoolData = testData['IN03']
yearData = testData['IN09']
genderData = testData['IN10']

def average(data):
    avr = sum(data) / len(data)
    return round(avr, 1)

def quantity(data, options):
    quantities = [0] * len(options)
    for value in data:
        i = 0
        for option in options:
            if str(option) == str(value):
                quantities[i] = quantities[i] + 1
            i = i + 1
    return quantities

def percentage(data, value):
    quantity = 0
    for number in data:
        if number == value:
            quantity = quantity + 1
    perc = (quantity / len(data)) * 100
    return round(perc, 1)

print("Average age: ", average(ageData))

yearOptions = ['1', '2', '3', '-9']
yearQuantity = quantity(yearData, yearOptions)
i = 0
for option in yearOptions:
    print("year ", option, ": ", yearQuantity[i])
    i = i + 1

schoolOptions = ['5', '7', '-9']
schoolQuantity = quantity(schoolData, schoolOptions)
print('SHSS: ', schoolQuantity[0])
print('SIT: ', schoolQuantity[1])
print('other: ', schoolQuantity[2])
print('female: ', percentage(genderData, 1))
print('male: ', percentage(genderData, 2))