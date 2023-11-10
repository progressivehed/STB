from telethon.sync import TelegramClient

api_id = 'your_api_id'
api_hash = 'your_api_hash'
channel_username = 'your_channel_username'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start()

    try:
        # Get the channel entity
        channel = await client.get_entity(channel_username)

        # Fetch recent messages
        messages = await client.get_messages(channel, limit=10)

        # Process and print messages
        for message in messages:
            print(f"From: {message.sender_id} - Date: {message.date} - Text: {message.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Disconnect from Telegram
        await client.disconnect()

if __name__ == '__main__':
    # Run the main function
    client.loop.run_until_complete(main())
