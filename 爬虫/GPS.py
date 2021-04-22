import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

class Car:
    def __init__(self):
        self.names = ['粤B000H6', '粤B542T0', '粤B544C2', '粤B555S3', '粤B568W9', '粤B574U3', '粤B604U0', '粤B694E1', '粤B0703D',
                      '粤B712S3', '粤B726F2', '粤B755A7', '粤B789Z3', '粤B795E2', '粤B797A1', '粤B805E0', '粤B813E1', '粤B834W7',
                      '粤B854R7', '粤B864W2']
        self.time = []
        self.jd = []
        self.wd = []
        self.status = []  # 0代表空载，1代表重载
        self.v = []  # 车速
        self.angle = []  # 方向
        self.number = 0

    def read_file(self, num):  # 一辆车
        file = open("D:\\大二小学期\\python学习\\大作业2-车辆轨迹数据\\" + self.names[num] + ".txt", "r")  # 读入文件
        text = file.readlines()
        ss = []
        for i in range(1, len(text)):
            line = text[i].strip('\n')
            ss = line.split(',')
            self.time.append(ss[1])
            self.jd.append(eval(ss[2]))
            self.wd.append(eval(ss[3]))
            self.status.append(ss[4])
            self.v.append(ss[5])
            self.angle.append(ss[6])
            self.number += 1
        file.close()

    def mat_draw(self):
        x = self.jd
        y = self.wd
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_title('Shenzhen\'s road map')
        ax1.set_xlabel('Longitude')
        ax1.set_ylabel('latitude')
        ax1.scatter(x, y, s=1, c='k')  # 绘制数据点
        plt.xlim(xmax=114.25, xmin=113.8)  # x轴范围
        plt.ylim(ymax=22.75, ymin=22.47)  # y轴范围
        plt.show()

    def get_date(self):
        date = []
        h = []
        m = []
        for i in range(self.number):  # 条目数
            date_time = self.time[i].split(' ')
            date.append(int(date_time[0].split('/')[2]))  # 取某一天

            time = date_time[1]  # 取时间
            h_m_s = time.split(':')
            h.append(int(h_m_s[0]))
            m.append(int(h_m_s[1]))

        return date, h, m

    def average_t(self):
        vs = 0
        vnum = 0
        d, h, m = self.get_date()   # 获取时间日期
        for i in range(self.number):
            if d[i] == 18:
                if (m[i] >= 30 and h[i] == 8) or (m[i] <= 30 and h[i] == 9):
                    vs += int(self.v[i])
                    vnum += 1
        if vnum != 0:
            print('第3辆车平均速度为 %.2f km/h'% (vs / vnum))
        else:
            print("该车18号没有移动")

    def mean_var_median(self):
        days = [18, 19, 20, 21, 22, 23, 24, 25]
        lake = [0, 0, 0, 0, 0, 0, 0, 0]

        d, h, m = self.get_date()
        sum = 0
        for i in range(self.number):
            if 18 <= d[i] <= 25:
                if self.status[i] == '1' and self.status[i + 1] == '0':
                    lake[d[i] - 18] += 1

        for i in range(8):
            print("{}日拉客人数{}人次".format(days[i], lake[i]))
            sum += lake[i]
        print("均值{}".format((np.mean(lake))))
        print("方差{}".format(np.var(lake)))
        print("中位数{}".format(np.median(lake)))

    def histogram(self):
        lake = [0, 0, 0, 0, 0, 0, 0, 0]
        hours = ['0H', '3H', '6H', '9H', '12H', '15H', '18H', '21H']  # 组距

        d, h, m = self.get_date()

        for i in range(self.number):
            if d[i] <= 20:
                if d[i] == 20:
                    if self.status[i] == '1' and self.status[i + 1] == '0':
                        lake[h[i] // 3] += 1
                else:
                    continue
            else:
                break
        fig, ax = plt.subplots()

        ax.bar(hours, lake, 0.5)
        plt.show()

    def density(self, num):

        position = np.zeros(shape=(23, 17), dtype=int)

        time_s = np.zeros(48, dtype=int)

        if num == 5:
            for i in range(self.number):
                x = int((self.jd[i] - 113.788513) // 0.03)
                y = int((self.wd[i] - 22.468666) // 0.03)
                position[x][y] = position[x][y] + 1

            for i in range(self.number):
                if eval(self.v[i]) <= 15:
                    temp_time = int(self.time[i][11:13]) * 2 + int(self.time[i][14:16]) // 30
                    time_s[temp_time] += 1
                else:
                    continue

        elif num == 6:
            for i in range(self.number):
                if i + 1 != self.number:
                    if self.status[i] != self.status[i + 1]:
                        x = int((self.jd[i] - 113.788513) // 0.03)
                        y = int((self.wd[i] - 22.468666) // 0.03)
                        position[x][y] = position[x][y] + 1
        else:
            print("Wrong!")

        max = np.max(position)
        p = np.where(position == max)
        max_time = np.max(time_s)
        t = np.where(time_s == max_time)

        h = t[0][0] // 2
        m = 30 * (t[0][0] % 2)
        h_n = (t[0][0] + 1) // 2
        m_n = 30 * ((t[0][0] + 1) % 2)
        print("最拥堵的时间段是 {}时{}分 - {}时{}分".format(h, m, h_n, m_n))

        jd_min = 113.788513 + 0.03 * p[0][0]
        jd_max = 113.788513 + 0.03 * (p[0][0] + 1)
        jd_cent = (jd_max + jd_min) / 2
        wd_min = 22.468666 + 0.03 * p[1][0]
        wd_max = 22.468666 + 0.03 * (p[1][0] + 1)
        wd_cent = (wd_max + wd_min) / 2
        print("密度最大的区域是 \n纬度 {:.3f} - {:.3f}\n经度 {:.3f} - {:.3f}".format(wd_min, wd_max, jd_min, jd_max))
        print("中心点是 {:.3f}  {:.3f}".format(wd_cent, jd_cent))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)

        x = self.jd
        y = self.wd

        ax1.set_title('Road Profile Map of Shenzhen')
        ax1.set_xlabel('Longitude')
        ax1.set_ylabel('latitude')
        ax1.scatter(x, y, s=1, c='k', marker='.', )

        plt.xlim(xmax=114.25, xmin=113.8)
        plt.ylim(ymax=22.75, ymin=22.47)
        if num == 5:
            plt.gca().add_patch(plt.Rectangle((jd_cent, wd_cent), 0.03, 0.03, fill=False, edgecolor='r', linewidth=2))
        elif num == 6:
            plt.gca().add_patch(plt.Rectangle((jd_cent, wd_cent), 0.03, 0.03, fill=False, edgecolor='g', linewidth=2))
        else:
            print("Wrong!")
        plt.show()

    def draw_route(self, num):
        file = open("D:\\大二小学期\\python学习\\大作业2-车辆轨迹数据\\" + self.names[num] + ".txt", "r")
        print("\033[31m[INFO]\033[0m{}文件名为: ".format(num + 1) + self.names[num])
        text = file.readlines()
        x = []
        y = []
        v = []
        number = 0
        for i in range(1, len(text)):
            line = text[i].strip('\n')
            ss = line.split(',')
            if '2011/04/18 06:30' <= ss[1] <= '2011/04/18 09:30':
                x.append(eval(ss[2]))
                y.append(eval(ss[3]))
                # self.status.append(ss[4])
                v.append(eval(ss[5]))
                # self.angle.append(ss[6])
                number += 1
                print("\r得到{}个点".format(number), end='')
        file.close()
        if number != 0:
            print('\n')
            fig = plt.figure()
            ax1 = fig.add_subplot(1, 1, 1)
            plt.grid(True)  # 添加网格
            plt.pause(3)

            for i in range(len(x) - 1):
                print("\r正在绘制第{}个点".format(i + 1), end='')
                plt.cla()
                # 设置标题
                ax1.set_title('Road Profile Map of Shenzhen')
                ax1.set_xlabel('Longitude')
                ax1.set_ylabel('latitude')
                # 动态调整界面大小
                plt.xlim(xmax=np.max(x[:i + 1]) + 0.005, xmin=np.min(x[:i + 1]) - 0.005)
                plt.ylim(ymax=np.max(y[:i + 1]) + 0.005, ymin=np.min(y[:i + 1]) - 0.005)
                # ax1.scatter(x[i], y[i], s=1, color='b', marker='.')
                # 动态绘制图形
                # ax1.scatter(self.jd, self.wd, s=1, c='c', marker='.')
                ax1.plot(x[:i + 1], y[:i + 1], color='b')
                # plt.annotate("%d km/h" % v[i], xy=(x[i], y[i]), xytext=(0, 0), fontsize=6, color='m',textcoords="offset points")
                plt.text(x[i], y[i], '%d km' % v[i])
                plt.pause(0.001)
            plt.pause(0)
        else:
            print("该司机没有2011/04/18 06:30到2011/04/18 09:30的数据")


if __name__ == "__main__":

    n = eval((input("输入题号：")))

    car = Car()
    if n == 1:
        for i in range(20):
            car.read_file(i)
        car.mat_draw()
    elif n == 2:
        car.read_file(2)
        car.average_t()
    elif n == 3:
        car.read_file(0)
        car.mean_var_median()
    elif n == 4:
        car.read_file(0)
        car.histogram()
    elif n == 5:
        for i in range(20):
            car.read_file(i)
        car.density(5)
    elif n == 6:
        for i in range(20):
            car.read_file(i)
        car.density(6)
    elif n == 7:
        car.draw_route(0)
