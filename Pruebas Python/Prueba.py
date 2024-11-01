import tkinter as tk

class CustomDropdown(tk.Frame):
    def __init__(self, master, options):
        super().__init__(master, bg='cyan')
        self.options = options
        self.value = tk.StringVar()
        self.button = tk.Button(self, text="Seleccionar", command=self.toggle_options)
        self.button.pack()
        self.option_frame = None

    def toggle_options(self):
        if not self.option_frame or not self.option_frame.winfo_exists():
            self.show_options()
        else:
            self.hide_options()

    def show_options(self):
        if self.option_frame and self.option_frame.winfo_exists():
            self.option_frame.destroy()
        self.option_frame = tk.Toplevel(self)
        self.option_frame.configure(bg='red', highlightthickness=0)
        self.option_frame.wm_attributes('-alpha', 0.5)
        self.option_frame.overrideredirect(True)

        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.button.winfo_height()
        self.option_frame.geometry(f"200x100+{x}+{y}")

        self.listbox = tk.Listbox(self.option_frame, bg='red', highlightthickness=0)  # Cambia el color de fondo aquí
        for option in self.options:
            self.listbox.insert(tk.END, option)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def hide_options(self):
        if self.option_frame and self.option_frame.winfo_exists():
            self.option_frame.destroy()

    def on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.value.set(self.options[selection[0]])
            self.button.config(text=self.value.get())
        self.hide_options()

root = tk.Tk()
root.geometry("300x200")
root.configure(bg='cyan')

options = ["Opción 1", "Opción 2", "Opción 3"]
dropdown = CustomDropdown(root, options)
dropdown.pack(pady=20)

root.mainloop()

