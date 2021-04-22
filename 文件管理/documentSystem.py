# DocumentSystem 2019/12/7
import os
import sys
import json
import shutil
import time

class Account:

    def __init__(self):
        self.name = ''
        self.key = ''
        self.allAccount = {}

    def saveAccout(self):  # 保存所有用户名和密码
        try:
            with open('accountMenu.txt', 'x') as fo:
                try:
                    key = self.name
                    value = self.key
                    self.allAccount.setdefault(key, value)

                    js = json.dumps(self.allAccount)  # 字典格式转换
                    fo.write(js)
                finally:
                    fo.close()
        except:
            with open('accountMenu.txt', 'r') as fo:  # 读出
                js = fo.read()
            fo.close()

            self.allAccount = json.loads(js)
            key = self.name
            value = self.key
            self.allAccount.setdefault(key, value)

            with open('accountMenu.txt', 'w') as fo:  # 写入
                js = json.dumps(self.allAccount)
                fo.write(js)
            fo.close()
        self.allAccount.clear()  # 清空字典缓存

    def createNewAccount(self):  # 创建新账户

        self.name = input("请输入用户名：")
        self.key = input("请输入用户密码：")

        aPath = self.name  # 账户文件夹地址

        isExists = os.path.exists(aPath)  # 判断账户文件夹是否存在

        if not isExists:
            os.makedirs(aPath)
            print('用户创建成功')

            self.saveAccout()  # 保存
        else:
            print('账户名已存在！！！')

            a = """
            1 重新创建
            2 返回登录
            """
            print(a)
            try:
                num = eval(input("请选择："))
            except:
                print('输入有误，请重新选择')
                num = eval(input("请选择："))

            while(1):
                if num == 1:
                    return 1

                if num == 2:
                    return 0

                if num != 1 or 2:
                    num = eval(input("输入有误，请重新输入："))

    def priAccount(self):
        menu = """
        ****************************************
                  二级文件管理系统
        ****************************************
                    1 账户登录
                    2 创建账户
                    3 查看账户
                    4 删除账户
                    5 关闭系统
        """
        print(menu)

        num = 0

        try:
            num = eval(input('请输入选项：'))
        except:
            print('输入有误，请重新选择')
            self.priAccount()

        if num == 1:
            num = self.loginAccount()

        if num == 2:
            a = 1
            while(a):
                a = self.createNewAccount()

        if num == 3:
            self.showAllAccount()

        if num == 4:
            self.delAccount()

        if num == 5:
            sys.exit(0)

        if num != 1 and num != 2 and num != 3 and num != 4 and num != 5 and num != 6:
            print("输入有误请重新输入!!!")

    def showAllAccount(self):  # 显示所有账户名
        try:
            with open('accountMenu.txt', 'r') as fo:
                try:
                    js = fo.read()
                finally:
                    fo.close()
            self.allAccount = json.loads(js)  # 转成字典

            print('已创建的账户有：')
            for key, value in self.allAccount.items():
                print(key)
        except:
            print('尚未创建账户')

        input('任意键返回')

    def delAccount(self):
        name = input('请输入删除的账户名称：')

        shutil.rmtree(name)  # 删除文件夹及所有子目录

        with open('accountMenu.txt', 'r') as fo:
            js = fo.read()
            self.allAccount = json.loads(js)
        fo.close()

        try:
            self.allAccount.pop(name)  # 删除对应字典
        except:
            print('改用户不存在')

        js = json.dumps(self.allAccount)

        with open('accountMenu.txt', 'w') as fo:
            fo.write(js)
        fo.close()

        print('%s账户已删除' % name)
        input('按任意键返回')

    def loginAccount(self):
        name = input('请输入账户名：')
        key = input('请输入密码：')

        with open('accountMenu.txt', 'r') as fo:
            js = fo.read()
        fo.close()

        self.allAccount = json.loads(js)  # 转换成字典

        try:
            exkey = self.allAccount.get(name)  # 获得字典对应账户值，如果字典中不存在，则报错

            if exkey == key:  # 判断密码是否正确
                print('***************************登录成功***************************')
                afile = file(name)  # 密码正确进入账户管理文件
                a = 1
                while(a):
                    a = afile.prifile()  # 调出文件目录
                    if a == 2:
                        return 5
                    if a == 3:
                        return 6
            else:
                if exkey == None:
                    print('用户未注册')
                    return 6
                else:
                    print('密码错误')
                    return 6
        except:
            print('未知错误')
            return 6

