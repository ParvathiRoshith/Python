class User:
    def __init__(self,user_id,username):
        self.id=user_id                       #attributes
        self.username=username
        self.followers=0
        self.following=0

    def follow(self, user):
        self.following = self.following+1         #object
        user.followers = user.followers+1   # user.followers += 1

user_1=User("001","Angela")
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2=User("002","Jack")
user_2.follow(user_1)
print(user_2.followers)
print(user_2.following)
print(user_1.followers)
print(user_1.following)