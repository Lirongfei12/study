def get_week_with_date(y,m,d):
    '''根据年月日来计算星期几'''
    #把1、2 月当作上一年的13、14 月来使用
    y = y-1 if m ==1 or m ==2 else y
    m =13 if m==1 else (14 if m == 2 else m)
    #使用公式来计算星期机并返回，关于公式可以在网上搜索套用
    w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
    return w
def is_leap_year(y):
    '''判断一个年份是否是闰年'''
    if y %400 == 0 or (y % 4 ==0 and y % 100 != 0):
        return True
    return False
def get_days_in_month(y,m):
    '''获取指定月份的天数'''
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leap_year(y) else 28

year =int( input('请输入年份:'))
month =int( input('请输入月份:'))

days = get_days_in_month(year,month)
print("一 二 三 四 五 六 日")
print('-'*20)
for i in range(1,days +1):
    w=get_week_with_date(year,month,i)
    if i == 1:
        print(f"{' '*(w-1)*3}",end="")
    else:
        if w ==1:
            print("")
    print(f"{i:2d}",end=" ")
