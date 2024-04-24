my_list=input().split()
for i in range(0,len(my_list)):
    if int(my_list[i]>my_list[i-1]):
        print(my_list[i], end=" ")
