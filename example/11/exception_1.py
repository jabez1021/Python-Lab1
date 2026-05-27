try:
    # 숫자로 이루어지지 않은 문자열은 무조건 에러 발생
    int('abcd')
    print("Try가 모두 실행되었습니다.")
except Exception as e:
    print("에러가 발생하였습니다.")
    print(e)
finally:
    print("Finally가 실행되었습니다.")
