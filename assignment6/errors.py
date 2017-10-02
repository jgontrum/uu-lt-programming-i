import traceback

try:
  print("1)")
  1/0
except:
  traceback.print_exc()

try:
  print("\n2)")
  1/""
except:
  traceback.print_exc()

try:
  print("\n3)")
  ""[0]
except:
  traceback.print_exc()

try:
  print("\n4)")
  [][0]
except:
  traceback.print_exc()

try:
  print("\n5)")
  print("code(syntax error): >>> return")
  #return
except:
  traceback.print_exc()

try:
  print("\n6)")
  python
except:
  traceback.print_exc()

try:
  print("\n7)")
  for i in 0:
    pass
except:
  traceback.print_exc()

try:
  print("\n8)")
  import gnu
except:
  traceback.print_exc()

try:
  print("\n9)")
  len(0)
except:
  traceback.print_exc()

try:
  print("\n10)")
  abs("")
except:
  traceback.print_exc()

try:
  print("\n11)")
  {[]: 1}
except:
  traceback.print_exc()

try:
  print("\n12)")
  range(0.1)
except:
  traceback.print_exc()
