import tkinter as tk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.root.configure(bg="#f0f0f0")  # Set background color for the main window

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")  # Green color for add button
        self.add_button.pack(pady=5)

        self.task_list_frame = tk.Frame(root, bg="#f0f0f0")  # Set background color for the task list frame
        self.task_list_frame.pack(pady=10)

        self.task_list = tk.Listbox(self.task_list_frame, width=40, selectmode=tk.MULTIPLE, bg="#FFFFE0")  # Yellow color for task list
        self.task_list.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete, bg="#008CBA", fg="white")  # Blue color for complete button
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_selected, bg="#f44336", fg="white")  # Red color for delete button
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for i, task_info in enumerate(self.tasks, start=1):
            task = task_info["task"]
            completed = task_info["completed"]
            task_text = f"{i}. {task} "
            if completed:
                task_text += "✔"
            self.task_list.insert(tk.END, task_text)

    def mark_complete(self):
        selected_indices = self.task_list.curselection()
        for index in selected_indices:
            self.tasks[index]["completed"] = True
        self.update_task_list()

    def delete_selected(self):
        selected_indices = self.task_list.curselection()
        for index in selected_indices[::-1]:  # Deleting in reverse order to avoid index shifting
            del self.tasks[index]
            self.task_list.delete(index)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
