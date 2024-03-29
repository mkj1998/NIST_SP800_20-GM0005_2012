import math
#from scipy.special import gamma, gammainc, gammaincc
from decimal import *
from gamma_functions import *

def runsdistribution(bits):
    n = len(bits)
    e = [0]*n
    k = 0

    for i in range(n):
        e[i] = (n-i+3)/pow(2, i+2)
        if e[i] >= 5:
            k = i
        else :
            print("k = ", k, "break cal")
            break

    g = [0]*n
    b = [0]*n
    runFlag = bits[0];
    j = 1

    for l in range(1,n):
        if bits[l] != runFlag:
            if runFlag == 0:
                g[j] += 1
            elif runFlag == 1:
                b[j] += 1
            runFlag = bits[l]  
            j = 1
        else:
            j += 1

    sum_bi = 0.0
    sum_gi = 0.0
    for i in range(1, k+1):
        bit = b[i]
        et = e[i]
        sum_bi += pow(bit-et, 2)/et

    for i in range(1, k+1):
        git = g[i]
        et = e[i]
        sum_gi += pow(git-et, 2)/et
    v = sum_bi + sum_gi
    #print(float(v))
    p = gammaincc(k-1, float(v)/2.0)
    success = (p >= 0.01)
    print(p)
    #print(v)
    return success, p, None

def change(bits):
    new_bits = []
    n = 10**6
    N = int(n/len(bits))
    for i in range(N):
        new_bits += bits
    m = n - N*len(bits)
    new_bits += bits[:m]
    return new_bits

if __name__ == "__main__":
    bits = ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1',
            '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '1', '0',
            '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1',
            '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1',
            '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0',
            '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1',
            '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1',
            '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1',
            '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0',
            '0',
            '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0',
            '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1',
            '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1',
            '1', '0']
    #bits = change(bits)
    s1, s2, s3 = RunsDistribution(bits)
    if s1 == True:
        print("通过检测,p value is %s" % s2)
    else:
        print("未通过检测")
