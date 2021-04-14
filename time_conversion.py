
def timeConversion(s):
  am_pm = s[-2:]
  hh = s[0:2]
  
  if am_pm == 'AM':
    if hh == '12':
      return '00' + s[2:-2]
    else:
      return s[0:-2]
  elif am_pm == 'PM':
    if hh == '12':
      return s[0:-2]
    else:
      return str(int(hh) + 12) + s[2:-2]

# s = '07:05:45PM'
# s = '12:45:54PM'
s = input()

print(timeConversion(s))




