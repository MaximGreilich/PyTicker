# Zweck der gui.py: Definiert die grafische Benutzeroberfläche der Anwendung mithilfe von Tkinter und
# verwaltet die Anzeige und Aktualisierung des Countdowns für die Aufgaben.

# Importieren der notwendigen Module
import tkinter as tk
from models import Task, parse_deadline_string, load_tasks_from_json, save_tasks

#


class AppGUI:
    def __init__(self, master):
        self.master = master
        # Zentrale Liste zur Speicherung der Aufgaben
        self.tasks = []

        # TKinter StringVar zur dynamischen Anzeige des Countdowns
        self.timer_display_var = tk.StringVar(value="00d 00h 00m 00s")
        self.title_var = tk.StringVar()
        self.date_var = tk.StringVar(value="YYYY-MM-DD")
        self.time_var = tk.StringVar(value="HH:MM")

        # Konfiguration des Timer-Labels(Große Schriftart, Farben)
        self.timer_label = tk.Label(
            self.master,
            textvariable=self.timer_display_var,
            font=("Arial", 40, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        self.timer_label.pack(pady=20, padx=10, fill=tk.X)

        # Widgets für die Aufgabeneingabe einrichten
        self.setup_input_widgets()

        # Startet den Timer-Update-Zyklus (ruft update_timer alle 1000 ms auf)
        self.update_timer()

    def add_task(self):
        # Wird beim Button-Klick aufgerufen, um eine neue Aufgabe hinzuzufügen
        task_title = self.title_var.get().strip()
        date_str = self.date_var.get().strip()
        time_str = self.time_var.get().strip()

        if not task_title:
            print("Error: Task title cannot be emptry")
            return
        deadline_dt = parse_deadline_string(date_str, time_str)

        if deadline_dt is None:
            print(
                f"Error: Invalid date or time format entered: {date_str}, {time_str}")
            return

            # Erstellen und Hinzufügen der neuen Aufgabe zur Aufgabenliste
            new_task = Task(title=task_title, deadline=deadline_dt)
            self.tasks.append(new_task)

            # Eingabefelder zurücksetzen
            self.date_var.set("YYYY-MM-DD")
            self.title_var.set("")

            print(f"Task added: {new_task.title} - Due: {new_task.deadline}")

    def get_closest_task(self):
        # Ermittelt die Aufgabe mit der nächsten Deadline
        active_tasks = [t for t in self.tasks if not getattr(
            t, 'completed', False)]
        if not active_tasks:
            return None

        active_tasks.sort(key=lambda task: task.deadline)
        return active_tasks[0]

    def update_timer(self):
        # Aktualisiert die Timer-Anzeige basierend auf der nächsten Aufgabe
        closest_task = self.get_closest_task()
        if closest_task:
            from models import get_time_remaining, format_timedelta
            time_remaining_td = get_time_remaining(closest_task.deadline)
            formatted_time = format_timedelta(time_remaining_td)
            self.timer_display_var.set(formatted_time)

            if time_remaining_td.total_seconds() <= 0:
                self.timer_label.config(bg="red")
            else:
                self.timer_label.config(bg="#2C3E50")
        else:

            self.timer_display_var.set("No Tasks Active")
            self.timer_label.config(bg="#3498DB")

        self.master.after(1000, self.update_timer)

    def setup_input_widgets(self):
        # Erstellt die Eingabefelder und den Button zum Hinzufügen von Aufgaben
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Task Title:").grid(
            row=0, column=0, padx=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.title_var, width=40).grid(
            row=0, column=1, columnspan=3, padx=5, pady=5)

        tk.Label(input_frame, text="Date:").grid(
            row=1, column=0, padx=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.date_var,
                 width=15).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Time:").grid(
            row=1, column=2, padx=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.time_var,
                 width=10). grid(row=1, column=3, padx=5, pady=5)

        tk.Button(
            self.master,
            text="➕ Add Task",
            command=self.add_task,
            bg="#27AE60", fg="white"
        ).pack(pady=10)

    def setup_task_list_widgets(self):
        self.list.container = tk.Frame(self.master, bg="#ECF0F1")
        self.list.container.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(
            self.list_container,
            height=8,
            selectmode=tk.SINGLE,
            font=("Arial", 12),
            bg="#ECF0F1",
            fg="#2C3E50",

        )

        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.list_container, orient=tk.VERTICAL)
        scrollbar.config(command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)

        tk.Button(
            self.master,
            text="✅ Mark as Done",
            command=self.mark).pack(pady=5)

    def delete_task(self):
        selected_indices = self.task_listbox.curselection()
        if not selected_indices:
            return

        selected_index = selected_indices[0]
        task_to_delete = self.tasks[selected_index]
        self.tasks.remove(task_to_delete)

        self.update_task_listbox()

    def mark_task_as_done(self):
        selected_indices = self.task_listbox.curselection()
        if not selected_indices:
            return

        selected_index = selected_indices[0]
        task_to_mark = self.tasks[selected_index]
        task_to_mark.completed = True

        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if getattr(task, 'completed', False) else "❌"
            self.task_listbox.insert(
                tk.END, f"{status} {task.title} - Due: {task.deadline}")

    def on_closing(self):
        from models import save_tasks_to_json  # Import hier oder oben machen
        save_tasks_to_json(self.tasks)
        self.master.destroy()
