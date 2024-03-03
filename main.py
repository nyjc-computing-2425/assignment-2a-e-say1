num = input('Enter a number (decimal or integer): ')
# type your code here
temp_num = num.strip()
temp_num = temp_num.replace(".", "")
temp_num = temp_num.lstrip("0")
sf = len(temp_num)




# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')

