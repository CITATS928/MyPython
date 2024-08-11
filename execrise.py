import sys

testlist=[]
def insert(i,e):
    return testlist.insert(i,e)
    
def remove(e):
    return testlist.remove(e)
    
def append(e):
    return testlist.append(e)
    
#def sort(lst:list):
#    lst.sort
#    return sort(lst)
    
test1=[1,2,3]
print(test1)
if __name__ == '__main__':
    N = int(input())
    for i in range(0,N+1):
        lst=sys.stdin.readline().split(' ')
        if lst[0]=='insert':
            insert(int(lst[1]),int(lst[2]))
        elif lst[0]=='print':
            print(testlist)
        elif lst[0]=='sort':
            testlist.sort(key=int)
        elif lst[0]=='pop':
            testlist.pop(len(testlist-1))
        elif lst[0]=='remove':
            remove(int(lst[1]))
        elif lst[0]=='append':
            append(int(lst[1]))
        elif lst[0]=='reverse':
            testlist.reverse()