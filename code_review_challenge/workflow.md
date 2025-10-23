# WORKFLOW.MD

## NB: When a test passes, a number in brackets will show how many have passed in total. 

```python
"""
As a user
Given I want to track a list of things I need to do
I want to initialize a list
"""
```

## 1 - Add test implementation 
Result: Failed -> "TodoList" doesn't exist\
Action: Import "TodoList"

## 2 - Import "TodoList"
Result: Failed -> "TodoList" object has no attribute "todo_list"\
Action: Add attribute "todo_list"

## 3 - Add Attribute "todo_list"
Result: Failed -> None =/= []\
Action: Initialize attribute todo_list = []

## 4 - Initialize attribute "todo_list" = []
Result: Test Passed (1)

```python
"""
As a user
Given I want to add a task to the todo_list
Add an instance of Todo to the list
"""
```

## 1 - Add test implementation 
Result: Failed -> "Todo" doesn't exist\
Action: Import "Todo" from lib.todo

## 2 - Import "Todo" from lib.todo
Result: Failed -> [] =/= [{"task": "Do groceries", "complete": False}]\
Action: Append Todo to todo_list

## 3 - Append Todo to todo_list
Result: Failed -> "Todo" object has no attribute "task"\
Action: Add "task" attribute and set to required string

## 4 - Add "task" attribute to "Todo" and set to required string 
Result: Failed -> "Todo" object has no attribute "complete"\
Action: Add "complete" attribute and set to False

## 5 - Add "complete" attribute to "Todo" and set to False 
Result: Test Passed (2)\
Action: Add second test case with multiple unique values

## 6 - Add second test case with multiple unique values
Result: Failed -> Second value missing\
Action: Replace required string with new string

## 7 - Replace required string with new string
Result: Test Passed, however the previous test failed -> Second value is extra\
Action: Replace required string with passed in parameter

## 8 - Replace required string with passed in parameter
Result: Both Tests Pass (3)

```python
"""
Given a list of todos
I want to see a list of incomplete todos
Show a list of todos where complete is False
"""
```

## 1 - Add test implementation
Result: Failed -> None =/= [list of four todo dictionaries]\
Action: Return required list of todos

## 2 - Return required list of todos
Result: Test Passed (4)\
Action: Add second test case implementation

## 3 - Add second test case implementation
Result: Failed -> [list of four todo dictionaries] =/= [list of three todo dictionaries]\
Action: Set incomplete() to return the required list

## 4 - Set incomplete() to return the required list
Result: Test Passed, however previous test failed -> [three todo dictionaries] =/= [four todo dictionaries]\
Action: Have incomplete() filter by complete: False in each dictionary

## 5 - Have incomplete() filter by complete: False in each dictionary
Result: Previous test passed, current test failed -> [four todo dictionaries] =/= [three todo dictionaries]\
Action: Add implementation for todo.mark_complete()

## 6 - Add implemenation for todo.mark_complete()
```python
"""
Given a task
I want to initialize it with string and boolean attributes
"""

"""
Given a task
I want to mark a task as completed
"""
```

### 6a - Add initializer unit test in todo.py
Result: Failed -> "Todo" doesn't exist\
Action: Import "Todo" class

### 6b - Import "Todo" class
Result: Test Passed (5)\
Action: Add new test case for marking as complete

### 6c - Add new test case for marking as complete
Result: Failed -> False =/= True\
Action: Set todo.complete = true

### 6d - Set todo.complete = true
Result: Test Passed (6)\
Action: Re-test # 5 to see if any changes since last attempt

## 7 - Re-test #5 to see if any change from last attempt
Result: Failed -> [four todo dictionaries] =/= [three todo dictionaries]\
Action: Refactor to not use dictionaries

## 8 - Refactor to not use dictionaries
Result: Test Passed (7)

```python
"""
Given a list of todos
I want to see a list of complete todos
Show a list of todos where complete is True
"""
```

## 1 - Add test implementation
Result: Failed -> None =/= [four todo objects]\
Action: Return the list of todo objects

## 2 - Return the list of todo objects
Result: Test Passed (8)\
Action: Add second test case implementation

## 3 - Add second test case implementation
Result: Failed -> Four todo objects =/= Two todo objects\
Action: Add filter for complete todos

## 4 - Add filter for complete todos
Result: Test Passed (9)

```python
"""
Given a list of todos
I want to give up for all todos
Set up all todos to be completed
"""
```

## 1 - Add test implementation
Result: Failed -> Empty list =/= Four todo objects\
Action: Set all instances of todo.complete to True

## 2 - Set all instances of todo.complete to True
Result: Test Passed (10)\
Action: Add second test case implementation

## 3 - Add second test case implementation
Result: Test Passed (11)\
Action: Refactor existing code to use proper logic

## 4 - Refactor existing code to use proper logic
Result: Unchanged

```python
"""
Given two todos with the exact same task
I want there to only be one of any one task
Only the first one is added to the list
"""
```

## 1 - Add test implementation
Result: Failed -> pytest doesn't exist\
Action: Import Pytest

## 2 - Import Pytest
Result: Failed -> No Exception Raised\
Action: Raise Exception if task is in the list of existing tasks

## 3 - Raise Exception if task is in the list of existing tasks
Result: Passed (12)

```python
"""
Given an invalid task input
Reject the task from being created
"""
```

## 1 - Add test implementation
Result: Failed -> pytest doesn't exist\
Action: Import pytest

## 2 - Import pytest
Result: Failed -> No Exception raised\
Action: Raise exception when task type is not string

## 3 - Raise exception when task type is not string
Result: Test Passed (13)