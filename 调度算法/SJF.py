# 短作业优先
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
    pl = pro.split(' ')
    # print(type(pr[1]))
    process = Process(pl[0], float(pl[1]), float(pl[2]))
    process_list.append(process)
    i += 1'''
process_list = []
process1 = Process(1, 8, 2)
process_list.append(process1)
process2 = Process(2, 8.5, 0.5)
process_list.append(process2)
process3 = Process(3, 9, 0.1)
process_list.append(process3)
process4 = Process(4, 9.5, 0.2)
process_list.append(process4)

# SJF算法
process_list.sort(key = lambda x: x.arrive_time)  # 按照到达时间排序
running_time = float(0)
buffer_list = []  # 缓存区
pr = []  # 结果区
while(1):
    #print(pr)
    if pr == []:
        buffer_list.append(process_list [0])
        buffer_list[0].start_serve_time = buffer_list[0].arrive_time  # 开始时间
        running_time = buffer_list[0].start_serve_time + buffer_list[0].serve_time
        buffer_list[0].finish_time = buffer_list[0].start_serve_time + buffer_list[0].serve_time  # 结束时间
        buffer_list[0].cycling_time = buffer_list[0].finish_time - buffer_list[0].arrive_time  # 周转时间
        buffer_list[0].w_cycling_time = buffer_list[0].cycling_time / buffer_list[0].serve_time  # 带权周转时间
        #finish_time = buffer_list[0].finish_time
        pr.append(buffer_list[0])
        buffer_list.clear()
        process_list.pop(0)
    else:
        while(1):
            if process_list != [] and process_list[0].arrive_time <= running_time:
                buffer_list.append(process_list[0])
                process_list.pop(0)
            else:
                if buffer_list != []:
                    buffer_list.sort(key = lambda x: x.serve_time)  # 按照运行时间排序
                    for p in buffer_list:
                        p.start_serve_time = running_time
                        running_time += p.serve_time
                        p.finish_time = running_time
                        p.cycling_time = p.finish_time - p.arrive_time
                        p.w_cycling_time = p.cycling_time / p.serve_time
                        pr.append(p)
                    buffer_list.clear()
                else:
                    break
    if process_list == [] and buffer_list == []:
        break

# 输出
for p in pr:
    print('name:', p.name, 'arrive_time:', p.arrive_time, 'serve_time:', p.serve_time, 'start_serve_time:',
          round(p.start_serve_time, 1),
          'finish_time', round(p.finish_time, 1), 'cycling_time', round(p.cycling_time, 1), 'w_cycling_time',
          round(p.w_cycling_time, 1))