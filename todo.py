import os
import json
import subprocess
from pathlib import Path
from typing import Any, Dict

"""
{
    "work":{
        "1": {
            "name": "Test 1",
            "status": "completed"
        }
    }
    
}
"""
# add task 'Category'
def get_cmd(todo : dict[str, Any], prompt : str):
    # add category Task
    # list category
    # delete category id

    try:
        if not prompt :
            print("Error - Command incorrect")
            return (None, None, None)
        
        prompt_list = prompt.split(" ")

        cmd = prompt_list[0]
        available_prompt = ['add', 'delete', 'list', 'quit', 'help', 'category', 'clear', 'done']
        
        if cmd not in available_prompt:
            print("Error. Type 'help' to see available command.")
            return (None, None, None)
        
        if cmd == 'quit':
            return (cmd, None, None)
        if cmd == 'help' :
            return (cmd, None, None)
        if cmd == "clear":
            return (cmd, None, None)
        
        # list or list category
        if cmd == 'list':
            if not prompt_list[1:]:
                return (cmd, None, None)
            else:
                category = prompt_list[1]
                if category not in todo.keys():
                    print(f"{category} is not in your todo categories")
                    return (None, None, None)
                
                if prompt_list[2:]:
                    print("Invalid command")
                    return (None, None, None)
            return (cmd, category, None)
        
        # done category id
        # delete category ID
        if cmd == 'done' or cmd == 'delete':
            if not prompt_list[1:]:
                print("Invalid command. Missing category and ID")
                return (None, None, None)
            else:
                category = prompt_list[1]
                if category not in todo.keys():
                    print(f"{category} is not in your todo categories")
                    return (None, None, None)
                
                if not prompt_list[2:]:
                    print("Invalid command. Missing ID")
                    return (None, None, None)
                else :
                    id = prompt_list[2]
                
                if prompt_list[3:]:
                    print("Invalid command")
                    return (None, None, None)
        
            return (cmd, category, id)
        
        # add category Task
        if cmd == 'add':
            if not prompt_list[1:]:
                print("Invalid command. Missing category and Task")
                return (None, None, None)
            else :
                category = prompt_list[1]
                if category not in todo.keys():
                    print(f"{category} not in your todo category")
                    return (None, None, None)
                if not prompt_list[2:]:
                    print("Invalid command. Missing Task")
                    return (None, None, None)
                else:
                    task_list = prompt_list[2:]

                    if len(task_list[0]) < 2:
                        print("Invalid task")
                        return (None, None, None)
                    
                    task = task_list[0]
                    
                    if task_list[1:] :
                        
                        for word in task_list[1:]:
                            task = task + " " + word
                    
            return (cmd, category, task)
        
        if cmd == 'category':
            return (cmd, None, None)
        
    except Exception as e:
        print(f"Error get_cmd {e}")
        return (None, None, None)

def manage_cmd(todo: dict[str, Any], cond : bool = True):
    while cond:

        prompt = prompt_input()
        if not prompt: continue

        try :
            c, x, e = get_cmd(todo, prompt)

            if not c :
                continue

            if c == 'help':
                help()
                continue

            if c == 'quit' :
                save(todo)
                clear_screen()
                break

            if c == 'add':
                if x != None and e != None:
                    category, task = x, e
                    added = add(todo, category, task)

                    if not added : continue
                    todo = added
                else: continue
                
            if c == 'list':
                if not todo:
                    print("Nothing")
                    continue
                if x == None :
                    x = 'all'
                lists(todo, x)
            
            if c == 'delete':
                ret = delete(todo, x, e)
                if not ret :
                    continue
                todo = ret
            
            if c == "category":
                prompt_list = prompt.split(" ")
                cat = cmd_category(todo, prompt_list)
                if not cat:
                    continue
                todo = cat
            
            if c == 'done':
                do = done(todo, x,e)
                if not do : continue
                todo = do
            
            if c == "clear":
                clear_screen()
                continue

            
        except KeyboardInterrupt:
            continue
        except Exception :
            continue


def help() -> None:
    """
    Print the contents of ``help.txt`` if it exists, otherwise show a fallback message.
    """
    clear_screen()
    help_path = Path("help.txt")
    if help_path.is_file():
        # ``Path.read_text`` handles opening/closing for us.
        print(help_path.read_text(encoding="utf-8"))
    else:
        print("Help not available!")

def save(data: Dict[str, Any], file: str = "todos.json") -> None:
    """
    Persist *data* as pretty‑printed JSON.

    Args:
        data: Mapping that will be serialised.
        file: Destination filename (defaults to ``todo.json``).
    """
    # ``Path`` gives us a convenient ``write_text`` wrapper.
    Path(file).write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )

def load(file: str ="todos.json") -> dict[str, Any]:
    """
    Load data from json

    Args:
        file (str)
    
    Return:
        dict
    """

    if Path(file).exists():
        # ``Path.read_text`` gère l’ouverture/fermeture du fichier.
        return json.loads(Path(file).read_text(encoding="utf-8"))
    return {}

def clear_screen() -> None:
    """
    Cross‑platform screen clear using ``subprocess`` (preferred over ``os.system``).
    """
    # ``shell=False`` is safer; ``/c`` for Windows, ``-c`` for POSIX.
    cmd = ["cls"] if os.name == "nt" else ["clear"]
    subprocess.run(cmd, check=False)

