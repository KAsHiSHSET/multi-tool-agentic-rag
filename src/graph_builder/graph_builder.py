"""Graph builder for Agentic RAG"""

from langgraph.graph import StateGraph, END

from src.state.rag_state import RAGState
from src.node.reactnode import RAGNodes


class GraphBuilder:

    def __init__(self, retriever, llm):

        self.nodes = RAGNodes(retriever, llm)
        self.graph = None

    def build(self):

        builder = StateGraph(RAGState)

        # Only one node now
        builder.add_node(
            "agent",
            self.nodes.generate_answer
        )

        builder.set_entry_point("agent")

        builder.add_edge(
            "agent",
            END
        )

        self.graph = builder.compile()

        return self.graph

    def run(self, question: str):

        if self.graph is None:
            self.build()

        state = RAGState(
            question=question
        )

        return self.graph.invoke(state)