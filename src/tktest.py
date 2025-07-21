import tkinter as tk
disp = 0
tt = 0
steps = 0
maximum = 0
dist = 0

root = tk.Tk()
root.geometry("800x600")
text_widget = tk.Text(root, wrap='word', height=20, width=80)
text_widget.insert(tk.END, "Displacement: " + str(disp)+" meters in " + str(tt)+" seconds \n")
text_widget.insert(tk.END, "Distance: " + str(dist) + " meters in " + str(tt)+" seconds \n" )
text_widget.insert(tk.END, "Steps: " + str(steps) +"\n")
text_widget.insert(tk.END, "Max: " + str(maximum) +"\n")
text_widget.pack(expand=True, fill='both')
root.mainloop()

