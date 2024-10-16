# Imports
import numpy as np
# from scipy import fft
from scipy import fft
from math import ceil


# GLobals
MAX_NUM_SAMPLES = 1500 # Statement requirement

import view
# Classes
class Signal():
    def __init__(self,time=[],amplitude=[],maxFrequency=0, path="null"):
        self.time = time
        self.amplitude = amplitude
        self.path = path
        self.maxFrequency = maxFrequency
        self.amplitudeWithNoise = 0
        self.snrdB = 0

    
    def getMaxFrequency(self):
        return self.maxFrequency
    
    def setMaxFrequency (self):
        numSamples = len(self.time)
        sampling_period =self.time[1] - self.time[0]  
        fft_result = (fft.fft(self.amplitude))
        frequencies = fft.fftfreq(numSamples, sampling_period)
        unified_frequencies = []
        for i in range(len(frequencies)):
            if fft_result[i]>0.001:
                unified_frequencies.append(frequencies[i])
        self.maxFrequency = ceil(max(unified_frequencies))


    def addWhiteNoise(self, signal, noiseLevel):
        #Note: random.normal(normal distribution, standard deviation, how many random values will be generated)
        max_amplitude = max(signal.amplitude)
        noiseStdDev = noiseLevel * 0.005 * max_amplitude
        noise = np.random.normal(0, noiseStdDev, len(signal.amplitude))        
        signal.amplitudeWithNoise = signal.amplitude + noise
        self.isAddedNoise = True
        view.signalPlotting(self, None ,False)
        Signal.calculateSNR(self, signal)
        view.samplingPlotting(self,self.FreqSamplerSlider.value())
        
    def calculateSNR(self,signal):
        
        signal_power = np.var(signal.amplitude)
        
        noise = signal.amplitudeWithNoise - signal.amplitude 
        noise_power = np.var(noise)
        if(noise_power == 0):
            snrdB = 0
            self.snrLcd.display(snrdB)
        else:    
            snrdB = 10 * np.log10(signal_power / noise_power)
            self.snrLcd.display(snrdB)
   

class Plotting():
    def __init__(self,plotWidget,xmin=0,xmax=1,ymin=0,ymax=1):
        self.plotWidget = plotWidget
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
    

    def setLimits(self):
        self.plotWidget.setXRange(xMin= self.xmin , xMax = self.xmax , yMin = self.ymin , yMax = self.ymax)






      
        