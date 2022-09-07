import time
def DeretAjaib(x):
    if x < 6:
        return x
    else:
        return DeretAjaib(x-2) + DeretAjaib(x//2)
    
for i in range(1,100):
    a = DeretAjaib(7)
print(a,end=" ")


start = time.time()

end = time.time()
print()
print("waktu yang ditempuh ialah",end-start)