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
    result_file=open('result_55.txt','w')
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
            a1 = multiply(protected_div(add_abs(maximum(maximum(add(f8, f9), minimum(f3, f6)), maximum(mt_if(f9, f7, f0), add_abs(f8, f9))), f6), add(subtract(add(add_abs(f6, f2), add_abs(f8, f2)), add(maximum(f3, f8), add_abs(f0, f6))), maximum(minimum(f6, f0), minimum(mt_if(f9, f8, f2), subtract(f4, f0))))), minimum(add_abs(multiply(minimum(sub_abs(f9, f1), mt_if(f8, f1, f8)), maximum(sub_abs(f6, f9), maximum(f8, f0))), subtract(sub_abs(add(f0, f6), subtract(f0, f6)), maximum(add_abs(0.1963262252182465, f7), subtract(f4, f0)))), maximum(sub_abs(sub_abs(mt_if(f4, f1, f1), protected_div(f8, f2)), subtract(mt_if(f4, f2, f2), minimum(f3, f2))), mt_if(multiply(minimum(f3, f3), subtract(f6, f9)), maximum(add_abs(f6, f7), mt_if(f4, f1, -0.4411283172696725)), protected_div(sub_abs(-0.5355545164071891, f2), sub_abs(-0.177181321315786, f2))))))

            reslist.append(str(a1))
            a2 = maximum(subtract(minimum(f6, f0), f3), f0)

            reslist.append(str(a2))
            a3 = maximum(0.08803865480573969, sub_abs(add_abs(f6, f3), minimum(f8, f0)))

            reslist.append(str(a3))
            a4 = multiply(minimum(subtract(minimum(sub_abs(minimum(f5, f6), add_abs(f2, f2)), maximum(subtract(f3, f3), protected_div(f7, f8))), subtract(protected_div(minimum(f2, f2), protected_div(f7, f2)), multiply(subtract(-0.10328484911415803, f3), sub_abs(f7, f7)))), add_abs(mt_if(add_abs(minimum(f6, f2), protected_div(f7, -0.40256687428925897)), protected_div(sub_abs(f8, f5), minimum(f0, f7)), multiply(sub_abs(f3, f7), subtract(f4, f7))), subtract(sub_abs(add(f2, f6), protected_div(f5, f8)), add(add_abs(-0.4338848615965041, f3), sub_abs(f3, f1))))), add(multiply(minimum(add_abs(add(f6, f9), add_abs(f3, f7)), sub_abs(maximum(f0, f6), mt_if(f5, f4, f0))), protected_div(subtract(add(f0, f8), multiply(f3, f4)), minimum(add_abs(f9, f3), minimum(f7, f8)))), protected_div(protected_div(subtract(minimum(f9, -0.21904026294474033), subtract(f3, f9)), multiply(add(f8, -0.029407999022061482), add(f8, f5))), protected_div(minimum(minimum(f2, f6), add(f7, f7)), subtract(protected_div(f0, f6), protected_div(f9, -0.12322320281449994))))))

            reslist.append(str(a4))
            a5 = add_abs(f5, f5)

            reslist.append(str(a5))
            a6 = protected_div(sub_abs(minimum(f6, f3), minimum(f7, f7)), multiply(sub_abs(sub_abs(protected_div(add(subtract(-0.6831881449431736, f8), sub_abs(f3, f8)), add_abs(minimum(f6, f3), multiply(f1, f6))), mt_if(sub_abs(maximum(f1, f5), add(f1, f6)), add_abs(protected_div(f0, -0.20046779837457507), subtract(f4, f2)), multiply(add(f0, f1), minimum(f0, f8)))), mt_if(add_abs(add(protected_div(f9, f7), multiply(f6, f8)), multiply(add(f8, f3), subtract(f8, f8))), add_abs(minimum(maximum(f9, f0), subtract(f8, f8)), multiply(mt_if(f7, f1, f0), multiply(f6, f5))), protected_div(mt_if(add(f8, f1), protected_div(f5, f6), multiply(f7, f2)), mt_if(subtract(f6, f7), mt_if(f0, f4, f7), minimum(f2, f7))))), subtract(mt_if(mt_if(add_abs(minimum(f3, f9), protected_div(f9, f5)), maximum(mt_if(f8, -0.605691914620694, f8), mt_if(f0, f0, f6)), minimum(mt_if(f5, f1, f9), subtract(f2, f0))), multiply(mt_if(mt_if(0.22189536239560104, f9, f3), subtract(f2, f8), sub_abs(f9, 0.7165048594374064)), subtract(mt_if(f5, f5, f0), multiply(f9, f4))), minimum(multiply(add(f2, f6), mt_if(f8, f3, f5)), sub_abs(protected_div(f9, f7), minimum(f6, f8)))), multiply(add_abs(maximum(maximum(f6, f9), protected_div(f3, f8)), subtract(add_abs(f7, f6), subtract(f7, f3))), multiply(protected_div(mt_if(f3, f1, -0.28008156203724077), add(f6, f0)), multiply(add(f8, f3), sub_abs(f8, f8)))))))

            reslist.append(str(a6))
            a7 = add(maximum(minimum(multiply(multiply(f4, f6), minimum(f8, f1)), mt_if(protected_div(f0, f2), protected_div(f2, f8), add(f5, f0))), multiply(sub_abs(sub_abs(f1, f5), minimum(0.5729570664392782, f9)), mt_if(multiply(f7, f8), mt_if(f4, f0, f2), minimum(f5, f6)))), protected_div(sub_abs(add_abs(protected_div(f3, f6), multiply(f0, f5)), subtract(protected_div(f2, f4), subtract(f9, f6))), mt_if(sub_abs(protected_div(f0, f0), multiply(f5, f2)), add_abs(protected_div(f5, f1), maximum(f9, f8)), minimum(multiply(f5, f4), protected_div(-0.06645815700228042, f3)))))

            reslist.append(str(a7))
            a8 = f10
            reslist.append(str(a8))
            result_file.write(' '.join(reslist))
            result_file.write('\n')
        else:
            break
    result_file.close()
    data_file.close()
