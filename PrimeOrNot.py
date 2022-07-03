import math


# If number is prime Print YES else print NO

def main():
    A = int(input('Enter a number: '))
    counter = 0

    for i in range(2, int(math.sqrt(A)), 1):
        print(A % i)
        if A % i == 0:
            counter += 1
            break
        if counter != 0:
            break
    if 0 == counter:
        print('YES')
    else:
        print('NO')
    return 0


if __name__ == '__main__':
    main()
