import discord
import asyncio
import random

client = discord.Client()

token = "NzEyNjAxMTQwODUxOTAwNTg2.XsT7lw.Jiv0UeUTRbha4qXy1rKU8_rsE60"

@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("가위바위보")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    import random

    if message.content == "!가위" or message.content == "!바위" or message.content == "!보":
        response = random.randint(1, 3)
        if response == 1:  # 가위
            await message.channel.send("가위")
            if message.content == "!가위":
                await message.channel.send("비겼다!")
            elif message.content == "!바위":
                await message.channel.send("까비..")
            elif message.content == "!보":
                await message.channel.send("아싸 이겼다!")
        if response == 2:  # 바위
            await message.channel.send("바위")
            if message.content == "!가위":
                await message.channel.send("아싸 이겼다!")
            elif message.content == "!바위":
                await message.channel.send("비겼다!")
            elif message.content == "!보":
                await message.channel.send("까비..")
        if response == 3:  # 보
            await message.channel.send("보")
            if message.content == "!가위":
                await message.channel.send("까비..")
            elif message.content == "!바위":
                await message.channel.send("아싸 이겼다!")
            elif message.content == "!보":
                await message.channel.send("비겼다!")





    if message.content == "문의":
      await message.channel.send("discord:Hmm#4112, 똥컴 유상 8kg 빼야 2070super로 바꿈 !!#3188")



    if message.content == "!명령어 리스트":
      await message.channel.send("야이좆밥아, 야병신, 내얼굴평가, 관리자얼굴평가, 이번년운세보기, 버그제보, 문의, !명령어 리스트")

    if message.content == "ㅎㅇ":
          await message.channel.send("ㄴㄱㅅㅇ?")

    if message.content == "!공지 ㅎㅇ명령어추가":
          await message.channel.send("@everyone 명령어 하나 추가 완료 추가 명령어:ㅎㅇ 추후 더 많은 명령어를 만들거입니다")



client.run(token)




