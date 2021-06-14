class People(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self._daily_salary = 0
        self._month_salary = 0
        self._year_salary = 0

    def set_daily_salary(self,daily_salary):
        self._daily_salary = daily_salary
    def get_daily_salary(self):
        return self._daily_salary
    def set_month_salary(self,month_salary):
        self._month_salary = month_salary
    def get_month_salary(self):
        return self._month_salary
    def set_year_salary(self,year_salary):
        self._year_salary = year_salary
    def get_year_salary(self):
        return self._year_salary
