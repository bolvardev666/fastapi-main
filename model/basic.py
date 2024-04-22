from tortoise import Tortoise, run_async


async def init():
    await Tortoise.init(
        db_url="asyncpg://main:246873915Ab.@192.168.3.5:5432/main",
        modules={"models": ["model.user_model"]}
    )
    await Tortoise.generate_schemas()


run_async(init())
