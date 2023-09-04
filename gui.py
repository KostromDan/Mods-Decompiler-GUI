import tkinter
from tkinter import ttk


class ProgressWindow:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Progress")
        self.root.geometry("500x250")
        self.tasks = {}

        self.do_merge = None
        self.copy_assets = None

        self.create_widgets()

    def create_widget(self, name):
        frame = tkinter.Frame(self.root)
        frame.pack(pady=20)
        self.frames[name] = frame

        label = tkinter.Label(frame, text=f"{name}:")
        label.grid(row=0, column=0, padx=10)

        progress_bar = ttk.Progressbar(frame, length=200, mode="determinate")
        progress_bar.grid(row=1, column=0, padx=10)

        text_label = tkinter.Label(frame, text="")
        text_label.grid(row=2, column=0)

        self.progress_bars[name] = progress_bar
        self.text_labels[name] = text_label

    def create_widgets(self):
        self.frames = {}
        self.progress_bars = {}
        self.text_labels = {}
        self.create_widget("Progress")
        self.create_widget("Task")

    def update_progress(self, task_id, progress_value):
        self.tasks[task_id] = progress_value
        self.root.after(100, self.update_ui)

    def update_text(self, task_id, text):
        self.text_labels[task_id]["text"] = text

    def update_ui(self):
        for task_id, progress_value in self.tasks.items():
            self.progress_bars[task_id]["value"] = progress_value
            self.progress_bars[task_id]["maximum"] = 100
            self.progress_bars[task_id].update()
            self.progress_bars[task_id].update_idletasks()

    def start(self):
        self.root.mainloop()

    def create_warn_window(self, text):
        window = tkinter.Toplevel(self.root)
        window.title("Warn")

        def destroy():
            window.destroy()
            self.root.lift()

        label = tkinter.Label(window, text=text)
        label.pack()

        ok_button = tkinter.Button(window, text="OK", command=destroy)
        ok_button.pack()

    def merge_mods_ask(self):
        window = tkinter.Toplevel(self.root)
        window.title("Merge Mods")

        def merge_mods():
            window.destroy()
            self.root.lift()
            self.do_merge = True
            self.copy_assets = var.get()

        def dont_merge_mods():
            window.destroy()
            self.root.lift()
            self.do_merge = False

        label = tkinter.Label(window, text="Do you want to merge all mods into mdk?\n"
                                           "If you will open result folder as project in ide, indexing won't work correct.\n"
                                           "So, implementation, declaration, usages buttons won't work.\n"
                                           "This action attempts to fix this, merging all mods into mdk.\n"
                                           "As result, you will be able to see minecraft, minecraftforge, mods source code. \n"
                                           "And implementation, declaration, usages, etc ide buttons will work correct in 99% cases.")
        label.pack(pady=20)

        var = tkinter.IntVar()

        copy_assets_checkbox = tkinter.Checkbutton(window, text="Copy assets?",variable=var)
        copy_assets_checkbox.select()
        copy_assets_checkbox.pack()

        yes_button = tkinter.Button(window, text="Yes", command=merge_mods)
        no_button = tkinter.Button(window, text="No", command=dont_merge_mods)

        yes_button.pack(padx=10, pady=10, side=tkinter.LEFT)
        no_button.pack(padx=10, pady=10, side=tkinter.RIGHT)

    def update_progress_value(self, progress_value):
        self.update_progress("Progress", progress_value)

    def update_progress_text(self, text):
        self.update_text("Progress", text)

    def update_task_value(self, progress_value):
        self.update_progress("Task", progress_value)

    def update_task_text(self, text):
        self.update_text("Task", text)

    def destroy(self):
        self.root.destroy()
