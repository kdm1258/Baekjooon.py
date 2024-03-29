# k = n이 주어졌을 때 임의의 값 k 부터 덧셈을 한다고 가정
# l = k ~ k+m 까지의 길이

import sys
n, l = map(int,input().split())
k=-1
for m in range(l-1,100):
    start = 0
    end = n
    while(end>=0):          #end가 음수가 되면 음수를 포함한 리스트를 출력할 수 있음 ex) 5 5 -> -1 0 1 2 3 
        mid = (end + start) // 2
        if(k==mid):         #1,000,000,000을 이분탐색했을때 499999999에서 무한루프 발생
            break
        k = mid
        if((m+2*k)*(m+1)/2 == n):
            for i in range(m+1):
                print(k+i, end=' ')
            sys.exit()
        elif ((m+2*k)*(m+1)/2 < n):
            start = mid+1
        elif ((m+2*k)*(m+1)/2 > n):
            end = mid -1
print(-1)
