# 1. 오른쪽으로 특정 횟수만큼 shift (길이가 최소가 되도록)
# 2. encording
# 3. 적용 후 길이
n = input()
minNum = []
# #문자 개수 세기


def run_Length_Encoding(n):
    cnt = 1
    st = ''
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            cnt += 1
        else:
            cnt = str(cnt)
            st = st + n[i-1] + cnt
            cnt = 1
    cnt = str(cnt)
    st = st + n[i-1] + cnt

    return len(st)



# #한 칸씩 넘겨보면서 개수를 세 보기. n+1까지
for i in range(len(n)+1):
    if len(n) == 1: #1일 때 예외 처리
        minNum.append(2)
        break
    minNum.append(run_Length_Encoding(n))
    n = n[-1] + n[:-1] #오른쪽으로 shift
    # temp = n[-1]
    # for j in range(len(n)-1, 0, -1):
    #     n[j] = n[j-1]
    # n[0] = temp
    
print(min(minNum))
