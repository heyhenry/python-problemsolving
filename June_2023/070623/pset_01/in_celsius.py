"""
Returns the celsius equivalent of the farhenheit `temp`
Examples:
in_celsius(32.0) ~> 0.0
in_celsius(212.0) ~> 100.0
in_celsius(-40.0) ~> -40.0
"""

def formula(farhenheit : float):

    return (farhenheit - 32) * 5/9

def in_celsius(temp : float) -> float:
    
    return formula(temp)

def main():
    print(in_celsius(32.0))
    print(in_celsius(212.0))
    print(in_celsius(-40.0))

if __name__ == "__main__":
    main()

# Completed