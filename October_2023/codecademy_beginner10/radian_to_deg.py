"""
1. Convert radians into degrees
Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself. 
One hint you get is that you’ll need to use Pi in order to solve this problem. You can import the value for Pi from Python’s math module.
"""
import math

def rad_to_deg(rad : float) -> float:

    return round(rad * (180/math.pi), 2)

def main():
    print(rad_to_deg(1))
    print(rad_to_deg(3))

if __name__ == "__main__":
    main()