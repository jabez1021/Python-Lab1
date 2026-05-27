try:
    # 숫자로 이루어진 문자열은 에러가 발생하지 않음
    int("100")
    print("Try가 모두 실행되었습니다.")
except Exception as e:
    print("에러가 발생하였습니다.")
    print(e)
finally:
    print("Finally가 실행되었습니다.")
