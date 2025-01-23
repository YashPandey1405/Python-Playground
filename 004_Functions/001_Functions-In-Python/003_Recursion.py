def Numbers(num):
    if(num==0):
        return
    print(num,end=" ")
    Numbers(num-1)

Numbers(10)