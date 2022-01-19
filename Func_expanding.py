#function expanding
def see(a):
    diff=a[1]-a[0]-1
    for i in range(1,len(a)):
        if diff<a[i]-a[i-1]:
            diff=a[i]-a[i-1]
        else:
            return(False)
    return (True)

a=list(map(int,input().split()))
print(see(a))

