import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Scheduling Algorithms ----------------

def fcfs(processes):
    processes.sort(key=lambda x: x[1])
    n = len(processes)
    wt = [0]*n
    tat = [0]*n
    time = 0
    gantt = []

    for i, (pid, at, bt) in enumerate(processes):
        if time < at:
            time = at
        start = time
        time += bt
        gantt.append((pid, start, time))
        wt[i] = start - at
        tat[i] = time - at
    return wt, tat, gantt


def sjf(processes):
    n = len(processes)
    wt = [0]*n
    tat = [0]*n
    done = [False]*n
    time = 0
    completed = 0
    gantt = []

    while completed < n:
        idx = -1
        mn = float('inf')
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and not done[i] and bt < mn:
                mn = bt
                idx = i
        if idx == -1:
            time += 1
            continue
        pid, at, bt = processes[idx]
        start = time
        time += bt
        gantt.append((pid, start, time))
        wt[idx] = start - at
        tat[idx] = time - at
        done[idx] = True
        completed += 1
    return wt, tat, gantt


def srjf(processes):
    n = len(processes)
    remaining = [bt for _, _, bt in processes]
    wt = [0]*n
    tat = [0]*n
    time = 0
    completed = 0
    gantt = []
    last_pid = -1

    while completed < n:
        idx = -1
        mn = float('inf')
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and remaining[i] > 0 and remaining[i] < mn:
                mn = remaining[i]
                idx = i
        if idx == -1:
            time += 1
            continue

        pid, at, bt = processes[idx]
        if last_pid != pid:
            gantt.append([pid, time])
            last_pid = pid

        remaining[idx] -= 1
        time += 1

        if remaining[idx] == 0:
            tat[idx] = time - at
            wt[idx] = tat[idx] - bt
            completed += 1

    final_gantt = []
    for i in range(len(gantt)):
        pid, start = gantt[i]
        end = gantt[i+1][1] if i+1 < len(gantt) else time
        final_gantt.append((pid, start, end))
    return wt, tat, final_gantt


def round_robin(processes, quantum):
    n = len(processes)
    remaining = [bt for _, _, bt in processes]
    wt = [0]*n
    tat = [0]*n
    time = 0
    finished = 0
    ready = []
    arrived = [False]*n
    gantt = []

    while finished < n:
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and not arrived[i]:
                ready.append(i)
                arrived[i] = True

        if not ready:
            time += 1
            continue

        i = ready.pop(0)
        pid, at, bt = processes[i]
        exec_time = min(quantum, remaining[i])
        start = time
        time += exec_time
        gantt.append((pid, start, time))
        remaining[i] -= exec_time

        for j in range(n):
            pid2, at2, bt2 = processes[j]
            if at2 <= time and not arrived[j]:
                ready.append(j)
                arrived[j] = True

        if remaining[i] == 0:
            tat[i] = time - at
            wt[i] = tat[i] - bt
            finished += 1
        else:
            ready.append(i)
    return wt, tat, gantt


# ---------------- CFA Algorithm ----------------

def cfa(processes, quantum=1):
    n = len(processes)
    remaining = [bt for _, _, bt in processes]
    wt = [0]*n
    tat = [0]*n
    time = 0
    completed = 0
    gantt = []

    while completed < n:
        executed = False
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and remaining[i] > 0:
                executed = True
                start = time
                exec_time = min(quantum, remaining[i])
                time += exec_time
                remaining[i] -= exec_time
                gantt.append((pid, start, time))

                if remaining[i] == 0:
                    tat[i] = time - at
                    wt[i] = tat[i] - bt
                    completed += 1
        if not executed:
            time += 1
    return wt, tat, gantt


# ---------------- GUI ----------------

class CPUSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Simulator")
        self.processes = []

        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10)

        tk.Label(self.frame_input, text="Arrival Time (AT)   Burst Time (BT)").grid(row=0, column=0, columnspan=4)

        self.entries = []
        tk.Button(self.frame_input, text="Add Process", command=self.add_process_input).grid(row=1, column=0)
        tk.Button(self.frame_input, text="Run Scheduler", command=self.run_scheduler).grid(row=1, column=1)
        tk.Button(self.frame_input, text="Clear", command=self.clear_all).grid(row=1, column=2)

        self.algorithm_var = tk.StringVar(value="FCFS")
        tk.Label(self.frame_input, text="Algorithm:").grid(row=1, column=3)
        tk.OptionMenu(self.frame_input, self.algorithm_var,
                      "FCFS", "SJF", "SRJF", "Round Robin", "CFA").grid(row=1, column=4)

        tk.Label(self.frame_input, text="Quantum (RR):").grid(row=1, column=5)
        self.quantum_entry = tk.Entry(self.frame_input, width=5)
        self.quantum_entry.grid(row=1, column=6)

        self.frame_table = tk.Frame(root)
        self.frame_table.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_table,
                                 columns=("PID","AT","BT","WT","TAT"),
                                 show="headings")
        for col in ("PID","AT","BT","WT","TAT"):
            self.tree.heading(col, text=col)
        self.tree.pack()

        self.gantt_text = tk.Text(root, height=6)
        self.gantt_text.pack(pady=10)

    def add_process_input(self):
        pid = len(self.entries) + 1
        at_entry = tk.Entry(self.frame_input, width=5)
        at_entry.grid(row=2+len(self.entries), column=0)
        bt_entry = tk.Entry(self.frame_input, width=5)
        bt_entry.grid(row=2+len(self.entries), column=1)
        self.entries.append((pid, at_entry, bt_entry))

    def run_scheduler(self):
        self.processes.clear()
        for pid, at_entry, bt_entry in self.entries:
            try:
                at = int(at_entry.get())
                bt = int(bt_entry.get())
                self.processes.append((pid, at, bt))
            except:
                messagebox.showerror("Error", "Enter valid integers")
                return

        alg = self.algorithm_var.get()

        if alg == "FCFS":
            wt, tat, gantt = fcfs(self.processes)
        elif alg == "SJF":
            wt, tat, gantt = sjf(self.processes)
        elif alg == "SRJF":
            wt, tat, gantt = srjf(self.processes)
        elif alg == "Round Robin":
            try:
                quantum = int(self.quantum_entry.get())
            except:
                messagebox.showerror("Error", "Enter valid quantum")
                return
            wt, tat, gantt = round_robin(self.processes, quantum)
        elif alg == "CFA":
            wt, tat, gantt = cfa(self.processes)
        else:
            return

        for row in self.tree.get_children():
            self.tree.delete(row)

        for i, (pid, at, bt) in enumerate(self.processes):
            self.tree.insert("", "end", values=(pid, at, bt, wt[i], tat[i]))

        self.gantt_text.delete(1.0, tk.END)
        self.gantt_text.insert(tk.END, "Gantt Chart:\n")
        for pid, start, end in gantt:
            self.gantt_text.insert(tk.END, f"P{pid} [{start} → {end}]\n")

    def clear_all(self):
        for _, at_entry, bt_entry in self.entries:
            at_entry.destroy()
            bt_entry.destroy()
        self.entries.clear()
        self.tree.delete(*self.tree.get_children())
        self.gantt_text.delete(1.0, tk.END)


# ---------------- Run ----------------
root = tk.Tk()
app = CPUSchedulerApp(root)
root.mainloop()