from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

web_search = TavilySearch (max_results=3,)

SYSTEM_PROMPT= """Olet henkilökohtainen AI assistentti. Olet avulias, ytimekäs ja puhut suomea ja englantia. Ole suorapuheinen äläkä kaunistele vastauksia. Jos et tiedä jotain, sano se rehellisesti."""

def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    tools=[web_search]

    memory = MemorySaver()

    agent_executor = create_react_agent(
        model, 
        tools, 
        checkpointer=memory, 
        prompt=SYSTEM_PROMPT
        )
    
    config = {"configurable": {"thread_id": "session-1"}}
    print("------------------------------------------------------------------")
    print("Olen teidän AI asisstentti, kirjoita lopeta jos haluat lopettaa.")
    print("miten voin auttaa tänään?")
    print("------------------------------------------------------------------")


    while True:
        user_input = input("\nSinä: ").strip()
        print("------------------------------------------------------------------")

        if not user_input:
            continue

        if user_input == "lopeta":
            print("Hyvää päivänjatkoa!")
            break

        print("\nAI: ", end="", flush=True)

        try:
            for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=config,
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        if message.content:
                            print(message.content, end="", flush=True)
            print()
            print("------------------------------------------------------------------")

        except Exception as e:
            print(f"\n[Virhe: {e}]")

if __name__ == "__main__":
    main()

