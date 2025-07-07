from uuid import uuid4
from chaos_agent.graph.build_graph import build_graph


if __name__ == "__main__":
    graph = build_graph()
    config = {"configurable": {"thread_id": f"{uuid4()}"}}
    result = graph.invoke({}, config=config)
    # print(result)
