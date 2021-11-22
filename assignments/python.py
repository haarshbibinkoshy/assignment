# duck typing
# class pycharm:
#     def execute(self):
#         print("compiling")
#         print("running")

# class vscode:
#     def execute(self):
#         print("spell checking")
#         print("compiling")
#         print("running")       

# class laptop:
#     def code(self,ide):
#         ide.execute()
# ide=vscode()
# ide.execute()
# lap1=laptop()
# lap1.code(ide)
# **************************************
# operator overloading
# class students:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,other):
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         s3=students(m1,m2)
#         return s3
# s1=students(58,69)
# s2=students(60,65)
# s3=s1+s2
# print(s3.m1)
# print(s3.m2)
# *********************************
# method overloading
class students:
    def __init__(self):
        self.m1 =0

    def sum(self,a,b,c=0):
        s=a+b+c
        return s

s1=students()
print(s1.sum(1,2))

