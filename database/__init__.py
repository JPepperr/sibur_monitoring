from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {
        "cherepaha": "sqlite://database/cherepaha",
    },
    "apps": {
        "models_problems": {
            "models": ["database.models"],
            "default_connection": "cherepaha",
        },
        "models_person": {
            "models": ["database.models"],
            "default_connection": "cherepaha",
        },
        "models_type": {
            "models": ["database.models"],
            "default_connection": "cherepaha",
        }
    },
}


async def setup():
    await Tortoise.init(config=TORTOISE_ORM, _create_db=True)
    await Tortoise.generate_schemas()
