def print_messages(pending , sent):
    while pending:
        sending = pending.pop()
        print(f"Sending message: {sending}")
        sent.append(sending)

def sent_messages(sent):
    print("\nThe following messages have been sent:")
    for sent in sent:
        print(sent)
    

pending = ["Hello" , "U Up?" , "WYD?"]
sent = []

print_messages(pending [:], sent)
sent_messages(sent)

print(f"\n{pending}")
