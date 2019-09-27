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

def xianqu():
    list3=[]
    list3=['辖东城区', '西城区', '朝阳区', '丰台区', '石景山区', '海淀区', '顺义区', '通州区', '大兴区', '房山区', '门头沟区', '昌平区', '平谷区', '密云区', '怀柔区', '延庆区','市辖区', '和平区', '河东区', '河西区', '南开区', '河北区', '红桥区', '塘沽区', '汉沽区', '大港区', '东丽区', '西青区', '北辰区', '津南区',\
           '武清区', '宝坻区', '静海县', '宁河县', '蓟县','黄浦区', '徐汇区', '长宁区', '静安区', '普陀区', '虹口区', '闸北区', '杨浦区', '闵行区', '宝山区', '青浦区', '松江区', '嘉定区', '奉贤区', '金山区', '浦东新区', '崇明县','渝中区', '沙坪坝', '九龙坡', '江北区', '北碚区', '大渡口', '渝北区', '涪陵区',\
           '万州区', '黔江区', '万盛区', '长寿区', '永川区', '江津区', '南川区', '合川区', '南岸区', '巴南区', '高新区', '经开区', '城口县', '垫江县', '开县', '铜梁县', '秀山县', '大足县', '綦江县', '彭水县', '璧山县', '丰都县', '巫山县', '忠县', '奉节县', '梁平县', '巫溪县', '云阳县', '荣昌县', '酉阳县',\
           '石柱县', '潼南县', '武隆县','长安区', '桥东区', '桥西区', '新华区', '井陉矿区', '裕华区', '辛集市','藁城市', ' 晋州市', ' 新乐市', ' 鹿泉市', '井陉县', '正定县', '栾城县', '行唐县', '灵寿县', '高邑县', '深泽县', '赞皇县', '无极县', '平山县', '元氏县', ' 赵路北区', ' 路南区', '古冶区', '开平区', '丰南区',\
           '丰润区', '遵化市', '迁安市', ' 滦州市','滦南县', '乐亭县', '迁西县', ' 玉田县', ' 唐海县海港区', '山海关区', '北戴河区', '昌黎县', '抚宁县', '卢龙县','青龙满族自治县丛台区', '邯山区', '复兴区', '峰峰矿区', '武安市', '邯郸县', '临漳县', '成安县', '大名县', '涉县', '磁县', '肥乡县', '永年县', '邱县', '鸡泽县',\
           '广平县', '馆陶县', '魏县', '曲周县桥东区', '桥西区', '南宫市', '沙河市','邢台县', '临城县', '内丘县', '柏乡县', '隆尧县', '任县', '南和县', '宁晋县', '巨鹿县', '新河县', '广宗县', '平乡县', '威县', '清河县', '临西县新市区', '北市区', '南市区', '涿州市', '定州市', '安国市', '高碑店市', '满城县', '清苑县',\
           '涞水县', '阜平县', '徐水县', '定兴县', '唐县', '高阳县', '容城县', '涞源县', '望都县', '安新县', '易县', '曲阳县', '蠡县', '顺平县', '博野县', '雄县桥西区', '桥东区', '宣化区', '下花园区', '张北县', '康保县', '沽源县', '尚义县', '蔚县', '阳原县', '怀安县', '万全区', '怀来县', '涿鹿县', '赤城县',\
           '崇礼县双桥区', '双滦区', '鹰手营子矿区', '承德县', '兴隆县', '平泉市', '滦平县', '隆化县', '丰宁满族自治县', '宽城满族自治县', '围场满族蒙古族自治县运河区', '新华', '泊头市', '任丘市', '黄骅市', '河间市', '沧县', '青县', '东光县', '海兴县', '盐山县', '肃宁县', '南皮县', '吴桥县', '献县', '孟村回族自治县安次区',\
           '广阳区', '霸州市', '三河市', '固安县', '永清县', '香河县', '大城县', '文安县', '大厂回族自治县桃城区', '冀州市', '深州市', '枣强县', '武邑县', '武强县', '饶阳县', '安平县', '故城县', '景县', '阜城县','杏花岭区', '小店区', '迎泽区', '尖草坪区', '万柏林区', '晋源区', '古交市', '阳曲县', '清徐县', '娄烦县南郊区',\
           '新荣区', '大同县', '天镇县', '灵丘县', '阳高县', '左云县', '广灵县', '浑源县平定县', '盂县潞城市', '长治县', '长子县', '平顺县', '襄垣县', '沁源县', '屯留县', '黎城县', '武乡县', '沁县', '壶关县高平市', '泽州县', '陵川县', '阳城县', '沁水县朔城区', '平鲁区', '山阴县', '右玉县', '应县', '怀仁市榆次区',\
           '介休市', '昔阳县', '灵石县', '祁县', '左权县', '寿阳县', '太谷县', '和顺县', '遥县', '榆社县盐湖区', '河津市', '永济市', '闻喜县', '新绛县', '平陆县', '垣曲县', '绛县', '稷山县', '芮城县', '夏县', '万荣县', '临猗县忻府区', '原平市', '代县', '神池县', '五寨县', '五台县', '偏关县', '宁武县', '静乐县', '繁峙县',\
           '河曲县', '保德县', '定襄县', '岢岚县', '经济开发区尧都区', '侯马市', '霍州市', '汾西县', '吉县', '安泽县', '大宁县', '浮山县', '古县', '隰县', '襄汾县', '翼城县', '永和县', '乡宁县', '曲沃县', '洪洞县', '蒲县离石区', '孝义市', '汾阳市', '文水县', '中阳县', '兴县', '临县', '方山县', '柳林县', '岚县', '交口县',\
           '交城县', '石楼县','回民区', ' 新城区', '玉泉区', ' 赛罕区', ' 托克托县', '武川县', '清水河县', '土默特左旗', '和林格尔县昆都仑区', '东河区', '青山区', '石拐区', '白云矿区', '九原区', '固阳县', '达尔罕茂明安联合旗', '土默特右旗海勃湾区', '海南区', '乌达区元宝山区', '红山区', '松山区', '林西县', '宁城县',\
           '巴林左旗', '巴林右旗', '克什克腾旗', '翁牛特旗', '喀喇沁旗', '敖汉旗', '阿鲁科尔沁旗科尔沁区', '霍林郭勒市', '开鲁县', '库伦旗', '奈曼旗', '扎鲁特旗', '科尔沁左翼中旗', '科尔沁左翼后旗东胜区', '达拉特旗', '准格尔旗', '鄂托克旗', '杭锦旗', '乌审旗', '伊金霍洛旗', '鄂托克前旗海拉尔区', '满洲里市', '牙克石市',\
           '扎兰屯市', '额尔古纳市', '根河市', '阿荣旗','陈巴尔虎旗', '新巴尔虎左旗', '新巴尔虎右旗', '莫力达瓦达斡尔族自治旗', '鄂伦春自治旗', '鄂温克族自治旗临河区','五原县','磴口县','乌拉特前旗','乌拉特中旗','乌拉特后旗','杭锦后旗集宁区', '丰镇市', '卓资县', '化德县', '商都县', '兴和县', '凉城县', '察哈尔右翼前旗',\
           '察哈尔右翼中旗', '察哈尔右翼后旗', '四子王旗乌兰浩特市', '阿尔山市', '突泉县', '科尔沁右翼前旗', '科尔沁右翼中旗', '扎赉特旗二连浩特市','锡林浩特市','多伦县','阿巴嘎旗','苏尼特左旗', '苏尼特右旗', '东乌珠穆沁旗','西乌珠穆沁旗','太仆寺旗','镶黄旗', '正镶白旗','正蓝旗阿拉善左旗','阿拉善右旗', '额济纳旗',\
           '松北区', '道里区','南岗区', '道外区', '平房区', '香坊区', '呼兰区', '阿城区', '双城市', '尚志市', '五常市', '依兰县', '方正县', '宾县', '巴彦县','木兰县', '通河县', '延寿县龙沙区', '建华区','铁锋区', '昂昂溪区', '富拉尔基区', '碾子山区', '梅里斯区', '讷河市', '龙江县', '依安县', '泰来县', '甘南县',\
           '富裕县', '克山县', '克东县', '拜泉县爱民区', '东安区','阳明区', '西安区', '绥芬河市', '海林市', '宁安市', '穆棱市', '东宁市', '林口县前进区','向阳区','东风区', '郊区', '永红', '同江市', '富锦市', '桦南县', '桦川县', '汤原县', '抚远市萨尔图区', '龙凤区', '让胡路区', '红岗区', '大同区', '肇州县',\
           '肇源县', '林甸县', '杜尔伯特蒙古族自治县鸡冠区', '恒山区', '滴道区', '梨树区', '城子河区', '麻山区', '虎林市', '密山市', '鸡东县尖山区', '岭东区', '四方台区','宝山区', '集贤县', '友谊县', '宝清县', '饶河县伊美区', '乌翠区', '友好区', '金林区', '丰林县', '汤旺县', '南岔县', '大箐县', '嘉荫县', '铁力市桃山区',\
           '新兴区', '茄子河区', '勃利县兴山区', '向阳区','工农区','南山区','兴安区', '东山区','萝北县', '绥滨县爱辉区', '北安市','五大连池市', '嫩江市', '逊克县',' 孙吴县北林区', '安达市', '肇东市', '海伦市', '望奎县', '兰西县青冈县', '庆安县', '明水县', '绥棱县加格达奇区', '松岭区','新林区','呼中区' ,'呼玛县','塔河县','漠河市',\
           '朝阳区', '南关区', '宽城区', '二道区', '绿园区', '双阳区', '德惠市', '九台市', '榆树市', '农安县船营区', '昌邑区', '龙潭区', '丰满区', '蛟河市', '桦甸市','舒兰市', '磐石市', '永吉县铁西区', '铁东区', '公主岭市', '双辽市', '梨树县', '伊通满族自治县龙山区', '西安区', ' 东丰县', '东辽县东昌区', '二道江区', '梅河口市',\
           '集安市', '通化县', '辉南县', '柳河县八道江区', '江源区', '临江市', '抚松县', '靖宇县', '长白朝鲜族自治县 宁江区', '长岭县', '乾安县', '扶余市','前郭尔罗斯蒙古族自治县洮北区', '洮南市', '大安市', '镇赉县', '通榆县延吉市', '图们市', '敦化市', '珲春市', '龙井市', '和龙市', '汪清县', '安图县','沈河区', '和平区', '大东区',\
           '皇姑区', '铁西区', '苏家屯区', '东陵区', '沈北新区', '于洪区', '新民市', '辽中县', '康平县', '法库县','西岗区','中山区', '沙河口区', '甘井子区', '旅顺口区', '金州区', '瓦房店市','普兰店市', '庄河市', '长海县', '经济技术开发区','铁东区', '铁西区','立山区','千山区','海城市','台安县','岫岩满族自治县','顺城区','新抚区',\
           '东洲区','望花区', '抚顺县','新宾满族自治县','清原满族自治县','太和区', '古塔区','凌河区','凌海市', '北镇市', '黑山县', '义县站前区', '西市区', '鲅鱼圈区', '老边区', ' 盖州市', '大石桥市海州区','新邱区','太平区', '清河门区', '细河区', '阜新蒙古族自治县', ' 彰武县白塔区', '文圣区','宏伟区', '弓长岭区', '太子河区',\
           '灯塔市', '辽阳县兴隆台区', '双台子区', '大洼区', '盘山县银州区', '清河区', '调兵山市', '开原市', '铁岭县', '西丰县', '昌图县双塔区', '龙城区', '北票市', '凌源市','朝阳县','建平县', '喀喇沁左翼蒙古族自治县龙港区', ' 连山区', ' 南票区', ' 兴城市', '绥中县', '建昌县','历下区', '市中区', '槐荫区', '天桥区', '历城区',\
           '长清区', '章丘市', '平阴县', '济阳县', '商河县', '高新区市北区', '四方区', '黄岛区', '崂山区', '李沧区', '城阳区', '胶州市', '即墨市', '平度市', '胶南市', '莱西市张店区', '淄川区', '博山区', '临淄区', '周村区', '桓台县', '高青县', ' 沂源县市中区', '薛城区', '峄城区', '台儿庄区', '山亭区', '滕州市东营区', '河口区',\
           '垦利县', '利津县', '广饶县芝罘区', '福山区', '牟平区', '莱山区', '龙口市', '莱阳市', '莱州市', '蓬莱市', '招远市', '栖霞市', '海阳市', '长岛县潍城区', '寒亭区', '坊子区', '奎文区', '青州市', '诸城市', '寿光市', '安丘市', '高密市', '昌邑市', '临朐县', '昌乐县环翠区', '文登市', '荣成市', '乳山市市中区', '任城区',\
           '曲阜市', '兖州市', '邹城市', '微山县', '鱼台县', '金乡县', '嘉祥县', '汶上县', '泗水县', '梁山县泰山区', '岱岳区', '新泰市', '肥城市', '宁阳县', '东平县东港区', '岚山区', '五莲县', ' 莒县莱城区', '钢城区兰山区', '罗庄区', '河东区', '沂南县', '郯城县', '沂水县', '苍山县', '费县', '平邑县', '莒南县', '蒙阴县',\
           '临沭县德城区', '乐陵市', '禹城市', '陵县', '宁津县', '庆云县', '临邑县', '齐河县', '平原县', '夏津县', '武城县东昌府区', '临清市', '阳谷县', '莘县', '茌平县', '东阿县', '冠县', '高唐县滨城区', '惠民县', '阳信县', '无棣县', '沾化县', '博兴县', '邹平县牡丹区', '曹县', '单县', '成武县', '巨野县', '郓城县', '鄄城县',\
           '定陶县', '东明县','玄武区', '白下区', '秦淮区', '建邺区', '鼓楼区', '下关区', '浦口区', '栖霞区', '雨花台区', '江宁区', '六合区', '溧水县', '高淳县崇安区', '南长区', '北塘区', '滨湖区', '锡山区', '惠山区', '江阴市', '宜兴市云龙区', '鼓楼区', '九里区', '贾汪区', '泉山区', '新沂市', '邳州市', '丰县', '沛县',\
           '铜山县', '睢宁县钟楼区', '天宁区', '戚墅堰区', '新北区', '武进区', '溧阳市', '金坛市金阊区', '沧浪区', '平江区', '虎丘区', '吴中区', '相城区', '常熟市', '张家港市', '昆山市', '吴江市', '太仓市崇川区', '港闸区', '启东市', '如皋市', '通州市', '海门市', '海安市', '如东县新浦区', '连云区', '海州区', '赣榆县', '东海县',\
           '灌云县', '灌南县清河区', '清浦区', '楚州区', '淮阴区', '涟水县', '洪泽县', '盱眙县', '金湖县亭湖区', '盐都区', '东台市', '大丰区', '响水县', '滨海县', '阜宁县', '射阳县', '建湖县广陵区', '邗江区', '维扬区', '仪征市', '高邮市', '江都市', '宝应县京口区', '润州区', '丹徒区', '丹阳市', '扬中市', '句容市海陵区', '高港区',\
           '兴化市', '靖江市', '泰兴市', '姜堰市', '经济开发区宿城区', '宿豫区', '沭阳县', '泗阳县', '泗洪县','拱墅区', '上城区', '下城区', '江干区', '西湖区', '滨江区', '萧山区', '余杭区', '建德市', '富阳市', '临安市', '桐庐县', '淳安县海曙区', '江东区', '江北区', '北仑区', '镇海区', '鄞州区', '余姚市', '慈溪市', '奉化市',\
           '象山县', '宁海县鹿城区', '龙湾区', '瓯海区', '瑞安市', '乐清市', '洞头县', '永嘉县', '平阳县', '苍南县', '文成县', '泰顺县南湖区', '秀洲区', '海宁市', '平湖市', '桐乡市', '嘉善县', '海盐县吴兴区', '南浔区', '德清县', '长兴县', '安吉县越城区', '诸暨市', '上虞市', '嵊州市', '绍兴县', '新昌县婺城区', '金东区', '兰溪市',\
           '义乌市', '东阳市', '永康市', '武义县', '浦江县', '磐安县柯城区', '衢江区', '江山市', '常山县', '开化县', '龙游县定海区', '普陀区', '岱山县', '嵊泗县椒江区', '黄岩区', '路桥区', '温岭市', '临海市', '玉环市', '三门县', '天台县', '仙居县 莲都区', '龙泉市', ' 青田县', '缙云县', '遂昌县', ' 松阳县', '云和县', ' 庆元县',\
           '景宁畲族自治县 ','庐阳区', '瑶海区', '蜀山区', '包河区', '长丰县', '肥东县', '肥西县镜湖区', '弋江区', '鸠江区', '三山区', '芜湖县', '繁昌县', '南陵县蚌山区', '禹会区', '淮上区', '怀远县', '五河县', '固镇县', '龙子湖区大通区', '谢家集区', '八公山区', '潘集区', '凤台县', '田家庵区雨山区', '金家庄', '花山区',\
           '当涂县相山区', '杜集区', '烈山区', '濉溪县铜官山区', '狮子山区', '郊区', '铜陵县迎江区', '大观区', '宜秀区', '桐城市', '怀宁县', '枞阳县', '潜山市', '太湖县', '宿松县', '望江县', '岳西县屯溪区', '黄山区', '徽州区', '歙县', '休宁县', '黟县', '祁门县琅琊区', '南谯区', '天长市', '明光市', '来安县', '全椒县', '定远县',\
           '凤阳县颍州区', '颍东区', '颍泉区', '界首市', '临泉县', '太和县', '阜南县', '颍上县埇桥区', '砀山县', '萧县', '灵璧县', '泗县居巢区', '庐江县', '无为县', '含山县', '和县金安区', '裕安区', '寿县', '霍邱县', '舒城县', '金寨县', '霍山县谯城区', '涡阳县', '蒙城县', '利辛县贵池区', '东至县', '石台县', '青阳县宣州区',\
           '宁国市', '郎溪县', '广德县', '泾县', '绩溪县', '旌德县','东湖区', '西湖区', '青云谱区', '湾里区', '青山湖区', '南昌县', '新建县', '安义县', '进贤县珠山区', '昌江区', '乐平市', '浮梁县安源区', '湘东区', '莲花县', '芦溪县', '上栗县浔阳区', '庐山市', '瑞昌市', '九江县', '武宁县', '修水县', '永修县', '德安县',\
           '都昌县', '湖口县', '彭泽县渝水区', '分宜县月湖区', '贵溪市', '余江县章贡区', '瑞金市', '南康市', '信丰县', '大余县', '上犹县', '崇义县', '安远县', '龙南县', '定南县', '全南县', '宁都县', '于都县', '兴国县', '会昌县', '寻乌县', '石城县', '赣县吉州区', '青原区', '吉安县', '吉水县', '峡江县', '新干县', '永丰县', '泰和县',\
           '遂川县', '万安县', '安福县', '永新县', '井冈山市袁州区', '丰城市', '樟树市', '高安市', '奉新县', '万载县', '上高市', '宜丰县', '靖安县', '铜鼓县临川区', '南城县', '黎川县', '南丰县', '崇仁县', '乐安县', '宜黄县', '金溪县', '资溪县', '东乡县', ' 广昌县信州区', '德兴市', '上饶县', '广丰县', '玉山县', '铅山县', '横峰县',\
           '弋阳县', '余干县', '鄱阳县', '万年县', '婺源县','鼓楼区', '台江区', '仓山区', '马尾区', '晋安区', '福清市', '长乐市', '闽侯县', '连江县', '罗源县', '闽清县', '永泰县', '平潭县思明区', '海沧区', '湖里区', '集美区', '同安区', '翔安区城厢区', '涵江区', '荔城区', '秀屿区', '仙游县梅列区', '三元区', '永安市', '明溪县',\
           '清流县', '宁化县', '大田县', '尤溪县', '沙县', '将乐县', '泰宁县', '建宁县鲤城区', '丰泽区', '洛江区', '泉港区', '石狮市', '晋江市', '南安市', '惠安县', '安溪县', '永春县', '德化县', '金门县芗城区', '龙文区', '龙海市', '云霄县', '漳浦县', '诏安县', '长泰县', '东山县', '南靖县', '平和县', '华安县延平区', '邵武市',\
           '武夷山市', '建瓯市', '建阳市', '顺昌县', '浦城县', '光泽县', '松溪县', '政和县新罗区', '漳平市', '长汀县', '永定县', '上杭县', '武平县', '连城县蕉城区', '福安市', '福鼎市', '霞浦县', '古田县', '屏南县', '寿宁县', '周宁县', '柘荣县','中原区', '二七区', '管城区', '金水区', '上街区', '惠济区', '巩义市', '荥阳市',\
           '新密市', '新郑市', '登封市', '中牟县鼓楼区', '龙亭区', '顺河区', '禹王台区', '金明区', '杞县', '通许县', '尉氏县', '开封县', '兰考县西工区', '老城区', '瀍河区', '涧西区', '吉利区', '洛龙区', '偃师市', '孟津县', '新安县', '栾川县', '嵩县', '汝阳县', '宜阳县', '洛宁县', '伊川县新华区', '卫东区', '湛河区', '石龙区',\
           '舞钢市', '汝州市', '宝丰县', '叶县', '鲁山县', '郏县山阳区', '解放区', '中站区', '马村区', '沁阳市', '孟州市', '修武县', '博爱县', '武陟县', '温县淇滨区', '山城区', '鹤山区', '浚县', '淇县卫滨区', '红旗区', '凤泉区', '牧野区', '卫辉市', '辉县市', '新乡县', '获嘉县', '原阳县', '延津县', '封丘县', '长垣县北关区',\
           '文峰区', '殷都区', '龙安区', '林州市', '安阳县', '汤阴县', '滑县', '内黄县华龙区', '清丰县', '南乐县', '范县', '台前县', '濮阳县魏都区', '禹州市', '长葛市', '许昌县', '鄢陵县', '襄城县源汇区', '郾城区', '召陵区', '舞阳县', '临颍县湖滨区', '义马市', '灵宝市', '渑池县', '陕县', '卢氏县卧龙区', '宛城区', '邓州市', '南召县',\
           '方城县', '西峡县', '镇平县', '内乡县', '淅川县', '社旗县', '唐河县', '新野县', '桐柏县梁园区', '睢阳区', '永城市', '民权县', '睢县', '宁陵县', '柘城县', '虞城县', '夏邑县浉河区', '平桥区', '罗山县', '光山县', '新县', '商城县', '固始县', '潢川县', '淮滨县', '息县川汇区', '项城市', '扶沟县', '西华县', '商水县', '沈丘县',\
           '郸城县', '淮阳县', '太康县', '鹿邑县驿城区', '西平县', '上蔡县', '平舆县', '正阳县', '确山县', '泌阳县', '汝南县', '遂平县', '新蔡县','江岸区', '江汉区', '硚口区', '汉阳区', '武昌区', '青山区', '洪山区', '东西湖区', '汉南区', '蔡甸区', '江夏区', '黄陂区', '新洲区黄石港区', '西塞山区', '下陆区', '铁山区', '大冶市',\
           '阳新县襄城区', '樊城区', '襄阳区', '老河口市', '枣阳市', '宜城市', '南漳县', '谷城县', '保康县', '高新区茅箭区', '张湾区', '丹江口市', '郧县', '郧西县', '竹山县', '竹溪县', '房县沙市区', '荆州区', '石首市', '洪湖市', '松滋市', '公安县', '监利县', '江陵县西陵区', '伍家岗区', '点军区', '猇亭区', '夷陵区', '宜都市', '当阳市',\
           '枝江市', '远安县', '兴山县', '秭归县', '长阳土家族自治县', '五峰土家族自治县东宝区', '掇刀区', '钟祥市', '京山市', '沙洋县鄂城区', '梁子湖区', '华容区孝南区', '应城市', '安陆市', '汉川市', '孝昌县', '大悟县', '云梦县黄州区', '麻城市', '武穴市', '团风县', '红安县', '罗田县', '英山县', '浠水县', '蕲春县', '黄梅县咸安区',\
           '赤壁市', '嘉鱼县', '通城县', '崇阳县', '通山县曾都区', '广水市恩施市', '利川市', '建始县', '巴东县', '宣恩县', '咸丰县', '来凤县', '鹤峰县仙桃市', '潜江市', '天门市', '神农架林区','芙蓉区', '天心区', '岳麓区', '开福区', '雨花区', '浏阳市', '长沙县', '望城县', '宁乡市荷塘区', '芦淞区', '石峰区', '天元区', '醴陵市', '株洲县',\
           '攸县', '茶陵县', '炎陵县雨湖区', '岳塘区', '湘乡市', '韶山市', '湘潭县珠晖区', '雁峰区', '石鼓区', '蒸湘区', '南岳区', '耒阳市', '常宁市', '衡阳县', '衡南县', '衡山县', '衡东县', '祁东县双清区', '大祥区', '北塔区', '武冈市', '邵东市', '新邵县', '邵阳县', '隆回县', '洞口县', '绥宁县', '新宁县', '城步自治县云溪区', '君山区',\
           '汨罗市', '临湘市', '华容县', '湘阴县', '平江县', '岳阳楼区武陵区', '鼎城区', '津市市', '安乡县', '汉寿县', '澧县', '临澧县', '桃源县', '石门县永定区', '武陵源区', '慈利县', '桑植县资阳区', '赫山区', '沅江市', '南县', '  桃江县', '安化县北湖区', '苏仙区', '资兴市', '桂阳县', '宜章县', '永兴县', '嘉禾县', '临武县', '汝城县',\
           '桂东县', '安仁县零陵区', '祁阳县', '东安县', '双牌县', '江永县', '宁远县', '蓝山县', '新田县', '江华瑶族自治县', '冷水滩区', '道县鹤城区', '洪江市', '沅陵县', '辰溪县', '溆浦县', '中方县', '会同县', '麻阳苗族自治县', '新晃侗族自治县', '芷江侗族自治县', '靖州苗族侗族自治县', '通道侗族自治县娄星区', '涟源市', '双峰县', '新化县',\
           '冷水江市吉首市', '泸溪县', '凤凰县', '花垣县', '保靖县', '古丈县', '永顺县', '龙山','越秀区', '荔湾区', '海珠区', '天河区', '白云区', '黄埔区', '番禺区', '花都区', '南沙区', '萝岗区', '增城市', '从化市福田区', '罗湖区', '南山区', '宝安区', '龙岗区', '盐田区', '高新区', '光明区', '龙华区', '坪山区香洲区', '斗门区',\
           '金湾区金平区', '龙湖区', '濠江区', '潮阳区', '潮南区', '澄海区', '南澳县浈江区', '武江区', '曲江区', '乐昌市', '南雄市', '始兴县', '仁化县', '翁源县', '新丰县', '乳源瑶族自治县禅城区', '南海区', '顺德区', '三水区高明区江海区', '蓬江区', '新会区', '台山市', '开平市', '鹤山市', '恩平市赤坎区', '霞山区', '坡头区', '麻章区',\
           '廉江市', '雷州市', '吴川市', '遂溪县', '徐闻县茂南区', '茂港区', '高州市', '化州市', '信宜市', '电白县端州区', '鼎湖区', '高要市', '四会市', '广宁县', '怀集县', '封开县', '德庆县惠城区', '惠阳区', '博罗县', '惠东县', '龙门县梅江区', '兴宁市', '大埔县', '丰顺县', '五华县', '平远县', '蕉岭县', '梅县陆丰市', '海丰县',\
           '陆河县源城区', '紫金县', '龙川县', '连平县', '和平县', '东源县江城区', '阳春市', '阳西县', '阳东县清城区', '英德市', '连州市', '佛冈县', '阳山县', '清新县', '连山壮族瑶族自治县', '连南瑶族自治县湘桥区', '潮安县', '饶平县榕城区', '普宁市', '揭东县', '揭西县', '惠来县云城区', '罗定市', '新兴县', '郁南县', '云安县','兴宁区',\
           '青秀区', '江南区', '西乡塘区', '良庆区', '邕宁区', '武鸣县', '隆安县', '马山县', '上林县', '宾阳县', '横县城中区', '鱼峰区', '柳南区', '柳北区', '柳江区', '柳城县', '鹿寨县', '融安县', '融水苗族自治县', '三江侗族自治县秀峰区', '叠彩区', '象山区', '七星区', '雁山区', '阳朔县', '临桂县', '灵川县   全州县', '兴安县', '永福县',\
           '灌阳县', '资源县', '平乐县', '荔浦县', '龙胜各族自治县', '恭城瑶族自治县万秀区', '蝶山区', '长洲区', '苍梧县', '藤县', '蒙山县', '岑溪市海城区', '银海区', '铁山港区', '合浦县港口区', '防城区', '上思县', '东兴市江州区', '扶绥县', '宁明县', '龙州县', '大新县', '天等县', '凭祥市钦南区', '钦北区', '灵山县', '浦北县港北区', '港南区',\
           '覃塘区', '平南县', '桂平市玉州区', '陆川县', '博白县', '兴业县', '北流市', '容县右江区', '田阳县', '田东县', '平果县', '德保县', '靖西市', '那坡县', '凌云县', '乐业县', '田林县', '西林县', '隆林各族自治县八步区', '昭平县', '钟山县', '富川瑶族自治县宜州市', '南丹县', '天峨县', '凤山县', '东兰县', '罗城仫佬族自治县',\
           '环江毛南族自治县', '巴马瑶族自治县', '都安瑶族自治县', '大化瑶族自治县', '金城江区兴宾区', '合山市', '忻城县', '象州县', '武宣县', '金秀瑶族自治县','文昌市', '琼海市', '万宁市', '五指山市', '东方市', '儋州市临高县', '澄迈县', '定安县', '屯昌县', '昌江黎族自治县', '白沙黎族自治县', '琼中黎族苗族自治县', '陵水黎族自治县',\
           '保亭黎族苗族自治县', '乐东黎族自治县龙华区', '秀英区', '琼山区', '美兰区天涯区', '吉阳区', '海棠区', '崖州区','锦江区', '青羊区', '金牛区', '武侯区', '成华区', '龙泉驿区', '青白江区', '新都区', '温江区', '都江堰市', '彭州市', '崇州市', '邛崃市', '金堂县', '双流县', '郫县', '大邑县', '蒲江县', '新津县自流井区', '贡井区',\
           '大安区', '沿滩区', '荣县', '富顺县东区', '西区', '仁和区', '米易县', '盐边县江阳区', '纳溪区', '龙马潭区', '泸县', '合江县', '叙永县', '古蔺县旌阳区', '广汉市', '什邡市', '绵竹市', '罗江县', '中江县涪城区', '游仙区', '江油市', '三台县', '盐亭县', '安州区', '梓潼县', '平武县', '北川羌族自治县利州区', '元坝区', '朝天区',\
           '旺苍县', '青川县', '剑阁县', '苍溪县船山区', '安居区', '蓬溪县', '射洪县', '大英县市中区', '东兴区', '威远县', '资中县', '隆昌市市中区', '沙湾区', '五通桥区', '金口河区', '峨眉山市', '犍为县', '井研县', '夹江县', '沐川县', '峨边彝族自治县', '马边彝族自治县顺庆区', '高坪区', '嘉陵区', '阆中市', '南部县', '营山县', '蓬安县',\
           '仪陇县', '西充县翠屏区', '宜宾县', '南溪县', '江安县', '长宁县', '高县', '珙县', '筠连县', '兴文县', '屏山县广安区', '华蓥市', '岳池县', '武胜县', '邻水县通川区', '万源市', '达县', '宣汉县', '开江县', '大竹县', '渠县东坡区', '仁寿县', '彭山县', '洪雅县', '丹棱县', '青神县雨城区', '名山县', '荥经县', '汉源县', '石棉县',\
           '天全县', '芦山县', '宝兴县巴州区', '通江县', '南江县', '平昌县雁江区', '简阳市', '安岳县', '乐至县马尔康市', '汶川县', '理县', '茂县', '松潘县', '九寨沟县', '金川县', '小金县', '黑水县', '壤塘县', '阿坝县', '若尔盖县', '红原县康定市', '泸定县', '丹巴县', '九龙县', '雅江县', '道孚县', '炉霍县', '甘孜县', '新龙县', '德格县',\
           '白玉县', '石渠县', '色达县', '理塘县', '巴塘县', '乡城县稻城县', '得荣县西昌市', '盐源县', '德昌县', '会理县', '会东县', '宁南县', '普格县', '布拖县', '金阳县', '昭觉县', '喜德县', '冕宁县', '越西县', '甘洛县', '美姑县', '雷波县', '木里自治县','乌当区', '南明区', '  云岩区', '花溪区', '白云区', '小河区', '清镇市', '开阳县',\
           '息烽县', '修文县', '金阳新区钟山区', '六枝特区', '水城县', '盘州市红花岗区', '汇川区', '赤水市', '仁怀市', '遵州区', '桐梓县', '绥阳县', '正安县', '凤冈县', '湄潭县', '余庆县', '习水县', '道真仡佬族苗族自治县', '务川仡佬族苗族自治县西秀区', '平坝县普定县', '镇宁布依族苗族自治县', '关岭布依族苗族自治县', '紫云苗族布依族自治县万山特区',\
           '铜仁市', '江口县', '石阡县', '思南县', '德江县', '玉屏侗族自治县', '印江土家族苗族自治县', '沿河土家族自治县', '松桃苗族自治县毕节市', '大方县', '黔西县', '金沙县', '织金县', '纳雍县', '赫章县', '威宁彝族回族苗族自治县兴义市', '兴仁县', '普安县', '晴隆县', '贞丰县', '望谟县', '册亨县', '安龙县凯里市', '黄平县', '施秉县', '三穗县',\
           '镇远县', '岑巩县', '天柱县', '锦屏县', '剑河县', '台江县', '黎平县', '榕江县', '从江县', '雷山县', '麻江县', '丹寨县都匀市', '福泉市', '荔波县', '贵定县', '瓮安县', '独山县', '平塘县', '罗甸县', '长顺县', '龙里县', '惠水县', '三都水族自治县','五华区', '盘龙区', '官渡区', '西山区', '东川区', '安宁市', '呈贡县', '晋宁县', '富民县',\
           '宜良县', '嵩明县', '石林彝族自治县', '禄劝彝族苗族自治县', '寻甸回族自治县麒麟区', '沾益区', '宣威市', '马龙县', '陆良县', '师宗县', '罗平县', '富源县', '会泽县红塔区', '江川县', '澄江县', '通海县', '华宁县', '易门县', '峨山彝族自治县', '新平彝族傣族自治县', '元江哈尼族彝族傣族自治县隆阳区', '施甸县', '腾冲市', '龙陵县', '昌宁县昭阳区',\
           '鲁甸县', '巧家县', '盐津县', '大关县', '永善县', '绥江县', '镇雄县', '彝良县', '威信县', '水富县古城区', '永胜县', '华坪县', '玉龙纳西族自治县', '宁蒗彝族自治县思茅区', '宁洱哈尼族彝族自治县', '墨江哈尼族自治县', '景东彝族自治县', '景谷彝族傣族自治县', '镇沅彝族哈尼族拉祜族自治县', '西盟佤族自治县', '江城哈尼族彝族自治县',\
           '孟连傣族拉祜族佤族自治县', '澜沧拉祜族自治县临翔区', '凤庆县', '云县', '永德县', '镇康县', '双江县', '耿马县', '沧源县蒙自县', '开远市', '个旧市', '绿春县', '建水县', '石屏县', '弥勒市', '红河县', '泸西县', '元阳县', '金平苗族瑶族傣族自治县', '河口瑶族自治县', '屏边苗族自治县大理市', '祥云县', '宾川县', '弥渡县', '永平县', '云龙县',\
           '洱源县', '剑川县', '鹤庆县', '漾濞彝族自治县', '南涧彝族自治县', '巍山彝族回族自治县楚雄市', '双柏县', '牟定县', '南华县', '姚安县', '大姚县', '永仁县', '元谋县', '武定县', '禄丰县文山县', '砚山县', '西畴县', '麻栗坡县', '马关县', '丘北县', '广南县', '富宁县景洪市', '勐海县', '勐腊县潞西市', '瑞丽市', '梁河县', '盈江县', '陇川县泸水市',\
           '福贡县', '贡山独龙族怒族自治县', '兰坪白族普米族自治县香格里拉市', '德钦县', '维西傈僳族自治县','城关区', '林周县', '当雄县', '尼木县', '曲水县', '堆龙德庆县', '达孜县', ' 墨竹', '工卡县那曲县', '嘉黎县', '比如县', '聂荣县', '安多县', '巴青县', '尼玛县', '索县', '班戈县', '申扎县昌都县', '江达县', '贡觉县', '类乌齐县', '丁青县', '察雅县',\
           '八宿县', '左贡县', '芒康县', '洛隆县', '边坝县乃东区', '扎囊县', '贡嘎县', '桑日县', '琼结县', '曲松县', '洛扎县', '加查县', '隆子县', '错那县', '浪卡子县', '措美县江孜县', '定日县', '萨迦县', '拉孜县', '昂仁县', '谢通门县', '白朗县', '仁布县', '康马县', '定结县', '仲巴县亚东县', '日喀则市', '南木林县', '吉隆县', '聂拉木县', '萨嘎县',\
           '岗巴县噶尔县', '普兰县', '札达县', '日土县', '革吉县', '改则县', '  措勤县林芝县', '工布江达县', '米林县', '墨脱县', '波密县', '察隅县', '朗县','高陵县', '户县', '周至县', '蓝田县', '临潼区', '阎良区', '雁塔区', '灞桥区', '莲湖区', '碑林区', '新城区', '未央区', '长安区', '高新区', '经开区', '曲江新区', '浐灞生态区', '沣渭新区武功县',\
           '淳化县', '旬邑县', '长武县', '彬州市', '永寿县', '礼泉县', '乾县', '泾阳县', '三原县', '兴平市', '渭城区', '秦都区', '泾渭新区太白县', '麟游县', '千阳县', '扶风县', '岐山县', '凤翔县', '陈仓区', '金台区', '渭滨区', '高新区', '凤县', '陇县', '眉县富平县', '白水县', '蒲城县', '澄城县', '合阳县', '大荔县', '潼关县', '韩城市', '临渭区',\
           '华阴市', '华县黄陵县', '黄龙县', '宜川县', '洛川县', '富县', '甘泉县', '吴起县', '志丹县', '安塞县', '子长市', '延川县', '延长县', '宝塔区宜君县', '印台区', '王益区', '耀州区佛坪县', '留坝县', '镇巴县', '略阳县', '宁强县', '勉县', '西乡县', '洋县', '城固县', '南郑县', '汉台区子洲县', '清涧县', '吴堡县', '佳县', '米脂县', '绥德县',\
           '定边县', '靖边县', '横山县', '府谷县', '神木县', '榆阳区', '经济开发区', '玉环市白河县', '旬阳县', '镇坪县', '平利县', '岚皋县', '紫阳县', '宁陕县', '石泉县', '汉阴县', '汉滨区柞水县', '镇安县', '山阳县', '商南县', '丹凤县', '洛南县', '商州区', '杨凌示范区','城关区', '七里河区', '西固区', '安宁区', '红古区', '永登县', '皋兰县',\
           '榆中县金川区', '永昌县白银区', '平川区', '靖远县', '会宁县', '景泰县秦州区', '麦积区', '清水县', '秦安县', '甘谷县', '武山县', '张家川回族自治县凉州区', '民勤县', '古浪县', '天祝藏族自治县甘州区', '民乐县', '临泽县', '高台县', '山丹县', '肃南裕固族自治县崆峒区', '泾川县', '灵台县', '崇信县', '华亭县', '庄浪县', '静宁县肃州区', '玉门市',\
           '敦煌市', '金塔县', '瓜州县肃北蒙古族自治县', '阿克塞哈萨克族自治县西峰区', '庆城县', '环县', '华池县', '合水县', '正宁县', '宁县', '镇原县安定区', '通渭县', '陇西县', '渭源县', '临洮县', '漳县', '  岷县武都区', '成县', '文县', '宕昌县', '康县', '西和县', '礼县', '徽县', '两当县合作市', '临潭县', '卓尼县', '舟曲县', '迭部县', '玛曲县',\
           '碌曲县', '夏河县临夏市', '临夏县', '康乐县', '永靖县', '广河县', '和政县', '东乡族自治县', '积石山保安族东乡族撒拉族自治县','兴庆区', '金凤区', '西夏区', '永宁县', '贺兰县', '灵武市大武口区', '惠农区', '平罗县利通区', '盐池县', '同心县', '青铜峡市原州区', '西吉县', '隆德县', '泾源县', '彭阳县沙坡头区', '中宁县', '海原县','城东区',\
           '城中区', '城西区', '城北区', '湟中县', '湟源县', '大通回族土族自治县平安县', '乐都县', '民和回族土族自治县', '互助土族自治县', '化隆回族自治县', '循化撒拉族自治县海晏县', '祁连县', '刚察县', '门源回族自治县同仁县', '尖扎县', '泽库县', '河南蒙古族自治县共和县', '同德县', '贵德县', '兴海县', '贵南县玛沁县', '班玛县', '甘德县', '达日县',\
           '久治县', '玛多县玉树市', '杂多县', '称多县', '治多县', '囊谦县', '曲麻莱县德令哈市', '格尔木市', '乌兰县', '都兰县', '天峻县', '冷湖行委', '大柴旦行委', '茫崖行委','天山区', '沙依巴克区', '新市区', '水磨沟区', '头屯河区', '达坂城区', '米东区', '乌鲁木齐县克拉玛依区', '独山子区', '白碱滩区乌尔禾区吐鲁番市', '托克逊县', '鄯善县哈密市',\
           '伊吾县', '巴里坤哈萨克自治县和田市', '和田县', '洛浦县', '民丰县', '皮山县', '策勒县', '于田县', '墨玉县温宿县', '库车县', '沙雅县', '新和县', '拜城县', '', '乌什县 阿瓦提县   柯坪县喀什市', '疏附县', '疏勒县', '泽普县', '莎车县', '叶城县', '麦盖提县', '岳普湖县', '伽师县', '巴楚县', '塔什库尔干', '阿克苏市', '英吉沙县', '阿拉尔市',\
           '塔吉克自治县塔城市', '乌苏市', '额敏县', '沙湾县   托里县   裕民县', '和布克赛尔蒙古自治县阿勒泰市', '布尔津县', '富蕴县', '福海县', '哈巴河县', '青河县', '吉木乃县阿图什市', '阿克陶县', '阿合奇县', '乌恰县库尔勒市', '轮台县', '尉犁县', '若羌县', '且末县', '和静县', '和硕县', '博湖县', '焉耆回族自治县昌吉市', '阜康市', '呼图壁县',\
           '玛纳斯县', '奇台县', '吉木萨尔县', '木垒哈萨克自治县博乐市', '精河县', '温泉县伊宁市', '奎屯市', '伊宁县', '霍城县', '巩留县', '新源县', '昭苏县', '特克斯县', '尼勒克县', '察布查尔锡伯自治县阿拉尔市', '图木舒克市', '五家渠市']
    return list3
