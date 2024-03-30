def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("정수를 입력하세요.")

def exchange(amount):
    # 500원짜리 동전의 개수 계산
    num_500_coins = amount // 500
    remaining_amount = amount % 500
    
    # 100원짜리 동전의 개수 계산
    num_100_coins = remaining_amount // 100
    remaining_amount %= 100
    
    # 50원짜리 동전의 개수 계산
    num_50_coins = remaining_amount // 50
    remaining_amount %= 50
    
    # 10원짜리 동전의 개수 계산
    num_10_coins = remaining_amount // 10
    
    # 결과 출력
    print("500원짜리 동전 개수:", num_500_coins)
    print("100원짜리 동전 개수:", num_100_coins)
    print("50원짜리 동전 개수:", num_50_coins)
    print("10원짜리 동전 개수:", num_10_coins)

# 사용자로부터 입력 받기
amount = get_integer("동전으로 교환하고자 하는 금액은?: ")

# 함수 호출하여 각 동전의 개수 계산 및 출력
exchange(amount)
