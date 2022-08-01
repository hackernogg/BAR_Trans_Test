import json
from threading import Thread
import luadata
from langid.langid import LanguageIdentifier, model

f_En_Inter = open('interface_en.json')
f_En_Scav = open('scavengers_en.json')
f_En_Tips = open('tips_en.json')
f_En_Units = open('units_en.json')
f_En_Feat = open('features_en.json')

trans_file_input = input("Enter your trans file full name, empty = test_unicode.lua (default)")
trans_file = ""
if trans_file_input == "":
    trans_file = 'test_unicode.lua'
else:
    trans_file = trans_file_input


dataCN = luadata.read(trans_file, encoding="utf-8")
dataEN_Inter = json.load(f_En_Inter)
dataEn_Scav = json.load(f_En_Scav)
dataEn_Tips = json.load(f_En_Tips)
dataEn_Units = json.load(f_En_Units)
dataEn_Feat = json.load(f_En_Feat)


identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

trans_lan = list(dataCN.keys())[0]
print("\n The targe trans language is ",trans_lan)
#CN_UI_ARRAY= list(dataCN['zh']['ui'].items())

def find_value(dict_info,path_list):
    if isinstance(dict_info[path_list[0]],str):
        #print(path_list[0])
        #print(dict_info)
        #print(dict_info[path_list[0]])
        answer = dict_info[path_list[0]]
        return answer
    else:
        return find_value(dict_info[path_list[0]],path_list[1:])

'''
function that get the number of key that each dict got with path info record
sample A = {
                B,
                C,
                D
            }
     A got 4 Keys, bcs (A,B,C,D) including itself
return the result as three list
'''

def num_list_array(dict_info,path_info,key_list,num_list,path_list,trans_Cnt):
    #--print(len(dict_info.keys())+1)
    num_list.append(len(dict_info.keys())+1)
    #num list ++

    for i in dict_info:
        #--print(i)
        key_list.append(i)
        #key list ++
        path = path_info + [i]
        #--print(path)
        path_list.append(path)
        #path list ++
        if isinstance(dict_info[i],dict):

            key = list(dict_info[i].keys())[0]

            num_list_array(dict_info[i],path,key_list,num_list,path_list,trans_Cnt)
        else:
            #--print("1")
            num_list.append(1)
            #num list ++
            if (identifier.classify(dict_info[i])[0]) == 'en' :
                trans_Cnt[0] = trans_Cnt[0] + 1
                #--print('En--------',dict_info[i],trans_Cnt)

    return key_list,num_list,path_list,trans_Cnt

EN_UI_key_list,EN_UI_num_list,EN_UI_path_list,EN_UI_trans_cnt=[],[],[],[]
EN_SCAV_key_list,EN_SCAV_num_list,EN_SCAV_path_list,EN_SCAV_trans_cnt=[],[],[],[]
EN_TIPS_key_list,EN_TIPS_num_list,EN_TIPS_path_list,EN_TIPS_trans_cnt=[],[],[],[]
EN_UNITS_key_list,EN_UNITS_num_list,EN_UNITS_path_list,EN_UNITS_trans_cnt=[],[],[],[]
EN_FEAT_key_list,EN_FEAT_num_list,EN_FEAT_path_list,EN_FEAT_trans_cnt=[],[],[],[]

CN_UI_key_list,CN_UI_num_list,CN_UI_path_list,CN_UI_trans_cnt=[],[],[],[]
CN_SCAV_key_list,CN_SCAV_num_list,CN_SCAV_path_list,CN_SCAV_trans_cnt=[],[],[],[]
CN_TIPS_key_list,CN_TIPS_num_list,CN_TIPS_path_list,CN_TIPS_trans_cnt=[],[],[],[]
CN_UNITS_key_list,CN_UNITS_num_list,CN_UNITS_path_list,CN_UNITS_trans_cnt=[],[],[],[]
CN_FEAT_key_list,CN_FEAT_num_list,CN_FEAT_path_list,CN_FEAT_trans_cnt=[],[],[],[]

