import statistics


class School:
    def __init__(self, studentNumber):
        self.studentNumber = studentNumber

    def set_inputData(self):
        self.age = School.get_preper_input_data()
        self.ghad = School.get_preper_input_data()
        self.vazn = School.get_preper_input_data()

    def get_preper_input_data():
        inputString = list(input().split(' '))
        return list(map(lambda x:float(x), inputString))

    def calc_ave(self):
        self.aveAge = statistics.mean(self.age)
        self.aveGhad = statistics.mean(self.ghad)
        self.aveVazn = statistics.mean(self.vazn)

    def print_ave(self):
        print(self.aveAge)
        print(self.aveGhad)
        print(self.aveVazn)

    def get_aveAge(self):
        return self.aveAge

    def get_aveGhad(self):
        return self.aveGhad

    def get_aveVazn(self):
        return self.aveVazn
    

inputlen = int(input())
school_A = School(inputlen)
school_A.set_inputData()

inputlen = int(input())
school_B = School(inputlen)
school_B.set_inputData()

school_A.calc_ave()
school_B.calc_ave()

school_A.print_ave()
school_B.print_ave()

if school_A.get_aveGhad() > school_B.get_aveGhad():
    print('A')
elif school_A.get_aveGhad() < school_B.get_aveGhad():
    print('B')
else:
    if school_A.get_aveVazn() < school_B.get_aveVazn():
        print('A')
    elif school_A.get_aveVazn() > school_B.get_aveVazn():
        print('B')
    else:
        print('Same')
