import os
import pickle

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = sum(s)
    return total / len(s) if s else 0

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(scores, filename):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    filename = 'score.bin'

    if os.path.exists(filename):
        print('[파일 읽기]')
        scores = load_scores(filename)
    else:
        print('[점수 입력]')
        scores = input_scores()

    print('\n[점수 출력]\n개인점수: ', end=' ')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')

    save_scores(scores, filename)

if __name__ == "__main__":
    main()
