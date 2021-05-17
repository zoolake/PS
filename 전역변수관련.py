def temp():
    a.append(1)
    #b += 1
    print(a)
    #print(b)

a = [3,2]
b = 1
temp()


# 리스트는 따로 global 처리 안해줘도 정상적으로 작동한다.
# 반면, 일반 변수는 global 처리를 안해주고 함수 내부에서 값을 재할당 하는 경우, 에러가 발생할 수 있다.
# 참고) https://otugi.tistory.com/249