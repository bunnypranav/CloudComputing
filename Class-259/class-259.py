from etherpad_lite import EtherpadLiteClient

etherClient = EtherpadLiteClient(
    base_params={
        "apikey": "8230eed3bd144c3288a6cb66163127cabca0e39113bb508a672544ab6bd5c6d4"
    }
)

group = etherClient.createGroup()
print(f"Your group is: {group}")

newPad = etherClient.createPad(padID="blackhat", text="Hello!")
print(f"Your pad is: {newPad}")
