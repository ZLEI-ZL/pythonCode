# 多解反馈队列调度

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
process1 = Process('1', 8, 2)
process_list.append(process1)
process2 = Process('2', 8.5, 0.5)
process_list.append(process2)
process3 = Process('3', 9, 0.1)
process_list.append(process3)
process4 = Process('4', 9.5, 0.2)
process_list.append(process4)
num = 4


# 多解反馈队列算法
process_list.sort(key = lambda x: x.arrive_time)  # 按到达时间排序
pr = []  # 结果区
buffer_list_1 = []  # 缓冲区1
buffer_list_2 = []  # 缓冲区2
running_time = 0
time = 1
finishtime = 0
if process_list != []:
    for p in process_list:
        p.start_serve_time = process_list[0].arrive_time + running_time
        # print(p.start_serve_time)
        running_time += time
        p.time_slice += time
        if p.time_slice >= p.serve_time:
            t = p.time_slice - p.serve_time
            running_time -= t
            p.finish_time = p.start_serve_time + p.serve_time
            # print(p.finish_time)
            p.cycling_time = p.finish_time - p.arrive_time
            p.w_cycling_time = p.cycling_time / p.serve_time
            pr.append(p)
            finishtime = p.finish_time
        else:
            buffer_list_1.append(p)

    if buffer_list_1 != []:
        for p in buffer_list_1:
            running_time += (time * 2)
            p.time_slice += (time * 2)
            if p.time_slice >= p.serve_time:
                t = p.time_slice - p.serve_time
                running_time -= t
                p.finish_time = p.start_serve_time + running_time
                p.cycling_time = p.finish_time - p.arrive_time
                p.w_cycling_time = p.cycling_time / p.serve_time
                pr.append(p)
            else:
                buffer_list_2.append(p)

            while(1):
                if buffer_list_2 != []:
                    for p in buffer_list_2:
                        running_time += (time * 4)
                        p.time_slice += (time * 4)
                        if p.time_slice >= p.serve_time:
                            t = p.time_slice - p.serve_time
                            running_time -= t
                            p.finish_time = p.start_serve_time + running_time
                            p.cycling_time = p.finish_time - p.arrive_time
                            p.w_cycling_time = p.cycling_time / p.serve_time
                            pr.append(p)
                            buffer_list_2.pop(p)
                else:
                    break

else:
    print("no task")




# 输出
for p in pr:
    print('name:', p.name, 'arrive_time:', p.arrive_time, 'serve_time:', p.serve_time, 'start_serve_time:',
          round(p.start_serve_time, 1),
          'finish_time', round(p.finish_time, 1), 'cycling_time:', round(p.cycling_time, 1), 'w_cycling_time:',
          round(p.w_cycling_time, 1))