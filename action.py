import numpy as np
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
def sub_abs(a, b):
    return np.absolute(subtract(a, b))
def subtract(a, b):
    a, b = fix_vectors(a, b)
    return np.subtract(a, b)
def subtract_abs(a, b):
    return np.absolute(subtract(a,b))
def multiply(a, b):
    a, b = fix_vectors(a, b)
    return np.multiply(a, b)
def maximum(a, b):
    return np.maximum(a, b)
def minimum(a, b):
    return np.minimum(a, b)
def protectedDiv(a, b):
    a, b = fix_vectors(a, b)
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
def concat(a, b):
    a, b = fix_vectors(a, b)
    return np.concatenate((a, b))
def min_v(a, b):
    a, b = fix_vectors(a, b)
    x = []
    for i in range(len(a)):
        x.append(min(a[i], b[i]))
    return x
def max_v(a, b):
    a, b = fix_vectors(a, b)
    x = []
    for i in range(len(a)):
        x.append(max(a[i], b[i]))
    return x
def if_v(a, b, c):
    if type(a) == float:
        a = [a]
    if type(b) == float:
        b = [b]
    if type(c) == float:
        c = [c]
    l = min(len(a), len(b), len(c))
    x = []
    for i in range(l):
        if a[i] >= 0:
            x.append(b[i])
        else:
            x.append(c[i])
    return x
