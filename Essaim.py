import random
import matplotlib.pyplot as plt


#fonction a maximiser
def f(x):
	return -x**2

class Boid:
	
	def __init__(self,xmin, xmax):
		self.x=random.uniform(xmin, xmax)
		self.v=random.gauss(0,1)
		self.p=self.x
		
	def maj(self, w, phip, phig,g, rp, rg):
		self.v=self.v*w + phip*rp*(self.p-self.x) + phig*rg*(g-self.x)
		self.x+=self.v
		self.calcul_p()
		
		
	def calcul_p(self):
		if (f(self.x)>f(self.p)):
			self.p=self.x

class Essaim:
	def __init__(self, N, xmin, xmax, w, phip, phig):
		self.boids=[]
		self.w=w
		self.phip=phip
		self.phig=phig
		for i in xrange(0,N):
			self.boids.append(Boid(xmin, xmax))
		self.g = self.calcul_g()

	def calcul_g(self):
		liste_p = [ self.boids[i].p for i in xrange(0, len(self.boids)) ]
		liste_ep = map(f,liste_p)
		indice_max = liste_ep.index(max(liste_ep))
		return liste_p[indice_max]
		
		
	def maximisation(self, t):
		liste_g = []
		liste_eg = []
		for i in xrange(0, t):
			
			liste_g.append(self.g)
			liste_eg.append(f(self.g))
			print "g : ",self.g, "    eg : ", f(self.g)
			rp=random.uniform(0,1)
			rg=random.uniform(0,1)
			
			for boid in self.boids:
				boid.maj(self.w, self.phip, self.phig, self.g, rp, rg)
				
			self.g = self.calcul_g()
			
		plt.plot(range(0,t), liste_eg, color='b', label = 'qualite')
		plt.plot(range(0,t), liste_g, color='r', label = 'position')
		axes = plt.gca()
		axes.set_xlabel('iterations')
		axes.set_ylabel('qualite ou position')
		plt.legend(loc='upper right', prop={'size':10})
		plt.show()
			

essaim = Essaim(10,-100,100,0.1,0.3,0.5)
essaim.maximisation(20)

#on retrouve bien le max de -x**2 qui vaut 0 en 0
