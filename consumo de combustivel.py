def liters_100km_to_miles_gallon(liters):
    NewM=(100/1.609344)/(liters/3.785411784)
    return NewM

 
 

def miles_gallon_to_liters_100km(miles):
    Km=(3.785411784)/((miles*1.609344)/100)
    return Km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))