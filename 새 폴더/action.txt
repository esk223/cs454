import numpy as np
def add(a, b):
    return np.add(a, b)
def add_abs(a, b):
    return np.absolute(add(a, b))
def sub_abs(a, b):
    return np.absolute(subtract(a, b))
def subtract(a, b):
    return np.subtract(a, b)
def subtract_abs(a, b):
    return np.absolute(subtract(a,b))
def multiply(a, b):
    return np.multiply(a, b)
def maximum(a, b):
    return np.maximum(a, b)
def minimum(a, b):
    return np.minimum(a, b)
def protected_div(a, b):
    x = 0.0
    if b == 0:
        x=1.0
    else:
        x=a/b
    return x
def mt_if(a, b, c):
    return np.where(a < 0, b, c)
def ddd(N_TREES, data):
    data_file=open(data,'r')
    result_file=open('result.txt','w')
    result_file.write('classLast,N_TREES,20,space\n')
    data_file.readline()
    while True :
        reslist=list()
        line = data_file.readline()
        if line:
            tolist=line.split()
            f0=float(tolist[0])
            f1=float(tolist[1])
            f2=float(tolist[2])
            f3=float(tolist[3])
            f4=float(tolist[4])
            f5=float(tolist[5])
            f6=float(tolist[6])
            f7=float(tolist[7])
            f8=float(tolist[8])
            f9=float(tolist[9])
            f10=float(tolist[10])
            a1 = subtract(f7, minimum(add_abs(f3, f4), mt_if(f5, f7, f9)))

            reslist.append(str(a1))
            a2 = add(f8, f7)

            reslist.append(str(a2))
            a3 = sub_abs(f4, add_abs(multiply(f7, f2), minimum(f7, f0)))

            reslist.append(str(a3))
            a4 = add_abs(maximum(multiply(f9, f4), minimum(f4, f4)), f8)

            reslist.append(str(a4))
            a5 = protected_div(subtract(multiply(subtract(sub_abs(multiply(0.026807086352760745, f8), add_abs(f6, f3)), sub_abs(add_abs(f3, f2), sub_abs(f2, f3))), subtract(maximum(add(f0, minimum(minimum(-0.7848234937871612, f3), add(f8, f5))), minimum(f9, f4)), multiply(minimum(f3, f3), sub_abs(f3, f3)))), add(protected_div(mt_if(sub_abs(f0, f6), protected_div(0.1701178639906884, f7), multiply(0.15286624574585184, f0)), maximum(add_abs(f8, f4), protected_div(f6, f3))), add(mt_if(sub_abs(f0, f0), mt_if(f9, f7, f3), maximum(f7, f3)), multiply(add(f5, f0), subtract(f0, f4))))), minimum(subtract(maximum(protected_div(multiply(f8, f1), subtract(f2, f5)), protected_div(add_abs(f3, f4), subtract(f0, f6))), sub_abs(protected_div(sub_abs(0.45143389927836397, f6), add_abs(f1, f9)), multiply(multiply(f1, f2), add(-0.5892713566545711, f5)))), protected_div(multiply(protected_div(minimum(f6, f4), subtract(f0, f6)), multiply(multiply(f9, f7), subtract(f3, f7))), subtract(f0, protected_div(maximum(f2, f8), mt_if(f8, f5, f9))))))

            reslist.append(str(a5))
            a6 = maximum(add_abs(maximum(multiply(f9, f4), minimum(f4, f4)), protected_div(add_abs(f4, f4), maximum(f2, f5))), add(protected_div(multiply(f3, f8), add_abs(f3, f9)), add(minimum(f7, f7), maximum(f2, f3))))

            reslist.append(str(a6))
            a7 = subtract(add_abs(sub_abs(f5, f4), mt_if(f1, f9, f3)), sub_abs(add_abs(f2, f5), add(f4, f1)))

            reslist.append(str(a7))
            a8 = f10
            reslist.append(str(a8))
            result_file.write(' '.join(reslist))
            result_file.write('\n')
        else:
            break
    result_file.close()
    data_file.close()
