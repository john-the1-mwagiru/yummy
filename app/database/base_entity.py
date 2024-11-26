"""Base model class to represent entities in the database"""

from abc import ABC, abstractmethod


class BaseEntityModel(ABC):
    """Abstract class to represent an entity database model"""

    @abstractmethod
    @classmethod
    def get_all(cls):
        """Method to retrieve all instances from database"""

    @abstractmethod
    @classmethod
    def get(cls, id):
        """Method to retrieve an instance from a database"""

    @abstractmethod
    @classmethod
    def create(cls, data):
        """Method to create an entity instance in the database"""

    @abstractmethod
    @classmethod
    def update(cls, id, data):
        """Method to update an entity instance in the database"""

    @abstractmethod
    @classmethod
    def delete(cls, id):
        """Method to delete an entity instance in the database"""
