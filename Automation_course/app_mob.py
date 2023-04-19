def positive():
    print("Positive")

def negative():
    print("Negative")

def test():
    data = int(input("Enter integer: "))
    if data > 0:
        positive()
    elif data < 0:
        negative()

test()