from tasktracker import TaskTracker
import unittest
from datetime import date


class TestTaskTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = TaskTracker(":memory:", "tasks")
        self.tracker.check()

    def test_add_and_list_task(self):
        self.tracker.add("Test Task 1")
        self.tracker.add("Test Task 2", due_date=date(2024, 12, 31).isoformat())
        tasks = self.tracker.list_task()
        self.assertEqual(len(tasks), 2)
        self.assertIn(("Test Task 1", date.today().isoformat(), 0), tasks)
        self.assertIn(("Test Task 2", date(2024, 12, 31).isoformat(), 0), tasks)

    def test_check_creates_table(self):
        # The check method should create the table if it doesn't exist
        result = self.tracker.check()
        self.assertTrue(result)
        # Verify that the table exists by adding a task
        try:
            self.tracker.add("Test Task 3")
            tasks = self.tracker.list_task()
            self.assertIn(("Test Task 3", date.today().isoformat(), 0), tasks)
        except Exception as e:
            self.fail(f"Table creation failed with exception: {e}")


if __name__ == "__main__":
    unittest.main()
