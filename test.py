import librosa
import math
import numpy as np
from sklearn.cluster import KMeans
import hmmlearn.hmm
import pickle
import os

# def get_mfcc(file_path):
#     y, sr = librosa.load(file_path) # read .wav file
#     hop_length = math.floor(sr*0.010) # 10ms hop
#     win_length = math.floor(sr*0.025) # 25ms frame
#     # mfcc is 12 x T matrix
#     mfcc = librosa.feature.mfcc(
#         y, sr, n_mfcc=12, n_fft=1024,
#         hop_length=hop_length, win_length=win_length)
#     # substract mean from mfcc --> normalize mfcc
#     mfcc = mfcc - np.mean(mfcc, axis=1).reshape((-1,1)) 
#     # delta feature 1st order and 2nd order
#     delta1 = librosa.feature.delta(mfcc, order=1)
#     delta2 = librosa.feature.delta(mfcc, order=2)
#     # X is 36 x T
#     X = np.concatenate([mfcc, delta1, delta2], axis=0) # O^r
#     # return T x 36 (transpose of X)
#     return X.T # hmmlearn use T x N matrix

def get_mfcc(file_path):
    y, sr = librosa.load(file_path) # read .wav file
    hop_length = math.floor(sr*0.010) # 10ms hop
    win_length = math.floor(sr*0.025) # 25ms frame
    # mfcc is 12 x T matrix
    mfcc = librosa.feature.mfcc(
        y, sr, n_mfcc=12, n_fft=1024,
        hop_length=hop_length, win_length=win_length)
    #energy
    rms = librosa.feature.rms(y=y, frame_length=win_length, hop_length=hop_length)
    
    mfcc = np.concatenate([mfcc, rms])
    # substract mean from mfcc --> normalize mfcc
    mfcc = mfcc - np.mean(mfcc, axis=1).reshape((-1,1)) 
    # delta feature 1st order and 2nd order
    delta1 = librosa.feature.delta(mfcc, order=1)
    delta2 = librosa.feature.delta(mfcc, order=2)
    # X is 36 x T
    X = np.concatenate([mfcc, delta1, delta2], axis=0) # O^r
    # return T x 36 (transpose of X)
    return X.T # hmmlearn use T x N matrix

def load_model(path):
    try:
        model_pkl = open(path, "rb")
        models = pickle.load(model_pkl)
    except:
        raise FileNotFoundError("You don't have any models at this path: ", path)
    return models

def test_score(file_path, model):
    new_mfcc = get_mfcc(file_path)
    # new_mfcc_clustered = kmeans.predict(new_mfcc).reshape(-1,1)
    return model.score(new_mfcc, [len(new_mfcc)])

def best_score(file_path):
    # get_mfcc = load_model(os.path.join("models","kmeans.pkl"))
    models = load_model(os.path.join("models","models.pkl"))
    scores = []
    for cname, model in models.items():
        # print(cname)
        if cname != 'khanh_linh':
            score = test_score(file_path, model)
            print(cname, score)
            scores.append((cname, score))
    
    b_score = scores[0]
    for score in scores:
        if (score[1] > b_score[1]):
            b_score = score
    
    return b_score
    
if __name__ == "__main__":
    # score = test_score('data/gia-dinh-test/29.wav', kmeans, models['gia-dinh'])
    b_score = best_score('long-voice/y-te/Audio Track-3.wav')
    print(b_score)