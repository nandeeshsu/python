print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

def dummyFunction():
    print("dummyFunction called")

print("before __name__ guard")
#https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# if __name__ == '__main__':
#     functionA()
#     functionB()
dummyFunction()
print("after __name__ guard")

print("foo__name__:: " + __name__)