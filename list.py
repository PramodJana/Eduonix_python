list1=[2,4,6]
print(list1[1])
print(len(list1))
list1.append(69)
print(len(list1))
print(list1)
print(list1.pop())
print(list1)
print("-------------")


print("------------------")

def sumvalues(A):
    result=0
    for i in A:
        result+= i
    return result


print("enter the numbers")
A=[1,2,5,2,8,2,58,85,55]
print(sumvalues(A))
