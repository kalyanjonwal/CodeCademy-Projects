def cost_of_ground(weight):
  if weight <= 2:
    return weight * 1.50 + 20.00
  elif weight > 2 and weight <= 6:
    return weight * 3.00 + 20.00
  elif weight > 6 and weight <= 10:
    return weight * 4.00 + 20.00
  else:
    return weight * 4.755 + 20.00

def cost_of_drone(weight):
  if weight <= 2 :
    return weight * 4.50
  if weight > 2 and weight <= 6:
    return weight * 9.00
  if weight > 6 and weight <=10:
    return weight * 12.00
  else:
    return weight * 14.25

def which_one_is_better(weight):
  ground_shipping = cost_of_ground(weight)
  premium_ground_shipping = 125.00
  drone_shipping = cost_of_drone(weight)
  if ground_shipping < premium_ground_shipping and ground_shipping < drone_shipping :
    print("ground shipping is cheapeast this cost",ground_shipping,"for",weight)
  elif premium_ground_shipping < ground_shipping and premium_ground_shipping < drone_shipping:
    print("premium ground shipping is cheapeast this cost",premium_ground_shipping,"for",weight)
  else:
    print("drone shipping is cheapeast this cost",drone_shipping,"for",weight)


which_one_is_better(41.5)
cost_of_drone_shipping = print(cost_of_drone(41.))
cost_of_premium_ground_shipping = 125.00
cost_of_groun_shipping = print(cost_of_ground(41.5))
