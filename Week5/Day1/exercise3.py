class Phone:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self,other_phone):
        print(f"{self.phone_number} called {other_phone}")
        self.call_history.append(f"You called: {other_phone}")    

    def show_call_history(self):
        print(self.call_history)

    def change_number(self,new_num):
        self.phone_number = new_num

    def send_messages(self, other_phone, message):
        nwdct = {}
        nwdct["to"] = other_phone
        nwdct["from"] = self.phone_number
        nwdct["content"] = message
        self.messages.append(nwdct)

    def  show_sent_to(self):
        for n in self.messages:
            # if "to" in n.keys():
            k = n["to"]
            print(f"This message was sent to {k}")

    def  show_sent_by(self):
        for n in self.messages:
            # if "to" in n.keys():
            k = n["from"]
            print(f"This message was sent by {k}")


    def  show_messages(self):
        for n in self.messages:
            # if "to" in n.keys():
            print(n["content"])


ph = Phone("mynum")
ph.call("adina")
ph.call("Joe")
ph.call("SHmow")
ph.show_call_history()
ph.send_messages("adina", "Yo whats going on")
ph.send_messages("joe", "hey")
ph.send_messages("joe", "yo")
ph.send_messages("joe", "me")
ph.change_number("joe")
ph.send_messages("mynum", "heyo")
ph.show_sent_by()
ph.show_messages()
ph.show_sent_to()