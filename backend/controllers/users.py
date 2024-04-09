from database.config import session
from models.users import UserModel


class UserController:
    def __init__(self) -> None:
        self.db = session

    def find_one_user(self, id: str):
        return self.db.query(UserModel).filter(UserModel.id == id)

    def find_user(self, id: str):
        user = self.find_one_user(id)
        return user.first()

    def find_all_users(self):
        return self.db.query(UserModel).all()

    def create_user(self, user):
        new_user = UserModel(**user)
        self.db.add(new_user)
        self.db.commit()
        return user

    def update_user(self, id: str, changes: UserModel):
        user = self.find_one_user(id)
        user.update(changes)

    def delete_user(self, id: str):
        user = self.find_one_user(id)
        return user.delete()
