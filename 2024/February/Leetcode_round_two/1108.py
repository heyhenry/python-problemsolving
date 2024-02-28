def defangIPAddr(address : str) -> str:

    return address.replace('.','[.]')

def main():
    print(defangIPAddr(address = "1.1.1.1"))
    print(defangIPAddr(address = "255.100.50.0"))


if __name__ == "__main__":
    main()