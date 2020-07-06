from model_bakery.recipe import Recipe


user_john = Recipe(
    "accounts.User",
    username="john@doe.com",
    email="john@doe.com",
    first_name="John",
    last_name="Doe",
    password="Doe",
    phone_number="+56 912345678"
)