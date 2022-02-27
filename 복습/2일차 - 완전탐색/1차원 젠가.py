# 격자 안에서 터지고 떨어지는 경우 temp 배열을 이용하자!
# Step1. Temp 배열을 새로 만들어준다.(2차월 배열)
# Step2. 아래에서 위로 올라오면서, 비어있지 않을 때만 temp에 넣어줍니다. col의 가장 및에서부터 폭탄을 채워줌. row 값을 n-1에서부터 0으로 감소시키며 하나씩 조사, temp를 위한 temp_row를 정의하여 n-1부터 순서대로 1씩 감소하며 채울 수 있도록 함.
# Step3. Temp값을 기존 배열에 다시 옮겨준다.
# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
def cut_array(start_idx, end_idx):
    global end_of_array, numbers
    
    temp_arr = []
    
    # 구간 외의 부분만 temp 배열에 순서대로 저장합니다.
    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(numbers[i])

    # temp 배열을 다시 numbers 배열로 옮겨줍니다.
    end_of_array = len(temp_arr)
    for i in range(end_of_array):    
        numbers[i] = temp_arr[i]


# 두 번에 걸쳐 지우는 과정을 반복합니다.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을 삭제합니다.
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])