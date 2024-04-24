my_list = input().split()
for i in range(0,len(my_list)):
    if int(i)%2==0:
        print(my_list[i], end=" ")
