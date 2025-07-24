import tkinter as tk

def getInformation():
    stride1 = stride.get()
    show_information.config(text="output"+stride1)

window = tk.Tk()
window.configure( bg="#c7e3c1")
window.title("UI")
window.geometry("500x350")
frame = tk.Frame(bg="#c7e3c1")

info_frame = tk.Frame(window)
info_frame.grid(row=1, column=1, columnspan=3, padx=100, pady=15, )

stride_label = tk.Label(info_frame, text="Enter Stride Length: ")
stride_label.grid(row=0, column=0, padx=5, pady=5)

stride = tk.Entry(info_frame)
stride.grid(row=0, column=1, padx=5, pady=5)

get_info = tk.Button(info_frame, text="Show output", command = getInformation)
get_info.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

show_information = tk.Label(font='serif', bg="#c7e3c1", fg="#3b3e45")
show_information.grid(row=2, column=2, pady=7, padx=10)

window.mainloop()

# outputs
#text_widget.insert(tk.END, "Distance: " + str(dist) + " meters in " + str(tt)
                #+ " seconds \n")
#text_widget.insert(tk.END, "Steps: " + str(steps) + "\n\n")
#text_widget.pack(expand=True, fill='both')
#root.mainloop()
#intiialise output window_height
#root = tk.Tk()
#root.geometry("500x350")
#text_widget = tk.Text(root, wrap='word', height=20, width=80,
#                      font='serif', bg="#c7e3c1", fg="#3b3e45")
