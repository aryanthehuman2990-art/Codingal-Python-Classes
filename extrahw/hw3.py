from datetime import date

PRIORITY = {"high": 1, "medium": 2, "low": 3}


class TaskScheduler:

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title, priority="medium", due=None):
        priority = priority.lower()
        if priority not in PRIORITY:
            print(f"Error: '{priority}' is not a valid priority. Choose from {list(PRIORITY)}.")
            return

        task = {
            "id": self._next_id,
            "title": title,
            "priority": priority,
            "due": due if due is not None else date.today(),
            "done": False,
        }
        self.tasks.append(task)
        print(f"Added task #{task['id']}: '{title}' (priority: {priority})")
        self._next_id += 1

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                print(f"Task #{task_id} ('{task['title']}') marked as complete.")
                return
        print(f"Task #{task_id} not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        print(f"Task #{task_id} deleted (if it existed).")

    def pending_tasks(self):
        return [t for t in self.tasks if not t["done"]]

    def display(self, tasks=None, title="All Tasks"):
        if tasks is None:
            tasks = self.tasks

        if not tasks:
            print(f"\n{title}: no tasks to show.")
            return

        sorted_tasks = sorted(tasks, key=lambda t: (PRIORITY[t["priority"]], t["due"]))

        print(f"\n{title}")
        print(f"{'ID':<4}{'Title':<20}{'Priority':<10}{'Due':<12}{'Status'}")
        print("-" * 56)
        for t in sorted_tasks:
            status = "✓ Done" if t["done"] else "Pending"
            print(f"{t['id']:<4}{t['title']:<20}{t['priority']:<10}{str(t['due']):<12}{status}")

    def filter_by_priority(self, priority):
        priority = priority.lower()
        filtered = [t for t in self.tasks if t["priority"] == priority]
        self.display(filtered, title=f"Tasks with priority: {priority}")

    def overdue_tasks(self):
        today = date.today()
        overdue = [t for t in self.tasks if not t["done"] and t["due"] < today]
        self.display(overdue, title="Overdue Tasks")

    def summary(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        print(f"\n{done}/{total} tasks completed")



if __name__ == "__main__":

    scheduler = TaskScheduler()

    scheduler.add_task("Finish project report", "high", date(2026, 6, 25))
    scheduler.add_task("Buy groceries", "low", date(2026, 8, 30))
    scheduler.add_task("Prepare presentation slides", "high", date(2026, 8, 20))
    scheduler.add_task("Read a book chapter", "low")
    scheduler.add_task("Fix bug in login page", "medium", date(2026, 8, 10))

    scheduler.display()

    scheduler.complete_task(1)
    scheduler.complete_task(3)

    scheduler.filter_by_priority("high")

    scheduler.overdue_tasks()

    scheduler.summary()