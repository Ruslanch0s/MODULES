import asyncio
import functools
import random

lock = asyncio.Lock()

background_tasks = set()


async def cancel_tasks():
    global background_tasks

    for task in background_tasks:
        task.cancel()


def done_callback(task):
    global background_tasks
    background_tasks.discard(task)  # удаляет из множества


async def my_task(symbol):
    try:
        while 1:
            print('Task', symbol)
            await asyncio.sleep(random.randint(0, 3))
    except asyncio.CancelledError:
        print(f'Задача {symbol} отменена')


async def set_tasks(symbols: list[str]):
    await asyncio.sleep(random.randint(0, 10))

    global background_tasks
    await cancel_tasks()
    for symbol in symbols:
        task = asyncio.create_task(my_task(symbol))
        background_tasks.add(task)
        # каждой задаче удалить свою ссылку из набора после завершения
        # functools.partial() для передачи параметров
        task.add_done_callback(
            functools.partial(done_callback)
        )
    await asyncio.gather(*background_tasks)


async def main():
    car_names_1 = ['audi', 'vw', 'bmw']
    car_names_2 = ['audi', 'vw', 'ggg']
    main_tasks = set()
    main_tasks.add(asyncio.create_task(set_tasks(car_names_1)))
    main_tasks.add(asyncio.create_task(set_tasks(car_names_2)))
    await asyncio.gather(*main_tasks)


asyncio.run(main())
