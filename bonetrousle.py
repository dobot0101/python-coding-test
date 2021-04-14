# s, t = 7, 11
# a, b = 5, 15
# m, n = 3, 2
# apples = [-2, 2, 1]
# oranges = [5, -6]

s,t = 2, 3
a,b = 1, 5
m,n = 1, 1
apples = [2]
oranges = [-2]

def countApplesAndOranges(s, t, a, b, apples, oranges):
  apple_locations = list(map(lambda x: x + a, apples))
  orange_locations = list(map(lambda x: x + b, oranges))
  print(len([i for i in apple_locations if i >= s and i <= t]))
  print(len([i for i in orange_locations if i >= s and i <= t]))

countApplesAndOranges(s,t,a,b,apples,oranges)