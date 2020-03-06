'''
A Python program to find the number of states required to solve an n-Missionary Cannibal Problem
Author: Rohit Kumar Bindal
Data: February 15th, 2020
Time: 22:13:40
'''


import sys
import string
from collections import deque


states = [[], []]
dQ = deque()
nCannibals = 0
nMissionaries = 0
allowedOnBoat = 0
combinations = [ ]


def getCombindations():
    global allowedOnBoat, combinations

    for i in range(0,allowedOnBoat+1):
        for j in range(0,allowedOnBoat+1):
            if i+j>0 and i+j<=allowedOnBoat:
                combinations.append((i,j))


def initStates():
    global nCannibals, nMissionaries, states
    for i in range(0, nCannibals+1):
        states[0].append([])
        states[1].append([])
        for j in range(0, nMissionaries+1):
            states[0][i].append(-1)
            states[1][i].append(-1)


def validState(nCannibals, nMissionaries):
    return (nMissionaries>=nCannibals) or (nMissionaries==0) or (nCannibals==0)


def BFS():
    global dQ, states, nCannibals, mn, allowedOnBoat, combinations

    while (len(dQ) > 0) and states[1][nCannibals][nMissionaries] == -1:
        (x,y,depth,boat) = dQ.popleft()

        present = boat
        next = 1-boat

        if states[present][x][y] != -1:
            continue

        states[present][x][y] = depth

        for comb in combinations:
            (dx,dy) = comb

            if x>=dx and y>=dy:
                new_st = (nCannibals-(x-dx),nMissionaries-(y-dy),depth+1,next)
                (lx,ly) = (nCannibals-(x-dx),nMissionaries-(y-dy))
                (rx,ry) = (nCannibals-lx,nMissionaries-ly)

                if validState(lx, ly) and validState(rx, ry) \
                       and states[next][lx][ly] == -1:
                    dQ.append(new_st)



def main():
    global dQ, nCannibals, nMissionaries, allowedOnBoat, combinations, states
    input_val = input().split()
    # input_val = input_val.split
    nCannibals = int(input_val[0])
    nMissionaries = int(input_val[1])
    allowedOnBoat  = int(input_val[2])
    # print(input_val)
    initStates()
    getCombindations()

    dQ.append((nCannibals, nMissionaries, 0, 0))
    BFS()

    print(states[1][nCannibals][nMissionaries])
    # return 0


if __name__ == "__main__":
    sys.exit(main())