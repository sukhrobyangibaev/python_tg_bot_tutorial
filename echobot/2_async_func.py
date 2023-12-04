import asyncio
import time


async def fun1(x):
    print('fun1 boshlandi')
    x**2
    await asyncio.sleep(3)
    print('fun1 bajarildi')


async def fun2(x):
    print('fun2 boshlandi')
    x**0.5
    await asyncio.sleep(3)
    print('fun2 bajarildi')


start = time.time()

# asinxron topshiriqlar siklini yaratish
loop = asyncio.get_event_loop()
# 1chi asinxron topshiriqni siklga qo'shish
task1 = loop.create_task(fun1(4))
# 2chi asinxron topshiriqni siklga qo'shish
task2 = loop.create_task(fun2(4))
# asinxron topshiriqlar siklini ishga tushirish
loop.run_until_complete(asyncio.wait([task1, task2]))

end = time.time()

print('sarflangan vaqt: {:.2f}s'.format(end - start))