def ddd(N_TREES, data):
    data_file=open(data,'r')
    result_file=open('result_58.txt','w')
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
            f11=float(tolist[11])
            f12=float(tolist[12])
            f13=float(tolist[13])
            f14=float(tolist[14])
            f15=float(tolist[15])
            f16=float(tolist[16])
            f17=float(tolist[17])
            f18=float(tolist[18])
            f19=float(tolist[19])
            f20=float(tolist[20])
            f21=float(tolist[21])
            f22=float(tolist[22])
            f23=float(tolist[23])
            f24=float(tolist[24])
            f25=float(tolist[25])
            f26=float(tolist[26])
            f27=float(tolist[27])
            f28=float(tolist[28])
            f29=float(tolist[29])
            f30=float(tolist[30])
            f31=float(tolist[31])
            f32=float(tolist[32])
            f33=float(tolist[33])
            f34=float(tolist[34])
            f35=float(tolist[35])
            f36=float(tolist[36])
            f37=float(tolist[37])
            f38=float(tolist[38])
            f39=float(tolist[39])
            f40=float(tolist[40])
            f41=float(tolist[41])
            f42=float(tolist[42])
            f43=float(tolist[43])
            f44=float(tolist[44])
            f45=float(tolist[45])
            f46=float(tolist[46])
            f47=float(tolist[47])
            f48=float(tolist[48])
            f49=float(tolist[49])
            f50=float(tolist[50])
            f51=float(tolist[51])
            f52=float(tolist[52])
            f53=float(tolist[53])
            f54=float(tolist[54])
            f55=float(tolist[55])
            f56=float(tolist[56])
            f57=float(tolist[57])
            f58=float(tolist[58])
            f59=float(tolist[59])
            f60=float(tolist[60])
            f61=float(tolist[61])
            f62=float(tolist[62])
            f63=float(tolist[63])
            f64=float(tolist[64])
            f65=float(tolist[65])
            f66=float(tolist[66])
            f67=float(tolist[67])
            f68=float(tolist[68])
            f69=float(tolist[69])
            f70=float(tolist[70])
            f71=float(tolist[71])
            f72=float(tolist[72])
            f73=float(tolist[73])
            f74=float(tolist[74])
            f75=float(tolist[75])
            f76=float(tolist[76])
            f77=float(tolist[77])
            f78=float(tolist[78])
            f79=float(tolist[79])
            f80=float(tolist[80])
            f81=float(tolist[81])
            f82=float(tolist[82])
            f83=float(tolist[83])
            f84=float(tolist[84])
            f85=float(tolist[85])
            f86=float(tolist[86])
            f87=float(tolist[87])
            f88=float(tolist[88])
            f89=float(tolist[89])
            f90=float(tolist[90])
            f91=float(tolist[91])
            f92=float(tolist[92])
            f93=float(tolist[93])
            f94=float(tolist[94])
            f95=float(tolist[95])
            f96=float(tolist[96])
            f97=float(tolist[97])
            f98=float(tolist[98])
            f99=float(tolist[99])
            f100=float(tolist[100])
            f101=float(tolist[101])
            f102=float(tolist[102])
            f103=float(tolist[103])
            f104=float(tolist[104])
            f105=float(tolist[105])
            f106=float(tolist[106])
            f107=float(tolist[107])
            f108=float(tolist[108])
            f109=float(tolist[109])
            f110=float(tolist[110])
            f111=float(tolist[111])
            f112=float(tolist[112])
            f113=float(tolist[113])
            f114=float(tolist[114])
            f115=float(tolist[115])
            f116=float(tolist[116])
            f117=float(tolist[117])
            f118=float(tolist[118])
            f119=float(tolist[119])
            f120=float(tolist[120])
            f121=float(tolist[121])
            f122=float(tolist[122])
            f123=float(tolist[123])
            f124=float(tolist[124])
            f125=float(tolist[125])
            f126=float(tolist[126])
            f127=float(tolist[127])
            f128=float(tolist[128])
            f129=float(tolist[129])
            f130=float(tolist[130])
            f131=float(tolist[131])
            f132=float(tolist[132])
            f133=float(tolist[133])
            f134=float(tolist[134])
            f135=float(tolist[135])
            f136=float(tolist[136])
            f137=float(tolist[137])
            f138=float(tolist[138])
            f139=float(tolist[139])
            f140=float(tolist[140])
            f141=float(tolist[141])
            f142=float(tolist[142])
            f143=float(tolist[143])
            f144=float(tolist[144])
            f145=float(tolist[145])
            f146=float(tolist[146])
            f147=float(tolist[147])
            f148=float(tolist[148])
            f149=float(tolist[149])
            f150=float(tolist[150])
            f151=float(tolist[151])
            f152=float(tolist[152])
            f153=float(tolist[153])
            f154=float(tolist[154])
            f155=float(tolist[155])
            f156=float(tolist[156])
            f157=float(tolist[157])
            f158=float(tolist[158])
            f159=float(tolist[159])
            f160=float(tolist[160])
            f161=float(tolist[161])
            f162=float(tolist[162])
            f163=float(tolist[163])
            f164=float(tolist[164])
            f165=float(tolist[165])
            f166=float(tolist[166])
            f167=float(tolist[167])
            f168=float(tolist[168])
            f169=float(tolist[169])
            f170=float(tolist[170])
            f171=float(tolist[171])
            f172=float(tolist[172])
            f173=float(tolist[173])
            f174=float(tolist[174])
            f175=float(tolist[175])
            f176=float(tolist[176])
            f177=float(tolist[177])
            f178=float(tolist[178])
            f179=float(tolist[179])
            f180=float(tolist[180])
            f181=float(tolist[181])
            f182=float(tolist[182])
            f183=float(tolist[183])
            f184=float(tolist[184])
            f185=float(tolist[185])
            f186=float(tolist[186])
            f187=float(tolist[187])
            f188=float(tolist[188])
            f189=float(tolist[189])
            f190=float(tolist[190])
            f191=float(tolist[191])
            f192=float(tolist[192])
            f193=float(tolist[193])
            f194=float(tolist[194])
            f195=float(tolist[195])
            f196=float(tolist[196])
            f197=float(tolist[197])
            f198=float(tolist[198])
            f199=float(tolist[199])
            f200=float(tolist[200])
            f201=float(tolist[201])
            f202=float(tolist[202])
            f203=float(tolist[203])
            f204=float(tolist[204])
            f205=float(tolist[205])
            f206=float(tolist[206])
            f207=float(tolist[207])
            f208=float(tolist[208])
            f209=float(tolist[209])
            f210=float(tolist[210])
            f211=float(tolist[211])
            f212=float(tolist[212])
            f213=float(tolist[213])
            f214=float(tolist[214])
            f215=float(tolist[215])
            f216=float(tolist[216])
            f217=float(tolist[217])
            f218=float(tolist[218])
            f219=float(tolist[219])
            f220=float(tolist[220])
            f221=float(tolist[221])
            f222=float(tolist[222])
            f223=float(tolist[223])
            f224=float(tolist[224])
            f225=float(tolist[225])
            a1 = subtract_abs(multiply(f27, f160), min_v(f31, f23))

            reslist.append(str(a1[0]))
            a2 = multiply(add(f83, f93), max_v(f160, f187))

            reslist.append(str(a2[0]))
            a3 = max_v(multiply(multiply(if_v(f26, f116, f29), if_v(f168, f221, f206)), subtract(max_v(f37, f158), subtract(f39, f181))), multiply(if_v(min_v(f104, f141), subtract(f62, f153), protectedDiv(f124, f142)), if_v(add_abs(f119, f201), subtract(f97, f168), if_v(f114, f112, f8))))

            reslist.append(str(a3[0]))
            a4 = multiply(f132, f167)

            reslist.append(str(a4[0]))
            a5 = multiply(f131, f207)

            reslist.append(str(a5[0]))
            a6 = min_v(f40, f36)

            reslist.append(str(a6[0]))
            a7 = min_v(f195, f152)

            reslist.append(str(a7[0]))
            a8 = min_v(multiply(f33, f224), multiply(f63, f133))

            reslist.append(str(a8[0]))
            a9 = min_v(f32, f79)

            reslist.append(str(a9[0]))
            a10 = if_v(concat(subtract_abs(f160, f172), if_v(f212, f90, f25)), if_v(min_v(f101, f40), min_v(f93, f212), if_v(f75, f110, f9)), min_v(min_v(f130, f179), add(f204, f221)))

            reslist.append(str(a10[0]))
            a11 = multiply(f84, f49)

            reslist.append(str(a11[0]))
            a12 = min_v(max_v(f209, f19), min_v(f110, f201))

            reslist.append(str(a12[0]))
            a13 = min_v(f177, f99)

            reslist.append(str(a13[0]))
            a14 = multiply(min_v(f169, f66), f80)

            reslist.append(str(a14[0]))
            a15 = multiply(if_v(min_v(if_v(f107, f48, f91), multiply(f217, f156)), concat(min_v(f84, f78), add_abs(f84, f121)), protectedDiv(min_v(f148, f109), concat(f54, f42))), concat(if_v(subtract_abs(f160, f148), multiply(f188, f143), add_abs(f209, f108)), multiply(multiply(f53, f110), concat(f221, f69))))

            reslist.append(str(a15[0]))
            a16 = subtract_abs(f85, f93)

            reslist.append(str(a16[0]))
            a17 = min_v(f140, f98)

            reslist.append(str(a17[0]))
            a18 = min_v(f43, f72)

            reslist.append(str(a18[0]))
            a19 = min_v(f151, f83)

            reslist.append(str(a19[0]))
            a20 = protectedDiv(subtract_abs(f69, f124), multiply(f74, f96))

            reslist.append(str(a20[0]))
            a21 = multiply(f19, f115)

            reslist.append(str(a21[0]))
            a22 = multiply(f25, f141)

            reslist.append(str(a22[0]))
            a23 = if_v(f193, [0.08664841317370331], f114)

            reslist.append(str(a23[0]))
            a24 = min_v(f104, f116)

            reslist.append(str(a24[0]))
            a25 = min_v(f146, f141)

            reslist.append(str(a25[0]))
            a26 = min_v(f153, f106)

            reslist.append(str(a26[0]))
            a27 = multiply(f81, f102)

            reslist.append(str(a27[0]))
            a28 = multiply(f181, f128)

            reslist.append(str(a28[0]))
            a29 = multiply(f134, f146)

            reslist.append(str(a29[0]))
            a30 = min_v(f223, f143)

            reslist.append(str(a30[0]))
            a31 = multiply(f154, f77)

            reslist.append(str(a31[0]))
            a32 = multiply(f38, f52)

            reslist.append(str(a32[0]))
            a33 = min_v(f139, f98)

            reslist.append(str(a33[0]))
            a34 = multiply(f85, f24)

            reslist.append(str(a34[0]))
            a35 = if_v(protectedDiv(if_v(max_v(min_v(f202, f190), concat(f22, f44)), add(add(f223, f20), subtract(f35, f108)), protectedDiv(subtract(f7, f50), add_abs(f164, f97))), add(concat(min_v(f181, f204), max_v(f140, f182)), multiply(max_v(f102, f156), protectedDiv(f30, f134)))), min_v(subtract_abs(multiply(min_v(f10, f171), min_v(f120, f218)), protectedDiv(min_v(f158, f64), protectedDiv(f100, f90))), multiply(subtract_abs(concat(f3, f145), min_v(f87, f137)), concat(min_v(f100, f25), multiply(f88, f133)))), if_v(protectedDiv(multiply(subtract(f170, f9), subtract(f91, f160)), add_abs(max_v(f86, f13), multiply(f215, f118))), concat(protectedDiv(max_v(f13, f93), if_v(f193, f108, f154)), max_v(min_v(f13, f61), protectedDiv(f32, f151))), add(protectedDiv(concat(f189, f153), concat(f31, f56)), multiply(if_v(f128, f141, f199), add(f61, f128)))))

            reslist.append(str(a35[0]))
            a36 = subtract_abs(f6, f6)

            reslist.append(str(a36[0]))
            a37 = protectedDiv(multiply(concat(max_v(subtract_abs(f202, f157), max_v(f97, f194)), concat(protectedDiv(f212, f34), add_abs(f188, f94))), min_v(add_abs(multiply(f214, f67), max_v(f68, f36)), add(subtract(f58, f49), subtract(f53, f163)))), max_v(protectedDiv(max_v(subtract_abs(f18, f54), multiply(f74, f65)), multiply(protectedDiv(f105, f169), multiply(f159, f106))), max_v(add_abs(protectedDiv(f209, f76), multiply(f178, [0.7078784673951861])), min_v(subtract(f219, f124), min_v(f79, f51)))))

            reslist.append(str(a37[0]))
            a38 = multiply(multiply(f98, f77), concat(f197, f31))

            reslist.append(str(a38[0]))
            a39 = multiply(f27, f45)

            reslist.append(str(a39[0]))
            a40 = min_v(min_v(protectedDiv(multiply(add(if_v(f161, f153, f189), min_v(f202, f185)), add(min_v(f79, f48), protectedDiv(f208, f179))), min_v(subtract_abs(subtract_abs(f181, f176), concat(f67, f69)), if_v(multiply(f38, f21), subtract(f142, f53), add_abs(f76, f163)))), subtract(max_v(multiply(min_v(f10, f202), max_v(f119, f116)), min_v(concat(f20, f71), concat(f185, f50))), multiply(add(min_v(f0, f21), min_v(f110, f67)), subtract(protectedDiv(f112, f222), multiply(f180, f49))))), subtract_abs(subtract_abs(if_v(subtract(protectedDiv(f170, f111), concat(f96, f201)), subtract_abs(protectedDiv(f147, f87), add_abs(f137, f26)), multiply(protectedDiv(f154, f25), if_v(f215, f164, f198))), concat(add_abs(add(f183, f76), add_abs(f185, f85)), add_abs(min_v(f155, f80), subtract(f149, f172)))), protectedDiv(protectedDiv(min_v(protectedDiv(f101, f165), if_v(f210, f147, f93)), multiply(add_abs(f34, f25), subtract(f16, f109))), subtract_abs(if_v(subtract(f175, f159), add_abs(f18, f119), multiply(f141, f223)), min_v(if_v(f80, f5, f65), subtract_abs(f157, f178))))))

            reslist.append(str(a40[0]))
            a41 = min_v(f13, f22)

            reslist.append(str(a41[0]))
            a42 = min_v(f178, f104)

            reslist.append(str(a42[0]))
            a43 = multiply(if_v(multiply(f105, f170), max_v(f138, f207), concat(f167, f75)), multiply(max_v(f64, f10), min_v(f208, f222)))

            reslist.append(str(a43[0]))
            a44 = min_v(multiply(f25, f70), if_v(f183, f93, f170))

            reslist.append(str(a44[0]))
            a45 = min_v(f17, f19)

            reslist.append(str(a45[0]))
            a46 = if_v(max_v(add(subtract_abs(f224, f117), concat(f218, f114)), subtract_abs(concat(f96, f161), subtract_abs(f32, f91))), concat(subtract(multiply(f188, f72), min_v(f7, f69)), multiply(max_v(f146, f105), subtract(f154, f221))), concat(max_v(protectedDiv(f157, f127), multiply(f126, f154)), add(add(f129, f33), if_v(f3, f208, f84))))

            reslist.append(str(a46[0]))
            a47 = add_abs(multiply(concat(multiply(if_v(max_v(f43, f100), max_v(f32, f40), subtract_abs(f184, f134)), multiply(min_v(f20, f21), add(f72, f118))), max_v(protectedDiv(add(f67, f63), max_v(f61, f89)), multiply(max_v(f143, f161), multiply(f108, f137)))), subtract(max_v(add(multiply(f208, f212), protectedDiv(f66, f194)), protectedDiv(add_abs(f66, f69), concat(f218, f222))), if_v(max_v(subtract_abs(f79, f88), concat(f29, f118)), add_abs(protectedDiv(f137, f23), concat(f72, f161)), subtract_abs(if_v(f42, f68, f194), if_v(f185, f0, f212))))), max_v(if_v(add_abs(max_v(subtract_abs(f55, f158), subtract_abs(f93, f180)), min_v(if_v(f66, f20, f222), subtract_abs(f200, f18))), multiply(concat(concat(f205, f147), add_abs(f15, f5)), max_v(min_v(f97, f186), multiply(f30, f124))), protectedDiv(protectedDiv(subtract_abs(f39, f34), multiply(f38, f39)), protectedDiv(protectedDiv(f139, f209), concat(f160, f201)))), if_v(max_v(protectedDiv(add(f195, f31), min_v(f96, f178)), protectedDiv(concat(f88, f144), protectedDiv(f204, f43))), min_v(min_v(if_v(f174, f29, f71), min_v(f10, f79)), max_v(max_v(f202, f65), subtract(f113, f94))), protectedDiv(min_v(multiply(f145, f110), protectedDiv(f223, f55)), add(min_v(f162, f14), subtract_abs(f138, f44))))))

            reslist.append(str(a47[0]))
            a48 = multiply(f144, f203)

            reslist.append(str(a48[0]))
            a49 = multiply(f31, f75)

            reslist.append(str(a49[0]))
            a50 = protectedDiv(add(add(max_v(add(max_v(f117, f18), concat(f190, f26)), max_v(add_abs(f191, f217), multiply(f10, f129))), add_abs(subtract(multiply(f113, f4), subtract_abs(f14, f130)), if_v(multiply(f11, f203), protectedDiv(f51, f208), if_v(f113, f97, f51)))), subtract(subtract(add(if_v(f165, f128, f212), if_v(f7, f23, f72)), protectedDiv(max_v(f221, f12), add_abs(f192, f40))), max_v(multiply(subtract_abs(f141, f91), min_v(f31, f132)), add_abs(concat(f103, f78), subtract(f127, f215))))), multiply(min_v(if_v(protectedDiv(if_v(f72, f164, f1), subtract_abs(f31, f70)), subtract(if_v(f156, f90, f223), multiply(f49, f120)), multiply(subtract(f201, f34), concat(f195, f204))), add_abs(subtract_abs(subtract_abs(f168, f206), concat(f107, f208)), protectedDiv(concat(f117, f181), add(f201, f24)))), max_v(protectedDiv(add_abs(add(f113, f101), protectedDiv(f109, f224)), min_v(concat(f167, f128), add(f136, f185))), min_v(subtract(subtract_abs(f101, f39), protectedDiv(f16, f132)), add_abs(multiply(f82, f120), subtract_abs(f162, f35))))))

            reslist.append(str(a50[0]))
            a51 = min_v(f54, f129)

            reslist.append(str(a51[0]))
            a52 = if_v(subtract(concat(multiply(protectedDiv(f121, f61), max_v(f175, f48)), if_v(concat(f143, f61), min_v(f180, f191), add_abs(f26, f16))), concat(concat(min_v(f52, f10), subtract_abs(f123, f20)), add(max_v(f187, f9), min_v(f142, f33)))), subtract_abs(multiply(concat(concat(f53, f167), add_abs(f190, f87)), min_v(if_v(f19, f159, f90), multiply(f1, f154))), max_v(min_v(max_v(f23, f155), if_v(f162, f42, f170)), min_v(min_v(f138, f106), subtract_abs(f75, f97)))), subtract(add_abs(add_abs(multiply(f140, f181), min_v(f210, f83)), protectedDiv(if_v(f71, f48, f164), protectedDiv(f119, f25))), multiply(max_v(multiply(f195, f21), add(f170, f197)), if_v(protectedDiv(f123, f70), max_v(f96, f11), min_v(f199, f120)))))

            reslist.append(str(a52[0]))
            a53 = multiply(if_v(f27, f34, f207), min_v(f145, f217))

            reslist.append(str(a53[0]))
            a54 = protectedDiv(f179, f108)

            reslist.append(str(a54[0]))
            a55 = min_v(f42, f198)

            reslist.append(str(a55[0]))
            a56 = if_v(multiply(subtract_abs(add_abs(min_v(f183, f88), max_v(f48, f138)), if_v(min_v(f192, f159), max_v(f100, f33), min_v(f35, f101))), min_v(add_abs(concat(f21, f85), concat(f8, f2)), subtract_abs(if_v(f59, f164, f36), max_v(f23, f167)))), concat(protectedDiv(subtract_abs(subtract(f42, f199), add(f211, f181)), min_v(if_v(f94, f78, f20), multiply(f81, f20))), protectedDiv(subtract(subtract_abs(f68, f145), add(f21, f213)), min_v(concat(f137, f51), concat(f33, f42)))), add_abs(add_abs(if_v(subtract_abs(f184, f180), if_v(f186, f181, f40), min_v(f197, f184)), concat(min_v(f77, f65), if_v(f129, f222, f210))), add_abs(subtract(concat(f185, f118), subtract_abs(f137, f29)), if_v(subtract_abs(f221, f149), protectedDiv(f212, f138), multiply(f116, f92)))))

            reslist.append(str(a56[0]))
            a57 = multiply(add(min_v(f186, f58), multiply(f102, f102)), max_v(add(f75, f195), min_v(f75, f126)))

            reslist.append(str(a57[0]))
            a58 = min_v(f45, f30)

            reslist.append(str(a58[0]))
            a59 = multiply(subtract_abs(add_abs(protectedDiv(f45, f155), add_abs(f111, f157)), subtract(protectedDiv(f26, f104), subtract_abs(f198, f78))), min_v(concat(protectedDiv(f204, f15), concat(f139, f109)), multiply(subtract_abs(f91, f65), concat(f93, f99))))

            reslist.append(str(a59[0]))
            a60 = multiply(min_v(add(add(multiply(f120, f218), subtract_abs(f110, f79)), max_v(add(f45, f98), if_v(f201, f220, f64))), multiply(max_v(add(f28, f22), min_v(f224, f6)), max_v(add(f191, f182), add_abs(f198, f4)))), if_v(concat(concat(protectedDiv(f20, f24), concat(f49, f6)), subtract(concat(f89, f185), subtract(f64, f200))), subtract_abs(subtract(if_v(f95, f110, f196), multiply(f43, f199)), subtract_abs(max_v(f27, f27), subtract_abs(f3, f95))), subtract(add(multiply(f24, f18), multiply(f119, f122)), multiply(add([-0.07785951085504594], f19), add(f183, f104)))))

            reslist.append(str(a60[0]))
            a61 = multiply(min_v(f193, f142), if_v(f165, f112, f182))

            reslist.append(str(a61[0]))
            a62 = multiply(f110, f27)

            reslist.append(str(a62[0]))
            a63 = min_v(f172, f9)

            reslist.append(str(a63[0]))
            a64 = min_v(f60, f204)

            reslist.append(str(a64[0]))
            a65 = min_v(subtract(min_v(concat(min_v(f190, f66), subtract(f163, f188)), max_v(subtract(f179, f138), protectedDiv(f212, f9))), protectedDiv(min_v(multiply(f188, f72), concat(f99, f22)), multiply(if_v(f160, f131, f19), multiply(f4, f210)))), subtract_abs(concat(subtract_abs(concat(f132, f19), add_abs(f157, f111)), min_v(if_v(f105, f23, f40), subtract_abs(f65, f64))), concat(concat(max_v(f196, f109), subtract(f157, f67)), subtract_abs(subtract(f189, f193), multiply(f157, f140)))))

            reslist.append(str(a65[0]))
            a66 = multiply(f127, f90)

            reslist.append(str(a66[0]))
            a67 = multiply(f171, f121)

            reslist.append(str(a67[0]))
            a68 = min_v(f156, f223)

            reslist.append(str(a68[0]))
            a69 = min_v(f9, f149)

            reslist.append(str(a69[0]))
            a70 = min_v(f209, f70)

            reslist.append(str(a70[0]))
            a71 = multiply(f158, f145)

            reslist.append(str(a71[0]))
            a72 = multiply(f163, f41)

            reslist.append(str(a72[0]))
            a73 = multiply(min_v(add(if_v(f222, f175, f101), add(f56, f144)), multiply(max_v(f62, f220), max_v(f33, f101))), add(concat(max_v(f116, f67), min_v(f142, f1)), add_abs(protectedDiv(f76, f216), multiply(f128, f54))))

            reslist.append(str(a73[0]))
            a74 = protectedDiv(add_abs(protectedDiv(add_abs(multiply(multiply(f25, f18), max_v(f45, f39)), max_v(max_v(f214, f98), add(f125, f167))), multiply(add_abs(concat(f90, f220), if_v(f161, [0.5123281711245469], f76)), multiply(protectedDiv(f203, f155), max_v(f33, f189)))), if_v(add(subtract(concat(f138, f205), add_abs(f222, f13)), subtract_abs(add_abs(f0, f46), multiply(f154, f156))), if_v(add(add_abs(f81, f67), max_v(f211, f165)), min_v(multiply(f150, f0), multiply(f177, f147)), subtract_abs(min_v(f125, f4), min_v(f214, [-0.8691171782654117]))), subtract(min_v(min_v(f48, f10), max_v(f13, f16)), multiply(add(f155, f134), if_v(f43, f217, f162))))), add(multiply(if_v(protectedDiv(add_abs(f190, f217), add_abs(f161, f116)), min_v(subtract(f53, f224), subtract(f107, f121)), if_v(add_abs(f115, f88), min_v(f72, f223), max_v(f173, f108))), if_v(concat(multiply(f191, f162), subtract_abs(f144, f125)), multiply(if_v(f142, f154, f85), protectedDiv(f213, f132)), add(min_v(f184, f96), add(f198, f190)))), multiply(multiply(min_v(max_v(f123, f45), multiply(f31, f157)), multiply(subtract(f186, f50), if_v(f126, f151, f90))), add_abs(add_abs(subtract_abs(f115, f92), concat(f105, f58)), subtract(min_v(f156, f199), add(f61, f193))))))

            reslist.append(str(a74[0]))
            a75 = multiply(concat(add(f29, f214), multiply(f15, f171)), min_v(max_v(f119, f74), subtract(f91, f55)))

            reslist.append(str(a75[0]))
            a76 = protectedDiv(f12, f122)

            reslist.append(str(a76[0]))
            a77 = multiply(f25, f110)

            reslist.append(str(a77[0]))
            a78 = min_v(f96, f90)

            reslist.append(str(a78[0]))
            a79 = concat(if_v(protectedDiv(add(f221, f173), protectedDiv(f71, f213)), min_v(multiply(f30, f20), add(f167, f172)), min_v(multiply(f170, f201), min_v(f15, f117))), multiply(multiply(concat(f181, f175), concat(f154, f168)), min_v(min_v(f223, f80), multiply(f202, f158))))

            reslist.append(str(a79[0]))
            a80 = multiply(f124, f165)

            reslist.append(str(a80[0]))
            a81 = multiply(f83, f122)

            reslist.append(str(a81[0]))
            a82 = min_v(f40, f155)

            reslist.append(str(a82[0]))
            a83 = min_v(f177, f207)

            reslist.append(str(a83[0]))
            a84 = multiply(f63, f162)

            reslist.append(str(a84[0]))
            a85 = multiply(f96, f40)

            reslist.append(str(a85[0]))
            a86 = multiply(multiply(multiply(max_v(f140, f152), protectedDiv(f19, f44)), subtract(multiply(f117, f9), add(f112, f200))), protectedDiv(multiply(subtract(f56, f184), add_abs(f52, f101)), subtract(max_v(f148, f87), protectedDiv(f33, f216))))

            reslist.append(str(a86[0]))
            a87 = max_v(subtract_abs(add_abs(subtract(multiply(subtract_abs(f157, f196), multiply(f13, f118)), multiply(add(f83, f66), subtract(f210, f133))), add_abs(protectedDiv(multiply(f82, f8), protectedDiv(f115, f173)), min_v(add(f123, f101), add_abs(f173, f163)))), protectedDiv(min_v(subtract_abs(max_v(f50, f134), concat(f4, f67)), max_v(if_v(f144, f219, f84), subtract(f137, f155))), min_v(concat(if_v(f52, f49, f197), subtract_abs(f15, f122)), min_v(add_abs(f171, f212), if_v(f99, f119, f102))))), multiply(add(subtract_abs(subtract_abs(subtract_abs(f73, f29), min_v(f57, f213)), add_abs(multiply(f168, f43), add_abs(f69, f119))), min_v(subtract_abs(add_abs(f23, f101), add_abs(f178, f207)), subtract_abs(add(f157, f216), min_v(f157, f22)))), add(concat(subtract_abs(subtract(f180, f183), max_v(f111, f64)), protectedDiv(add_abs(f0, f37), add_abs(f103, f185))), min_v(add_abs(subtract_abs(f53, f58), max_v(f127, f118)), subtract(protectedDiv(f34, f194), add_abs(f217, f24))))))

            reslist.append(str(a87[0]))
            a88 = multiply(f190, f82)

            reslist.append(str(a88[0]))
            a89 = min_v(f154, f106)

            reslist.append(str(a89[0]))
            a90 = if_v(if_v(subtract_abs(f136, f18), subtract_abs(f152, f193), subtract(f223, f54)), multiply(add(f161, f94), max_v(f163, f114)), multiply(protectedDiv(f44, f117), max_v(f200, f162)))

            reslist.append(str(a90[0]))
            a91 = multiply(f96, f152)

            reslist.append(str(a91[0]))
            a92 = add(max_v(multiply(multiply(f87, f178), add(f107, f197)), concat(subtract(f119, f84), multiply(f181, f70))), max_v(protectedDiv(add(f160, f72), multiply(f97, f165)), max_v(min_v(f3, f46), min_v(f92, f118))))

            reslist.append(str(a92[0]))
            a93 = min_v(add_abs(multiply(protectedDiv(concat(subtract_abs(f26, f138), subtract_abs(f18, f175)), max_v(add(f84, f217), subtract_abs(f12, f154))), concat(min_v(max_v(f209, f10), multiply(f194, f90)), if_v(protectedDiv(f20, f20), add(f80, f169), subtract(f123, f3)))), if_v(min_v(multiply(add_abs(f169, f173), min_v(f4, f160)), concat(subtract_abs(f136, f16), multiply(f215, f38))), if_v(add_abs(if_v(f181, f114, f208), if_v(f207, f62, f0)), max_v(add_abs(f149, f80), if_v(f3, f111, f47)), multiply(subtract_abs(f150, f9), multiply(f99, f80))), add(subtract(multiply(f89, f74), if_v(f67, f124, f102)), protectedDiv(subtract(f130, f20), subtract_abs(f184, f82))))), concat(min_v(add_abs(add(subtract(f161, f36), max_v(f45, f220)), add_abs(add(f60, f26), if_v(f181, f175, f100))), max_v(min_v(if_v(f141, f72, f172), min_v(f32, f166)), concat(concat(f134, f24), add(f53, f76)))), concat(subtract(add_abs(protectedDiv(f98, f205), subtract_abs(f61, f191)), protectedDiv(subtract(f154, f48), protectedDiv(f161, f77))), subtract(protectedDiv(concat(f116, f31), min_v(f124, f103)), concat(subtract(f49, f121), add_abs(f221, f88))))))

            reslist.append(str(a93[0]))
            a94 = min_v(f108, f192)

            reslist.append(str(a94[0]))
            a95 = min_v(add_abs(add(f223, f186), min_v(f122, f156)), multiply(subtract_abs(f99, f9), max_v(f101, f192)))

            reslist.append(str(a95[0]))
            a96 = min_v(f192, f224)

            reslist.append(str(a96[0]))
            a97 = min_v(concat(multiply(min_v(subtract(min_v(f159, f194), if_v(f91, f74, f2)), add_abs(concat(f31, f133), concat([-0.5804659923642765], f41))), multiply(add(add(f180, f23), max_v(f207, f208)), min_v(protectedDiv(f6, f209), protectedDiv(f151, f172)))), subtract_abs(protectedDiv(subtract_abs(if_v(f75, f132, f159), multiply(f80, f165)), protectedDiv(protectedDiv(f67, f26), subtract(f170, f79))), min_v(max_v(subtract_abs(f59, f61), protectedDiv(f37, f101)), min_v(min_v(f36, f103), protectedDiv(f168, f44))))), subtract_abs(if_v(subtract_abs(multiply(multiply(f213, f124), multiply(f143, f162)), if_v(multiply(f148, f86), add(f202, f97), if_v(f98, f143, f109))), min_v(multiply(max_v(f104, f184), add(f181, f134)), concat(subtract(f84, f152), multiply(f89, f95))), concat(add_abs(if_v(f46, f222, f189), subtract(f181, f30)), add_abs(min_v(f39, f51), subtract(f15, f143)))), max_v(min_v(min_v(if_v(f78, f18, f101), add_abs(f85, f126)), min_v(min_v(f193, f148), multiply(f140, f186))), if_v(add(if_v(f199, f186, f37), add_abs(f6, f190)), min_v(if_v(f21, f189, f81), add(f146, f8)), max_v(max_v(f191, f26), max_v(f198, f25))))))

            reslist.append(str(a97[0]))
            a98 = multiply(f138, f8)

            reslist.append(str(a98[0]))
            a99 = min_v(min_v(f162, f182), max_v(f216, f223))

            reslist.append(str(a99[0]))
            a100 = min_v(f44, f187)

            reslist.append(str(a100[0]))
            a101 = f225
            reslist.append(str(a101))
            result_file.write(' '.join(reslist))
            result_file.write('\n')
        else:
            break
    result_file.close()
    data_file.close()
