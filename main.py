import asyncio
import database, web



async def main():
    await database.setup()
    await web.setup()


if __name__ == '__main__':
    asyncio.run(main())
