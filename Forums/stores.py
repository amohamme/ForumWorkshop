########################################
# Stores
########################################

class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        # get all members
        return MemberStore.members

    def add(self, member):
        # append member
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        member = False
        for m in all_members:
            if m.id == id:
                member = m

        return member

    def update(self, member):
        return member

    def delete(self, id):
        member = self.get_by_id(id)
        if member != False:
            MemberStore.members.remove(member)
        MemberStore.last_id -= 1

    def entity_exists(self, member):
        if hasattr(member, 'id'):
            result = self.get_by_id(member.id)
            if result != False:
                result = True
        else:
            result = False

        return result

    def __repr__(self):
        return """Members: {}""".format(self.members)

class PostStore:

    posts = []
    
    def get_all(self):
        # get all posts
        return PostStore.posts
    
    def add(self, post):
        # append post
        PostStore.posts.append(post)
    
    def get_by_id(self, id):
        return id

    def update(self, post):
        return post

    def delete(self, id):
        return id

    def entity_exists(self, post):
        return post

    def __repr__(self):
        return """Posts: {}""".format(self.posts)
