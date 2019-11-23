num = 8
i = input("input range 1 to 9:")
try:
    int(i)
    ii = int(i)
    if(ii<8):
        print("too small")
    elif(ii>8):
        print("too big")
    else:
        print("yeah! that's 8!")
except:
    print("wrong input you motherfucker!")
