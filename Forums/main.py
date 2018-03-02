########################################
# Main
########################################

import models
import stores

member_store = stores.MemberStore()
post_store = stores.PostStore()

name1 = 'Name 1'
age1  = '11'
name2 = 'Name 2'
age2  = '12'
name3 = 'Name 3'
age3  = '13'
name4 = 'Name 4'
age4  = '14'

title1 = 'title 1'
content1 = 'content 1'

title2 = 'title 2'
content2 = 'content 2'

title3 = 'title 3'
content3 = 'content3'

member1 = models.member(name1,age1)
member2 = models.member(name2,age2)
member3 = models.member(name3,age3)
member4 = models.member(name4,age4)

post1 = models.post(title1,content1)
post2 = models.post(title2,content2)
post3 = models.post(title3,content3)

member_store.add(member1)
member_store.add(member2)
member_store.add(member3)

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

#print(member1)
#print(post1)
print(member_store.get_all())
print(post_store.get_all())
print(member_store.get_by_id(2))
print(member_store.entity_exists(member4))
print(member_store.delete(2))
print(member_store.get_all())
print(member_store.get_by_id(2))
member_store.add(member2)
print(member_store.get_all())

