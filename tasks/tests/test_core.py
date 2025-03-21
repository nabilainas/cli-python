import os, json, unittest

from tasks.task_manager.core import add_task, load_tasks, delete_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tasks_file = "test_tasks.json"
        os.environ["TASKS_FILE_PATH"] = self.tasks_file
        with open(self.tasks_file, 'w') as file:
            json.dump([], file)

    def tearDown(self):
        os.remove(self.tasks_file)

    def test_add_task(self):
        add_task("Test Task", 1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test Task")
        self.assertEqual(tasks[0]['priority'], 1)

    def test_delete_task(self):

        tasks = load_tasks()
        print("Before deletion:", tasks)
        for task in tasks:
            delete_task(task['id'])

        tasks = load_tasks()
        print("After deletion:", tasks) 

        self.assertEqual(len(tasks), 0)  


if __name__ == "__main__":
    unittest.main()