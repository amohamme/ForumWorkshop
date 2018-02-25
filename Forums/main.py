########################################
# Main
########################################

from models import member
from models import post

name1 = 'Ahmed'
age1  = 32
name2 = 'Mohammed'
age2  = '22'

title1 = 'title 1'
content1 = 'content 1'

title2 = 'title 2'
content2 = 'content 2'

title3 = 'title 3'
content3 = 'content3'

member1 = member(name1,age1)
member2 = member(name2,age2)

post1 = post(title1,content1)
post2 = post(title2,content2)
post3 = post(title3,content3)

print(member1.name)
print(member2.age)
