def read_single_digit(digit):
    digit_dict = {'0': '영', '1': '일', '2': '이', '3': '삼', '4': '사', '5': '오', '6': '육', '7': '칠', '8': '팔', '9': '구'}
    return digit_dict[str(digit)]

def read_number(number):
    result = ''
    
    if number // 100 > 0:
        result += read_single_digit(number // 100)
        number %= 100
    
    if number // 10 > 0:
        result += ' ' + read_single_digit(number // 10)
        number %= 10
    
    if number > 0:
        result += ' ' + read_single_digit(number)
    return result.strip()


def main():
    try:
        number = int(input("세 자리 정수 입력: "))
        if number < 0 or number > 999:
            raise ValueError("입력한 값은 세 자리 정수가 아닙니다.")
        
        
        print(read_number(number))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
