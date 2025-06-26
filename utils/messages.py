async def send_message(client, user_id, message):
    # отправка
    await client.send_message(user_id, message)