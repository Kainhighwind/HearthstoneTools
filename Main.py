'''TODO
    - bomber simulator

'''
from scipy.stats import hypergeom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import sys
from PyQt4 import QtGui, QtCore
import Calc_UI
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class HSCalc(QtGui.QMainWindow, Calc_UI.Ui_MainWindow):
    def __init__(self):
        super(HSCalc, self).__init__()
        self.setupUi(self)
        # set up a figure to draw on
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        #If I wanna add a navigation bar
        '''self.toolbar = NavigationToolbar(self.canvas, self)'''

        self.CalculateButton.pressed.connect(self.calculateByDraw)
        self.ResetButton.pressed.connect(self.reset)
        oddsPlot = QtGui.QVBoxLayout()
        oddsPlot.addWidget(self.canvas)
        self.GraphArea.setLayout(oddsPlot)

        # Method to plot the pmf graph

    #Method to reset the spinboxes and the table
    def reset(self):
        #clear everything
        self.numberOfOutsInDeckSpinBox.clear()
        self.remainingDeckSizeSpinBox.clear()
        self.numberOfDrawsSpinBox.clear()
        self.probabilityTable.clear()
        #paint the header title again
        matrixElement = QtGui.QTableWidgetItem()
        self.probabilityTable.setItem(0, 0, matrixElement)
        matrixElement = QtGui.QTableWidgetItem()
        self.probabilityTable.setItem(0, 1, matrixElement)
        matrixElement = QtGui.QTableWidgetItem()
        self.probabilityTable.setItem(0, 2, matrixElement)
        matrixElement = QtGui.QTableWidgetItem()
        self.probabilityTable.setItem(0, 3, matrixElement)
        item = self.probabilityTable.item(0, 0)
        item.setText(_translate("MainWindow", "Exactly", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        item = self.probabilityTable.item(0, 1)
        item.setText(_translate("MainWindow", "Probability", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        item = self.probabilityTable.item(0, 2)
        item.setText(_translate("MainWindow", "At Least", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        item = self.probabilityTable.item(0, 3)
        item.setText(_translate("MainWindow", "Probability", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)



    def calculateByDraw(self):
        # Method to calculate and display the probabilites for the number of successful draws out of a single pool of OUTS

        # hypergeometric formula: assumes draws are just total # of draws
        rv = hypergeom(self.remainingDeckSizeSpinBox.value(), self.numberOfOutsInDeckSpinBox.value(),
                       self.numberOfDrawsSpinBox.value())
        outs = np.arange(0, self.numberOfOutsInDeckSpinBox.value() + 1)
        draws = np.arange(0, self.numberOfDrawsSpinBox.value() + 1)
        PMF = rv.pmf(outs)
        self.probabilityTable.clear()

        odds = np.empty(self.numberOfOutsInDeckSpinBox.value() + 1, dtype=float)
        surviveodds = np.empty(self.numberOfOutsInDeckSpinBox.value()+1, dtype=float)
        self.probabilityTable.setRowCount(len(outs) + 1)
        self.probabilityTable.setColumnCount(4)

        # initialize the table. This code looks terrible

        i = 0
        j = 0
        while i < self.probabilityTable.columnCount():
            while j < self.probabilityTable.rowCount():
                matrixElement = QtGui.QTableWidgetItem()
                self.probabilityTable.setItem(j, i, matrixElement)
                j += 1
            i += 1
            j = 0

        item = self.probabilityTable.item(0, 0)
        item.setText(_translate("MainWindow", "Exactly", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        item = self.probabilityTable.item(0, 1)
        item.setText(_translate("MainWindow", "Probability", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        item = self.probabilityTable.item(0, 2)
        item.setText(_translate("MainWindow", "At Least", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        item = self.probabilityTable.item(0, 3)
        item.setText(_translate("MainWindow", "Probability", None))
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        #Loop to build the table and calculate the PMF and SF based on inputs
        if len(outs)> len(draws):
            maxSuccess = draws
        else:
            maxSuccess = outs
        for out in maxSuccess:
            # creating spaces in table
            matrixElement = QtGui.QTableWidgetItem()
            self.probabilityTable.setItem(out + 1, 0, matrixElement)
            matrixElement = QtGui.QTableWidgetItem()
            self.probabilityTable.setItem(out + 1, 1, matrixElement)

            # Calculate PMF for each out
            odds[out] = rv.pmf(out)
            surviveodds[out] = rv.sf(out)

            # populate the table
            # exact outs
            item = self.probabilityTable.item(out + 1, 0)
            item.setText(_translate("MainWindow", "{0:d}".format(out), None))
            item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            item = self.probabilityTable.item(out + 1, 1)
            item.setText(_translate("MainWindow", "{0:3f}".format(odds[out]), None))
            item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            # Atleast outs
            if out != 0:  # atleast zero outs is meaningless
                item = self.probabilityTable.item(out + 1, 2)
                item.setText(_translate("MainWindow", "{0:d}".format(out), None))
                item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                item = self.probabilityTable.item(out + 1, 3)
                item.setText(_translate("MainWindow", "{0:3f}".format(surviveodds[out-1]), None))
                item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        # create the pmf graph)
        print(surviveodds)

        print(outs)
        print("The odds of getting at least {0:d} outs is {1:3f}".format(out, odds[out]))

        #### Bar graphs if I want to add them later


        ax = self.figure.add_subplot(111)
        width = 0.3
        ax.bar(outs, PMF, width, color = 'r' )
        ax.hold(True)
        ax.bar(outs+(1.2*width+1), surviveodds, width, color = 'b')
        ax.set_xticks(outs + width)
        ax.set_xticklabels(outs)
        ax.hold(False)
        self.canvas.draw()



def main():
    app = QtGui.QApplication(sys.argv)
    form = HSCalc()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()
