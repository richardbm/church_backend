from model_bakery.recipe import Recipe

# ############### About ###############

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


# ############### Contact ###############


contact_john_doe = Recipe(
    "church.Contact", name="John Doe", description="Main Pastor", order=1
)

contact_jane_doe = Recipe(
    "church.Contact", name="Jane Doe", description="Elder", order=2
)

contact_workship = Recipe(
    "church.Contact", name="Workship ministry", description="", order=3
)


contact_biblical_school = Recipe(
    "church.Contact", name="Biblical school", description="", order=3
)


# ############### News ###############


news_changing_schedule = Recipe(
    "church.News",
    subject="Changes in biblical shcool schedule since April 22",
    content="Next week the schedule will be on Sunday at 11am",
)


news_special_activity = Recipe(
    "church.News",
    subject="We are preparing a new special activity for next month",
    content="We are preparing a new special activity for next month",
)
