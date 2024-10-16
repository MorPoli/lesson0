immutable_var = (2, 4, 10 , 'lol', False)
print('Immutable tuple: ', immutable_var)

#immutable_var[3] = 'oreo'  ## I cann't do this, because tuple is immutable

mutable_list = ['rockDog', 34, 25]
print('Mutable tuple: ', mutable_list)
mutable_list[2] = True
print('New Mutable tuple: ', mutable_list)