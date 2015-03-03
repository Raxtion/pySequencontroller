
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Form1
import Form2
import Form3
import fileSaveDialog
import Raxpy3Libbasic

#-----------------------------------------------------------------------------------------------
#parameter
RaxLib = Raxpy3Libbasic

#-----------------------------------------------------------------------------------------------


class mainsys(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Form1.Ui_Form()
        self.ui.setupUi(self)
        self.FastA_file_ori = RaxLib.openFastAfile()
        self.FastA_keylist = []
        self.FastA_file_oup = RaxLib.openFastAfile()
        
        self.seq = ""
        
        self.ui2 = QtWidgets.QDialog()
        self.Form2 = Form2.Ui_Form()
        self.Form2.setupUi(self.ui2)
        
        self.ui3 = QtWidgets.QWidget()
        self.Form3 = Form3.Ui_Form()
        self.Form3.setupUi(self.ui3)
        
        self.ui.pushButton_1.clicked.connect(self.pB_1_change)
        self.ui.pushButton_2.clicked.connect(self.pB_2_change)
        self.ui.pushButton_3.clicked.connect(self.pB_3_change)
        self.ui.pushButton_4.clicked.connect(self.pB_4_change)
        self.ui.pushButton_5.clicked.connect(self.pB_5_change)
        self.ui.pushButton_6.clicked.connect(self.pB_6_change)
        self.ui.pushButton_7.clicked.connect(self.pB_7_change)
        self.ui.pushButton_8.clicked.connect(self.pB_8_change)
        self.ui.pushButton_9.clicked.connect(self.pB_9_change)
        self.ui.pushButton_10.clicked.connect(self.pB_10_change)
        self.ui.pushButton_11.clicked.connect(self.pB_11_change)
        self.ui.pushButton_12.clicked.connect(self.pB_12_change)
        self.ui.pushButton_14.clicked.connect(self.pB_14_change)
        self.ui.pushButton_15.clicked.connect(self.pB_15_change)

    def pB_1_change(self, ):
        if self.FastA_file_ori.data_number == 0:
            InputWord = self.ui.textEdit_1.toPlainText()
            if self.ui.radioButton_1.isChecked() is True:
                nuclotides = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']
                E = [x for x in InputWord if x in nuclotides]
                InputWord = "".join(E)
            elif self.ui.radioButton_2.isChecked() is True:
                nuclotides = ['A', 'U', 'G', 'C', 'a', 'u', 'g', 'c']
                E = [x for x in InputWord if x in nuclotides]
                InputWord = "".join(E)
            elif self.ui.radioButton_3.isChecked() is True:
                InputWord = InputWord.lower()
                peptide = ['f', 'l', 'i', 'm', 'v', 's', 'p', 't', 'a', 'y', 'h', 'q', 'n', 'k', 'd', 'e', 'c', 'w', 'r', 'g']
                E = [x for x in InputWord if x in peptide]
                InputWord = "".join(E)
            self.ui.textEdit_2.setText(InputWord)
            self.seq = InputWord
        else:
            self.FastA_file_oup.build(self.FastA_file_ori.FastA_dictionary.copy())
            self.seq = ""
            self.ui.textEdit_2.setText(self.FastA_file_ori.report())
        
    def pB_2_change(self, ):
        if self.FastA_file_oup.data_number == 0:
            InputWord = self.seq
            InputWord = RaxLib.ntComRev(InputWord, 'nC', 'r')
            self.ui.textEdit_2.setText(InputWord)
            self.seq = InputWord
        else:
            for key in self.FastA_keylist:
                InputWord = self.FastA_file_oup.FastA_dictionary[key]
                InputWord = RaxLib.ntComRev(InputWord, 'nC', 'r')
                self.FastA_file_oup.FastA_dictionary.pop(key)
                self.FastA_file_oup.FastA_dictionary[key] = InputWord
            self.ui.textEdit_2.setText(self.FastA_file_oup.report())
        
    def pB_3_change(self, ):
        if self.FastA_file_oup.data_number == 0:
            if self.ui.radioButton_3.isChecked() is True:
                pass
            else:
                InputWord = self.seq
                InputWord = RaxLib.ntComRev(InputWord, 'C', 'nr')
                self.ui.textEdit_2.setText(InputWord)
                self.seq = InputWord
        else:
            for key in self.FastA_keylist:
                InputWord = self.FastA_file_oup.FastA_dictionary[key]
                InputWord = RaxLib.ntComRev(InputWord, 'C', 'nr')
                self.FastA_file_oup.FastA_dictionary.pop(key)
                self.FastA_file_oup.FastA_dictionary[key] = InputWord
            self.ui.textEdit_2.setText(self.FastA_file_oup.report())
        
    def pB_4_change(self, ):
        _translate = QtCore.QCoreApplication.translate
        if self.FastA_file_oup.data_number == 0:
            if self.ui.radioButton_3.isChecked() is True:
                pass
            else:
                if self.ui.pushButton_4.text() == 'Transcription':
                    InputWord = self.seq
                    InputWord = RaxLib.ntComRev(InputWord, 'nC', 'nr', 'U or L', 'RNA')
                    self.ui.textEdit_2.setText(InputWord)
                    self.seq = InputWord
                    self.ui.pushButton_4.setText(_translate('Form', 'reverseTranscript', None))
                elif self.ui.pushButton_4.text() == 'reverseTranscript':
                    InputWord = self.seq
                    InputWord = RaxLib.ntComRev(InputWord, 'nC', 'nr', 'U or L', 'DNA')
                    self.ui.textEdit_2.setText(InputWord)
                    self.seq = InputWord
                    self.ui.pushButton_4.setText(_translate('Form', 'Transcription', None))
        else:
            pass
        
    def pB_5_change(self, ):
        if self.FastA_file_oup.data_number == 0:
            if ' ' in self.ui.textEdit_2.toPlainText() or self.ui.radioButton_3.isChecked() is True:
                pass
            else:
                E = [(x[0], x[1]) for x in self.Form3._gene_code_list]
                M = {x:y for x,y in E}
                InputWord = self.seq
                InputWord = RaxLib.ntComRev(InputWord, 'nC', 'nr', 'U', 'RNA')
                EE = RaxLib.listNSplit(list(InputWord), 3)
                item_list = ["".join(x) for x in EE]
                E = []
                #E = [M[x] for x in item_list]
                for item in item_list:
                    try:
                        E.append(M[item])
                    except:
                        E.append(RaxLib.ntComRev(item, 'nC', 'nr', 'L', 'RNA'))
                InputWord = ' '.join(E)
                self.ui.textEdit_2.setText(InputWord)
                self.seq = InputWord
        else:
            pass
        
    def pB_6_change(self, ):
        if self.FastA_file_oup.data_number == 0:
            if self.ui.textEdit_2.toPlainText() == "":
                self.ui.textEdit_2.setText(str(len(self.ui.textEdit_1.toPlainText())))
            else:
                self.ui.textEdit_2.setText(str(len(self.ui.textEdit_2.toPlainText())))
        else:
            self.ui.textEdit_2.setText(str(self.FastA_file_ori.data_number))
        
    def pB_7_change(self, ):
        _translate = QtCore.QCoreApplication.translate
        if self.FastA_file_oup.data_number == 0:
            if self.ui.radioButton_3.isChecked() is True:
                pass
            else:
                if self.ui.pushButton_7.text() == 'Split':
                    InputWord = self.seq
                    E = list(InputWord)
                    E = RaxLib.listNSplit(E, 3)
                    InputWord = ' '.join(["".join(x) for x in E])
                    self.ui.textEdit_2.setText(InputWord)
                    self.seq = InputWord
                    self.ui.pushButton_7.setText(_translate('Form', 'Join', None))
                elif self.ui.pushButton_7.text() == 'Join':
                    InputWord = self.seq
                    InputWord = InputWord.replace(' ', "")
                    self.ui.textEdit_2.setText(InputWord)
                    self.seq = InputWord
                    self.ui.pushButton_7.setText(_translate('Form', 'Split', None))
        else:
            pass
        
    def pB_8_change(self, ):
        _translate = QtCore.QCoreApplication.translate
        if self.FastA_file_oup.data_number == 0:
            if self.ui.pushButton_8.text() == 'Ucase':
                InputWord = self.seq
                InputWord = RaxLib.ntComRev(InputWord, 'nC', 'nr', 'U', )
                self.ui.textEdit_2.setText(InputWord)
                self.seq = InputWord
                self.ui.pushButton_8.setText(_translate('Form', 'Lcase', None))
            elif self.ui.pushButton_8.text() == 'Lcase':
                InputWord = self.seq
                InputWord = RaxLib.ntComRev(InputWord, 'nC', 'nr', 'L', )
                self.ui.textEdit_2.setText(InputWord)
                self.seq = InputWord
                self.ui.pushButton_8.setText(_translate('Form', 'Ucase', None))
        else:
            pass
        
    def pB_9_change(self, ):
        if self.ui.radioButton_1.isChecked() is True:
            self.ui3.show()
            change_seq = self.Form3.MultylineOutPut(self.seq)
            self.Form3.textEdit.setText(change_seq)
        else:
            pass
        
    def pB_10_change(self, ):
        if self.FastA_file_oup.data_number == 0:
            if ' ' in self.ui.textEdit_2.toPlainText() or self.ui.radioButton_3.isChecked() is True:
                pass
            else:
                translation_3_seq = self.Form3.Translation_3(self.seq)
                self.ui.textEdit_2.setText(translation_3_seq)
                self.seq = translation_3_seq
        else:
            pass
        
    def pB_11_change(self, ):
        m_fileName = ""
        m_fileName = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "Open Sequence", m_fileName, "Sequence Files (*.txt *.fa ) ")[0]
        if m_fileName == "":
            pass
        elif m_fileName.split('.')[-1] == 'fa':
            self.FastA_file_ori.open(m_fileName)
            self.FastA_keylist = list(self.FastA_file_ori.FastA_dictionary.keys())
            self.FastA_keylist.sort()
            
            display = self.FastA_file_ori.report(self.FastA_keylist)
            self.ui.textEdit_1.setText(display)
            
        else:
            rowdata = open(m_fileName, 'r').read()
            self.ui.textEdit_1.setText(rowdata)
        
    def pB_12_change(self, ):
        m_fileName = ""
        m_fileName = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QFileDialog(), "Save Sequence", m_fileName, "Sequence Files (*.txt *.fa ) ")[0]
        if self.FastA_file_ori.data_number == 0:
            
            if m_fileName == "":
                pass
            elif m_fileName.split('.')[-1] == 'fa':
                Dialog = QtWidgets.QDialog()
                self.Save_ui = fileSaveDialog.Ui_Dialog()
                self.Save_ui.setupUi(Dialog)
                Dialog.show()
                Dialog.exec_()
                if Dialog.result() == 1:
                    self.FastA_file_oup.build({self.Save_ui.lineEdit.text().split('>')[-1]:self.seq})
                    f = open(m_fileName, 'w')
                    f.write('\n'.join(self.FastA_file_oup.report().split('\n')[:-1])+'\n')
                    f.close()
                    self.FastA_file_oup.FastA_dictionary.clear()
                    
                elif Dialog.result() == 0:
                    pass
            elif m_fileName.split('.')[-1] == 'txt':
                f = open(m_fileName, 'w')
                f.write(self.seq)
                f.close()
            else:
                Massager = QtWidgets.QMessageBox()
                Massager.setText('Place add Filename extension !!')
                Massager.setWindowTitle('Filename extension')
                Massager.show()
                Massager.exec_()
                pass
        elif m_fileName == "":
            pass
        else:
            f = open(m_fileName, 'w')
            f.write(self.FastA_file_oup.report())
            f.close()
        
    def pB_14_change(self, ):
        self.ui2.show()
        
    def pB_15_change(self, ):
        self.ui.textEdit_1.clear()
        self.ui.textEdit_2.clear()
        self.seq = ""
        self.Form3.clear()
        del self.FastA_file_ori
        self.FastA_file_ori = RaxLib.openFastAfile()
        del self.FastA_file_oup
        self.FastA_file_oup = RaxLib.openFastAfile()
    
    
'''
if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = mainsys() 
    myapp.show()
    sys.exit(app.exec_())
'''
app = QtWidgets.QApplication(sys.argv)
myapp = mainsys()
myapp.show()
sys.exit(app.exec_())