def main():
    #write your code below this line
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    answer = sum(num1, num2, num3, num4)
    print("Sum: " + str(answer))

def sum(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

if __name__ == '__main__':
    main()
