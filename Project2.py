train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def get_force(train_mass, train_acceleration):
  return train_mass * train_acceleration


def f_to_c(f_temp):
  c_temp = (f_temp - 32 ) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

def get_energy(bomb_mass, c=3*10**8):
  return bomb_mass*(c*c)

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force*distance

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass)
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GR train supplies",train_force,"Newtons of force")
print("A 1kg bomb supplies",bomb_energy,"Joules")
print("The GE train does ",train_work,"Joules of work over",train_distance,"meters")
