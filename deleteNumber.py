#program to delete unsecessary 0 before value
def DeleteNumber(n):
    for i in range(len(n)):
        while n[i]==0:  
            del n[i]
        break
    return n
