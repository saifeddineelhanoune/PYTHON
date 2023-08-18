#this code is successed with 91% i'm happy cuz it's my first time in py
import sys
import math

n = int(input())
temperatures_str = input()
temperatures = list(map(int, temperatures_str.split()))
closest = float('inf')
for temperature in temperatures:
    if abs(temperature) < abs(closest):
        closest = temperature
    elif abs(temperature) == abs(closest) and temperature > closest:
        closest = temperature

print(closest)
