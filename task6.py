from datetime import datetime

name=input("Enter Name : ")

lists ='''
Rice Rs 20/kg
Sugar   Rs 30/kg
salt    Rs 20/kg
chocos  Rs 100/500g
oil     Rs  35/L
paneer  Rs 115/Kg
milk    Rs 30/500ml
tomato  Rs 35/500g
'''

price=0
pricelist=[]
totalprice=0
Finalfinalyprice=0
ilist=[]
qlist=[]
plist=[]


items={'rice':20,
       'Sugar':30,
       'salt':20,
       'chocos':100,
       'oil':35,'paneer':115,'milk':30,'tomato':35}
option=int(input("Press 1 to see today's stock : "))
if option == 1:
       print(lists)

for i in range(len(items)):
       inp1=int(input("Click 1 to buy or click 2 to exit : "))
       if inp1 == 2:
              print("Thank You For Visiting, Hope You Visit Again")
              break
       if inp1 == 1:
              item=input("Enter The Items You Want To Buy : ")
              quantity=int(input("Enter The Quantity : "))
              if item in items.keys():
                     price = quantity*(items[item])
                     pricelist.append((item,quantity,items,price))
                     totalprice += price
                     ilist.append(item)
                     qlist.append(quantity)
                     plist.append(price)
                     gst = (totalprice*5)/100
                     finalamount = gst + totalprice
              else:
                  print(item,"Not On Stock")
       else:
           print("You Enter A Wrong Number")
       inp=input("DO You Want To Bill The items? Enter y for yes and n for no : ")
       if inp == 'y':
              pass
              if finalamount != 0:
                     print(25*"=","RR Bros supermarket",25*"=")
                     print(28*"="," ","Sainikpuri",28*"=")
                     print("name : ",name,30*" ","Date: ",datetime.now())
                     print(75*"-")
                     print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
                     for i in range(len(pricelist)):
                            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
                     print(75*"-")
                     print(50*" ",'Total Amount: ','Rs',totalprice)
                     print("Gst Amount: ",40*" ",'Rs',gst)
                     print(75*"-")
                     print(50 * " ", 'Final Amount: ', 'Rs', finalamount)
                     print(75 * "-")
                     print(50 * " ",'Thanks For Visiting')
                     print(75 * "-")
                     break



