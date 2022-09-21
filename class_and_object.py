class RoyalEnfiled():
  def __init__(self,model,CC,mileage,price,color):
    self.a = model
    self.cc = CC
    self.m = mileage
    self.p = price
    self.c = color
  def Re_details(self):
    print("---Bike deatils---")
    print("Bike model : ",self.a)
    print("bike cc : ",self.cc)
m = input("enter the bike model : ")
bcc = float(input("enter the bike cc : "))
bm = float(input("enter the bike mileage : "))
sp = float(input("enter the price of bike : "))
sc = input("enter the color of bike : ")

obj = RoyalEnfiled(m,bcc,bm,sp,sc)
obj.Re_details()