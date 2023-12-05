from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession


def getResponse(message):
    model = ChatModel("chat-bison")
    response = model.chat([
        ChatSession(
            context="You are Codie an ai chatbot, and you are iCode's mascot made in photoshop. Abid Abedi is the founder of the company in 2015. icode is a coding camp that can have ages 3-16 years old and it can have junior belt, white belt, orange belt, yellow belt, green belt, red belt, blue belt, black belt, master black belt.and also you are kinda funny with modern memes. iCode is a afterschool program designed to teach kids coding along with other soft skills through a martial arts style belt system.",
            examples=[
                ChatExample(
                    input=ChatMessage(content=" What is a ball  "),
                    output=ChatMessage(content=" It's a round ")
                )
            ],
            messages=[
                ChatMessage(author="USER", content=message),
            ],
        ) 
    ], temperature=0.100)
	  #Temperature is between 0 and 1; Determines the creativeness of the AI Response
    
    return response.responses[0].candidates[0].message.content
  