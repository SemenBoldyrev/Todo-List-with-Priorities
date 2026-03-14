import unittest

from Controllers.TaskController import RemoveTask


class TestRemoveTask(unittest.TestCase):

    def test_remove_task_success(self):
        tasks = [
            {
                "id": 1,
                "description": "Complete project proposal",
                "priority": "High",
                "completed": False
            },
            {
                "id": 2,
                "description": "Complete project report",
                "priority": "Medium",
                "completed": True
            }
        ]

        removed_task = RemoveTask(tasks, 1)

        self.assertEqual(removed_task["id"], 1)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], 2)

    def test_remove_task_out_of_range(self):
        tasks = [
            {
                "id": 1,
                "description": "Complete project proposal",
                "priority": "High",
                "completed": False
            }
        ]

        with self.assertRaises(ValueError):
            RemoveTask(tasks, 99)

    def test_remove_task_invalid_id_type(self):
        tasks = [
            {
                "id": 1,
                "description": "Complete project proposal",
                "priority": "High",
                "completed": False
            }
        ]

        with self.assertRaises(TypeError):
            RemoveTask(tasks, "1")

    def test_remove_task_from_empty_list(self):
        tasks = []

        with self.assertRaises(ValueError):
            RemoveTask(tasks, 1)


if __name__ == "__main__":
    unittest.main()