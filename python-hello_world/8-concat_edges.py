#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(f"{' '.join(str.split()[5:7])}", end=" ")
print("with Python")
