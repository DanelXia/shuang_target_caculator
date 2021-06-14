from base.People import People
# 具备一定影响力的人，抽象出一些特殊的私有属性，包括
class Shuang(People):
    def __init__(self,name,sex,represent_works,represent_words):
        super().__init__(name,sex)
        self.representative_works = represent_works
        self.fan_number = 0
        self.represent_words = represent_words
        self._law_breaker = False

    #代表性言辞
    def shuangyan_shuangyu(self):
        print(self.represent_words)

    #特殊技能，号召粉丝
    def skill_fan_Fan(self,):
        pass

    def __str__(self):
        str =  "1{}:{},月{}:{},日{}:{}".format(self.name,self.get_year_salary(),self.name,self.get_month_salary(),self.name,self.get_daily_salary())
        return str