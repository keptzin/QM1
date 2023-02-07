import matplotlib as plt
import math
import decimal

#constants
e = 1.6 * 10**-19
pi = 3.141592654
ez = 8.854187817 * 10**-12
r0 = 1.2 #fm
x = 9 * 10**9
h = 6.626 * 10**-34 #(m^2)kg/s [plank's constant]
#h = 4.135 * (10**-15) #eVs

#COMBINED
def POT(I,E1,E2,Z1,Z2,MA,MB): 
#I is whether input is an isotop or not 
#E1 is element one name
#E2 is element two name
#charge 1
#charge 2
#mass 1
#mass 2
#E = total kinetic energy in MeV of particle
  L = 100
  RA = r0 * (MA ** (1/3)) #returns fm
  RB = r0 * (MB ** (1/3)) #fm
  d = RA + RB
  J = (Z1*Z2*(e**2))/(4*pi*ez*(d*(10**-15)))
  MeV = J * (6.242 * (10**12)) #height of barrier (MeV)

  if MeV > 150:
    MeV = MeV * (10**6)
    E = MeV
    frac, intNum = math.modf(E)
    E = str(frac)
    E = float(E[0:8]) + 0.0000001
    E = int(MeV) + E

  elif MeV > 40:
    MeV = MeV * (10**6)
    E = MeV
    frac, intNum = math.modf(E)
    E = str(frac)
    E = float(E[0:9])
    E = int(MeV) + E
  else:
    MeV = MeV * (10**6)
    E = MeV
    frac, intNum = math.modf(E)
    E = str(frac)
    E = float(E[0:8])
    E = int(MeV) + E

  m = MA * (1.6605402 * (10**-27)) #turn into kg
  L = L * (10**-12)
  A = (-4*L*pi)/h
  B = (MeV-E)*(1.6*(10**-19)) #convert into J
  C = math.sqrt(2*m*(B))
  P = math.exp(A*C)
  P = P * 100
  E = E * (10**-6)
#  E1 = "hydrogen"
#  E2 = "hydrogen"
  I = I
  if P > 0.005:
    a = P
  else:
    a = ("{:e}".format(P))

  return ('''Element 1: ''' + E1 + '''
Element 2: ''' + E2 + '''
isotope: ''' + I + '''
total kinetic energy used: ''' + str(E) + " MeV"
'''
probability of tunneling: ''' + str(a) + "%")


#testing! Please put parenthesis around I, E1, and E2 
# maybe will develop interactive inputs/sliders to make this less tedius
test1 = POT("no","hydrogen","hydrogen",1,1,1.00784,1.00784)
test2 = POT("no","hydrogen","helium",1,2,1.00784,4.002602)
test3 = POT("no","lead","boron",5,82,10.811,207.2)
test4 = POT("no","plutonium","plutonium",94,94,244,244)

test5 = POT("no","helium","hydrogen",2,1,4.002602,1.00784)
print(test1)
print("")
print(test2)
print("")
print(test3)
print("")
print(test4)
print("")
print(test5)



