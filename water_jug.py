'''

A Python Program to Solve the Water Jug Problem using 2 jugs.
Author: Rohit Kumar Bindal
Data: March 22nd, 2020
Time: 17:15:05

'''


class waterJug:
    def __init__(self,maxCapJug_1,maxCapJug_2,goal):
        self.maxCapJug_1 = maxCapJug_1
        self.maxCapJug_2 = maxCapJug_2
        self.goal = goal

    def fillJug(self, jug_1, jug_2):
        print("%d\t%d" % (jug_1, jug_2))
        if jug_1 == self.goal:
            return        
        elif jug_2 == self.goal:
            self.fillJug(jug_2, 0)
        elif jug_2<self.maxCapJug_2:
            self.fillJug(jug_1, self.maxCapJug_2)
        elif (jug_1+jug_2)<=self.maxCapJug_1 and jug_2>0:
            self.fillJug(jug_1+jug_2, 0)  
        elif (jug_1+jug_2)>=self.maxCapJug_1 and jug_2>0:
            self.fillJug(self.maxCapJug_1, jug_2-(self.maxCapJug_1-jug_1))


if __name__ == "__main__":
    capJug_1, capJug_2, target = 4 ,3 ,2
    waterJugs = waterJug(capJug_1,capJug_2,target)
    waterJugs.fillJug(0 ,0)