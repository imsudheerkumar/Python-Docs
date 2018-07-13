def if_demo(s):
  if s == 'Hello' or s == 'Hi':
    s = s + ' nice to meet you'
    print(s)
  else:
    s = s + ' woo hoo!'
    print(s)
  return s

s="Hello"
if_demo(s)
