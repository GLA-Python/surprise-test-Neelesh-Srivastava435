#1  11  21  1211    111221
a=int(input("NUmber of terms you want"))
Value=1
print(Value)
while a>1:
    ans=""
    while Value>0:
        c=Value%10
        count=1
        Value//=10
        while Value>0 and Value%10==c:
            count+=1
            Value//=10
        ans=str(count)+str(c)+ans
    print(ans)
    Value=int(ans)
    a-=1