import re
import json
province=shengfen()
city=chengshi()
x=input()
x = x.replace(".", "")
if x[0]=="1":
    x=re.sub("1!","",x,1)
    x = re.sub("省", "", x, 1)
    x = re.sub("回族自治区", "", x, 1)
    x = re.sub("自治区", "", x, 1)
    x = re.sub("维吾尔族自治区", "", x, 1)
    x = re.sub("壮族自治区", "", x, 1)
    print(x)
    llist=x.split(",",1)
    dict={}
    dict["姓名"]=llist[0]
    y=re.findall(r"\d\d\d\d\d\d\d\d\d\d\d",llist[1])
    #print(y)
   # y=re.findall(r"\d\d\d\d\d\d\d\d\d\d\d",llist[1])
    dict["手机"] =y[0]
    m=re.sub(y[0],"",llist[1],1)#原地址中去掉号码
   # print(m)
   # print(dict)
    dict1=[]
    for i in range(len(province)):
        p=re.match(province[i],m)
        if(p):
            s=i
            ss=p.group()
            if(i<4):
               dict1.append(ss)
            elif(5<i<26):
                ss2=p.group()
                ss=p.group()+'省'
                dict1.append(ss)
                m=re.sub(ss2,"",m,1)

            elif(i==27):
                ss2 = p.group()
                ss=p.group()+'回族自治区'
                dict1.append(ss)
                m = re.sub(ss2, "", m, 1)
            elif(27<i<30):
                ss2 = p.group()
                ss=p.group()+'自治区'
                dict1.append(ss)
                m = re.sub(ss2, "", m, 1)
            elif(i==30):
                ss2 = p.group()
                ss=p.group()+'维吾尔族自治区'
                dict1.append(ss)
                m = re.sub(ss2, "", m, 1)
            else:
                ss2 = p.group()
                ss=p.group()+'壮族自治区'
                dict1.append(ss)
                m = re.sub(ss2, "", m, 1)
            break

    for j in range(len(city[s])):
        q=re.match(city[s][j],m)
       # print(m)
        if(q):
            s1=q
            ss1=q.group()+'市'
            #print(ss1)
            dict1.append(ss1)
            w=re.match(ss1,m)
            if w:
                m=re.sub(ss1,"",m,1)
            else:
                m=re.sub(q.group(),"",m,1)
            #dict1.append(ss1)
            break
        if j == len(city[s]) - 1:
            if q == None:
                dict1.append(" ")
    #print(dict1)

    k=re.match(r'.*?(县|区|市)',m)
    if k:
        kk=k.group()
        dict1.append(kk)
        m=re.sub(kk,"",m,1)
    else:
        dict1.append("")
    k=re.match(r'.*?(街道|镇|乡)',m)
    if k:
        kk = k.group()
        dict1.append(kk)
        m = re.sub(kk, "", m, 1)
    else:
        dict1.append("")
    dict1.append(m)
    dict["地址"] = dict1
    #print(dict)
    Json = json.dumps(dict, indent=4, ensure_ascii=False)
    print(Json)



else:
    x=re.sub('2!',"",x,1)
    x = re.sub("1!", "", x, 1)
    x = re.sub("省", "", x, 1)
    x = re.sub("回族自治区", "", x, 1)
    x = re.sub("自治区", "", x, 1)
    x = re.sub("维吾尔族自治区", "", x, 1)
    x = re.sub("壮族自治区", "", x, 1)
    print(x)
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
        #print(m)
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
    k=re.match(r'.*?(路)',m)
    if k:
        kk = k.group()
        dict1.append(kk)
        m = re.sub(kk, "", m, 1)
    else:
        dict1.append("")
    k=re.match(r'.*?(号)',m)
    if k:
        kk = k.group()
        dict1.append(kk)
        m = re.sub(kk, "", m, 1)
    else:
        dict1.append("")
    dict1.append(m)
    dict["地址"]=dict1
    Json = json.dumps(dict, indent=4, ensure_ascii=False)
    print(Json)
   # print(dict1)

