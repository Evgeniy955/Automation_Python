pi=3.14
r = 5
h = 10
def cylinder():
    def circle():
        global c_circle
        c_circle = float(pi*r**2)
        return c_circle
    s = 2 * pi * r * h
    if input("Вы хотите получить боковую прощадь или полную плодадь? ") == "N":
        circle()
        s += 2 * c_circle
    print(s)

cylinder()