#! /usr/bin/env python
# -*- coding:utf-8 -*-

from random import randint

class Individu:
  """docstring for Individu"""
  def __init__(self, ge_le):
    
    self.genome = [randint(0,1) for _ in range(ge_le)]
    
  def mutation_ponct(self, pos):
    self.genome[pos] = 0 if self.genome[pos] == 1 else 1

  def mutation_invers(self, posi, posj):
    """Switches posi with posj, posi+1 with poj-1, etc."""

    posi, posj = (posi,posj) if posi <= posj else (posj,posi) 

    while True :
      tmp = self.genome[posi]
      self.genome[posi] = self.genome[posj]
      self.genome[posj] = tmp

      if posj-posi <= 1 :
        break
      posi += 1
      posj -= 1

  def mutation_transloc(self, posi, posj, posk):
    """Moves the segment from posi-posj to posk-posk+1"""
    segment = self.genome[posi : posj+1]

    #Make sure that posk is not in segment and take into
    #account both possible cases (posk before or after segment)
    if posk > posj:
      p = posk - (posj - posi)
    elif posk < posi:
      p = posk
    else :
      return

    del self.genome[posi : posj+1]
    self.genome[p:p] = segment
 
if __name__ == '__main__':
  test = Individu(20)
  print "INIT"
  print test.genome
  test.mutation_ponct(2)
  print "PONCT (2)"
  print test.genome
  test.mutation_invers(0,19)
  print "INVERS 0,19"
  print test.genome
  test.mutation_transloc(1,4,19)
  print "TRANSLOC (1-4, 19)"
  print test.genome