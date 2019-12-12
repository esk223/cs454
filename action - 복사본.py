def fix_vectors(a, b):
    if type(a) == float:
        a = [a]
    if type(b) == float:
        b = [b]
    shortest = min(len(a), len(b))
    a = a[:shortest]
    b = b[:shortest]
    return a, b
def add(a, b):
    a, b = fix_vectors(a, b)
    return np.add(a, b)
def add_abs(a, b):
    return np.absolute(add(a, b))
def subtract(a, b):
    a, b = fix_vectors(a, b)
    return np.subtract(a, b)
def subtract_abs(a, b):
    return np.absolute(subtract(a,b))
def multiply(a, b):
    a, b = fix_vectors(a, b)
    return np.multiply(a, b)
def maximum(a, b):
    a, b = fix_vectors(a, b)
    return np.maximum(a, b)
def minimum(a, b):
    a, b = fix_vectors(a, b)
    return np.minimum(a, b)
def protectedDiv(a, b):
    a, b = fix_vectors(a, b)
    x = []
    for i in range(len(a)):
        if b[i] == 0:
            x.append(1)
        else:
            x.append(a[i]/b[i])
    return x
def mt_if(a, b, c):
    return np.where(a < 0, b, c)
def main(N_TREES, data):
	data_file=open(data,'r')
	result_file=open("result.txt",'w')
	result_file.write("classLast,N_TREES,20,space")
	data_file.readline()
	while True :
		reslist=list()
		line = data_file.readline()
		if line:
			tolist=line.strip()
