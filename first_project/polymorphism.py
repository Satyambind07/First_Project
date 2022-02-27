
# class Bird:
#   def intro(self):
#     print("There are many types of birds.")
     
#   def flight(self):
#     print("Most of the birds can fly but some cannot.")
   
# class sparrow(Bird):
#   def flight(self):
#     print("Sparrows can fly.")
     
# class ostrich(Bird):
#   def flight(self):
#     print("Ostriches cannot fly.")

# def f1(obj):
#     obj.intro()

# i = [Bird(),sparrow(),ostrich()]
# for obj in i:
#     f1(obj)
     
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
 
# obj_bird.intro()
# obj_bird.flight()
 
# obj_spr.intro()
# obj_spr.flight()
 
# obj_ost.intro()
# obj_ost.flight()










# # operator overloading


# class A:
#     def __init__(self, a):
#         self.a = a
#     def __gt__(self, other):
#         if(self.a>other.a):
#             return True
#         else:
#             return False
# ob1 = A(2)
# ob2 = A(3)
# if(ob1>ob2):
#     print("ob1 is greater than ob2")
# else:
#     print("ob2 is greater than ob1")







# method overloading----------------------

# class Test:
#     def m1(self):
#         print("no arg method")
    
#     def m1(self, a):
#         print("one arg method")

#     def m1(self, a, b):
#         print("two arg method")

# t = Test()
# t.m1(1,2)

# how to handle method overloading------------

# class Test:
#     def sum(self,a=None, b=None, c=None):
#         if a!= None and b!=None and c!=None:
#             print("The sum of 3 numbers:", a+b+c)
#         elif a!=None and b!= None:
#             print("The sum of two numbers:", a+b)
#         else:
#             print("please provide 2 or 3 arguments")  

# t= Test()
# t.sum(1,2)
# t.sum(10,20,30)
# t.sum(50)




# method overriding-----------------

# class Parents:
#     def wawar(self):
#         print("wawar ahe t power ahe")

# class child(Parents):
#     def cash(self):
#         print("cash hai to ash hai")

# x = child()
# x.wawar()
# x.cash()
