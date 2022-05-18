listA = []
# Input number of elemetns
n = int(input("Enter number of elements in the list : "))
# iterating till the range
for i in range(0, n):
   print("Enter element No-{}: ".format(i+1))
   elm = int(input())
   listA.append(elm) # adding the element
print("The entered list is: \n",listA)
res = [ele for ele in listA if ele > 0]
print("The positive integers in the list: ",str(res))

