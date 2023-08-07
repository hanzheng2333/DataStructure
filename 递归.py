def add(a, b):  # 2
    return a + b


def add(a, b, c):
    return a + b + c


array = [1, 2, 3, 4, 5]

'''
i = 1
while (i < 5):
    array[0] = array[0] + array[i]
    i = i + 1
'''


# arr[0] + ... + arr[index]
# arr[0= + ... + arr[index-1] + arr[index]
# add(arr,index-1] + arr[index]
def add(arr, index):
    if index == 0:
        return arr[index]
    return add(arr, index - 1) + arr[index]


# arr[i] + ... + arr[len-1]
# arr[i] + arr[i+1] + ... + arr[len-1]
def add(arr, i):
    if i == (len(arr) - 1):
        return arr[i]
    return arr[i] + add(arr, i + 1)


def f(n):
    if n == 1:
        return 1
    return f(n - 1) * n


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return f(n - 1) + f(n - 2)


# print(add(array,len(array)))
print(array)
print(add(array, 3))
print(f(3))
