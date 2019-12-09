import operator
import numpy as np


def change_output(filename, N_TREES, data, run_num, the_rep):
    thenum=open(data,'r')
    fnum=int(thenum.readline().split(",")[1])
    thenum.close()
    with open(filename) as f:
        result_file=open("action.py",'w')
        result_file.write("import numpy as np\n")
        if the_rep == 1:
            result_file.write("def fix_vectors(a, b):\n")
            result_file.write("    if type(a) == float:\n")
            result_file.write("        a = [a]\n")
            result_file.write("    if type(b) == float:\n")
            result_file.write("        b = [b]\n")
            result_file.write("    shortest = min(len(a), len(b))\n")
            result_file.write("    a = a[:shortest]\n")
            result_file.write("    b = b[:shortest]\n")
            result_file.write("    return a, b\n")
        result_file.write("def add(a, b):\n")
        if the_rep == 1:
            result_file.write("    a, b = fix_vectors(a, b)\n")
        result_file.write("    return np.add(a, b)\n")
        result_file.write("def add_abs(a, b):\n")
        result_file.write("    return np.absolute(add(a, b))\n")
        result_file.write("def sub_abs(a, b):\n")
        result_file.write("    return np.absolute(subtract(a, b))\n")
        result_file.write("def subtract(a, b):\n")
        if the_rep == 1:
            result_file.write("    a, b = fix_vectors(a, b)\n")
        result_file.write("    return np.subtract(a, b)\n")
        result_file.write("def subtract_abs(a, b):\n")
        result_file.write("    return np.absolute(subtract(a,b))\n")
        result_file.write("def multiply(a, b):\n")
        if the_rep == 1:
            result_file.write("    a, b = fix_vectors(a, b)\n")
        result_file.write("    return np.multiply(a, b)\n")
        result_file.write("def maximum(a, b):\n")
        result_file.write("    return np.maximum(a, b)\n")
        result_file.write("def minimum(a, b):\n")
        result_file.write("    return np.minimum(a, b)\n")
        if the_rep == 0:
            result_file.write("def protected_div(a, b):\n")
            result_file.write("    x = 0.0\n")
            result_file.write("    if b == 0:\n")
            result_file.write("        x=1.0\n")
            result_file.write("    else:\n")
            result_file.write("        x=a/b\n")
            result_file.write("    return x\n")
        if the_rep == 1:
            result_file.write("def protectedDiv(a, b):\n")
            result_file.write("    a, b = fix_vectors(a, b)\n")
            result_file.write("    a, b = fix_vectors(a, b)\n")
            result_file.write("    x = []\n")
            result_file.write("    for i in range(len(a)):\n")
            result_file.write("        if b[i] == 0:\n")
            result_file.write("            x.append(1)\n")
            result_file.write("        else:\n")
            result_file.write("            x.append(a[i]/b[i])\n")
            result_file.write("    return x\n")
        result_file.write("def mt_if(a, b, c):\n")
        result_file.write("    return np.where(a < 0, b, c)\n")
        if the_rep == 1:
            result_file.write("def concat(a, b):\n")
            result_file.write("    a, b = fix_vectors(a, b)\n")
            result_file.write("    return np.concatenate((a, b))\n")
            result_file.write("def min_v(a, b):\n")
            result_file.write("    a, b = fix_vectors(a, b)\n")
            result_file.write("    x = []\n")
            result_file.write("    for i in range(len(a)):\n")
            result_file.write("        x.append(min(a[i], b[i]))\n")
            result_file.write("    return x\n")
            result_file.write("def max_v(a, b):\n")
            result_file.write("    a, b = fix_vectors(a, b)\n")
            result_file.write("    x = []\n")
            result_file.write("    for i in range(len(a)):\n")
            result_file.write("        x.append(max(a[i], b[i]))\n")
            result_file.write("    return x\n")
            result_file.write("def if_v(a, b, c):\n")
            result_file.write("    if type(a) == float:\n")
            result_file.write("        a = [a]\n")
            result_file.write("    if type(b) == float:\n")
            result_file.write("        b = [b]\n")
            result_file.write("    if type(c) == float:\n")
            result_file.write("        c = [c]\n")
            result_file.write("    l = min(len(a), len(b), len(c))\n")
            result_file.write("    x = []\n")
            result_file.write("    for i in range(l):\n")
            result_file.write("        if a[i] >= 0:\n")
            result_file.write("            x.append(b[i])\n")
            result_file.write("        else:\n")
            result_file.write("            x.append(c[i])\n")
            result_file.write("    return x\n")
        result_file.write("def ddd(N_TREES, data):\n")
        result_file.write("    data_file=open(data,'r')\n")
        result_file.write("    result_file=open('result_%d.txt','w')\n" %(run_num))
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
            b=f.readline()
            if not b:
                N_TREES=i
                break
            result_file.write("            a%d = " %(i+1))
            result_file.write(b)
            result_file.write("\n")
            if the_rep == 0:
                result_file.write("            reslist.append(str(a%d))\n"%(i+1))
            if the_rep == 1:
                result_file.write("            reslist.append(str(a%d[0]))\n"%(i+1))
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
        ddd(str(N_TREES),data)