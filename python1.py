from decimal import *
from wsgiref.simple_server import demo_app
getcontext().prec = 10
n= Decimal(10)/Decimal(3)

print(n)