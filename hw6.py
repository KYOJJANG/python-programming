def print_multiplication_table():
    for k in range(0, 5, 4):
        for i in range(1, 10):
            for j in range(2, 6):
                print(j+k, 'x', i, '=', str((j+k)*i).rjust(2), end='\t')
                if j == 5:
                    print()
        print()

print_multiplication_table()
