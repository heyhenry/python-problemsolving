num = -123
reversed_num = 0

while num != 0:
    # extract the tail digit
    extracted_num = num % 10
    # push the existing digits in reversed_num to the left
    reversed_num *= 10
    # add the extracted_num value to the tail of the reversed_num
    reversed_num += extracted_num
    # remove the tail digits from the current num
    num //= 10
print(reversed_num)