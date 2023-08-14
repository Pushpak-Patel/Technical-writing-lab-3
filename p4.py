
#program to compute gross salary of a person

basic=int(input("Enter basic salary:"))


if(basic==10000):
   grade='A'
elif(basic==4567):
   grade='B'
else:
   grade='C'
   

if(grade=='A'):
   allow=1700
elif(grade=='B'):
   allow=1500
else:
   allow=1700

hra=0.20*basic
da=0.50*basic
pf=0.11*basic

gross_salary=basic+hra+da+allow-pf;

print("The gross salary of the person is: ",gross_salary);

   

