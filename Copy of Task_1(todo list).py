{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"1SL55aIiMZRyajMi2KEvSUomejjTSN11P","timestamp":1707904617724},{"file_id":"10QHjRoHgu39ozhbm08p6Y1Ac5XejPwRV","timestamp":1707903691039},{"file_id":"1Lqi1SiS-c2zHXTCRDH1a2yApTFTs3ijn","timestamp":1707903562677}],"authorship_tag":"ABX9TyPBQcJUAE7z/xX5AEU7MwUU"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["class TodoList:\n","    def __init__(self):\n","        self.tasks = []\n","\n","    def add_task(self, task):\n","        self.tasks.append(task)\n","\n","    def delete_task(self, task_name):\n","        for task in self.tasks:\n","            if task['name'] == task_name:\n","                self.tasks.remove(task)\n","                return True\n","        return False\n","\n","    def display_tasks(self):\n","        if not self.tasks:\n","            print(\"No tasks in the list.\")\n","        else:\n","            for i, task in enumerate(self.tasks, 1):\n","                print(f\"{i}. {task['name']} - {task['description']}\")\n","\n","# Example usage\n","todo_list = TodoList()\n","\n","todo_list.add_task({\"name\": \"Task 1\", \"description\": \"Description of task 1\"})\n","todo_list.add_task({\"name\": \"Task 2\", \"description\": \"Description of task 2\"})\n","\n","todo_list.display_tasks()\n","\n","todo_list.delete_task(\"Task 1\")\n","\n","print(\"\\nAfter deleting Task 1:\\n\")\n","todo_list.display_tasks()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"nbcZR8LfC9Qq","executionInfo":{"status":"ok","timestamp":1707904596827,"user_tz":-330,"elapsed":536,"user":{"displayName":"Mahvish Azam","userId":"10901743372676544111"}},"outputId":"fe1c7481-7666-4e81-be7d-eff148ed9fe1"},"execution_count":2,"outputs":[{"output_type":"stream","name":"stdout","text":["1. Task 1 - Description of task 1\n","2. Task 2 - Description of task 2\n","\n","After deleting Task 1:\n","\n","1. Task 2 - Description of task 2\n"]}]}]}