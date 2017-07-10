import math

def isPrime(n):
    for x in range(1, int(math.sqrt(n) + 1)):
        if x!=1 and n%x == 0:
            return False
    return True

def getMonisen():
    sum=0
    P=2
    print ("P M")
    #print(P)
    while True:
        #print("before prime : ",P)
        if isPrime(P):
            #print(P)
            M=2**P-1
            #print("2**p - 1 =",M)
            if isPrime(M):
                print (P,M)
                sum+=1
                if sum==5:
                    break
        P+=1


getMonisen()
