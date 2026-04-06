def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "Invalid calculation"

def search_tool(query):
    return f"Search result for: {query}"