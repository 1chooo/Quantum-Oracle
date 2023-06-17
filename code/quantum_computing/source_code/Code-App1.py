# %% [markdown]
# # 附錄1原始程式碼

# %%
#Below are examples of using print function
print('The name of the language is',"Python")
print("The radius of the circle is", 3, '\nIts area is', 3.14159*3**2)

# %%
#Below are examples of using print function
print('The name of the language is',"Python",end=". ")
print('Its version is',"3.x",sep="....")
print("The radius of the circle is", 3)
print("The area of the circle is", 3.14159*3**2)

# %%
r=input('Please enter the radius of the circle:')
print('The radius of the circle:', r) 

# %%
r=input('Please enter the radius of the circle:')
ri=int(r)
rf=float(r)
print('The radius of the circle:', ri) 
print("The area of the circle:", 3.14159*rf**2)

# %%
a=123;b=123.456;c=False;d=123+456j;e="123";f=[1,2,3];g=(1,2,3);h={1,2,3};i={1:'x',2:'y',3:'z'}
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h),type(i))

# %%
a=3;b=8
print(a+b)  #11
print(a-b)  #-5
print(a*b)  #24
print(a/b)  #0.375
print(a//b) #0
print(a%b)  #3
print(a**b) #6561
print(a+b//a**b)    #3
print((a+b)//a**b)  #0


# %%
a=3.0;b=8.0;c=8
print(a+b)  #11.0
print(a-b)  #-5.0
print(a*b)  #24.0
print(a/b)  #0.375
print(a//b) #0.0
print(a%b)  #3.0
print(a**b) #6561.0
print(a+c)  #11.0
print(a+b//a**b)    #3.0
print((a+b)//a**b)  #0.0

# %%
a=3.0;b=8.0;c=8
print(a==b)  #False
print(a!=b)  #True
print(a>b)   #False
print(a<b)   #True
print(a>=b)  #False
print(a<=b)  #True
print(not (a==b)) #True
print(a==b or a!=b and a>b)       #False
print(a==b and a>b or a!=b)       #True
print(a==b and a>b or not (a!=b)) #False

# %%
a=2+4j;b=3-8j
print(a+b)  #(5-4j)
print(a-b)  #(-1+12j)
print(a*b)  #(38-4j)
print(a/b)  #(-0.3561643835616438+0.3835616438356164j)
print(a+b/a)    #(0.7+2.6j)
print((a+b)/a)  #(-0.3-1.4j)
print(a.real)   #2.0
print(a.imag)   #4.0
print(a.conjugate()) #(2-4j)
print(abs(a))   #4.47213595499958

# %%
a={1,2,3};b={2,4,6}
print(a|b)         #{1, 2, 3, 4, 6}
print(a.union(b))  #{1, 2, 3, 4, 6}
print(a&b)               #{2}
print(a.intersection(b)) #{2}
print(a-b)               #{1,3}
print(a.difference(b))   #{1,3}
print(a^b)                        #{1,3,4,6}
print(a.symmetric_difference(b))  #{1,3,4,6}

# %%
ex = {"a":1, "b":2, "c":3, 1: "integer", 2.3: "float", 4+5j: "complex", (6,7): "tuple"}
print(ex["a"],ex["b"],ex["c"],ex[1],ex[2.3],ex[4+5j],ex[(6,7)])
ex["a"]=100
print(ex["a"])
print(len(ex))
ex["d"]=4
print(ex.get("d"))
del ex["d"]
print(ex.get("d"))
print("e" in ex)
print("e" not in ex)
print(ex.keys())
print(ex.values())

# %%
a=5
a+=3  #a=a+3  (a=8)
a-=3  #a=a-3  (a=5)
a*=3  #a=a*3  (a=15)
a%=8  #a=a%8  (a=7)
a//=3 #a=a//3 (a=2)
a/=3  #a=a/3  (a=0.6666666666666666)
a**=3 #a=a**3 (a=0.2962962962962962)
print(a)

# %%
score=90
if score >=60:
  print("PASS")

# %%
score=90
if score >=60:
  print("PASS")
else:
  print("FAIL")

# %%
score=90
if score >=90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")
else:
  print("F")

# %%
i=0
while i<5:
  i+=1  
  print(i,end="") 

# %%
i=0
while i<5:
  i+=1  
  print(i,end="")
else:
  print("#")

# %%
for i in [1,2,3,4,5]:
  print(i,end="")

# %%
for i in [1,2,3,4,5]:
  print(i,end="")
else:
  print("#")

# %%
print(list(range(5)))       #range(5)會回傳0、1、2、3、4
print(list(range(2,5)))     #range(2,5)會回傳2、3、4
print(list(range(0,5,2)))   #range(0,2,5)會回傳0、2、4
print(list(range(5,0,-1)))  #range(5,0,-1)會回傳5、4、3、2、1
print(list(range(5,0)))     #range(5,0)是一個空序列

# %%
i=0
while i<5:
  i+=1  
  if i==3:
    break
  print(i,end="")

# %%
for i in range(1,6):
  if i==3:
    break
  print(i,end="")

# %%
i=0
while i<5:
  i+=1  
  if i==3:
    continue
  print(i,end="")

# %%
for i in range(1,6):
  if i==3:
    continue
  print(i,end="")

# %%
def odd_check(n):
  """Check if n is odd (return True) or not (return False)."""
  if n%2==0:
    return False
  else:
    return True
print(odd_check(5))
print(odd_check(10))

# %%
def test(aa,bb,cc=123,dd='abc'):
  return aa,bb,cc,dd
print(test(1,2,3,4))
print(test(1,2,3))
print(test(1,2,dd='edf'))
print(test(1,2))

# %%
def adding(*num):
  sum=0
  for n in num:
    sum+=n
  return sum
print(adding(1,2,3,4,5))

# %%
adding = lambda x,y: x+y 
print(adding(3,8))             #顯示11
print((lambda x,y: x+y)(3,8))  #顯示11
lista=[1,3,5,7,9]
#以下將lambda函數當作map函數的參數
listb=list(map(lambda x:x+8, lista)) 
print(listb)

# %%
class Rectangle:
  length=0
  width=0
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    return self.length*self.width
  def perimeter(self):
    return 2*(self.length+self.width)
rect1=Rectangle(3,8)
rect2=Rectangle(2,4)
print('rect1:',rect1.length,rect1.width,rect1.area(),rect1.perimeter())
print('rect2:',rect2.length,rect2.width,rect2.area(),rect2.perimeter())

# %%
class NamedRectangle(Rectangle):
  name=''
  def __init__(self,length,width,name):
    super().__init__(length,width)
    self.name=name
  def show_name(self):
    print(self.name)
rect1=NamedRectangle(3,8,'rectangle1')
rect2=NamedRectangle(2,4,'rectangle2')
print('rect1:',rect1.length,rect1.width,rect1.area(),rect1.perimeter())
print('rect2:',rect2.length,rect2.width,rect2.area(),rect2.perimeter())
rect1.show_name()
rect2.show_name()