def prompt_input():
    """
    Input function.
    eg.: todo=# ...
    """
    try :
        prompt = input("todo=# ")
        return prompt
    except KeyboardInterrupt:
        print("\n")
        return False


def cmd_category(todo: dict[str, Any], prompt_list : list[str]):
    # category create name
    try:
        if prompt_list[0] == "category":
            if not prompt_list[1:]:
                print("Error - commmand not complete. Use : category [create/remove/rename] category_name")
                return False
            else:
                action = prompt_list[1]

                if action not in ["create", "remove", "rename"]:
                    print("Action incorrect. Action must be in ['create', 'remove', 'rename']")
                    return False
                else:
                    if not prompt_list[2:]:
                        print("Error - commmand not complete. Use : category [create/remove/rename] category_name")
                        return False
                    
                    if prompt_list[2] == "" or prompt_list[2] == " ":
                        print("Invalid category")
                        return False
                    
                    category = prompt_list[2]

                    if action == 'create':
                        if prompt_list[3:]:
                            print("Category must be one word. Use : category create category_name")
                            return False
                        create = create_category(todo, category)
                        if not create : return False
                        return create

                    elif action == 'remove':
                        if prompt_list[3:]:
                            print("Category must be one word. Use : category removecategory_name")
                            return False
                        
                        removed = remove_category(todo, category)
                        if not removed : return False
                        return removed
                        
                    elif action == 'rename':
                        if prompt_list[4:]:
                            print("Error. Use : category rename old_name new_name")
                            return False
                        new = prompt_list[3]
                        rename = rename_category(todo, category, new)
                        if not rename : return False
                        return rename
                        
        else:
            print("Error - command incorrect. Use : category [create/remove/rename] category_name")
            return False
    except:
        return False

def create_category(todo: dict[str, Any], category : str):
    try :
        if category in todo:
            print(f"Category '{category}' already in your todo list")
            return True
        else:
            todo[category] = {}
            print(f"Category {category} created.")
            return todo
    except Exception:
        print("Error")
        return False

def remove_category(todo: dict[str, Any], category: str):
    try:
        if category not in todo:
            print(f"error : Category {category} not exist.")
            return False
        else:
            count_lelment = len(todo[category])
            confirmed = input(f"you have {count_lelment} in this category. Are sure to remove it ? (o/N) : ")
            if confirmed in ["o", "O"]:
                try : 
                    todo.pop(category)
                    print(f"Category '{category}' deleted.")
                    return todo
                except Exception:
                    print(f"Error - category {category} not deleted")
                    return False
            else :
                print("Canceled")
                return False
    except Exception:
        print("Error")
        return False

def rename_category(todo: dict[str, Any], old : str, new : str):
    try:
        if old not in todo:
            print(f"Category '{old}' not i  your todo categories")
            return False
        else :
            if new in todo:
                print(f"New name '{new}' already in your todo category.")
                return False
            todo[new] = todo[old]

            try:
                todo.pop(old)
                print(f"Category {old} renamed to {new}")
                return todo
            except Exception:
                print(f"Error - Category duplicated")
                return False
            
    except Exception:
        print("Error")
        return False
    
def list_category():
    pass

def add(todo : dict[str, Any], category : str, task : str):

    position = str(len(todo[category]) + 1)
    todo[category][position] = {"name": task, "status": "incomplete"}
    
    print(f"Task added: \"{task}\" (ID: {position})")

    return todo

def lists(todo : dict[str, Any], category : str):

    if category == "all":
        for categ in todo:
            print(f"--> {categ}")
            for id, task in todo[categ].items():
                print(f"\t{id}. {task["name"]} [{task["status"]}]")
    else :            
        for id, task in todo[category].items():
            print(f"{id}. {task["name"]} [{task["status"]}]")

def done(todo: dict[str, Any], category : str, id : str):
    try : 

        if id not in todo[category].keys():
            print(f"ID {id} isn't in your todo list")
            return False
        
        try:
            todo[category][id]['status'] = 'completed'
            print(f"Task {id} completed")
        except Exception as e:
            print(f"Error : {e}")

        return todo

        # if prompt_list[2:]:
        #     print("Syntax erro. Print only 'done' whith id of task. Eg. : done 1")
        #     return False
        # if not int(prompt_list[1]):
        #     pass
        # if prompt_list[1] not in todo.keys() :
        #     print(f"Task {prompt_list[1]} doesn't exist.")
        #     return False

        # todo[prompt_list[1]]["status"] = "completed"
        # print(f"Task {prompt_list[1]} completed")

        # return todo

    except Exception:
        print("Second argument must be integer")
    # finally :
    #     print("Second argument must be integer")

def delete(todo: dict[str, Any], category : str, id : str):
    try :
        if category not in todo.keys() :
            print(f"Category {category} doesn't exist.")
            return False

        if id not in todo[category]:
            print(f"Task {id} doesn't exist.")
            return False
        
        todo[category].pop(id)
        
        todo[category] = {str(i) : value for i, (_, value) in enumerate(todo[category].items(), start=1)}

        print(f"Task deleted")

        return todo

    except ValueError :
        print("Error")

if __name__ == '__main__':
    clear_screen()
    todo = load()

    try:
        manage_cmd(todo = todo)

    except Exception as e:
        print(e)