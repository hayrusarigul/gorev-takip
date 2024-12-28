import unittest
from io import StringIO
import sys
import os

# Oluşturulan dosya adı
FileName = "test_task.txt"

# Görev ekleme işlevini test et
def taskAdd(task):
    with open(FileName, "a") as file:
        file.write(task + "\n")

# Görev silme işlevini test et
def taskDelete(index):
    with open(FileName, "r") as file:
        tasks = file.readlines()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        with open(FileName, "w") as file:
            file.writelines(tasks)

# Görev tamamlama işlevini test et
def taskComplete(index):
    with open(FileName, "r") as file:
        tasks = file.readlines()
    if 0 <= index < len(tasks):
        tasks[index] = "X " + tasks[index]
        with open(FileName, "w") as file:
            file.writelines(tasks)

# Unit test sınıfı
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Test dosyasını oluştur
        with open(FileName, "w") as file:
            file.write("Görev 1\nGörev 2\n")

    def tearDown(self):
        # Test dosyasını temizle
        os.remove(FileName)

    def test_taskAdd(self):
        taskAdd("Görev 3")
        with open(FileName, "r") as file:
            tasks = file.readlines()
        self.assertEqual(len(tasks), 3)

    def test_taskDelete(self):
        taskDelete(0)
        with open(FileName, "r") as file:
            tasks = file.readlines()
        self.assertEqual(len(tasks), 1)

    def test_taskComplete(self):
        taskComplete(0)
        with open(FileName, "r") as file:
            tasks = file.readlines()
        self.assertTrue(tasks[0].startswith("X "))

if __name__ == "__main__":
    unittest.main()
