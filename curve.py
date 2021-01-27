import numpy as np
import scipy.stats
import math
class curve:
    def __init__(self, mean, std, ming=0, maxg=100, grades = [], default=True, plus_minus=True):
        self.mean = mean
        self.std = std
        self.ming = ming
        self.maxg = maxg
        if (default == True and plus_minus == True):
            self.grade_boundaries = {
                10:"A",
                20:"A-",
                26:"B+",
                32:"B",
                38:"B-",
                44:"C+",
                50:"C",
                56:"C-",
                62:"D+",
                68:"D",
                74:"D-",
                80:"F",
            }
        elif (default == False and plus_minus == True):
            self.grade_boundaries = {
                grades[0]:"A",
                grades[1]:"A-",
                grades[2]:"B+",
                grades[3]:"B",
                grades[4]:"B-",
                grades[5]:"C+",
                grades[6]:"C",
                grades[7]:"C-",
                grades[8]:"D+",
                grades[9]:"D",
                grades[10]:"D-",
                grades[11]:"F",
            }
        elif (default == False and plus_minus == False):
                self.grade_boundaries = {
                grades[0]:"AA",
                grades[1]:"BA",
                grades[2]:"BB",
                grades[3]:"CB",
                grades[4]:"CC",
                grades[5]:"DC",
                grades[6]:"DD",
                grades[7]:"FD",
                grades[8]:"FF",
            }
        elif (default == True and plus_minus == False):
                self.grade_boundaries = {
                11:"AA",
                22:"BA",
                33:"BB",
                44:"CB",
                55:"CC",
                66:"DC",
                77:"DD",
                88:"FD",
                99:"FF",
            }
    def higher_probability(self, grade):
        #returns the probability of someone scoring higher than you
        table_grade = scipy.stats.norm.cdf(grade,self.mean,self.std)
        table_max = scipy.stats.norm.cdf(self.maxg,self.mean,self.std)
        table_min = scipy.stats.norm.cdf(self.ming,self.mean,self.std)



        #this part corresponds to:
        #P(grade < x < highest grade | lowestgrade < x < highest grade)
        if (grade >= self.mean):
            return (table_max - table_grade)  / (table_max + table_min)
        else:
            return (table_max + table_grade) / (table_max + table_min)

    def rank(self, grade, num): 

        if (grade >= self.maxg):
            return 1
        elif (grade <= self.ming):
            return num
        probability = self.higher_probability(grade)
        return round(num*probability + 1)

    def percentage(self, grade):
        return (self.higher_probability(grade) * 100)

    def grade(self,grade):
        percent = self.percentage(grade)
        for key in self.grade_boundaries.keys():
            if (percent < key):
                return self.grade_boundaries[key]

class curveObject:
    #class for any grade such as homeworks and exams
    def __init__(self, mean, std, weight, grade, ming=0, maxg=100):
        self.mean = mean
        self.std = std
        self.ming = ming
        self.maxg = maxg
        self.weight = weight
        self.grade = grade

class multiCurve(curve):
    def __init__(self, curveObjectList, num, grades = [], default=True, plus_minus=True):
        self.num = num
        self.c_grade = 0
        c_mean = 0
        c_var = 0
        c_ming = 0
        c_maxg = 0
        for obj in curveObjectList:
            c_mean += obj.mean * obj.weight
            c_var += (obj.weight * obj.std)**2
            self.c_grade += obj.grade * obj.weight
            c_ming += obj.ming * obj.weight
            c_maxg += obj.maxg * obj.weight
        curve.__init__(self, c_mean, math.sqrt(c_var), c_ming, c_maxg, grades, default, plus_minus)
    def rank(self):
        return curve.rank(self, self.c_grade,self.num)
    def grade(self):
        return curve.grade(self, self.c_grade)


        


    
    