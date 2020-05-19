#Defining a function to run various physics equations
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#converts f to c
def f_to_c(f_temp):
  c_temp = (f_temp-32) * 5/9
  return c_temp

#test run
f100_in_celcius = f_to_c(100)

#converts c to f
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#test run
c0_in_fahrenheit = c_to_f(0)

#determines force
def get_force(mass, acceleration):
  return mass*acceleration

#test run
train_force = get_force(train_mass, train_acceleration)

#test printing the values
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#determines energy
def get_energy(mass, c=3*10**8):
  get_energy = (mass*c)**2
  return get_energy

#test run 
bomb_energy = get_energy(bomb_mass,3*10**8)

#print test
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#determines work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return (force) * distance

#test run
train_work= get_work(train_mass, train_acceleration, train_distance)

#print test
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")