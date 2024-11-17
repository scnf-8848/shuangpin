import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from Ui_Gui import Ui_MainWindow
from random import randint
from config_shuangpin import load_data, trans_shuangpinkey



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        self.Button_set.clicked.connect(self.config_data)
        self.lineEdit.textEdited.connect(self.check_input)
        self.checkBox_mode.checkStateChanged.connect(self.change_show_mode)
        self.selected_range = [] # 选择的练习项目
        self.selected_word_and_key = [[],[]] #选择的项目里所有词-拼音列表
        self.max_word_count = 0    # 选择的词的数量
        self.showed_word_and_key = ['scnf','565764'] #当前显示的字和拼音
        self.show_mode = 1 # 1-显示按键提示 0-不显示按键提示
        self.last_index = 0 # 上一个词语的序号

    
    # 应用勾选项目
    def config_data(self):
        checkboxes = [self.checkBox_00,
                      self.checkBox_01,
                      self.checkBox_02,
                      self.checkBox_03,
                      self.checkBox_04,
                      self.checkBox_05,
                      self.checkBox_06,
                      self.checkBox_07,
                      self.checkBox_08,
                      self.checkBox_09,
                      self.checkBox_10]
        self.selected_range = []
        for i,cb in enumerate(checkboxes):
            if cb.isChecked():
                self.selected_range.append(i)
        # 将所选项目的数据从词库中 提取到 选择词库.txt 并转化为对应双拼按键
        trans_shuangpinkey(self.selected_range)
        
        # 导入 选择词库和按键
        self.selected_word_and_key = load_data() 
        self.max_word_count = len(self.selected_word_and_key[0])
        # 为空则不开始
        if self.max_word_count <= 0:
            return
        # 随机选词
        i = randint(0,self.max_word_count-1)
        self.last_index = i
        self.showed_word_and_key = [self.selected_word_and_key[0][i],self.selected_word_and_key[1][i]]                                                                                                                                                                                                                                                                                                                                                                                      
        self.lineEdit.setText("")
        self.check_input()
        self.lineEdit.setFocus()    




    def check_input(self):

        # 回答正确
        if self.lineEdit.text() == self.showed_word_and_key[1]:
            self.lineEdit.setText("")
            i = randint(0,self.max_word_count-1)
            # 避免与上次重复
            if self.max_word_count != 1:
                while i == self.last_index:
                    i = randint(0,self.max_word_count-1)
            self.last_index = i
            self.showed_word_and_key = [self.selected_word_and_key[0][i],self.selected_word_and_key[1][i]]  

        # 答案不符合 验证长度 显示对应情况
        input_text = self.lineEdit.text()        
        correct_length = min(len(input_text), len(self.showed_word_and_key[1]))
        showed_key = ""
        # 1型 显示按键 未输入-灰 正确-绿色 错误-红色答案
        if self.show_mode == 1:
            for i in range(correct_length):
                if input_text[i] == self.showed_word_and_key[1][i]:
                    showed_key += f'<span style="color:green">{self.showed_word_and_key[1][i]}</span>'
                else:
                    showed_key += f'<span style="color:red; font-weight:bold">{self.showed_word_and_key[1][i]}</span>'
                # 每两个字符加一个空格
                if i%2 != 0: showed_key += ' '

            if len(input_text) < len(self.showed_word_and_key[1]):
                for i in range(len(input_text),len(self.showed_word_and_key[1])):
                    showed_key += f'<span style="color:grey">{self.showed_word_and_key[1][i]}</span>'
                    if i%2 != 0: showed_key += ' '

        # 0型 不显示按键  正确-绿色 错误-红色输入
        if self.show_mode == 0:
            for i in range(correct_length):
                if input_text[i] == self.showed_word_and_key[1][i]:
                    showed_key += f'<span style="color:green">{input_text[i]}</span>'
                else:
                    showed_key += f'<span style="color:red; font-weight:bold">{input_text[i]}</span>'
                if i%2 != 0: showed_key += ' '

        self.label_word.setText(self.showed_word_and_key[0])
        self.label_key.setText(showed_key)


    def change_show_mode(self):
        if self.checkBox_mode.isChecked():
            self.show_mode = 1
        else:
            self.show_mode = 0
        if self.max_word_count > 0:
            self.check_input()
            self.lineEdit.setFocus()    
            



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
