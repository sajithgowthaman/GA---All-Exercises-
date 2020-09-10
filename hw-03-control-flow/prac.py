

# x = 5
# y = 10
# z = 15

# if  x > y: #NO
#     print('x is greater')
# elif y > 15:
#     print ('y is greater')   #NO again 
# else:
#     print('both are false')

# if  x > y: #NO
#     print('x is greater')
# elif y > 5: #YES -> It prints
#     print ('y is greater') 
# else:
#     print('both are false') 

def add_bonus_points(score):
  if score > 50:
    return score + 10

  score += 20
  return score

total_points = add_bonus_points(45)
print(total_points)