from uuid import uuid4
from langgraph.types import Command
from chaos_agent.graph.build_graph import build_graph


if __name__ == "__main__":
    graph = build_graph()
    config = {"configurable": {"thread_id": f"{uuid4()}"}}
    result = graph.invoke({}, config=config)
    # print(result)

    # Request user input if interrupted
    while result.get("__interrupt__"):
        print(result["__interrupt__"]) # Shows prompt

        user_response = input("Input: ")
        result = graph.invoke(Command(resume=user_response), config=config)

    print("\n--- Practice Session Complete ---")