result_file.write("            f%d=float(tolist[%d])", i)
			f1=float(tolist[1])
			f2=float(tolist[2])
			---
			f9=float(tolist[9])
            a1 = subtract(maximum(add(f0, f3), f1), f1)
			result_file.write(reslist.join(" "))
			
		else:
			break
	result_file.close()
	data_file.close()
	
	
		

		
	
	a1 = subtract(maximum(add(f0, f3), f1), f1)
	a2add(f8, add_abs(minimum(minimum(mt_if(maximum(add(maximum(f9, f4), maximum(f6, f8)), minimum(mt_if(f2, f2, f5), protected_div(f6, f9))), protected_div(protected_div(add_abs(f0, f6), maximum(f4, f0)), minimum(mt_if(f0, f5, f4), minimum(f5, f9))), protected_div(multiply(add_abs(f0, f6), protected_div(f1, f3)), subtract(protected_div(f1, f9), mt_if(f7, f8, -0.5757800062223395)))), add_abs(f3, f2)), sub_abs(add(multiply(maximum(add(0.5925673049711659, f0), sub_abs(0.4007392170743562, f8)), protected_div(subtract(f6, f8), minimum(f3, f2))), sub_abs(multiply(protected_div(f5, -0.8635971149996542), subtract(f2, f0)), minimum(sub_abs(f8, f9), add(f4, f0)))), add_abs(subtract(minimum(sub_abs(f1, f7), subtract(f9, f8)), mt_if(sub_abs(f6, f4), f0, minimum(f4, f9))), subtract(protected_div(add_abs(f8, f0), subtract(f7, f1)), protected_div(sub_abs(f0, f7), mt_if(f7, f5, f6)))))), add_abs(add_abs(add(add_abs(sub_abs(add(f8, f3), mt_if(f8, f0, f2)), protected_div(minimum(f9, 0.5259391074347315), protected_div(f8, f7))), add_abs(add(add(f7, f3), add(f3, f0)), maximum(minimum(f7, f0), add_abs(f9, f1)))), mt_if(mt_if(sub_abs(minimum(f4, 0.6141337373543381), add(f7, -0.421759150939057)), minimum(maximum(f7, f7), protected_div(f4, f0)), maximum(protected_div(f4, f9), minimum(f3, 0.41100852876798677))), subtract(multiply(add_abs(f1, f1), maximum(f3, f8)), protected_div(minimum(f0, f3), protected_div(f0, f3))), sub_abs(subtract(maximum(f6, f0), maximum(f8, f1)), sub_abs(minimum(f2, f6), add(f9, f7))))), add(maximum(subtract(add_abs(mt_if(f9, f5, f2), sub_abs(f5, f3)), subtract(multiply(f5, f8), mt_if(f8, f8, f8))), multiply(sub_abs(add(f0, f7), subtract(-0.0044416445232515755, f0)), add_abs(maximum(f6, f7), f3))), protected_div(subtract(minimum(protected_div(f5, f5), maximum(f5, f7)), subtract(sub_abs(f5, f4), add(-0.9243011544835997, f6))), add(sub_abs(add(f5, f7), maximum(f7, f0)), subtract(sub_abs(f3, f9), add_abs(f3, f5))))))))
	a3protected_div(sub_abs(add(minimum(add_abs(f2, f9), mt_if(f6, f4, f1)), add_abs(protected_div(f9, f1), maximum(f1, f1))), mt_if(sub_abs(sub_abs(-0.1417810217530313, f7), protected_div(0.9527204750313243, f3)), subtract(multiply(f3, f7), protected_div(f6, f6)), protected_div(subtract(f6, 0.9681161726560599), maximum(f7, f0)))), sub_abs(subtract(minimum(add(f2, f9), minimum(f2, f3)), sub_abs(sub_abs(sub_abs(maximum(f6, f5), minimum(f7, f0)), maximum(add(f1, 0.20171875623806823), multiply(minimum(f3, f3), sub_abs(f3, f3)))), subtract(f5, f9))), subtract(maximum(subtract(f2, f6), add_abs(f5, f7)), maximum(add_abs(f7, f7), subtract(f8, f9)))))
	a4:add_abs(maximum(minimum(subtract(protected_div(add(minimum(f4, f9), f5), mt_if(f0, f4, f4)), minimum(add(multiply(minimum(f3, f3), sub_abs(f3, f3)), f8), multiply(f4, f4))), maximum(multiply(subtract(f1, f5), protected_div(f5, f6)), f8)), minimum(multiply(add_abs(f0, f6), protected_div(f7, f3)), f4)), f8)
	a5:protected_div(subtract(multiply(subtract(sub_abs(multiply(0.026807086352760745, f8), add_abs(f6, f3)), sub_abs(add_abs(f3, f2), sub_abs(f2, f3))), subtract(maximum(add(f0, minimum(minimum(-0.7848234937871612, f3), add(f8, f5))), minimum(f9, f4)), multiply(minimum(f3, f3), sub_abs(f3, f3)))), add(protected_div(mt_if(maximum(f8, f0), protected_div(0.1701178639906884, f7), multiply(0.15286624574585184, f0)), maximum(add_abs(f8, f4), protected_div(f6, f3))), add(mt_if(sub_abs(f0, f0), mt_if(f9, f7, f3), maximum(f7, f3)), multiply(add(mt_if(minimum(0.17821782094459593, f5), subtract(f6, f1), maximum(f7, f3)), f0), subtract(f0, f4))))), minimum(add_abs(protected_div(f6, f1), protected_div(f3, f5)), protected_div(multiply(protected_div(minimum(f6, f1), subtract(f0, f6)), multiply(multiply(f9, f7), subtract(f3, f7))), subtract(maximum(add(f1, 0.20171875623806823), multiply(minimum(f3, f3), sub_abs(f3, f3))), protected_div(maximum(f2, f8), mt_if(f8, f5, f9))))))
	a6:maximum(f8, add(protected_div(multiply(f3, f4), f1), maximum(subtract(multiply(minimum(sub_abs(mt_if(f0, f2, -0.8436710500765563), protected_div(f0, f3)), sub_abs(maximum(f6, f5), minimum(f7, f0))), multiply(subtract(mt_if(f3, f7, f1), mt_if(f2, f0, f7)), mt_if(sub_abs(f8, f8), sub_abs(f7, f4), maximum(f4, f7)))), add_abs(protected_div(add(f8, f8), mt_if(subtract(f8, f3), sub_abs(-0.5642210168405601, f1), add(f2, f4))), add_abs(f9, maximum(minimum(f3, f9), multiply(f3, f5))))), maximum(subtract(protected_div(maximum(protected_div(f4, f3), add(f7, f2)), sub_abs(minimum(f2, f7), maximum(f3, f8))), protected_div(maximum(protected_div(f7, f1), sub_abs(f9, 0.6785947224547937)), protected_div(add(f0, f5), protected_div(f1, f4)))), mt_if(minimum(minimum(add_abs(f1, f3), protected_div(f3, f6)), multiply(add_abs(f5, f4), multiply(f1, f5))), multiply(multiply(add_abs(f3, f2), minimum(0.4394050609725839, f0)), sub_abs(add(f0, f6), protected_div(f6, f1))), add_abs(add_abs(protected_div(f7, f7), protected_div(f7, f0)), multiply(protected_div(f4, f4), subtract(f8, f8))))))))
	a7:subtract(add_abs(sub_abs(f5, multiply(protected_div(add_abs(protected_div(sub_abs(f8, -0.22253244143094064), minimum(f4, 0.7691604208982443)), add(add(f8, f2), sub_abs(f3, f2))), multiply(protected_div(add(f2, f2), sub_abs(f5, f0)), minimum(add_abs(f1, -0.6242884070212424), mt_if(f8, -0.3316264888092777, f8)))), sub_abs(protected_div(multiply(add(f9, f5), maximum(-0.34702959629404306, f5)), sub_abs(maximum(f2, f6), protected_div(0.3706951482251497, f2))), mt_if(f6, maximum(minimum(f7, f8), protected_div(f1, f2)), minimum(multiply(f7, f5), f1))))), mt_if(f8, f9, f3)), sub_abs(add_abs(f4, 0.15286624574585184), add(f4, f9)))