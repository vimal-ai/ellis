"""
 Import python packages
"""
import chatbot
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time

""" 
GUI class contains everythig related to gui
"""
class GUI(tk.Tk):

    """
    Create & set window variables.
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Ellie")
        self.initialize()

    """ 
    Set window layout.
    """
    def initialize(self):

        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)

    """
        Get a response from the chatbot and display it.
    """
    def get_response(self):
        """ get response from textbox"""
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        """ get response from mic"""
        #user_input = chatbot.getAudio()
        #print("0")
        """ get response from chatbot """
        output = chatbot.chat(user_input)
        #print("1")
        self.conversation['state'] = 'normal'

        """ show oputput """
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + output + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)

# def main():
root = GUI()
root.mainloop()

# if __name__ == "__main__":
#     main()

