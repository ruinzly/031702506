import re
import json
def shengfen():
    list1=[]
    list1.append("北京")#1
    list1.append("天津")
    list1.append("上海")
    list1.append("重庆")#4
    list1.append("河北")#5
    list1.append("河南")
    list1.append("云南")
    list1.append("辽宁")
    list1.append("黑龙江")
    list1.append("湖南")#10
    list1.append("安徽")
    list1.append("山东")
    list1.append("江苏")
    list1.append("浙江")
    list1.append("江西")#15
    list1.append("湖北")
    list1.append("甘肃")
    list1.append("山西")
    list1.append("陕西")
    list1.append("吉林")#20
    list1.append("福建")
    list1.append("贵州")
    list1.append("广东")
    list1.append("青海")
    list1.append("四川")
    list1.append("海南")#26
    list1.append("宁夏")#27
    list1.append("西藏")
    list1.append("内蒙古")
    list1.append("新疆")
    list1.append("广西")#31
    return list1

def chengshi():
    list2=[]
    list2.append("北京")
    list2.append("天津")
    list2.append("上海")
    list2.append("重庆")#3
    list2.append(["保定","沧州","承德","邯郸","衡水","廊坊","秦皇岛","石家庄","唐山","邢台","张家口"])#5
    list2.append(["安阳","鹤壁","济源","焦作","开封","洛阳","漯河","南阳","平顶山","濮阳","三门峡","商丘","新乡","信阳","许昌","郑州","周口","驻马店"])
    list2.append(["西双版纳","宝山","楚雄","大理","德宏","迪庆","红河","昆明","丽江","临沧","怒江","普洱","曲靖","文山","玉溪","昭通"])
    list2.append(["鞍山","本溪","朝阳","大连","丹东","抚顺","阜新","葫芦岛","锦州","辽阳","盘锦","沈阳","铁岭","营口"])
    list2.append(["哈尔滨", "齐齐哈尔", "牡丹江", "大庆", "伊春", "双鸭山", "鹤岗", "鸡西", "佳木斯", "七台河", "黑河", "绥化", "大兴安岭"])
    list2.append(["长沙", "邵阳", "常德", "郴州", "吉首", "株洲", "娄底", "湘潭", "益阳", "永州", "岳阳", "衡阳", "怀化", "韶山", "张家界"])
    list2.append(["合肥", "巢湖", "蚌埠", "安庆", "六安", "滁州", "马鞍山", "阜阳", "宣城", "铜陵", "淮北", "芜湖", "毫州", "宿州", "淮南", "池州"])
    list2.append(["沈阳", "大连", "葫芦岛", "旅顺", "本溪", "抚顺", "铁岭", "辽阳", "营口", "阜新", "朝阳", "锦州", "丹东", "鞍山"])
    list2.append(["南京", "苏州", "昆山", "南通", "太仓", "吴县", "徐州", "宜兴", "镇江", "淮安", "常熟", "盐城", "泰州", "无锡", "连云港", "扬州", "常州", "宿迁"])
    list2.append(["杭州", "湖州", "金华", "宁波", "丽水", "绍兴", "雁荡山", "衢州", "嘉兴", "台州", "舟山", "温州"])
    list2.append(["南昌", "萍乡", "九江", "上饶", "抚州", "吉安", "鹰潭", "宜春", "新余", "景德镇", "赣州"])
    list2.append(["武汉", "宜昌", "黄冈", "恩施", "荆州", "神农架", "十堰", "咸宁", "襄樊", "孝感", "随州", "黄石", "荆门", "鄂州"])
    list2.append(["兰州", "白银", "庆阳", "酒泉", "天水", "武威", "张掖", "甘南", "临夏", "平凉", "定西", "金昌"])
    list2.append(["太原", "阳泉", "晋城", "晋中", "临汾", "运城", "长治", "朔州", "忻州", "大同", "吕梁"])
    list2.append(["西安", "韩城", "安康", "汉中", "宝鸡", "咸阳", "榆林", "渭南", "商洛", "铜川", "延安"])
    list2.append(["长春", "延边", "吉林", "白山", "白城", "四平", "松原", "辽源", "大安", "通化"])#19
    list2.append(["福州", "厦门", "龙岩", "南平", "宁德", "莆田", "泉州", "三明", "漳州"])#20
    list2.append(["贵阳", "安顺", "赤水", "遵义", "铜仁", "六盘水", "毕节", "凯里", "都匀"])
    list2.append(["广州", "深圳", "潮州", "韶关", "湛江", "惠州", "清远", "东莞", "江门", "茂名", "肇庆", "汕尾", "河源", "揭阳", "梅州", "中山", "德庆", "阳江", "云浮", "珠海", "汕头", "佛山"])
    list2.append(["西宁", "海北", "海西", "黄南", "果洛", "玉树", "海东", "海南"])
    list2.append(["成都", "泸州", "内江", "凉山", "阿坝", "巴中", "广元", "乐山", "绵阳", "德阳", "攀枝花", "雅安", "宜宾", "自贡", "甘孜州", "达州", "资阳", "广安", "遂宁", "眉山", "南充"])
    list2.append(["海口", "三亚", "儋州", "琼山", "通什", "文昌"])
    list2.append(["银川", "固原", "中卫", "石嘴山", "吴忠"])
    list2.append(["拉萨","昌都地区","山南地区","阿里地区","那曲地区","林芝地区","日喀则地区"])
    list2.append(["呼和浩特", "呼伦贝尔", "锡林浩特", "包头", "赤峰", "海拉尔", "乌海", "鄂尔多斯", "通辽"])
    list2.append(["乌鲁木齐", "阿勒泰", "阿克苏", "昌吉", "哈密", "和田", "喀什", "克拉玛依", "石河子", "塔城", "库尔勒", "吐鲁番", "伊宁"])
    list2.append(["南宁", "桂林", "阳朔", "柳州", "梧州", "玉林", "桂平", "贺州", "钦州", "贵港", "防城港", "百色", "北海", "河池", "来宾", "崇左"])
    return list2

