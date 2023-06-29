import math
def autocorrelation(bits):
    n = len(bits)
    d = 1 #816 #2
    n_d = n - d;
    Ad = 0
    V = 0.0
    p = 0.0
    sqrt2 = 1.41421356237309504880;

    for i in range(n-d-1):
        Ad += int(bits[i]) ^ int(bits[i + d])

    V = 2 * (float(Ad) - float(n_d / 2)) / math.sqrt(n_d)

    p= math.erfc(math.fabs(V) / sqrt2)

    print(p)

    success = (p >= 0.01)
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
    s1, s2, s3 = Autocorrelation(bits)
    if s1 == True:
        print("通过检测,p value is %s" % s2)
    else:
        print("未通过检测")