from lib.todo_list import TodoList
from lib.todo import Todo
import pytest

"""
As a user
Given I want to track a list of things I need to do
I want to initialize a list
"""

def test_todo_list_initialised():
    tl = TodoList()
    assert tl.todo_list == []

"""
As a user
Given I want to add a task to the todo_list
Add an instance of Todo to the list
"""

def test_add_todo_to_todo_list():
    tl = TodoList()
    todo = Todo("Do groceries")
    tl.add(todo)
    assert tl.todo_list[0].task == todo.task
    assert tl.todo_list[0].complete == False

def test_add_multiple_todos_to_todo_list():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    todo_B = Todo("Wash dishes")
    tl.add(todo_A)
    assert tl.todo_list == [todo_A]
    tl.add(todo_B)
    assert tl.todo_list == [todo_A, todo_B]

"""
Given a list of todos
I want to see a list of incomplete todos
Show a list of todos where complete is False
"""

def test_show_incomplete_todos_where_only_incomplete_todos_exist():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    tl.add(todo_A)
    todo_B = Todo("Wash dishes")
    tl.add(todo_B)
    todo_C = Todo("Do laundry")
    tl.add(todo_C)
    todo_D = Todo("Mop floor")
    tl.add(todo_D)

    assert tl.incomplete() == [todo_A, todo_B, todo_C, todo_D]


def test_show_incomplete_todos_where_complete_varies():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    tl.add(todo_A)
    todo_B = Todo("Wash dishes")
    tl.add(todo_B)
    todo_C = Todo("Do laundry")
    tl.add(todo_C)
    todo_D = Todo("Mop floor")
    tl.add(todo_D)

    todo_C.mark_complete()

    assert todo_C.complete == True

    assert tl.incomplete() == [todo_A, todo_B, todo_D]

"""
Given a list of todos
I want to see a list of complete todos
Show a list of todos where complete is True
"""

def test_show_complete_todos_where_only_complete_todos_exist():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    tl.add(todo_A)
    todo_B = Todo("Wash dishes")
    tl.add(todo_B)
    todo_C = Todo("Do laundry")
    tl.add(todo_C)
    todo_D = Todo("Mop floor")
    tl.add(todo_D)

    todo_A.mark_complete()
    todo_B.mark_complete()
    todo_C.mark_complete()
    todo_D.mark_complete()

    assert tl.complete() == [todo_A, todo_B, todo_C, todo_D]

def test_show_all_complete_todos_where_complete_varies():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    tl.add(todo_A)
    todo_B = Todo("Wash dishes")
    tl.add(todo_B)
    todo_C = Todo("Do laundry")
    tl.add(todo_C)
    todo_D = Todo("Mop floor")
    tl.add(todo_D)

    todo_A.mark_complete()
    todo_D.mark_complete()

    assert tl.complete() == [todo_A, todo_D]

"""
Given a list of todos
I want to give up for all todos
Set up all todos to be completed
"""

def test_change_all_todos_to_be_complete_where_all_start_incomplete():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    tl.add(todo_A)
    todo_B = Todo("Wash dishes")
    tl.add(todo_B)
    todo_C = Todo("Do laundry")
    tl.add(todo_C)
    todo_D = Todo("Mop floor")
    tl.add(todo_D)

    assert tl.complete() == []
    tl.give_up()
    assert tl.complete() == [todo_A, todo_B, todo_C, todo_D]

def test_change_all_todos_to_be_complete_where_complete_varies():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    tl.add(todo_A)
    todo_B = Todo("Wash dishes")
    tl.add(todo_B)
    todo_C = Todo("Do laundry")
    tl.add(todo_C)
    todo_D = Todo("Mop floor")
    tl.add(todo_D)

    todo_B.mark_complete()
    todo_D.mark_complete()

    assert tl.complete() == [todo_B, todo_D]
    tl.give_up()
    assert tl.complete() == [todo_A, todo_B, todo_C, todo_D]

"""
Given two todos with the exact same task
I want there to only be one of any one task
Only the first one is added to the list
"""

def test_add_two_todos_with_same_task():
    tl = TodoList()
    todo_A = Todo("Do groceries")
    todo_B = Todo("Do groceries")

    tl.add(todo_A)
    with pytest.raises(Exception) as e:
        tl.add(todo_B)
    result = str(e.value)
    assert result == "This task already exists"
