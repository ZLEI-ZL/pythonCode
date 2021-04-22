from datetime import datetime

D = datetime(2019, 7, 3, 22, 33, 32)

print(D.strftime("%Y-%m-%d %H:%M:%S"))
print(D.strftime("%Y %m %d %H:%M:%S"))
print(D.strftime("%Y~%m~%d %H %M %S"))
print(D.strftime("%Y~%m~%d %H:%M:%S"))
print(D.strftime("%Y-%m-%d %H~%M~%S"))
