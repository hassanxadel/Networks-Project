from tkinter import messagebox
import registry  # Import functions/classes from registry.py
import peer  # Import functions/classes from peer.py
import db  # Import functions/classes from db.py
import tkinter as tk

class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Peer-to-Peer Chat App")
        self.logged_in = False
        self.create_login_widgets()

    def create_login_widgets(self):
        # Login UI elements
        self.label_username = tk.Label(self.root, text="Username:")
        self.entry_username = tk.Entry(self.root)
        self.label_password = tk.Label(self.root, text="Password:")
        self.entry_password = tk.Entry(self.root, show="*")
        self.btn_login = tk.Button(self.root, text="Login", command=self.login)

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.btn_login.pack()

    def login(self):
        # Authentication logic (placeholder)
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if db.authenticate_user(username, password): 
            messagebox.showinfo("Login", "Login successful")
            self.logged_in = True

        if self.logged_in:
            self.create_main_widgets()

    def create_main_widgets(self):
        # Main window after login
        self.root.withdraw()  # Hide the login window
        self.main_window = tk.Toplevel()
        self.main_window.title("Main Menu")

        # Buttons for functionalities
        self.btn_one_to_one_chat = tk.Button(self.main_window, text="One-to-One Chat", command=self.one_to_one_chat)
        self.btn_create_room = tk.Button(self.main_window, text="Create Room", command=self.create_room)
        self.btn_join_room = tk.Button(self.main_window, text="Join Room", command=self.join_room)

        self.btn_one_to_one_chat.pack()
        self.btn_create_room.pack()
        self.btn_join_room.pack()
        self.btn_logout = tk.Button(self.main_window, text="Logout", command=self.logout)
        self.btn_logout.pack()
        
    def one_to_one_chat(self):
        # Call function from peer.py for one-to-one chat
        peer_name = "ExampleUser"  # Get peer name from UI input
        message = "Hello!"  # Get message from UI input
        response = peer.send_message(peer_name, message)  # Example function call (not implemented)
        messagebox.showinfo("One-to-One Chat", response)

    def create_room(self):
        # Call function from registry.py to create a room
        room_name = "Example Room"  # Get room name from UI input
        response = registry.create_room(room_name)  # Example function call (not implemented)
        messagebox.showinfo("Create Room", response)

    def join_room(self):
        # Call function from registry.py to join a room
        room_name = "Example Room"  # Get room name from UI input
        response = registry.join_room(room_name)  # Example function call (not implemented)
        messagebox.showinfo("Join Room", response)
    def logout(self):
        self.logged_in = False
        if hasattr(self, 'main_window'):  # Check if the main window exists
            self.main_window.destroy()  # Destroy the main window if it exists
        self.root.deiconify()  # Show the login window again
        self.create_login_widgets()  # Recreate login widgets

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ChatApp()
    app.start()
