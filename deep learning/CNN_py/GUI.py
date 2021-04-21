from tkinter import *

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    # batch_size = 128  # 一批训练样本128张图片
    # epochs = 15  # 迭代轮数
    # init_lr = 0.000005  # 学习率
    # validation_split = 0.2
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("毕业设计")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #输入文本框
        #self.batch_size = Text(self.init_window_name, width=20, height=1)  #batch_size输入框
        Label(self.init_window_name, text='batch_size').grid(row=0, columnspan=2)  #batch_size输入框
        Entry(self.init_window_name).grid(row=0, column=1, columnspan=2)

        Label(self.init_window_name, text='epochs').grid(row=1, columnspan=2)  #epochs输入框
        Entry(self.init_window_name).grid(row=1, column=1, columnspan=2)

        Label(self.init_window_name, text='lr').grid(row=2, columnspan=2)
        Entry(self.init_window_name).grid(row=2, column=1, columnspan=2)  #学习率输入框

        Label(self.init_window_name, text='validation_split').grid(row=3, columnspan=2)  #validation_split输入框
        Entry(self.init_window_name).grid(row=3, column=1, columnspan=2)

        Button(self.init_window_name, text='开始训练').grid(row=4, column=1, columnspan=2)

        # 创建frame容器
        frmLT = Frame(width=500, height=320, bg='white')

        frmLT.grid(row=6, column=0, padx=1, pady=3)

        # #self.batch_size.grid(row=0, column=0, columnspan=20)
        # self.epochs = Text(self.init_window_name, width=20, height=1)  #epochs输入框
        # self.epochs.grid(row=5, column=0, columnspan=20)
        # self.init_lr = Text(self.init_window_name, width=20, height=1)  #lr输入框
        # self.init_lr.grid(row=10, column=0, columnspan=20)
        # self.validation_split = Text(self.init_window_name, width=20, height=1)  #validation_split输入框
        # self.validation_split.grid(row=15, column=0, columnspan=20)
        # #按钮
        # self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10)  # 调用内部方法  加()为直接调用
        # self.str_trans_to_md5_button.grid(row=1, column=11)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()