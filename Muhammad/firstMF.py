def main():
    print("Hello")
    print("what is your name")

    #name = input()
    #print(f"hello, {name}!")

    #variable called none which stores a none type: does not store any kind of values
    #python has 4 times of values..integers, floating, boolean, none
    #in python you dont need to specify value type

    x = 28

    print(f"{x}")
    if x>0:
        print("x is positive")
    elif x<0:
        print("x is negative")
    else:
        print("x is zero")

    name = "Alice"#string
    coordinates = (10.0, 20.0)
    names = ["Alice", "Ben", "Bongo"]#list

    letter = name[1]
    oneOftheNames = names[2]

    print(f"The Letter is: {letter} and one of the names is: {oneOftheNames}")

    for i in range(4):
        print(i)

    for aName in names:
        print(name)

    s = set()
    s.add(1)
    s.add(2)
    s.add(5)
    s.add(3)

    print(s)

    ages = {"Alice": 22, "Bob": 48}
    ages["Charlie"] = 30
    ages["Alice"]+= 1
    #or ages["Alice"] = ages["Alice"] + 1

    print(ages)

def square(x):
    return x*x
    
if __name__ == "__main__":
    main()
