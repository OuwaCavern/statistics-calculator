import numpy as np

def calculate(list):
  arr = np.array(list)
  if not arr.size == 9:
    raise ValueError("List must contain nine numbers.")
  mmatrix = arr.reshape((3,3))
  mean0 = np.mean(mmatrix, axis=0).tolist()
  mean1 = np.mean(mmatrix, axis=1).tolist()
  meanf = np.mean(mmatrix).tolist()
  var0 = np.var(mmatrix, axis=0).tolist()
  var1 = np.var(mmatrix, axis=1).tolist()
  varf = np.var(mmatrix).tolist()
  std0 = np.std(mmatrix, axis=0).tolist()
  std1 = np.std(mmatrix, axis=1).tolist()
  stdf = np.std(mmatrix).tolist()
  min0 = np.min(mmatrix, axis=0).tolist()
  min1 = np.min(mmatrix, axis=1).tolist()
  minf = np.min(mmatrix).tolist()
  max0 = np.max(mmatrix, axis=0).tolist()
  max1 = np.max(mmatrix, axis=1).tolist()
  maxf = np.max(mmatrix).tolist()
  sum0 = np.sum(mmatrix, axis=0).tolist()
  sum1 = np.sum(mmatrix, axis=1).tolist()
  sumf = np.sum(mmatrix).tolist()
  calculations = {
    'mean': [mean0, mean1, meanf],
    'variance': [var0, var1, varf],
    'standard deviation': [std0, std1, stdf],
    'max': [max0, max1, maxf],
    'min': [min0, min1, minf],
    'sum': [sum0, sum1, sumf]
  }
  return calculations