import re
import json
province=shengfen()
city=chengshi()
while(1):
    x = input()
    if(x == "END"):
        break
    x = x.replace(".", "")
    if x[0] == "1":
        x = re.sub("1!", "", x, 1)
        x = re.sub("省", "", x, 1)
        x = re.sub("回族自治区", "", x, 1)
        x = re.sub("自治区", "", x, 1)
        x = re.sub("维吾尔族自治区", "", x, 1)
        x = re.sub("壮族自治区", "", x, 1)
        # print(x)
        llist = x.split(",", 1)
        dict = {}
        dict["姓名"] = llist[0]
        y = re.findall(r"\d\d\d\d\d\d\d\d\d\d\d", llist[1])
        # print(y)
        # y=re.findall(r"\d\d\d\d\d\d\d\d\d\d\d",llist[1])
        dict["手机"] = y[0]
        m = re.sub(y[0], "", llist[1], 1)  # 原地址中去掉号码
        # print(m)
        # print(dict)
        dict1 = []
        for i in range(len(province)):
            p = re.match(province[i], m)
            if (p):
                s = i
                ss = p.group()
                if (i < 4):
                    dict1.append(ss)
                elif (5 < i < 26):
                    ss2 = p.group()
                    ss = p.group() + '省'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)

                elif (i == 27):
                    ss2 = p.group()
                    ss = p.group() + '回族自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                elif (27 < i < 30):
                    ss2 = p.group()
                    ss = p.group() + '自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                elif (i == 30):
                    ss2 = p.group()
                    ss = p.group() + '维吾尔族自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                else:
                    ss2 = p.group()
                    ss = p.group() + '壮族自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                break

        for j in range(len(city[s])):
            q = re.match(city[s][j], m)
            # print(m)
            if (q):
                s1 = q
                ss1 = q.group() + '市'
                # print(ss1)
                dict1.append(ss1)
                w = re.match(ss1, m)
                if w:
                    m = re.sub(ss1, "", m, 1)
                else:
                    m = re.sub(q.group(), "", m, 1)
                # dict1.append(ss1)
                break
            if j == len(city[s]) - 1:
                if q == None:
                    dict1.append(" ")
        # print(dict1)

        k = re.match(r'.*?(县|区|市)', m)
        if k:
            kk = k.group()
            dict1.append(kk)
            m = re.sub(kk, "", m, 1)
        else:
            dict1.append("")
        k = re.match(r'.*?(街道|镇|乡)', m)
        if k:
            kk = k.group()
            dict1.append(kk)
            m = re.sub(kk, "", m, 1)
        else:
            dict1.append("")
        dict1.append(m)
        dict["地址"] = dict1
        # print(dict)
        Json = json.dumps(dict,ensure_ascii=False)
        print(Json)



    else:
        x = re.sub('2!', "", x, 1)
        x = re.sub("1!", "", x, 1)
        x = re.sub("省", "", x, 1)
        x = re.sub("回族自治区", "", x, 1)
        x = re.sub("自治区", "", x, 1)
        x = re.sub("维吾尔族自治区", "", x, 1)
        x = re.sub("壮族自治区", "", x, 1)
        #print(x)
        llist = x.split(",", 1)
        dict = {}
        dict["姓名"] = llist[0]
        y = re.findall(r"\d\d\d\d\d\d\d\d\d\d\d", llist[1])
        # print(y)
        # y=re.findall(r"\d\d\d\d\d\d\d\d\d\d\d",llist[1])
        dict["手机"] = y[0]
        m = re.sub(y[0], "", llist[1], 1)  # 原地址中去掉号码
        # print(m)
        # print(dict)
        dict1 = []
        for i in range(len(province)):
            p = re.match(province[i], m)
            if (p):
                s = i
                ss = p.group()
                if (i < 4):
                    dict1.append(ss)
                elif (5 < i < 26):
                    ss2 = p.group()
                    ss = p.group() + '省'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)

                elif (i == 27):
                    ss2 = p.group()
                    ss = p.group() + '回族自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                elif (27 < i < 30):
                    ss2 = p.group()
                    ss = p.group() + '自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                elif (i == 30):
                    ss2 = p.group()
                    ss = p.group() + '维吾尔族自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                else:
                    ss2 = p.group()
                    ss = p.group() + '壮族自治区'
                    dict1.append(ss)
                    m = re.sub(ss2, "", m, 1)
                break

        for j in range(len(city[s])):
            q = re.match(city[s][j], m)
            # print(m)
            if (q):
                s1 = q
                ss1 = q.group() + '市'
                # print(ss1)
                dict1.append(ss1)
                w = re.match(ss1, m)
                if w:
                    m = re.sub(ss1, "", m, 1)
                else:
                    m = re.sub(q.group(), "", m, 1)
                # dict1.append(ss1)
                break
            if j == len(city[s]) - 1:
                if q == None:
                    dict1.append(" ")
        # print(dict1)

        k = re.match(r'.*?(县|区|市)', m)
        if k:
            kk = k.group()
            dict1.append(kk)
            m = re.sub(kk, "", m, 1)
        else:
            dict1.append("")
        k = re.match(r'.*?(街道|镇|乡)', m)
        if k:
            kk = k.group()
            dict1.append(kk)
            m = re.sub(kk, "", m, 1)
        else:
            dict1.append("")
        k = re.match(r'.*?(路)', m)
        if k:
            kk = k.group()
            dict1.append(kk)
            m = re.sub(kk, "", m, 1)
        else:
            dict1.append("")
        k = re.match(r'.*?(号)', m)
        if k:
            kk = k.group()
            dict1.append(kk)
            m = re.sub(kk, "", m, 1)
        else:
            dict1.append("")
        dict1.append(m)
        dict["地址"] = dict1
        Json = json.dumps(dict, ensure_ascii=False)
        print(Json)
    # print(dict1)

