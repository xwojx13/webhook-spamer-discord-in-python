from discord_webhook import DiscordWebhook
import random
weebhookurl = "https://discord.com/api/webhooks/910365500561842267/jUkmoPc0Usvak-I_yl8Fhg1IdYjntqkoZazPkDZhTfhJvGEs3D3NoQ2zJB_Lgi1dMMFl"
while True:
    a = random.randint(1000000000000,99999999999999999999999)
    b = random.randint(1000000000000,99999999999999999999999)
    c = random.randint(1000000000000,99999999999999999999999)
    d = random.randint(1000000000000,99999999999999999999999)
    f = random.randint(1000000000000,99999999999999999999999)
    g = random.randint(1000000000000,99999999999999999999999)
    print("wysłałes spam hook")
    webhook = DiscordWebhook(url=weebhookurl, rate_limit_retry=True,
                             content=f'{a,b,c,d,f,g}')
    response = webhook.execute()