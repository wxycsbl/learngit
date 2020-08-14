score=int(input("请输入需要的分值:"))
time=input("请输入时间(10年、年、季、月、周（以 , 分割）):").split(",")
ifor=input("请问是否需要去除广告图标(Y/N):")
if ifor=="Y" or ifor=="y":
    price=13
elif ifor=="N" or ifor=="n":
    price=11
else:
    print("请输入正确格式")

def cont_money():
    ten_years=int(time[0])
    years=int(time[1])
    quarters=int(time[2])
    months=int(time[3])
    weeks=int(time[4])
    a=go_ten(ten_years)
    b=go_year(years)
    c=go_quarter(quarters)
    d=go_month(months)
    e=go_week(weeks)
    count=a+b+c+d+e
    return count

def go_ten(ten_years):
    return score*ten_years*480*(price-5)

def go_year(years):
    money=0
    if years>9:
        money=go_ten(years//10)
        years=years%10
    return money+score*years*48*(price-3)

def go_quarter(quarters):
    money=0
    if quarters>3:
        money=go_year(quarters//4)
        quarters=quarters%4
    return money+score*quarters*12*(price-2)

def go_month(months):
    money=0
    if months>2:
        money=go_quarter(months//3)
        months=months%3
    return money+score*months*4*(price-1)

def go_week(weeks):
    money=0
    if weeks>3:
        money=go_month(weeks//4)
        weeks=weeks%4
    return money+score*weeks*price

print(cont_money())
wait=input()
