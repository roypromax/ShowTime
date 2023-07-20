from app import mongo
from typing import Dict, Any

class User:
    def __init__(self, username: str, email: str, password: str, status: bool = True, gender: str = None,
                 membership_type: str = 'Regular', bio: str = None, dob: str = None):
        if not all([username, email, password, gender, dob]):
            raise ValueError("All required fields must be provided.")

        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.gender = gender
        self.membership_type = membership_type
        self.bio = bio
        self.dob = dob

    def save(self):
        user_data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'status': self.status,
            'gender': self.gender,
            'membership_type': self.membership_type,
            'bio': self.bio,
            'dob': self.dob
        }
        return mongo.db.users.insert_one(user_data)

    @staticmethod
    def get_all():
        users = mongo.db.users.find({})
        return [user for user in users]

    @staticmethod
    def get_by_id(user_id):
        user = mongo.db.users.find_one({'_id': user_id})
        return user

    @staticmethod
    def update(user_id, update_data: Dict[str, Any]):
        update_result = mongo.db.users.update_one({'_id': user_id}, {'$set': update_data})
        return update_result

    @staticmethod
    def delete(user_id):
        delete_result = mongo.db.users.delete_one({'_id': user_id})
        return delete_result
