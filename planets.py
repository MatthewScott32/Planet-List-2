planet_list = ['Mercury', 'Mars']
planet_list_2 = ['Uranus', 'Neptune']
planet_list.append('Jupiter')
planet_list.append('Saturn')
planet_list.extend(planet_list_2)
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
planet_list.append('Pluto')
rocky_planets = slice(0, 4)
print(planet_list[rocky_planets])
del planet_list[8]