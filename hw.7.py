shopping_bag = {}  # 장바구니 (상품명: 수량)

# 상품명과 수량을 입력받아 장바구니에 추가하는 함수
def add_to_shopping_bag(object, quantity):
    if object in shopping_bag:
        shopping_bag[object] += quantity
    else:
        shopping_bag[object] = quantity
    print(f"장바구니에 {object} {quantity}개가 담겼습니다.\n")

# 장바구니 내 상품의 수량을 검색하고 출력하는 함수
def print_quantity(object):
    if object in shopping_bag:
        print(f"{object}은(는) {shopping_bag[object]}개 담겼습니다.")
    else:
        print(f"{object}은(는) 장바구니에 없습니다.")

print("[구입]")
while True:
    object = input("상품명? ")
    if not object:
        break
    quantity = int(input("수량은? "))
    add_to_shopping_bag(object, quantity)  # 장바구니에 상품 추가

print("\n>>>장바구니 보기:", shopping_bag)

print("\n[검색]")
search_object = input("장바구니에서 확인하고자 하는 상품은? ")
print_quantity(search_object)


