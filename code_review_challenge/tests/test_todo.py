from lib.todo import Todo
import pytest

"""
Given a task
I want to initialize it with string and boolean attributes
"""

def test_todo_initialized():
    todo = Todo("Mark this as done")
    assert todo.task == "Mark this as done"
    assert todo.complete == False

"""
Given a task
I want to mark a task as completed
"""

def test_mark_task_completed():
    todo = Todo("Mark this as done")
    todo.mark_complete()
    assert todo.complete == True

"""
Given an invalid task input
Reject the task from being created
"""

def test_invalid_task_type():
    with pytest.raises(Exception) as e:
        todo = Todo(False)
    result = str(e.value)
    assert result == "Task type is invalid, must be a string"
