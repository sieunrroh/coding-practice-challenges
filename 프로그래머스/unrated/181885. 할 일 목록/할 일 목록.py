def solution(todo_list, finished):
  
    unfinished_tasks = [task for task, is_finished in zip(todo_list, finished)       if not is_finished]
    return unfinished_tasks

