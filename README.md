# 🖥️ CPU Scheduling Simulator

An interactive **GUI-based desktop application** designed to simulate and compare classical CPU scheduling algorithms. This project helps students and learners understand how different scheduling strategies impact CPU utilization, responsiveness, and fairness through **visualization and metrics**.

---

## 📌 Problem Statement

Traditional CPU scheduling algorithms often favor either **early-arriving processes** or **shorter jobs**, which can result in:

* Unfair CPU allocation
* Process starvation
* Poor responsiveness for long or late-arriving processes

There is a strong need for a system that:

* Allows **comparison of multiple scheduling algorithms**
* Demonstrates how **fair scheduling** (using CFA – Completely Fair Algorithm) improves CPU utilization and system fairness

---

## 🎯 Objectives

* Implement and compare **classical CPU scheduling algorithms**
* Visualize process execution using **Gantt Charts**
* Demonstrate fairness in scheduling using **Completely Fair Algorithm (CFA)**
* Help students understand **Operating System scheduling concepts** through interaction and visualization

---

## 🔍 Scope of the Project

### ✔️ Included Features

The simulator supports the following CPU scheduling algorithms:

* **FCFS (First Come First Serve)**
* **SJF (Shortest Job First)**
* **SRJF (Shortest Remaining Job First)**
* **Round Robin**
* **CFA (Completely Fair Algorithm)**

For each algorithm, the system calculates:

* ⏳ **Waiting Time (WT)**
* 🔄 **Turnaround Time (TAT)**

Additional features:

* 📊 **Gantt Chart visualization** for process execution
* 🖱️ **GUI-based desktop application** for easy interaction

---

## 🚫 Out of Scope

The following features are not covered in this project:

* ❌ Real **kernel-level CPU scheduling**
* ❌ **Multi-core CPU** simulation

---

## 📊 Output & Visualization

* Algorithm-wise comparison of performance metrics
* Gantt charts showing process execution order
* Clear visualization of how CFA distributes CPU time fairly among processes

---

## 🧠 Key Learning Outcomes

* Understand the strengths and weaknesses of different CPU scheduling algorithms
* Observe how starvation occurs in FCFS and SJF
* Learn how CFA ensures **fair CPU distribution**
* Gain hands-on experience with scheduling concepts used in Operating Systems

---
## Outputs.

## FCFS

![WhatsApp Image 2026-01-07 at 4 29 29 PM](https://github.com/user-attachments/assets/dd5dc7aa-c58e-4710-8ccc-334aad676b23)

## SJF

<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/93608151-3d92-4388-982a-b2aadb564cab" />

## SRJF

<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/400ca04b-9a7d-48e9-98c3-062f2de7aa10" />

## Round Robin

<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/4f8b2924-b5bf-4e81-a2b2-667bdbe5bc24" />

## CFS

<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/48b57429-5327-4a8c-8bca-cb5c0f40873e" />


## ✅ Conclusion

The **CPU Scheduling Simulator** successfully demonstrates how different scheduling algorithms affect overall system performance. While algorithms like **FCFS** and **SJF** may cause starvation, the **Completely Fair Algorithm (CFA)** ensures equitable CPU allocation among processes.

By combining **performance metrics** and **visual Gantt charts**, this project significantly enhances the understanding of CPU scheduling concepts through interaction and visualization.

---

## 🚀 Future Enhancements (Optional)

* Multi-core CPU scheduling simulation
* Real-time process arrival handling
* Export results as reports
* Web-based version of the simulator

---

📌 *This project is ideal for students studying Operating Systems and CPU scheduling concepts.*
