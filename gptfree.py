from freeGPT import AsyncClient
from asyncio import run


async def main():
    while True:
        prompt = input("Input: ")
        try:
            resp = await AsyncClient.create_completion("gpt3", prompt)
            print(f"Resposta: {resp}")
        except Exception as e:
            print(f": {e}")


run(main())