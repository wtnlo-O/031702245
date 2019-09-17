import re
str=input("")


names=str.split('.')                                #以.为标记切分为数组
for name in names[:-1]:
    erji=name.split(',')[0]                         #以，为标记切分出姓名
    print("姓名:",end="")
    print(erji,end="")
    print(",",end="")
    name = name.replace(erji, "")
    m = re.findall(r'\d{11}', name)[0]             #正则匹配11位电话号码
    name = name.replace(m, "")
    print("手机:",end="")
    print(m, end="")
    print(",", end="")
    province= re.findall(r",(.*?)省", name)
    if province:
        print("地址:",end="")
        print(province[0], end="")
        print("省",end="")
        print(",", end="")
        name = name.replace(province[0],"")
        name = name.replace("省", "")
        city = re.findall(r",(.*?)市", name)
        print(city[0], end="")
        print("市", end="")
        print(",", end="")
        name=name.replace(city[0],"")

        name = name.replace("市", "")

    else:
       city= re.findall(r",(.*?)市",name)
       print("地址:",end="")
       print(city[0], end="")
       print(",", end="")
       print(city[0],end="")
       print("市", end="")
       print(",", end="")
       name = name.replace(city[0], "")
       name = name.replace("市", "")


    classify= re.findall(r",(.*?)区", name)
    country_town= re.findall(r",(.*?)县", name)
    if classify:
       print(classify[0],end="")
       print("区",end="")
       print(",",end="")
       name = name.replace(classify[0], "")
       name = name.replace("区", "")
    elif country_town:
        print(country_town[0], end="")
        print("县", end="")
        print(",", end="")
        name = name.replace(country_town[0], "")
        name = name.replace("县", "")
    else:
        print(" ",end="")
        print(",", end="")
    jiedao=re.findall(r",(.+?)街道", name)
    zhen=re.findall(r",(.+?)镇", name)

    if jiedao:
        print(jiedao[0],end="")
        print("街道", end="")
        name = name.replace(jiedao[0], "")
        name = name.replace("街道", "")
    elif zhen:
        print(zhen[0],end="")
        print("镇", end="")
        name = name.replace(zhen[0], "")
        name = name.replace("镇", "")
    else:
        print("  ",end="")

    zuihoujiedao=re.findall(r",[^\r\n]+", name)
    if zuihoujiedao:
        print(zuihoujiedao[0])



