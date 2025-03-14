version = "1.0.0-alpha"

import tkinter as tk
import time
import subprocess as sp

user = "user"


def startup():
    message = greeting() + ", " + user + ". it's currently "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+" what do you want to do?"
    return message


def greeting():
    if time.localtime().tm_hour < 5:
        greet = "Good Morning"
    elif time.localtime().tm_hour < 12:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"
    return greet

def on_classworkbutton_clicked():
    #profile_directory is r"C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data" !!!
    profile_name = "Profile 1"
    sp.run([r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            f"--profile-directory={profile_name}",
            "https://classroom.google.com/a/not-turned-in/all"])


def show_output():
    global root

    root = tk.Tk()
    root.title("Python Output")
    root.attributes('-fullscreen', True)
    root.config(bg="#808080")

    defaulttext_color = "white"
    defaultbutton_color = "#808080"
    defaulttext_font = "Comic Sans MS"

    message = startup()
    greet = tk.Label(root, text=message, padx=20, pady=20, font=(defaulttext_font, 20))
    greet.pack()

    version_label = tk.Label(root,text=version, fg=defaulttext_color , bg=defaultbutton_color, font=(defaulttext_font, 20))
    version_label.pack(side="bottom", anchor="w",)


    exit_button = tk.Button(root, text="Exit", command=root.destroy, fg=defaulttext_color, bg=defaultbutton_color, font=(defaulttext_font, 20))
    exit_button.pack(side="bottom", anchor="se", padx=10, pady=10)

    classwork_button = tk.Button(root, text="Track your homework (launch google)" ,command=on_classworkbutton_clicked, fg=defaulttext_color,bg=defaultbutton_color, font=(defaulttext_font, 20))
    classwork_button.pack(padx=20,pady=20)
    root.mainloop()


if __name__ == "__main__":
    show_output()