from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent


@tool
def calculator(a: float, b: float) -> str:
    """useful for performing basic arithmatic calculations with numbers"""
    return f"The sum of {a} and {b} is {a+b}"
def main():
   
    model = ChatOllama(model="llama2")
  

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant (running on Ollama). Type 'quit' to exit.")
    print("You can ask me to perform calculations or just chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
