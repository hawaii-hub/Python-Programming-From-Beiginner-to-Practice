# 8.10发送消息
def send_messages(pending_messages, sent_messages):
    """打印每条消息,保留到一个列表"""
    while pending_messages:
        message = pending_messages.pop()
        sent_messages.append(message)
    print(f"pending_message: {pending_messages}")
    print(f"sent_messages:{sent_messages}")

hello = ['hello', 'nihao', 'good night', '早上好']
sent_messages = []

send_messages(hello, sent_messages)

# 8.11 消息归档
#调用函数副本，确定保留所有信息
hello = ['hello', 'nihao', 'good night', '早上好']
send_messages(hello[:], sent_messages)
print(f"Original: {hello}")