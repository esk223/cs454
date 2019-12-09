def main(filename, N_TREES, data):
    thenum=open(data,'r')
    fnum=int(thenum.readline().split(",")[1])
    thenum.close()
    with open(filename) as f:
        result_file=open("action.py",'w')
        result_file.write("import numpy as np\n")
        result_file.write("def add(a, b):\n")
        result_file.write("    return np.add(a, b)\n")
        result_file.write("def add_abs(a, b):\n")
        result_file.write("    return np.absolute(add(a, b))\n")
        result_file.write("def sub_abs(a, b):\n")
        result_file.write("    return np.absolute(subtract(a, b))\n")
        result_file.write("def subtract(a, b):\n")
        result_file.write("    return np.subtract(a, b)\n")
        result_file.write("def subtract_abs(a, b):\n")
        result_file.write("    return np.absolute(subtract(a,b))\n")
        result_file.write("def multiply(a, b):\n")
        result_file.write("    return np.multiply(a, b)\n")
        result_file.write("def maximum(a, b):\n")
        result_file.write("    return np.maximum(a, b)\n")
        result_file.write("def minimum(a, b):\n")
        result_file.write("    return np.minimum(a, b)\n")
        result_file.write("def protected_div(a, b):\n")
        result_file.write("    x = 0.0\n")
        result_file.write("    if b == 0:\n")
        result_file.write("        x=1.0\n")
        result_file.write("    else:\n")
        result_file.write("        x=a/b\n")
        result_file.write("    return x\n")
        result_file.write("def mt_if(a, b, c):\n")
        result_file.write("    return np.where(a < 0, b, c)\n")
        result_file.write("def ddd(N_TREES, data):\n")
        result_file.write("    data_file=open(data,'r')\n")
        result_file.write("    result_file=open('result.txt','w')\n")
        result_file.write("    result_file.write('classLast,N_TREES,20,space\\n')\n")
        result_file.write("    data_file.readline()\n")
        result_file.write("    while True :\n")
        result_file.write("        reslist=list()\n")
        result_file.write("        line = data_file.readline()\n")
        result_file.write("        if line:\n")
        result_file.write("            tolist=line.split(" ")\n")
        for i in range(fnum+1):
            result_file.write("            f%d=float(tolist[%d])\n" %(i,i))
        for i in range(N_TREES):
            result_file.write("            a%d = " %(i+1))
            result_file.write(f.readline())
            result_file.write("\n")
            result_file.write("            reslist.append(str(a%d))\n"%(i+1))
        result_file.write("            a%d = f%d\n" %(N_TREES+1,fnum))
        result_file.write("            reslist.append(str(a%d))\n"%(N_TREES+1))
        result_file.write("            result_file.write(' '.join(reslist))\n")
        result_file.write("            result_file.write('\\n')\n")
        result_file.write("        else:\n")
        result_file.write("            break\n")
        result_file.write("    result_file.close()\n")
        result_file.write("    data_file.close()\n")
        result_file.close()
        from action import ddd
        ddd("7","10d20c.data")

        

if __name__ == "__main__":
    main("100_ind.txt",7,"10d20c.data")