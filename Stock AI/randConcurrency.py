import datetime
import time
import AI
import asyncio
import timeit

title = "Google's revenue surpassed the expectations"



async def conc():


    gptTask = asyncio.create_task(AI.GPT(title))

    bardTask = asyncio.create_task(AI.Bard(title))

    gpt, bard = await asyncio.gather(gptTask, bardTask)


    return gpt, bard

# print(newsAPI.getNews())

async def test():

    start = time.time()

    print(AI.GPTNo(title))
    print(AI.BardNo(title))


    end = time.time()




    print(f"without async {(end-start)}")


    start = time.time()

    print(await conc())


    end =  time.time()


    print(f"with async {(end-start) }")

    # return gpt, bard



res = asyncio.run(test())

print(res)








