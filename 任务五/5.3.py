a = input("请输入字符串：")#字符串用""转码

def isNum(a):
    n = type(eval(a))
    
    if n == type(1) or n == type(1.1) or n == type(1-5j):
        print(True)
    else:
        print(False)
def main():
    isNum(a)
    
main()
