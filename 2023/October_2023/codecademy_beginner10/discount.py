"""
8. Give me the discount
Create a function in Python that accepts two parameters. 
The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. 
For example, if the price is 100 and the discount is 20, the function should return 80.
"""
def give_discount(full_price : int, discount : int) -> int:

    return full_price - ((discount/100) * full_price)

def main():
    print(give_discount(100, 20))
    print(give_discount(800, 20))
    print(give_discount(605, 35))

if __name__ == "__main__":
    main()