from model_bakery.recipe import Recipe


about_mission = Recipe(
    "church.About",
    label="Mission",
    description="This is the mission of the church...",
    order=1,
)

about_vision = Recipe(
    "church.About",
    label="Vision",
    description="This is the vision of the church...",
    order=2,
)

about_history = Recipe(
    "church.About",
    label="History",
    description="This is the history of the church...",
    order=1,
)