def Make_En_list():
    global EN_UI_key_list,EN_UI_num_list,EN_UI_path_list,EN_UI_trans_cnt
    global EN_SCAV_key_list,EN_SCAV_num_list,EN_SCAV_path_list,EN_SCAV_trans_cnt
    global EN_TIPS_key_list,EN_TIPS_num_list,EN_TIPS_path_list,EN_TIPS_trans_cnt
    global EN_UNITS_key_list,EN_UNITS_num_list,EN_UNITS_path_list,EN_UNITS_trans_cnt
    global EN_FEAT_key_list,EN_FEAT_num_list,EN_FEAT_path_list,EN_FEAT_trans_cnt

    EN_UI_key_list,EN_UI_num_list,EN_UI_path_list,EN_UI_trans_cnt = num_list_array(dataEN_Inter['en']['ui'],[],[],[],[],[0])
    EN_SCAV_key_list,EN_SCAV_num_list,EN_SCAV_path_list,EN_SCAV_trans_cnt = num_list_array(dataEn_Scav['en']['scav'],[],[],[],[],[0])
    EN_TIPS_key_list,EN_TIPS_num_list,EN_TIPS_path_list,EN_TIPS_trans_cnt = num_list_array(dataEn_Tips['en']['tips'],[],[],[],[],[0])
    EN_UNITS_key_list,EN_UNITS_num_list,EN_UNITS_path_list,EN_UNITS_trans_cnt = num_list_array(dataEn_Units['en']['units'],[],[],[],[],[0])
    EN_FEAT_key_list,EN_FEAT_num_list,EN_FEAT_path_list,EN_FEAT_trans_cnt = num_list_array(dataEn_Feat['en']['features'],[],[],[],[],[0])
    
def Make_Trans_list():
    global CN_UI_key_list,CN_UI_num_list,CN_UI_path_list,CN_UI_trans_cnt
    global CN_SCAV_key_list,CN_SCAV_num_list,CN_SCAV_path_list,CN_SCAV_trans_cnt
    global CN_TIPS_key_list,CN_TIPS_num_list,CN_TIPS_path_list,CN_TIPS_trans_cnt
    global CN_UNITS_key_list,CN_UNITS_num_list,CN_UNITS_path_list,CN_UNITS_trans_cnt
    global CN_FEAT_key_list,CN_FEAT_num_list,CN_FEAT_path_list,CN_FEAT_trans_cnt

    CN_UI_key_list,CN_UI_num_list,CN_UI_path_list,CN_UI_trans_cnt = num_list_array(dataCN[trans_lan]['ui'],[],[],[],[],[0])
    CN_SCAV_key_list,CN_SCAV_num_list,CN_SCAV_path_list,CN_SCAV_trans_cnt = num_list_array(dataCN[trans_lan]['scav'],[],[],[],[],[0])
    CN_TIPS_key_list,CN_TIPS_num_list,CN_TIPS_path_list,CN_TIPS_trans_cnt = num_list_array(dataCN[trans_lan]['tips'],[],[],[],[],[0])
    CN_UNITS_key_list,CN_UNITS_num_list,CN_UNITS_path_list,CN_UNITS_trans_cnt = num_list_array(dataCN[trans_lan]['units'],[],[],[],[],[0])
    CN_FEAT_key_list,CN_FEAT_num_list,CN_FEAT_path_list,CN_FEAT_trans_cnt = num_list_array(dataCN[trans_lan]['features'],[],[],[],[],[0])

def mistake_check(Key_List_OG,Key_List_Tran):
    mistake = False
    mistake_index = -1
    if len(Key_List_Tran) <= len(Key_List_OG):
        for i in range(0,len(Key_List_OG)):
            if Key_List_Tran[i] != Key_List_OG[i]:
                mistake = True
                mistake_index = i
                return mistake_index

    else:
        for i in range(0,len(Key_List_Tran)):
            if Key_List_Tran[i] != Key_List_OG[i]:
                mistake = True
                mistake_index = i
                return mistake_index
    return mistake_index

