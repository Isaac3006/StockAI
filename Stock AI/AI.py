import openai
import os
import sys
import pprint
import google.generativeai as palm
import asyncio



defaultMessage = open("defaultMessage.txt", "r").read()

openaiKey = "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"
# openai.api_key = os.getenv(openaiKey)
openai.api_key = openaiKey
bardKey = "AIzaSyAnJy8TlbebWGrkRxYGue6fqC96P1i9ZGU"

palm.configure(api_key=bardKey)


bardModel = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods][0].name


async def analyze(title):
    
    gptTask = asyncio.create_task(GPT(title))

    bardTask = asyncio.create_task(Bard(title))

    gpt, bard = await asyncio.gather(gptTask, bardTask)


    return gpt, bard



def bardModels():
    print(bardModel)

async def Bard(title):



    completion = palm.generate_text(
        model=bardModel,
        prompt="".join([defaultMessage, title]),
        temperature=0,
    )
    return parseResponse(completion.result)


def BardNo(title):


    completion = palm.generate_text(
        model=bardModel,
        prompt="".join([defaultMessage, title]),
        temperature=0,
    )
    return parseResponse(completion.result)

    

# Working

def GPTNo(title):

    worked = False

    completion = None

    tries = 0

    while not worked and tries < 5:
        
        try:

            

            completion, worked = connectGPT(title)


            

        except:
            print(sys.exc_info())

        tries += 1

    if tries >= 5:
        return None

    return parseResponse(completion.choices[0].message.content)



# Working

async def GPT(title):

    worked = False

    completion = None

    tries = 0

    while not worked and tries < 5:
        
        try:

            

            completion, worked = connectGPT(title)


            

        except:
            print(sys.exc_info())

        tries += 1

    if tries >= 5:
        return None

    return parseResponse(completion.choices[0].message.content)


def connectGPT(title):
    message=[
                {"role": "user", "content": "".join([defaultMessage, title])}

            ]
            


    completion = openai.ChatCompletion.create(
    model="gpt-4-0613",

    messages = message
    
    )

    return completion, True


def parseResponse(response):
    start = response.index("{")
    end = response.index("}")

    try:

        return eval(response[start: end + 1])
    
    except:
        return {}