from modules import * 
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg 
import numpy as np
import connectors
import main
import mixer

def signalPlotting(self, plotWidget =None,isMixer = False ):
     if isMixer == True:
          self.plotsItems[0].plotWidget.clear()
          self.plotsItems[1].plotWidget.clear()
          self.plotsItems[2].plotWidget.clear()
          self.plotsItems[3].plotWidget.clear()
          self.isSamplerEmpty = False
          self.originalSignal.maxFrequency = mixer.getMaxFrequecnyComponent(self)
          self.FreqSamplerSlider.setMaximum(4*int(self.originalSignal.maxFrequency))
          self.maxFreqSamplerLcd.display(self.originalSignal.maxFrequency)
          self.plotsItems[0].plotWidget.setData(self.originalSignal.time,self.originalSignal.amplitude)

          if(self.isAddedNoise == True):
               self.plotsItems[0].plotWidget.setData(self.originalSignal.time,self.originalSignal.amplitudeWithNoise)
     else:
          
          
          self.plotsItems[0].plotWidget.clear()
          self.plotsItems[1].plotWidget.clear()
          self.plotsItems[2].plotWidget.clear()
          self.plotsItems[3].plotWidget.clear()
          self.isSamplerEmpty = False
          self.originalSignal.setMaxFrequency()
          self.FreqSamplerSlider.setMaximum(4*int(self.originalSignal.maxFrequency))
          self.maxFreqSamplerLcd.display(self.originalSignal.maxFrequency)
          self.plotsItems[0].plotWidget.setData(self.originalSignal.time,self.originalSignal.amplitude)

          if(self.isAddedNoise == True):
               self.plotsItems[0].plotWidget.setData(self.originalSignal.time,self.originalSignal.amplitudeWithNoise)
          
     
def addNoiseControlsView(self):
     if self.isSamplerEmpty == True:
              self.noiseCheckbox.setChecked(False);
              QtWidgets.QMessageBox.warning(self,"Error","No signal is found")
              return 
     self.isNoiseChecked ^= True
     if(self.isNoiseChecked == True):
          self.noiseSlider.show()
          self.snrLabel.show()
          self.snrLcd.show()

     if(self.isNoiseChecked == False):
          self.isAddedNoise= False
          self.noiseSlider.hide()
          self.snrLabel.hide()
          self.snrLcd.hide()
          self.noiseSlider.setValue(0)
          signalPlotting(self)
          samplingPlotting(self,self.FreqSamplerSlider.value())



def  sincInterPolation(originalTimeArr, sampledTimerArr, sampledAmplitudeArr):
      if len(sampledTimerArr)>0:
            periodTime = sampledTimerArr[1]-sampledTimerArr[0]
      timeConvolutionShift =  np.tile(originalTimeArr, (len(sampledTimerArr), 1)) - \
        np.tile(sampledTimerArr[:, np.newaxis], (1, len(originalTimeArr)))       
      return np.dot(sampledAmplitudeArr,np.sinc(timeConvolutionShift/periodTime))


def getSampledData(timeArr = [],amplitudeArr = [] , fSampling = 0):
     sampled_timeArr , sampled_amplitudeArr = [] , []
     mxTimeShift = max(timeArr)
     for i in range(0,len(timeArr),round((len(timeArr)/mxTimeShift)/fSampling)):
          sampled_timeArr.append(timeArr[i])
          sampled_amplitudeArr.append(amplitudeArr[i])
     return sampled_timeArr,sampled_amplitudeArr     
  

def  samplingPlotting(self,sliderFs):
         if self.isSamplerEmpty == True :
             QtWidgets.QMessageBox.warning(self,"Error","No signal Added") 
             self.FreqSamplerSlider.setValue(0)
             return 
         if(self.isAddedNoise == True): 
              self.sampled_timeArr , self.sampled_amplitudeArr = getSampledData(self.originalSignal.time,self.originalSignal.amplitudeWithNoise,sliderFs)
         else:
              self.sampled_timeArr , self.sampled_amplitudeArr = getSampledData(self.originalSignal.time,self.originalSignal.amplitude,sliderFs)
         self.plotsItems[1].plotWidget.setData(self.sampled_timeArr,self.sampled_amplitudeArr, symbol="o" , pen=None , symbolPen=None , symbolSize=5,symbolBrush=(255, 0, 0))
      
         self.interPolatedAmplitudeArr = sincInterPolation(self.originalSignal.time,
                                                           np.array(self.sampled_timeArr),np.array(self.sampled_amplitudeArr))
         
         self.plotsItems[2].plotWidget.setData(self.originalSignal.time ,self.interPolatedAmplitudeArr,pen = pg.mkPen(color="#00F010",width=1 ))
         if(self.isAddedNoise==True):
               self.plotsItems[3].plotWidget.setData(self.originalSignal.time ,self.originalSignal.amplitudeWithNoise-self.interPolatedAmplitudeArr,pen = pg.mkPen(color="#d0F010",width=1 ))
         else:
               self.plotsItems[3].plotWidget.setData(self.originalSignal.time ,self.originalSignal.amplitude-self.interPolatedAmplitudeArr,pen = pg.mkPen(color="#d0F010",width=1 ))

         viewbox0 = self.plotsItems[0].plotWidget.getViewBox()
         viewbox3 = self.plotsItems[3].plotWidget.getViewBox()
          
         viewbox2 = self.plotsItems[2].plotWidget.getViewBox()
         y_range, x_range = viewbox0.viewRange()

         viewbox3.setYRange(x_range[0], x_range[1])
         viewbox3.setXRange(y_range[0], y_range[1])
         viewbox2.setYRange(x_range[0], x_range[1])
         viewbox2.setYRange(x_range[0], x_range[1])
          


def clearingGraphs(self):
     self.originalSignal.time=[]
     self.originalSignal.amplitude=[]
     self.plotsItems[0].plotWidget.setData()
     self.plotsItems[1].plotWidget.setData()
     self.plotsItems[2].plotWidget.setData()
     self.plotsItems[3].plotWidget.setData()
     self.maxFreqSamplerLcd.display(0)
     self.freqSamplerFactorLcd.display(0)
     main.ResettingNoise(self)          
