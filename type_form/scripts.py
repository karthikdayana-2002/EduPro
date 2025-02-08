from type_form.models import UserModel
import uuid

users = list(UserModel.scan(UserModel.email == "example@test.com"))

if users:
    for user in users:
        print(f"User ID: {user.id}")
else:
    print("No users found with the given email.")