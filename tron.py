# -*- coding: utf-8 -*-
"""voice_processing_final_assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Ce7x-JA4IJYaVOVdd6LAti9Wo7j35Pp
"""

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

import os
import re
import numpy as np
import math
path = '/content/gdrive/My Drive/voice_processing_final_assignment'
print(path)
!google-drive-ocamlfuse -cc

import sys
sys.path.append(path)

!pip install eyed3
!pip install pydub

from silence import remove_silence
import scipy.io.wavfile as wavfile



!pip install noisereduce

import matplotlib.pyplot as plt
import noisereduce as nr

from pydub import AudioSegment

def to_mono(file_path):
  res_path = os.path.join(path, 'temp.wav')
  sound = AudioSegment.from_wav(file_path)
  sound = sound.set_channels(1)
  sound.export(res_path, format="wav")
  return res_path

def getSpeakers(dirpath):
  filenames= os.listdir (dirpath) # get all files' and folders' names in the current directory

  result = []
  for filename in filenames: # loop through all the files and folders
    filepath = os.path.join(dirpath, filename)
    if os.path.isdir(filepath) and filename not in result: # check whether the current object is a folder or not
      result.append(filename)
  return result

from numpy import *
import numpy.linalg as linalg
from utils import cached_func, diff_feature

POWER_SPECTRUM_FLOOR = 1e-100

def hamming(n):
    """ Generate a hamming window of n points as a numpy array.  """
    return 0.54 - 0.46 * cos(2 * pi / n * (arange(n) + 0.5))

