from etherpad_lite import EtherpadLiteClient
import datetime

etherClient = EtherpadLiteClient(
    base_params={
        "apikey": "8230eed3bd144c3288a6cb66163127cabca0e39113bb508a672544ab6bd5c6d4"
    }
)

newPad = etherClient.createPad(padID="c260", text="Hello!")
print(f"Your pad is: {newPad}")

createAuthor = etherClient.createAuthor(name="clouduser")
print(createAuthor)

padCount = etherClient.padUsersCount(padID="c260")
print(padCount)

timestamp = etherClient.getLastEdited(padID="c260")
print(timestamp)
print("Date Time: ", datetime.datetime.fromtimestamp(timestamp["lastEdited"] / 1000.0))

deletePad = etherClient.deletePad(padID="c260")
print(deletePad)
