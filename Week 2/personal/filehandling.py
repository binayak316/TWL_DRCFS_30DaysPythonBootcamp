# pwd = open('/home/commando/PycharmProjects/python bootcamp/TWL_DRCFS_30DaysPythonBootcamp/Week 2/personal/password.txt','r')
# print(pwd)

# actual_file = pwd.read()
# print(actual_file)
# pwd.close

# open the file in write-only mode

# file = open('/home/commando/PycharmProjects/python bootcamp/TWL_DRCFS_30DaysPythonBootcamp/Week 2/personal/newfile.txt','w')
# file.write('hello binayak \n')
# file.write(' k xa')
# file.close()

# appendmode
# file = open('/home/commando/PycharmProjects/python bootcamp/TWL_DRCFS_30DaysPythonBootcamp/Week 2/personal/newfile.txt','a')
# file.write('\n this is an additional line')
# file.close()






# lllllllllllll  

# open the file in read-only mode using the 'with'keyword
# with open('/home/commando/PycharmProjects/python bootcamp/TWL_DRCFS_30DaysPythonBootcamp/Week 2/personal/newfile.txt','r')as file:
# # with keyword use gareera text file ma lyaiyo as file garera and contents ma variable banara pathaiyo
# # with keyword use garesi .close() garnu pardaina
#     contents = file.read()
#     print(contents)






# \\\\\\\\\\\\\\\\\\\\
username_pwd = open('/home/commando/PycharmProjects/python bootcamp/TWL_DRCFS_30DaysPythonBootcamp/Week 2/personal/password.txt','r').read()
username_pwd = username_pwd.split()
print(username_pwd[0].split(',')[1])

for u_pwd in username_pwd:
    print(u_pwd.split(',')[1])