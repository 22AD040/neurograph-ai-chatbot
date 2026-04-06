from chatbot.agent import run_agent

def chatbot_graph(messages):
    response = run_agent(messages)
    return response