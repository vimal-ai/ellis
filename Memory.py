import numpy as np

class Memory():

  def __init__(self,capacity=10):
    self.store = np.empty(capacity, dtype='<U16')
    self.capacity = capacity
    self.size = 0

  def push(self,a):
    if(self.size < 10):
      for i in range(0, self.size):
        self.store[self.capacity - self.size - 1 + i] = self.store[self.capacity - self.size + i]
      self.store[self.capacity-1] = a
      self.size +=1
    else:
      for i in range(0, self.size):
        if i > 0:
          self.store[i-1] = self.store[i]
      self.store[self.capacity-1] = a
      self.size = 10