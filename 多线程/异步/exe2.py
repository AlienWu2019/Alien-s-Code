import asyncio

async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)

#定义一个回调函数
def done_callback(futu):
    print('Done')


loop = asyncio.get_event_loop()
futu = asyncio.ensure_future(do_some_work(3))
futu.add_done_callback(done_callback)
loop.run_until_complete(futu)
# print(asyncio.iscoroutinefunction(do_some_work)) #判断do_some_work是否为一个协程函数
# print(asyncio.iscoroutine(do_some_work(3))) #判断是否返回一个协程对象