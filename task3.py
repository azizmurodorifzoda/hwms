my_list=input().split()
c=0
for i in range(0,len(my_list)):
    if int(my_list[i])>0:
        c+=1
print(c)
