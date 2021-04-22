# 时间片轮转调度

class Process:
    def __init__(self, name, arrive_time, serve_time):
        self.name = name
        self.arrive_time = arrive_time
        self.serve_time = serve_time
        self.start_serve_time = -1
        self.finish_time = 0
        self.cycling_time = 0
        self.w_cycling_time = 0
        self.time_slice = 0

'''# 输入
num = int(input("请输入任务个数:"))
i = 0
process_list = []
for i in range(num):
    pro = input("输入任务名字，提交时间，运行时间:")
    pl = pro.split(' ')
    # print(type(pr[1]))
    process = Process(pl[0], float(pl[1]), float(pl[2]))
    process_list.append(process)
    i += 1'''
process_list = []
process1 = Process('A', 0, 4)
process_list.append(process1)
process2 = Process('B', 1, 3)
process_list.append(process2)
process3 = Process('C', 2, 4)
process_list.append(process3)
process4 = Process('D', 3, 2)
process_list.append(process4)
process5 = Process('E', 4, 4)
process_list.append(process5)
num = 5


# 时间轮片算法
process_list.sort(key = lambda x: x.arrive_time)  # 按到达时间排序
pr = []  # 结果区
running_time = float(0)
time = 1
N = 0
while(1):
    for p in process_list:
        #print(p.time_slice)
        if N != -num and p.time_slice != -1:
            if running_time == 0:
                p.start_serve_time = p.arrive_time
                p.time_slice = time
                running_time = time
                if p.time_slice >= p.serve_time:
                    t = p.time_slice - p.serve_time
                    running_time -= t
                    p.finish_time = running_time
                    p.cycling_time = p.finish_time - p.arrive_time
                    p.w_cycling_time = p.cycling_time / p.serve_time
                    p.time_slice = -1
                    N += p.time_slice
                    pr.append(p)
            else:
                if p.start_serve_time == -1:
                    p.start_serve_time = running_time
                p.time_slice += time
                running_time += time
                if p.time_slice >= p.serve_time:
                    t = p.time_slice - p.serve_time
                    running_time -= t
                    p.finish_time = running_time
                    p.cycling_time = p.finish_time - p.arrive_time
                    p.w_cycling_time = p.cycling_time / p.serve_time
                    p.time_slice = -1
                    N += p.time_slice
                    pr.append(p)

        if N == -num:
            break

    if N == -num:
        break


# 输出
for p in pr:
    print('name:', p.name, 'arrive_time:', p.arrive_time, 'serve_time:', p.serve_time, 'start_serve_time:',
          round(p.start_serve_time, 1),
          'finish_time', round(p.finish_time, 1), 'cycling_time:', round(p.cycling_time, 1), 'w_cycling_time:',
          round(p.w_cycling_time, 1))