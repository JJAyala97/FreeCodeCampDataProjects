import numpy as np

def calculate(list):
#Checking that list has exactly 9 numbers
  try:
      if len(list) != 9:
        raise ValueError ('List must contain nine numbers.')
      else:
        newlist = np.array(list).reshape(3,3)
        stats = { 'mean': [np.mean(newlist, axis=0).tolist(), np.mean(newlist, axis=1).tolist(), np.mean(newlist)],
                  'variance': [np.var(newlist, axis=0).tolist(), np.var(newlist, axis=1).tolist(), np.var(newlist)],
                  'standard deviation': [np.std(newlist, axis=0).tolist(), np.std(newlist, axis=1).tolist(), np.std(newlist)],
                  'max': [np.max(newlist, axis=0).tolist(), np.max(newlist, axis=1).tolist(), np.max(newlist)],
                  'min': [np.min(newlist, axis=0).tolist(), np.min(newlist, axis=1).tolist(), np.min(newlist)],
                  'sum': [np.sum(newlist, axis=0).tolist(), np.sum(newlist, axis=1).tolist(), np.sum(newlist)]
                  }
        for key, value in stats.items():
          print(key, ':', value)
  except TypeError:
      print("Something went wrong. Please input 9 numbers")



calculate([1.2,1,2,3,4,5,6,7,9])


