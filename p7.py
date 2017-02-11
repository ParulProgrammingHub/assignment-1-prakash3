7)	WPP to enter 2 angles and using function thirdangle( angle1, angle2) calculate third angle.
Solution:
p=int( input( "Enter a value of first angle : " ))
q=int( input( "Enter a value of second angle : " ))
def  r(p,q) :
       s = 180-p-q
       print ("Third angle is : ",s)
       return s
r(p,q)
