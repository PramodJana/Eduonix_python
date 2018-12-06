item_catalog={"Blank CD's":7.99,"USB Drivers":12.50,"keyboards":18.00}
def exists_in(A,name):
    flag=0
    result=0
    for i in A:
        if (name==i):
            flag=1
            result=A[name]

    if flag==1:
        return result
    else:
        return "item is not present in the list"






print("please enter your choice")
for i in item_catalog:
    print (i)


choice=input()
print(exists_in(item_catalog,choice))
