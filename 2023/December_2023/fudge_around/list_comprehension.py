# play 1
# squares = [x ** 2 for x in range(10)]
# print(squares)

# play 2
# nums = [0,1,2,3,4,5,6,7,8,9]
# new_list = [x for x in nums if x != 3]
# print(new_list)

# play 3
# sentence = "This is a sample sentence"
# word_list = []

# for word in sentence.split(' '):
#     word_list.append(word)

# print(word_list)

# word_list = [word for word in sentence.split(' ')]
# print(word_list)

# play 4
# Desc: Find the even number and square them
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [i*i for i in given_list if i % 2 == 0]
print(new_list)