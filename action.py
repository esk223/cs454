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
    result_file=open('result_90.txt','w')
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
            a1 = protected_div(f218, f123)

            reslist.append(str(a1))
            a2 = f225
            reslist.append(str(a2))
            result_file.write(' '.join(reslist))
            result_file.write('\n')
        else:
            break
    result_file.close()
    data_file.close()