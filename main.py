def mult(a,b):
  return a*b
  
print(mult(4,5))




print(mult(a=6,b=5))




def varargs(*args):
  return args

print(varargs(1,5,10))
print(varargs(1))
print(varargs(1,5,10,15,20))
print(varargs(1,5,1032,324,5464))




def complex(x1,x2,*args,**kwargs):
  print(x1)
  print(x2)
  print(args[0])
  print(kwargs["first"])
  print(kwards["second"])

complex(1,2,3,first=4,second=5)