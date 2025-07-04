import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
start_date = datetime(2025, 7, 4)

months = 360
money = 1000000
total = 0
while(months > 0):
    lixi = money * 0.026 / 12
    total += lixi + 2278
    t1 = start_date + relativedelta(months=360-months+1)
    print(f'第 {360-months+1} 个月({t1.strftime("%Y-%m-%d")})，\t我欠银行 {int(money)} 元，\t应付利息 {int(lixi)} 元，\t应还本金 2778 元，\t本金加利息一共 {int(lixi) + 2778} 元')
    money -= money / months
    months -= 1

print(f'100W，30年 连本带息应付 {int(total)} 元')
