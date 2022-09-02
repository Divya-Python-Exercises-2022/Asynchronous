import asyncio

async def greeting():
    print('Preparing to say Hi')
    await asyncio.sleep(10)
    print('hi')

async def greeting2():
    print('Preparing to say Hello')
    await asyncio.sleep(5)
    print('hello')

async def main():
    task1 = asyncio.create_task(greeting())
    task2 = asyncio.create_task(greeting2())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    asyncio.run(main())
