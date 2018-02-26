########################################
# Stores
########################################

class MemberStore:

    members = []

    def get_all(self):
        # get all members
        return self.members

    def add(self, member):
        # append member
        self.members.append(member)

    def get_by_id(self, id):
        return id

    def update(self, member):
        return member

    def delete(self, id):
        return id

    def entity_exists(self, member):
        return member
    
    def __repr__(self):
        return """Members: {}""".format(self.members)

class PostStore:

    posts = []
    
    def get_all(self):
        # get all posts
        return self.posts
    
    def add(self, post):
        # append post
        self.posts.append(post)
    
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