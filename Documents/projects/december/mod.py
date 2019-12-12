def is_even(n):
    if n % 2 == 1:
        return True
    else:
        return False

print(is_even(4))
jaha = [2,4,6,8,7,10]
res = []
def evens (numbers):
    for i in numbers:
        if i % 2 ==0:
            res.append(i)
    return res

print(evens(jaha))

