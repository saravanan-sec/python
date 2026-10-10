def add(*nums):
    temp = 0
    for num in nums:
        temp = temp + num
    return temp

def arguments(**args):
    print(args)
    if 'two' in args:
        print("two irukkirathu"+args['two'])

print(add(1,2,3,4,5,6,7,2,33,22,45,78,44,87,5,4,7,9))
arguments(a="A", one="1", b="B", two="2")