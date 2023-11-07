"""
8. Give me the discount
Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. 
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. 
For example, if the price is 100 and the discount is 20, the function should return 80.
"""
def give_discount(full_price : int, discount : int):

    actual_discount = full_price * (discount / 100)

    return full_price - actual_discount

def main():
    print(give_discount(100,20))
    print(give_discount(500,35))
    print(give_discount(643,16))

if __name__ == "__main__":
    main()