def validate_permissions(operation, user):  # pragma: no cover
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"