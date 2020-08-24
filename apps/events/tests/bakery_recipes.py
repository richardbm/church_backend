from model_bakery.recipe import Recipe, foreign_key

rule_weekly = Recipe(
    "schedule.Rule",
    name="Weekly",
    description="Every week",
    frequency="WEEKLY"
)

biblical_school_event = Recipe(
    "schedule.Event",
    title="Biblical school",
    start="2020-08-08T10:00:00Z",
    end="2020-08-08T12:00:00Z",
    color_event="blue",
    description="This is the biblical school",
    rule=foreign_key(rule_weekly)
)
