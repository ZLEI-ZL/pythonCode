# 先来先服务
class Process:
    def __init__(self, name, arrive_time, serve_time):
        self.name = name
        self.arrive_time = arrive_time
        self.serve_time = serve_time
        self.start_serve_time = -1
        self.finish_time = 0
        self.cycling_time = 0
        self.w_cycling_time = 0

'''# 输入
num = int(input("请输入任务个数:"))
i = 0
process_list = []
for i in range(num):
    pro = input("输入任务名字，提交时间，运行时间:")
    pr = pro.split(' ')
    # print(type(pr[1]))
    process = Process(pr[0], float(pr[1]), float(pr[2]))
    process_list.append(process)
    i += 1
#return process_list'''
process_list = []
process1 = Process(1, 2, 8)
process_list.append(process1)
process2 = Process(2, 8.5, 0.5)
process_list.append(process2)
process3 = Process(3, 9, 0.1)
process_list.append(process3)
process4 = Process(4, 9.5, 0.2)
process_list.append(process4)

# FCFS算法
process_list.sort(key = lambda x: x.arrive_time)  # 到达时间排序
'''for p in process_list:
    print(p.name, p.arrive_time, p.serve_time)'''
running_time = float(0)
pr = []
for p in process_list:  # 计算时间

    if running_time == 0:
        p.start_serve_time = p.arrive_time
        running_time = p.start_serve_time + p.serve_time
    else:
        p.start_serve_time = running_time
        running_time += p.serve_time
    p.finish_time = p.start_serve_time + p.serve_time
    p.cycling_time = p.finish_time - p.arrive_time
    p.w_cycling_time = p.cycling_time / p.serve_time
    pr.append(p)

# 输出
for p in pr:
    print('name:', p.name, 'arrive_time:', p.arrive_time, 'serve_time:', p.serve_time, 'start_serve_time:',
          round(p.start_serve_time, 1),
          'finish_time', round(p.finish_time, 1), 'cycling_time', round(p.cycling_time, 1), 'w_cycling_time',
          round(p.w_cycling_time, 1))