class MFCCExtractor(object):

    def __init__(self, fs, win_length_ms, win_shift_ms, FFT_SIZE, n_bands, n_coefs,
                 PRE_EMPH, verbose = False):
        self.PRE_EMPH = PRE_EMPH
        self.fs = fs
        self.n_bands = n_bands
        self.coefs = n_coefs
        self.FFT_SIZE = FFT_SIZE

        self.FRAME_LEN = int(float(win_length_ms) / 1000 * fs)
        self.FRAME_SHIFT = int(float(win_shift_ms) / 1000 * fs)

        self.window = hamming(self.FRAME_LEN)


        self.M, self.CF = self._mel_filterbank()

        dctmtx = MFCCExtractor.dctmtx(self.n_bands)
        self.D = dctmtx[1: self.coefs + 1]
        self.invD = linalg.inv(dctmtx)[:, 1: self.coefs + 1]

        self.verbose = verbose
        # The inverse DCT matrix. Change the index to [0:COEFS] if you want to keep the 0-th coefficient


    def dprint(self, msg):
        """ Debug print """
        if self.verbose:
            print(msg)

    def extract(self, signal):
        """
        Extract MFCC coefficients of the sound x in numpy array format.
        """
        if signal.ndim > 1:
            self.dprint("INFO: Input signal has more than 1 channel; the channels will be averaged.")
            signal = mean(signal, axis=1)
        assert len(signal) > 5 * self.FRAME_LEN, "Signal too short!"
        frames = (len(signal) - self.FRAME_LEN) / self.FRAME_SHIFT + 1
        feature = []
        for f in range(int(frames)):
            # Windowing
            frame = signal[f * self.FRAME_SHIFT : f * self.FRAME_SHIFT +
                           self.FRAME_LEN] * self.window
            # Pre-emphasis
            frame[1:] -= frame[:-1] * self.PRE_EMPH
            # Power spectrum
            X = abs(fft.fft(frame, self.FFT_SIZE)[:self.FFT_SIZE // 2 + 1]) ** 2
            X[X < POWER_SPECTRUM_FLOOR] = POWER_SPECTRUM_FLOOR  # Avoid zero
            # Mel filtering, logarithm, DCT
            X = dot(self.D, log(dot(self.M, X)))
            feature.append(X)
        feature = row_stack(feature)
        # Show the MFCC spectrum before normalization
        # Mean & variance normalization
        if feature.shape[0] > 1:
            mu = mean(feature, axis=0)
            sigma = std(feature, axis=0)
            feature = (feature - mu) / sigma

        return feature

    def _mel_filterbank(self):
        """
        Return a Mel filterbank matrix as a numpy array.
        Ref. http://www.ifp.illinois.edu/~minhdo/teaching/speaker_recognition/code/melfb.m
        """
        f0 = 700.0 / self.fs
        fn2 = int(floor(self.FFT_SIZE / 2))
        lr = log(1 + 0.5 / f0) / (self.n_bands + 1)
        CF = self.fs * f0 * (exp(arange(1, self.n_bands + 1) * lr) - 1)
        bl = self.FFT_SIZE * f0 * (exp(array([0, 1, self.n_bands, self.n_bands + 1]) * lr) - 1)
        b1 = int(floor(bl[0])) + 1
        b2 = int(ceil(bl[1]))
        b3 = int(floor(bl[2]))
        b4 = min(fn2, int(ceil(bl[3]))) - 1
        pf = log(1 + arange(b1, b4 + 1) / f0 / self.FFT_SIZE) / lr
        fp = floor(pf)
        pm = pf - fp
        M = zeros((self.n_bands, 1 + fn2))
        for c in range(b2 - 1, b4):
            r = int(fp[c] - 1)
            M[r, c+1] += 2 * (1 - pm[c])
        for c in range(b3):
            r = int(fp[c])
            M[r, c+1] += 2 * pm[c]
        return M, CF

    @staticmethod
    def dctmtx(n):
        """ Return the DCT-II matrix of order n as a numpy array.  """
        x, y = meshgrid(range(n), range(n))
        D = sqrt(2.0 / n) * cos(pi * (2 * x + 1) * y / (2 * n))
        D[0] /= sqrt(2)
        return D

@cached_func
def get_mfcc_extractor(fs, win_length_ms=32, win_shift_ms=16,
                       FFT_SIZE=2048, n_filters=50, n_ceps=13,
                       pre_emphasis_coef=0.95):
    ret = MFCCExtractor(fs, win_length_ms, win_shift_ms, FFT_SIZE, n_filters,
                       n_ceps, pre_emphasis_coef)
    return ret

def extract(fs, signal=None, diff=False, **kwargs):
    """accept two argument, or one as a tuple"""
    if signal is None:
        assert type(fs) == tuple
        fs, signal = fs[0], fs[1]
    signal = cast['float'](signal)
    ret = get_mfcc_extractor(fs, **kwargs).extract(signal)
    if diff:
        return diff_feature(ret)
    return ret

import librosa

def get_mfcc(file_path, noise):
  fs, y = wavfile.read(to_mono(file_path)) # read .wav file

  y = remove_silence(fs, y)

  if not np.issubdtype(y.dtype, np.floating):
    y = [np.float32(i) for i in y]
    y = np.array(y)
  if len(noise) > 0:
    if not np.issubdtype(noise.dtype, np.floating):
      noise = [np.float32(i) for i in noise]
      noise = np.array(noise)
    y = nr.reduce_noise(audio_clip=np.array(y), noise_clip=np.array(noise), verbose=False)
 
  mfcc = extract(fs, y)
 
  return mfcc

from sklearn import mixture

datapath = os.path.join(path, 'data')
speakers = getSpeakers(datapath)

n_mixtures = 32
max_iterations = 1000
models = {}
for speaker in speakers:
  speakerPath = os.path.join(datapath, speaker)
  all_data = []
  print('loading data for speaker', speaker)
  train_path = os.path.join(speakerPath, 'train')
  for wavefile in os.listdir(train_path):
    mfcc = get_mfcc(os.path.join(train_path, wavefile), [])
    if len(all_data) == 0:
      all_data = mfcc
    else:
      all_data = np.concatenate((all_data, mfcc), axis=0)
    
  print('DONE!')
  print('training data for speaker', speaker)
  gmm = mixture.GaussianMixture(n_components=n_mixtures, covariance_type="diag", max_iter=max_iterations, verbose=True).fit(all_data)
  models[speaker] = gmm
  print('DONE!')

drive.mount('/content/gdrive', force_remount=True)

total_speaker = len(speakers)
print('Testing')
accuracy = {}
for test_speaker in speakers:
  speaker_path = os.path.join(datapath, test_speaker)
  noise = []
  print(test_speaker)
  try:
    noise_path = os.path.join(speaker_path, 'test_noise.wav')
    
    [fs, y] = wavfile.read(to_mono(noise_path))
    noise = y
  except:
    print('Load test noise error')

  point = 0
  try:
    for testfile in os.listdir(os.path.join(speaker_path, 'test')):
        mfcc = get_mfcc(os.path.join(speaker_path, 'test', testfile), noise)
        score = {speaker: model.score(mfcc) for speaker, model in models.items()}
        print(test_speaker, max(score, key=score.get), score)
        if test_speaker == max(score, key=score.get):
          point += 1
    accuracy[test_speaker] = point / 10
  except: 
    print("Test error")
print(accuracy)

import pickle as pkl

print("Saving models")
model_path = os.path.join(path, 'models')
with open(os.path.join(model_path, 'models.pkl'), 'wb') as file:
    pkl.dump(models, file)