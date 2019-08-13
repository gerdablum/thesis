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
