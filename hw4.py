def rep_char(c, n):
    return c * n

def draw_line_string(msg):
    nstr = len(msg)
    rep_char('-', nstr)
    print(f' {msg} ')
    rep_char('-', nstr)

def main():
    name = input("Input his/her name: ")
    
    msg1 = f"Hello, {name},"
    msg2 = "Welcome to Seoul."

    line_length = max(len(msg1), len(msg2))
    line = '-' * (line_length*1 + 4)
    print(line)
    draw_line_string(msg1.ljust(line_length))
    draw_line_string(msg2.ljust(line_length))
    print(line)

if __name__ == "__main__":
    main()
