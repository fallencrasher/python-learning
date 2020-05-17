import asyncio

async def func(name): # 定义一个协程函数
    print('start',name)
    # await 可能会发生阻塞的方法
    # await 关键字必须写在一个 async 函数里
    await asyncio.sleep(1) # await 在这里声明，我要在这里阻塞了，时间片需要切走
    print('end')

loop = asyncio.get_event_loop()
loop.run_until_complete(func('alex')) # 这是同时启动一个协程

loop.run_until_complete(asyncio.wait([func('taibai'),func('wusir')]))