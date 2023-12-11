import time

# print("Loading.....")
# time.sleep(0.5)
# print("Loading....")
# time.sleep(0.5)
# print("Loading...")
# time.sleep(0.5)
# print("Loading..")
# time.sleep(0.5)
# print("Loaded!")

loading = ["Loading... 0%", "Loading... 5%", "Loading... 10%", "Loading... 30%", "Loading... 50%", "Loading... 70%", "Loading... 100%", "Loaded!"]

for i in loading:
    print(i)
    time.sleep(0.8)

