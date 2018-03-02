########################################
# Main
########################################

import models
import stores

member_store = stores.MemberStore()
post_store = stores.PostStore()

def create_members():

    member1 = models.member("Mohammed", 20)
    member2 = models.member("Omar", 22)
    member3 = models.member("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)

    return member1, member2, member3


def add_models_to_store(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)

def test_update(member_store, member3):
    member3_copy = models.member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "Ahmed"
    member3_copy.age = "26"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))

def test_get_by_name(member_store, name):
    print("=" * 30)
    member = member_store.get_by_name(name)
    print(member)

def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


members_instances = create_members()
member1, member2, member3 = members_instances

add_models_to_store(members_instances, member_store)

#print_all_members(member_store)

test_update(member_store, member3)

test_get_by_name(member_store, 'Mohammed')
