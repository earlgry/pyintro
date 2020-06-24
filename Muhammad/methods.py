def cSquared(x):
    return x*x


for i in range(10):
    print("{} squared is {}". format(i, cSquared(i)))
#basically for plugging in values in strings AKA .format



#importing function:

from first import square

#so when you import like this it runs the code in the file as well
#to avoid that you put other code in side a main function
#aka def main():
