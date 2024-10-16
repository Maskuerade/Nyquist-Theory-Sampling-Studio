import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
from PyQt5 import QtWidgets, QtCore
import view
import main
from modules import MAX_NUM_SAMPLES


class MixedSignalComponent():
    def __init__(self, magnitude=0,frequency=0, phase=0,period=1,sineWave=None):
        self.magnitude = magnitude
        self.phase = phase
        # self.frequency = 1 / period if period != 0 else 0
        self.frequency=frequency
        self.sineWave =sineWave
        self.period=period




def ComponentDynamicUpdate(self, isMixerMagChanged, isMixerFreqChanged, isMixerPhaseChanged):
        if (isMixerMagChanged == True):
                self.magnitude = self.magnitudeMixerSlider.value()
        if(isMixerFreqChanged == True):
                self.frequency = self.freqMixerSlider.value()
        if(isMixerPhaseChanged == True):
                self.phase = self.phaseMixerSlider.value()


     
def sinosoidalPlotting(self,plotWidget):
          magnitude = self.magnitude
          phase = self.phase
          frequency = self.frequency
          if frequency == 0:
             sineWave = np.zeros(10000)

          num_cycles = 20  
          num_points = 1500
          total_time = num_cycles / frequency
          self.timeVector = np.linspace(0, 2*np.pi, num_points)
          self.sineWave = magnitude * np.sin((2 * np.pi * frequency * self.timeVector) + phase)
          sineWave=self.sineWave
          self.mixerSignal=MixedSignalComponent(magnitude,frequency,phase,1,sineWave)
          self.mixerSinusoidalsArr.append(self.mixerSignal)
          summedSineWave=0
          for i in range(len(self.mixerSinusoidalsArr)):
               summedSineWave+= self.mixerSinusoidalsArr[i].sineWave
          # timeVector = np.linspace(0, 1/frequency, 10000)
          # self.sineWave = magnitude * np.sin(2 * np.pi * frequency * timeVector + phase)
         
          plotWidget.clear()  
          plotWidget.plot(self.timeVector, summedSineWave, pen='w')
          self.signalMixerMenu.addItem(f"Signal{len(self.mixerSinusoidalsArr)}")
          self.signalMixerMenu.setCurrentIndex(self.signalMixerMenu.count()-1)


def deleteSinosoidalSignal(self,plotWidget):
      num_points=1500
      self.timeVector=np.linspace(0,2*np.pi,num_points)
      if not self.mixerSinusoidalsArr:

                QtWidgets.QMessageBox.warning(self,"Error","No signals to delete")
                return 
      else:
                selectedComponentIndex = self.signalMixerMenu.currentIndex()
                self.mixerSinusoidalsArr.pop(selectedComponentIndex)
                self.signalMixerMenu.removeItem(selectedComponentIndex)

      for i in range(self.signalMixerMenu.count()):
               self.signalMixerMenu.setItemText(i, f"Signal{i+1}")
      summedSineWave=0
      for i in range(len(self.mixerSinusoidalsArr)):
               summedSineWave+= self.mixerSinusoidalsArr[i].sineWave

      plotWidget.clear()
      if np.any(summedSineWave):         
        plotWidget.plot(self.timeVector,summedSineWave,pen='w')
      

def clearSinosoidalSignals(self,plotWidget):
       if not self.mixerSinusoidalsArr:

                QtWidgets.QMessageBox.warning(self,"Error","No signals to delete")
                return 
       for _ in range(len(self.mixerSinusoidalsArr)):
              self.mixerSinusoidalsArr.pop()
       plotWidget.clear()
       self.phaseMixerSlider.setValue(0)
       self.freqMixerSlider.setValue(0)
       self.magnitudeMixerSlider.setValue(0)
       self.signalMixerMenu.clear()

def sampleButtonPressed(self):
        if not self.mixerSinusoidalsArr:

                        QtWidgets.QMessageBox.warning(self,"Error","No signal is found to be Sampled")
                        return 
        summedSineWave=0
        for i in range(len(self.mixerSinusoidalsArr)):
                summedSineWave+= self.mixerSinusoidalsArr[i].sineWave
        summedSineWave=summedSineWave.tolist()
        main.settingNewOriginalSignal(self,summedSineWave)
        self.windowTabs.setCurrentIndex(1)
        

           

def getMaxFrequecnyComponent(self):
         ans = self.mixerSinusoidalsArr[0].frequency
         for i in range(len(self.mixerSinusoidalsArr)):
              if self.mixerSinusoidalsArr[i].frequency > ans:
                     ans = self.mixerSinusoidalsArr[i].frequency
         return ans            