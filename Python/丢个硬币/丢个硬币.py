import random,time,re
from typing import Mapping
def biu(n,Result):
    for i in range(0,n):
        seed=str(time.time()).split(".")
        random.seed(seed[1])
        result=(random.random())*100000000000000
        R=result%2*10000
        R=R%2
        Result.append(int(R))
if __name__ == "__main__":
    print(">",end="")
    input()
    Result=list()
    biu(100,Result)
    a0=0 ##
    a1=0
    for i in Result:
        if i==0:
            a0+=1
        else:
            a1+=1
    if a0>a1:
        print("反面")
    elif a0<a1:
        print("正面")
    else:
        print("竖起来了，再丢一次吧")
    