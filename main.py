from base.Shuang import Shuang
from base.People import People
from base.calculate import *
from decimal import Decimal
def main():
    #造爽
    shuang = Shuang(name="爽",sex="女",represent_works=['爽代表作'],represent_words=['哎呀烦死了！','我们只好做了一件好事情'])
    shuang.set_daily_salary(2080000)#日爽
    shuang.set_month_salary(2080000*30)#月爽
    shuang.set_year_salary(2080000*365)#年爽
    #造你
    zhangsan = People(name="张三",sex="男")
    salary = int(input("请输入你的月薪："))
    zhangsan.set_month_salary(salary)
    calresult = calculate(zhangsan.get_month_salary(), shuang.get_daily_salary())
    print("你一个月大约可以赚{}日{}".format(Decimal(calresult).quantize(Decimal('0.0000')),shuang.name))

if __name__ == '__main__':
    main()