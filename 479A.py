x,y,z= int(input()),int(input()),int(input())

a= x*y*z
b=x+y+z
c=(x+y)*z
d= x*(y+z)
e= x*y+z
f= x+y*z

print(max(a,b,c,d,e,f))