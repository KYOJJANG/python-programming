import math

def get_radius(prompt):
    r = int(input(prompt))
    return r

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def get_circle_area(radius):
    return calculate_circle_area(radius)

def main():
    try:
        radius = get_radius("넓이를 구하고자 하는 원의 반지름은?: ")
        if radius < 0:
            print("반지름은 음수일 수 없습니다.")
            return
        area = get_circle_area(radius)
        print("반지름이", radius, "인 원의 넓이는:", area)
    except ValueError:
        print("반지름은 정수로 입력해주세요.")

if __name__ == "__main__":
    main()
