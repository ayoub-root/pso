# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from src.ann_criterion import optimality_criterion, np
from src.pso import PSO


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 867)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(936, 867))
        MainWindow.setMaximumSize(QtCore.QSize(936, 867))
        MainWindow.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"font: 8pt \"Segoe UI\";\n"
"color: rgb(187, 187, 187);")
        self.consoleText = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 60, 391, 402))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 15, 10, 15)
        self.formLayout.setVerticalSpacing(18)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(1000000000)
        self.spinBox_2.setProperty("value", 30)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setMinimum(0.3)
        self.doubleSpinBox.setMaximum(1.2)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.9)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_2.setMinimum(0.3)
        self.doubleSpinBox_2.setMaximum(1.2)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setProperty("value", 0.4)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_3.setMinimum(0.4)
        self.doubleSpinBox_3.setMaximum(3.0)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setProperty("value", 2.5)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_3)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_4.setMinimum(0.4)
        self.doubleSpinBox_4.setMaximum(3.0)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.setProperty("value", 0.5)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_4)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_5.setMinimum(0.4)
        self.doubleSpinBox_5.setMaximum(3.0)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setProperty("value", 2.5)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_5)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_6.setMinimum(0.4)
        self.doubleSpinBox_6.setMaximum(3.0)
        self.doubleSpinBox_6.setSingleStep(0.1)
        self.doubleSpinBox_6.setProperty("value", 0.5)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_6)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_7.setMinimum(-1000000000.0)
        self.doubleSpinBox_7.setMaximum(1000000000.0)
        self.doubleSpinBox_7.setProperty("value", -10.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_7)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_8.setMinimum(-1000000000.0)
        self.doubleSpinBox_8.setMaximum(1000000000.0)
        self.doubleSpinBox_8.setProperty("value", 10.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_8)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 500, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(490, 30, 101, 21))
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 60, 391, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 0, 22)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(430, 60, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 60, 20, 411))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setWindowModality(QtCore.Qt.NonModal)
        self.line_3.setGeometry(QtCore.QRect(880, 60, 20, 411))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(480, 60, 20, 411))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setWindowModality(QtCore.Qt.NonModal)
        self.line_5.setGeometry(QtCore.QRect(490, 50, 401, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(490, 460, 401, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(40, 460, 401, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(40, 50, 401, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 101, 16))
        self.label_17.setObjectName("label_17")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 540, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(430, 540, 20, 41))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(40, 540, 20, 41))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(47, 530, 391, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(47, 570, 391, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 620, 841, 211))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                                                                         PSO"))
        self.label.setText(_translate("MainWindow", "Number of Iterations:"))
        self.label_2.setText(_translate("MainWindow", "Number of Particles:"))
        self.label_4.setText(_translate("MainWindow", "Initial Inertia Coefficient:"))
        self.label_5.setText(_translate("MainWindow", "Final Inertia Coefficient:"))
        self.label_6.setText(_translate("MainWindow", "Initial Cognitive Acceleration Coefficient:"))
        self.label_7.setText(_translate("MainWindow", "Final Cognitive Acceleration Coefficient:"))
        self.label_8.setText(_translate("MainWindow", "Initial Social Acceleration Coefficient:"))
        self.label_9.setText(_translate("MainWindow", "Final Social Acceleration Coefficient:"))
        self.label_16.setText(_translate("MainWindow", "Lower Bound:"))
        self.label_18.setText(_translate("MainWindow", "Upper Bound:"))
        self.label_3.setText(_translate("MainWindow", "Training Execution"))
        self.label_10.setText(_translate("MainWindow", "Training Details"))
        self.label_12.setText(_translate("MainWindow", "Current Iteration:"))
        self.label_13.setText(_translate("MainWindow", "Current Best Position:"))
        self.label_11.setText(_translate("MainWindow", "Cost Function Value:"))
        self.label_17.setText(_translate("MainWindow", "Training Options"))
        self.pushButton.setText(_translate("MainWindow", "Train"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton.clicked.connect(self.train)
        self.pushButton_2.clicked.connect(self.exit)

    def train(self):
        num_particles = self.spinBox_2.value()
        iter_max = self.spinBox.value()
        var_min = self.doubleSpinBox_7.value()
        var_max = self.doubleSpinBox_8.value()
        wi = self.doubleSpinBox.value()
        wf = self.doubleSpinBox_2.value()
        cpi = self.doubleSpinBox_3.value()
        cpf = self.doubleSpinBox_4.value()
        csi = self.doubleSpinBox_6.value()
        csf = self.doubleSpinBox_5.value()
        p = PSO(optimality_criterion, 60, num_particles, iter_max, var_min, var_max, wi, wf, cpi, cpf, csi, csf)
        w = p.optimize(self)
        result = optimality_criterion(w)
        self.consoleText += f'\nOptimized weights: {w}\nEvaluation of ANN performance: {result}\n\n'
        self.textBrowser.setText(self.consoleText)

    def exit(self):
        exit(0)