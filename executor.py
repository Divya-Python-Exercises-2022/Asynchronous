import asyncio
from asyncio import sleep


def greeting(future):
    sleep(6)
    print('hi')
    future.set_result('greeting 1 done')


def greeting2(future):
    sleep(3)
    print('hello')
    future.set_result('greeting 2 done')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    f1 = loop.create_future()
    f2 = loop.create_future()

    loop.run_in_executor(None, greeting, f1)
    loop.run_in_executor(None, greeting2, f2)

    while not f1.done() or not f2.done():
        sleep(1)
        print('Waiting for 2 tasks to be done')

    print(f1.result())
    print(f2.result())

