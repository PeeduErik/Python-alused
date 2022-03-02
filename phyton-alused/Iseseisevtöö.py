#Peedu Erik Pajo
#Iseseisevtöö
#02.03.2022



email = input("Sisesta email: ")
print("@" in email)
print("Email oli : " + str(email))
s = email[email.index("@") + 1 : email.index(".")  ]
t = email[email.index("@") - 1 : ]
print("Tere" + str(t))



POOLELI