class file:
    def __init__(self, name):
        self.space = 512 * 1024  # 磁盘空间大小512KB
        self.filestate = 0  # 文件状态，是否打开
        self.filename = ''
        self.time = 0  # 创建时间
        self.accname = name
        self.beginspace = 0
        self.sizefile = 0
        self.filemode = 'r'
        self.fileAllSpace = 0
        self.list = []  # 列表格式文件信息
        self.text = 'none'

    def prifile(self):
        a = """
         mkdir filename_新建文件 格式：mkdir a1 100 rw,创建100字节的读写文件a1
         rm filename_删除文件
         cat filename_打开文件，查看内容
         write filename_写入文件内容
         fine filename_查看文件属性
         close filename_关闭文件
         ls_查看当前用户所有文件
         space_查看磁盘剩余
         return_退出登录，返回登录界面
         exit_退出程序
        """
        print(a)

        try:
            commond = input('输入命令：')
            commond = commond.split(' ')

            if commond[0] == 'mkdir':
                self.createfile(commond)
                return 1

            if commond[0] == 'rm':
                self.removefile(commond)
                return 1

            if commond[0] == 'cat':
                self.fileText(commond)
                return 1

            if commond[0] == 'write':
                self.writetext(commond)
                return 1

            if commond[0] == 'close':
                self.closefile(commond)
                return 1

            if commond[0] == 'fine':
                self.finefile(commond)
                return 1

            if commond[0] == 'ls':
                self.showALLfile()
                return 1

            if commond[0] == 'space':
                self.spacecheck()
                return 1

            if commond[0] == 'return':
                return 3

            if commond[0] == 'exit':
                return 2
        except:
            print('输入有误，请重新输入')
            return 1

    def fileMsg(self):  # 获取文件信息
        self.beginspace = self.fileAllSpace  # 文件的开始位置

        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间

    def createfile(self, commond):  # 创建新文件
        self.filename = commond[1]
        self.sizefile = commond[2]
        self.filemode = commond[3]
        flag = 0

        lis = []
        llis = []
        try:
            with open(self.accname + '/fileMsg.txt', 'r') as fo:
                for line in fo.readlines():
                    line = line.strip('\n')
                    line = line.strip('/')
                    lis.append(line)
            fo.close()
        except:
            flag = 0

        for i in lis:
            llis.append(i.split('/'))

        for i in llis:
            if i[0] == commond[1]:
                print('该文件已存在')
                flag = 1

        if flag == 0:
            str1 = str(self.filemode)

            if str1 != 'r' and str1 != 'w' and str1 != 'rw' and str1 != 'wr':
                print('文件属性错误，属性为r,w,rw,wr')
                input('回车键继续')
                return

            self.fileMsg()  # 获取文件信息

            str1 = self.filename + '/' + str(self.filestate) + '/' + str(self.beginspace) + '/' + str(
                self.sizefile) + '/' + self.filemode + '/' + str(self.time) + '/' + self.text + '/' + '\n'

            with open(self.accname + '/fileMsg.txt', 'a+') as fo:
                fo.write(str1)
            fo.close()

            try:
                with open('spaceMsg.txt', 'r') as fo:
                    self.fileAllSpace = int(fo.read())
                    self.fileAllSpace = self.fileAllSpace + int(self.sizefile)
                fo.close()

                self.saveSpace()
            except:
                self.fileAllSpace = self.fileAllSpace + int(self.sizefile)
                self.saveSpace()

            print('文件创建成功')

        input('回车键返回')

    def saveSpace(self):  # 已使用磁盘空间更新
        with open('spaceMsg.txt', 'w+') as fo:
            fo.write(str(self.fileAllSpace))
        fo.close()

    def readSpace(self):
        try:
            with open('spaceMsg.txt', 'r') as fo:
                self.fileAllSpace = int(fo.read())
            fo.close()
        except:
            print('磁盘空间获取失败')

    def readfile(self):  # 读取文件保存到列表
        lis = []
        self.list.clear()
        try:
            with open(self.accname + '/fileMsg.txt', 'r') as fo:
                for line in fo.readlines():
                    line = line.strip('\n')
                    line = line.strip('/')
                    lis.append(line)
            fo.close()
        except:
            print('该用户无文件')

        for i in lis:
            self.list.append(i.split('/'))

    def list2file(self):
        with open(self.accname + '/fileMsg.txt', 'w+') as fo:
            for i in self.list:  # 将列表转成字符串
                str1 = ''
                for j in i:
                    str1 = str1 + j + '/'
                fo.write(str1 + '\n')
        fo.close()

    def removefile(self, commond):  # 删除文件
        self.readfile()  # 获取文件信息列表

        self.readSpace()  # 获取文件已使用空间

        for i in self.list:  # 循环寻找要删的文件
            if i[0] == commond[1]:
                self.fileAllSpace = self.fileAllSpace - int(i[3])  # 计算磁盘空间
                self.saveSpace()  # 保存空间
                self.list.remove(i)  # 删除文件信息

        self.list2file()

        print('%s文件删除成功' % commond[1])

        input('回车键继续')

    def showALLfile(self):
        self.readfile()

        print('%s用户所有文件:' % self.accname)

        for i in self.list:
            print(i[0])

        input('回车键返回')

    def fileText(self, commond):  # 显示文件内容
        self.readfile()

        flag = 0
        for i in self.list:
            if i[0] == commond[1]:
                if i[4] == 'r' or i[4] == 'rw' or i[4] == 'wr':
                    i[1] = '1'
                    print(i[-1])
                    flag = 1
                    break
                else:
                    flag = 1
                    print('该文件为不可读文件')

        self.list2file()  # 保存至文件里

        if flag == 0:
            print('无此文件')

        input('输入回车继续')

    def writetext(self, commond):
        self.readfile()  # 读取文件

        for i in self.list:
            if commond[1] == i[0]:
                if i[1] == '1':
                    text = input('输入内容：')
                    i[-1] = text
                    print('文件写入成功')
                    self.list2file()
                else:
                    print('该文件未打开，请先打开文件')

    def closefile(self, commond):
        self.readfile()
        flag = 0

        for i in self.list:
            if i[0] == commond[1]:
                i[1] = '0'
                flag = 1

        if flag == 1:
            self.list2file()
            print('文件关闭成功')
        else:
            print('%s文件不存在' % commond[1])

    def finefile(self, commond):
        self.readfile()

        flag = 0

        for i in self.list:
            if i[0] == commond[1]:
                if i[1] == '1':
                    mode = '打开'
                else:
                    mode = '关闭'

                addr1 = int(i[2])  # 计算文件位置
                addr2 = int(i[2]) + int(i[3])

                flag = 1
                print('文件名：' + i[0]+ '\n' + '状态：%s' %mode + '\n' + '大小：'+ i[3] + '\n' +'位置: %d-%d' %(addr1, addr2) + '\n' +'属性：' + i[4] + '\n' + '创建时间：' + i[5] + '\n')

        if flag == 0:
            print('该文件不存在')

    def spacecheck(self):
        try:
            with open('spaceMsg.txt', 'r') as fo:
                space = fo.read()
            fo.close()
        except:
            print('磁盘尚未使用')

        print('磁盘大小：%d \n 磁盘剩余：%d' %(int(self.space), int(self.space)-int(space)))



if __name__ == '__main__':
    accout = Account()

    while(1):
        accout.priAccount()