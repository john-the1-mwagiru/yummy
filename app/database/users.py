from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """Class representing a single user"""

    id: Optional[int]
    email: str
    password: str
    user_id: int


class UserModel:
    """User data class"""
    id_counter = 5
    saved_users = [
        User(
            id=1,
            email="name1@example.com",
            password="gravity@1777",
            user_id=1,
        ),
        User(
            id=2,
            email="name2@example.com",
            password="bunns124@",
            user_id=1,
        ),
        User(
            id=3,
            email="name3@example.com",
            password="Graviton@77",
            user_id=2,
        ),
        User(
            id=4,
            email="name4@example.com",
            password="@cupAtee",
            user_id=2,
        ),
    ]
    

    @classmethod
    def get_all(cls):
        return cls.saved_users

    @classmethod
    def get(cls, id: int) :
        all = cls.get_all()
        for one in all:
            if id == one.id:
                return one

        raise Exception("User not found")

    @classmethod
    def create(cls, data: User) -> User:
        if data.id is not None:
            return "User already exists"
        
        cls.id_counter +=1 
        data.id =cls.id_counter
        cls.saved_users.append(data)
        return data
                     
    @classmethod
    def update(cls, id: int, data: User) -> User:
        all = cls.get_all()
        for user_to_update in all:
            if user_to_update.id ==id:
                user_to_update.email = data.email
                user_to_update.password = data.password
                return user_to_update

        raise Exception("User not found")        

    @classmethod
    def delete(cls, id: int) -> bool:
        user_to_delete = cls.get(id)
        cls.saved_users.remove(user_to_delete)
        return True
                



