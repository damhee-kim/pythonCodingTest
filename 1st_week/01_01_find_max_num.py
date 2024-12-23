# 배열 내에서 가장 큰 수를 반환하십시오.

## 1. 하나의 원소를 다른 원소들과 비교해서 최대인지 분석하는 방법
def find_max_num1(array):
    for number in array:
        is_max_num = True
        for compare_number in array:
            if compare_number > number:
                is_max_num = False
        if is_max_num:
            return number

print("정답 = 6 / 현재 풀이 값 = ", find_max_num1([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num1([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num1([6, 9, 2, 7, 1888]))


## 2. 하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법
def find_max_num2(array):
    max_number = array[0]
    for number in array:
        if number > max_number:
            max_number = number
    return max_number

print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num2([6, 9, 2, 7, 1888]))