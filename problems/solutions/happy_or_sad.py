SAD_EMOTICON = ':-('
HAPPY_EMOTICON = ':-)'

message = input()

sad_emote_amount = message.count(SAD_EMOTICON)
happy_emote_amount = message.count(HAPPY_EMOTICON)

result = 'sad'
if sad_emote_amount == happy_emote_amount:
    result = 'unsure'
    if sad_emote_amount == 0:
        result = 'none'
elif happy_emote_amount > sad_emote_amount:
    result = 'happy'

print(result)
    
        