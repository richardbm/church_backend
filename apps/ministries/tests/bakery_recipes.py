from model_bakery.recipe import Recipe, foreign_key

from apps.church.tests.bakery_recipes import contact_biblical_school
from apps.ministries.models import Ministry


ministry_biblical_school = Recipe(
    Ministry,
    name="Biblical School",
    description="The biblical school...",
    contact_information=foreign_key(contact_biblical_school)
)
