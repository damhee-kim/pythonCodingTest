# 배열에서 특정 요소 찾기
# 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False를 반환하시오.
def is_number_exist(number, array):

    for item in array: # array의 길이 만큼 아래 연산이 실행
        if item == number: # 비교 연산 1번 실행
         return True # 시간 복잡도는 N만큼 걸린다.

    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))