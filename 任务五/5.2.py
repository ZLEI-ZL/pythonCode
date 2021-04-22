a = eval(input("请输入整数："))

def isOdd():
    if a % 2 != 0:
        return True
    else:
        return False
def main():
    b = isOdd()
    print(b)
    
main()
