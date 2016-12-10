#! /usr/bin/env python
# -*- coding:utf-8 -*-

from random import gauss, randint
from numpy.random import uniform
from copy import copy


class Individu:
  """docstring for Individu"""
  def __init__(self, x):
  
    self.x = x
    self.f = self.fct_F()

  def fct_F(self):
    return -(self.x**2)

  def fct_M(self):
    return Individu(self.x + gauss(0,1))

class Population:
  """Array of given size with Individu objects with x
    initialized with Uniform(-i,i)"""

  def __init__(self, i, size):
    
    tab = uniform (low = -i, high=i, size=size)
    self.pop = []

    for x in tab:
      self.pop.append(Individu(x))

    self.bf = self.pop[0]
    self.find_best_fitness()

  def __repr__(self):
    s="Population :"
    for ind in self.pop:
      s+="\nfitness :\t"+str(ind.f)
    s += "\n BEST FITNESS :\t"+str(self.bf.f)

    return s

  def find_best_fitness(self):
    for indi in self.pop:
      self.bf = fct_S(self.bf,indi)

  def update(self):
    for i, ind in enumerate(self.pop):
      self.pop[i] = fct_S(ind,ind.fct_M())
    
    self.find_best_fitness()

    
def fct_S(A,B):
  if A.f > B.f :
    return A
  elif A.f < B.f:
    return B
  else:
    return (A,B)[randint(0,1)]




if __name__ == '__main__':
  # test = Individu(-30)
  # test2 = Individu(20)

  test_pop = Population(100,10)
  # print test.x,test.f
  # print test2.x,test2.f
  
  # for i in range(10):
  #   test = fct_S(test,test.fct_M())
  #   print test.f


  #print test_pop
  print "\nPress Enter to execute update\n"
  print "Xb :\t",test_pop.bf.x,", fXb : \t",test_pop.bf.f
  while True :
    test_pop.update()
    print "Xb :\t",test_pop.bf.x,", fXb : \t",test_pop.bf.f
    raw_input()


###REPONSE AUX QUESTIONS
"""
Note : la réponse à la 1ère question est valable pour la manière 
dont j'ai abordé le pb, vous aurez sûrement la vôtre différente.

1) J'ai créé une classe individu pour pouvoir attribuer les fonctions 
  fct_M() et fct_F() à l'objet. Une classe population a permis de 
  stocker l'individu avec la meilleure fitness aisément. Enfin, la fonction
  fct_S() n'avait pas besoin d'appartenir à une des 2 classes en particulier.

2) La flemme de faire un fichier... regardez le terminal ;)


3) Pour tracer la fitness du meilleur individu en fonction des itérations, 
faites un truc comme ca (oubliez pas d' import matplolib.pyplot as plt):
  
  x = []
  y = []
  for i in range (nb_iteration):
    x.append(i)
    pop.update()
    y.append(pop.bf.f)

  plt.plot(x,y)
  plt.show()



"""