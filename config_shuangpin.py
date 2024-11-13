from pypinyin import pinyin
from pypinyin.contrib.tone_convert import to_initials, to_finals


# 读取双拼映射规则
def read_rule():
    rule = {}
    with open('双拼规则.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            old_value, new_value = line.strip().split()
            rule[old_value] = new_value
    return rule


# 汉字转拼音 再转双拼按键
def hanzi_2_shuangpin(line,rule):
    pykey = ''
    for word_pinyin in pinyin(line,strict=False):
        i = to_initials(word_pinyin[0],strict=False) # 声母
        f = to_finals(word_pinyin[0],strict=False) # 韵母

#       零声母特殊处理
#       单字母韵母，零声母 + 韵母所在键：啊=aa 哦=oo 额=ee
#       双字母韵母，零声母 + 韵母末字母：爱=ai 恩=en 欧=ou
#       三字母韵母，零声母 + 韵母所在键：昂=ah
#       简单说：双字母音节保持全拼方式，一三字母音节为首字母加韵母所在键
        if i == '':
            if f in ['a','o','e']:
                i = f[0]
            if f in ['ang']:
                i = 'a'
                f = 'h'
        else:
            i = rule.get(i,i)
            f = rule.get(f,f)
        pykey += i + f
    return pykey



# 把选择的词语txt转换成按键txt
def trans_shuangpinkey(selected_range:list):
    rule = read_rule()
    selected_word = []
    selected_pykey=[]

    for i in range(0,11):
        if i in selected_range:
            with open(f'./词库/{i}.txt', 'r',encoding='utf - 8') as f:
                lines = f.readlines()
                for line in lines:
                    selected_word.append(line.strip())
                    selected_pykey.append(hanzi_2_shuangpin(line.strip(),rule))


    with open('选择词库.txt', 'w',encoding='utf - 8') as output_file:
        for line in selected_word:
            output_file.write(line + '\n')    

    with open('选择词库按键.txt', 'w',encoding='utf - 8') as output_file:
        for line in selected_pykey:
            output_file.write(line + '\n')



# 导入 选择词库和按键
def load_data():
    word = []
    key = []
    with open('选择词库.txt', 'r',encoding='utf - 8') as input_file:
        lines = input_file.readlines()
        for line in lines:
            word.append(line.strip())

    with open('选择词库按键.txt', 'r',encoding='utf - 8') as input_file:
        lines = input_file.readlines()
        for line in lines:
            key.append(line.strip())    
    return [word,key]    



