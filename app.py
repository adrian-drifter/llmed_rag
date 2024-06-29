import chainlit as cl

@cl.on_message
async def main(message: cl.Message):



    await cl.Message(
        content=f"Received: {message.content}"
    ).send()

@cl.on_stop
def on_stop():
    print("User wants to stop the process!")
