def update_car_info(**kwargs):

  car = kwargs  
  car['is_available'] = True
  return car


car_data = update_car_info(brand="Toyota", price=25000)
print(car_data)
