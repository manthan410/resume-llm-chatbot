import chainlit as cl


# continuously on a loop
@cl.on_message
async def main(message:cl.Message):
        # your logic will be here
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload your resume as pdf!", accept=["text/plain"]
        ).send()
    # Decode the file
    text_file = files[0]
    text = text_file.content.decode("utf-8")
    
    # Let the user know that the system is ready
    await cl.Message(
        content=f"`{text_file.name}` uploaded, it contains {len(text)} characters!"
    ).send()


@cl.on_chat_start
async def start():
   content ="Hi I am a OpenX-Job-assistant, Here to help you apply for relevant job postings available in our job portal. I will guide you through the requirements step-by-step. Can you pls. upload your resume?"
   await cl.Message(content=content).send()



