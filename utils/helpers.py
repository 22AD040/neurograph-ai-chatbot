def generate_chat_title(message):
    return message[:30] + "..." if len(message) > 30 else message

def format_messages(messages):
    return "\n".join([f"{m['role']}: {m['content']}" for m in messages])