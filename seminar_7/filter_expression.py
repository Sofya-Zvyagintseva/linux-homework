#!/usr/bin/python3
def filter_expression(values, threshold=5.0):
    return [x for x in values if x > threshold]

values = [2.5, 7.1, 0.8, 5.4, 9.2, 3.0]
print(filter_expression(values))
