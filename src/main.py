from modules import *
import sys
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import csv, wfdb
import numpy as np 
import pandas as pd
from math import ceil
#Local Imports

import modules
import connectors
import view
import mixer
#Globals
main_Window = any


class MainWindow(QtWidgets.QMainWindow, ):
    def __init__(self,*args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        uic.loadUi("./UI/layout.ui",self)

        self.setWindowTitle("Sampling-Studio")
        self.setWindowIcon(QtGui.QIcon("./Images/radio-waves.png"))
        init_connectors(self)
        
        self.isSamplerEmpty  = True
        self.timeVector=[]
        self.mixerSinusoidalsArr = []
 
        self.plotsItems = [] # shayla kol el plotitems

        # graph1 -> Orginal , graph2 -> reConsrtructed , Graph3 -> Difference (error)
        self.plotsItems.append(Plotting(self.samplerGraph1.plot())) # original signal --> 0
        self.plotsItems.append(Plotting(self.samplerGraph1.plot())) # sampled points  --> 1

        self.plotsItems.append(Plotting(self.samplerGraph2.plot())) # reconstructed signal --> 2 
        self.plotsItems.append(Plotting(self.samplerGraph3.plot())) # difference signal (error) --> 3
        self.originalSignal = Signal()
        self.magnitude=0
        self.frequency=0
        self.phase=0

        self.isAddedNoise = False
        self.isNoiseChecked = False
        self.noiseSlider.hide()
        self.snrLabel.hide()
        self.snrLcd.hide()


        # self.mixerSignal = mixer.MixedSignalComponent()
        #  self.reconstructedSignal = Signal()
        # self.selectedOrigianlSignal = SampledPoints()


    



def browseFile(self):
     self.fileName = QFileDialog.getOpenFileName(None,"Open a File","./",filter="Raw Data(*.txt *.csv *.xls)" )
     if self.fileName[0]:
                  
                  openFile(self,self.fileName[0])
                  ResettingNoise(self)  
                  view.signalPlotting(self) 


                  
  

def openFile(self, path:str,):
            timeArr, amplitudeArr = [],[]
            length = len(path)
            fileExtentsion = path[length-3:]
            self.fsampling = 1
            if fileExtentsion == "csv" or fileExtentsion == "txt" or fileExtentsion == "xls":
               with open(path, 'r') as file:
                csv_data = csv.reader(file, delimiter=',')
                for row in csv_data:
                      timeArr.append(float(row[0]))
                      amplitudeArr.append(float(row[1]))
                      if len(timeArr)>=modules.MAX_NUM_SAMPLES:
                                break
            self.fsampling = 1/(timeArr[1]-timeArr[0])
            self.originalSignal.time = timeArr
            self.originalSignal.amplitude = amplitudeArr 
            self.isAddedNoise== False
            self.noiseSlider.setValue(0)
   
            
           
          #  add the data to a certain Signal Object


def settingNewOriginalSignal(self,summedSineWave):
        
        self.originalSignal.amplitude = summedSineWave
        self.originalSignal.time=self.timeVector
        self.fsampling = 1/(self.timeVector[1]-self.timeVector[0])
        if (self.isAddedNoise==True):
              modules.Signal.addWhiteNoise(self,self.originalSignal,self.noiseSlider.value())
        ResettingNoise(self)



        view.signalPlotting(self,None ,True)

def init_connectors(self):
        self.browseSamplerButton.clicked.connect(lambda:browseFile(self))
        self.FreqSamplerSlider.valueChanged.connect(lambda:self.freqSamplerLcd.display(self.FreqSamplerSlider.value()))
        self.FreqSamplerSlider.setMinimum(1)
        self.FreqSamplerSlider.valueChanged.connect(lambda:self.freqSamplerFactorLcd.display(round(self.FreqSamplerSlider.value()/self.maxFreqSamplerLcd.value(),1)))
        self.FreqSamplerSlider.sliderReleased.connect(lambda:view.samplingPlotting(self,self.FreqSamplerSlider.value()))

        ###########   Mask
        self.magnitudeMixerSlider.valueChanged.connect(lambda:mixer.ComponentDynamicUpdate(self,True, False, False ))      
        self.freqMixerSlider.valueChanged.connect(lambda:mixer.ComponentDynamicUpdate(self, False, True, False))
        self.phaseMixerSlider.valueChanged.connect(lambda:mixer.ComponentDynamicUpdate(self, False, False, True))

        self.magnitudeMixerSlider.valueChanged.connect(lambda:self.magnitudeMixerLcd.display(self.magnitudeMixerSlider.value()))
        self.freqMixerSlider.valueChanged.connect(lambda:self.freqMixerLcd.display(self.freqMixerSlider.value()))
        self.phaseMixerSlider.valueChanged.connect(lambda:self.phaseMixerLcd.display(self.phaseMixerSlider.value()))
        self.confirmMixerButton.clicked.connect(lambda: mixer.sinosoidalPlotting(self,self.mixerGraph1))
        self.deleteMixerButton.clicked.connect(lambda:mixer.deleteSinosoidalSignal(self,self.mixerGraph1))
        self.clearMixerButton.clicked.connect(lambda:mixer.clearSinosoidalSignals(self,self.mixerGraph1))
        self.sampleMixerButton.clicked.connect(lambda:mixer.sampleButtonPressed(self))
        self.noiseSlider.setMinimum(0)
        self.noiseSlider.setMaximum(10)   

        self.noiseCheckbox.toggled.connect(lambda:view.addNoiseControlsView(self))

        self.noiseSlider.valueChanged.connect(lambda: modules.Signal.addWhiteNoise(self,self.originalSignal, self.noiseSlider.value()))
        self.clearSamplerButton.clicked.connect(lambda:view.clearingGraphs(self))



def ResettingNoise(self):
        self.noiseSlider.show()
        self.noiseSlider.setValue(0)
        self.isAddedNoise= False
        self.noiseSlider.hide()
        self.snrLabel.hide()
        self.snrLcd.hide()
        self.noiseCheckbox.setCheckState(False)
        self.FreqSamplerSlider.setValue(0)
        ###########
def main():
     myapp = QtWidgets.QApplication(sys.argv)
     main_Window = MainWindow()
     main_Window.show()
     sys.exit(myapp.exec_())        


if __name__ == "__main__" :
    main()    