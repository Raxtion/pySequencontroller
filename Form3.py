# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form3.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Raxpy3Libbasic

#-----------------------------------------------------------------------------------------------
#parameter
RaxLib = Raxpy3Libbasic

#-----------------------------------------------------------------------------------------------


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 450)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("windows_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 541, 391))

        self.ui3 = Form
        self.gridLayout = QtWidgets.QGridLayout(self.ui3)
        self.gridLayout.setObjectName("gridLayout")

        font = QtGui.QFont()
        font.setFamily("DotumChe")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.RS = QtGui.QResizeEvent(self.ui3.size(), QtCore.QSize(400, 450))

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self._gene_code_list = [('UUU', 'F', 'Phe '), ('UUC', 'F', 'Phe '), ('UUA', 'L', 'Leu '), ('UUG', 'L', 'Leu '),
                                ('CUU', 'L', 'Leu '), ('CUC', 'L', 'Leu '), ('CUA', 'L', 'Leu '), ('CUG', 'L', 'Leu '),
                                ('AUU', 'I', 'Ile '), ('AUC', 'I', 'Ile '), ('AUA', 'I', 'ile '), ('AUG', 'M', 'Met '),
                                ('GUU', 'V', 'Val '), ('GUC', 'V', 'Val '), ('GUA', 'V', 'Val '), ('GUG', 'V', 'Val '),
                                ('UCU', 'S', 'Ser '), ('UCC', 'S', 'Ser '), ('UCA', 'S', 'Ser '), ('UCG', 'S', 'Ser '),
                                ('CCU', 'P', 'Pro '), ('CCC', 'P', 'Pro '), ('CCA', 'P', 'Pro '), ('CCG', 'P', 'Pro '),
                                ('ACU', 'T', 'Thr '), ('ACC', 'T', 'Thr '), ('ACA', 'T', 'Thr '), ('ACG', 'T', 'Thr '),
                                ('GCU', 'A', 'Ala '), ('GCC', 'A', 'Ala '), ('GCA', 'A', 'Ala '), ('GCG', 'A', 'Ala '),
                                ('UAU', 'Y', 'Tyr '), ('UAC', 'Y', 'Tyr '), ('UAA', 'Stop', 'Stop'), ('UAG', 'Stop', 'Stop'),
                                ('CAU', 'H', 'His '), ('CAC', 'H', 'His '), ('CAA', 'Q', 'Gln '), ('CAG', 'Q', 'Gln '),
                                ('AAU', 'N', 'Asn '), ('AAC', 'N', 'Asn '), ('AAA', 'K', 'Lys '), ('AAG', 'K', 'Lys '),
                                ('GAU', 'D', 'Asp '), ('GAC', 'D', 'Asp '), ('GAA', 'E', 'Glu '), ('GAG', 'E', 'Glu '),
                                ('UGU', 'C', 'Cys '), ('UGC', 'C', 'Cys '), ('UGA', 'Stop', 'Stop'), ('UGG', 'W', 'Trp '),
                                ('CGU', 'R', 'Arg '), ('CGC', 'R', 'Arg '), ('CGA', 'R', 'Arg '), ('CGG', 'R', 'Arg '),
                                ('AGU', 'S', 'Ser '), ('AGC', 'S', 'Ser '), ('AGA', 'R', 'Arg '), ('AGG', 'R', 'Arg '),
                                ('GGU', 'G', 'Gly '), ('GGC', 'G', 'Gly '), ('GGA', 'G', 'Gly '), ('GGG', 'G', 'Gly ')]


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MultylineOutput"))

    def clear(self, ):
        self.textEdit.setText("")

    def Translation_3(self, seq):
        E = [(x[0], x[2]) for x in self._gene_code_list]
        M = {x:y for x,y in E}
        InputWord = seq
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
        InputWord = "".join(E)
        seq = InputWord
        return seq

    def seq_3Split(self, seq):
        InputWord = seq
        E = list(InputWord)
        E = RaxLib.listNSplit(E, 3)
        outputWord = ' '.join(["".join(x) for x in E])
        return outputWord

    def MultylineOutPut(self, seq):
        Line_one = self.seq_3Split(RaxLib.ntComRev(seq, 'nC', 'nr'))
        Line_two = self.seq_3Split(RaxLib.ntComRev(seq, 'C', 'r'))
        Line_thr = self.Translation_3(seq)

        Line_one_E = RaxLib.listNSplit([x for x in Line_one], int(0.12*self.ui3.width()-2))
        Line_two_E = RaxLib.listNSplit([x for x in Line_two], int(0.12*self.ui3.width()-2))
        Line_thr_E = RaxLib.listNSplit([x for x in Line_thr], int(0.12*self.ui3.width()-2))

        E_ = []
        i = 1
        for x in Line_one_E:
            E_.append(["".join(x) for x in Line_one_E][i-1])
            E_.append(["".join(x) for x in Line_two_E][i-1])
            E_.append(["".join(x) for x in Line_thr_E][i-1])
            E_.append(""*len(["".join(x) for x in Line_thr_E][i-1]))
            i += 1

        display = '\n'.join(E_)

        return display


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())