import asyncio

async def greeting():
    print('Preparing to say Hi')
    await asyncio.sleep(5)
    print('hi')

async def greeting2():
    print('Preparing to say Hello')
    await asyncio.sleep(2)
    print('hello')

async def main():
    await greeting()
    await greeting2()

if __name__ == '__main__':
    asyncio.run(main())
