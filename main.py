import asyncio
import database


async def main():
    await database.setup()


if __name__ == '__main__':
    asyncio.run(main())
