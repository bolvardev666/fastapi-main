from tortoise import Tortoise, run_async
import os

fast_user = os.getenv('FAST_USER')
fast_password = os.getenv('FAST_PASSWORD')
fast_url = os.getenv('FAST_URL')
fast_port = os.getenv('FAST_PORT')
fast_db = os.getenv('FAST_DB')

db_url = f"asyncpg://{fast_user}:{fast_password}@{fast_url}:{fast_port}/{fast_db}"
print(db_url)


async def init():
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["model.user_model"]}
    )
    await Tortoise.generate_schemas()

run_async(init())