def mistake_check_2(Path_List_OG,Path_List_Trans):
    mistake = False
    mistake_index_List_not_in_OG = []
    mistake_index_List_not_in_Trans = []
    for i in Path_List_Trans:
        if not (i in Path_List_OG):
            mistake = True
            mistake_index_List_not_in_OG.append(i)
    for i in Path_List_OG:
        if not (i in Path_List_Trans):
            mistake = True
            mistake_index_List_not_in_Trans.append(i)
    return mistake_index_List_not_in_OG,mistake_index_List_not_in_Trans

def percentage(part, whole):
    percentage = 100 * float(part)/float(whole)
    return str(percentage) + "%"

def show_error():
    UI_outrange, UI_miss = mistake_check_2(EN_UI_path_list,CN_UI_path_list)
    SCAV_outrange, SCAV_miss = mistake_check_2(EN_SCAV_path_list,CN_SCAV_path_list)
    TIPS_outrange, TIPS_miss = mistake_check_2(EN_TIPS_path_list,CN_TIPS_path_list)
    UNITS_outrange, UNITS_miss = mistake_check_2(EN_UNITS_path_list,CN_UNITS_path_list)
    FEAT_outrange, FEAT_miss = mistake_check_2(EN_FEAT_path_list,CN_FEAT_path_list)
    print("\n!!!!!!!!!!!!!!!!!!!    UI    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n---------------UI trans Out range keys:-----------------")
    print("\n",UI_outrange)
    print("\n---------------UI trans missing keys:-----------------")
    print("\n",UI_miss)
    print('\n---------------UI translate rate:----------------')
    print('\n######',percentage(EN_UI_trans_cnt[0]-CN_UI_trans_cnt[0],EN_UI_trans_cnt[0]),'######')

    print("\n!!!!!!!!!!!!!!!!!!!    SCAV    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n---------------SCAV trans Out range keys:-----------------")
    print("\n",SCAV_outrange)
    print("\n---------------SCAV trans missing keys:-----------------")
    print("\n",SCAV_miss)
    print('\n---------------SCAV translate rate:----------------')
    print('\n######',percentage(EN_SCAV_trans_cnt[0]-CN_SCAV_trans_cnt[0],EN_SCAV_trans_cnt[0]),'######')

    print("\n!!!!!!!!!!!!!!!!!!!    TIPS    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n---------------TIPS trans Out range keys:-----------------")
    print("\n",TIPS_outrange)
    print("\n---------------TIPS trans missing keys:-----------------")
    print("\n",TIPS_miss)
    print('\n---------------TIPS translate rate:----------------')
    print('\n######',percentage(EN_TIPS_trans_cnt[0]-CN_TIPS_trans_cnt[0],EN_TIPS_trans_cnt[0]),'######')

    print("\n!!!!!!!!!!!!!!!!!!!    UNITS    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n---------------UNITS trans Out range keys:-----------------")
    print("\n",UNITS_outrange)
    print("\n---------------UNITS trans missing keys:-----------------")
    print("\n",UNITS_miss)
    print('\n---------------UNITS translate rate:----------------')
    print('\n######',percentage(EN_UNITS_trans_cnt[0]-CN_UNITS_trans_cnt[0],EN_UNITS_trans_cnt[0]),'######')

    print("\n!!!!!!!!!!!!!!!!!!!    FEATURES    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n---------------FEATURES trans Out range keys:-----------------")
    print("\n",FEAT_outrange)
    print("\n---------------FEATURES trans missing keys:-----------------")
    print("\n",FEAT_miss)
    print('\n---------------FEATURES translate rate:----------------')
    print('\n######',percentage(EN_FEAT_trans_cnt[0]-CN_FEAT_trans_cnt[0],EN_FEAT_trans_cnt[0]),'######')


t1 = Thread(target=Make_En_list)
t2 = Thread(target=Make_Trans_list)

t1.start()
t2.start()

t1.join()
t2.join()

show_error()

