########################################
# Stores
########################################
import itertools

class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        member = None
        for m in all_members:
            if m.id == id:
                member = m
        return member

    def update(self, item_instance):
        instance_found = self.get_by_id(item_instance.id)
        if (instance_found != False):
            self._data_provider[self._data_provider.index(instance_found)] = item_instance

    def delete(self, id):
        member = self.get_by_id(id)
        if member != False:
            self._data_provider.remove(member)

    def entity_exists(self, item_instance):
        result = False
        result = self.get_by_id(item_instance.id)
        if result != False:
            result = True
        return result


class MemberStore(BaseStore):

    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, name):
        all_members = self.get_all()
        member = None
        for m in all_members:
            if m.name == name:
                member = m
        return member

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all()
        for member, post in itertools.product(all_members, all_posts):
                if (member.id == post.member_id):
                    member.posts.append(post)
        return(all_members)

    def get_top_two(self, all_posts):
        top_number = 2
        member_with_posts = self.get_members_with_posts(all_posts)
        member_with_posts_sorted = sorted(member_with_posts, key=lambda member_with_posts: len(member_with_posts.posts), reverse=True)
        return member_with_posts_sorted[0:top_number]

    def __repr__(self):
        return """Members: {}""".format(self.members)

class PostStore(BaseStore):

    posts = []

    def __init__(self):
        super().__init__(PostStore.posts,0)

    def __repr__(self):
        return """Posts: {}""".format(self.posts)
