def checkNum(i):
    if (i%3!=0 and i%5!=0):
        return (i)
    if(i%3==0):
        return "Fixx"
    else:
         return "Fuzz"
for num in range(1,100):
    ans = checkNum(num)
    print(ans);
