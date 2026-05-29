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
        available_prompt = ['add', 'delete', 'list', 'quit', 'help', 'category']
        
        if cmd not in available_prompt:
            print("Erro. Type 'help' to see available help.")
            return (None, None, None)
        
        if cmd == 'quit':
            return (cmd, None, None)
        if cmd == 'help' :
            return (cmd, None, None)
        
        if not prompt_list[1] :
            print("command incomplete. Type 'help' to see available help.")

        category = prompt_list[1]

        if category not in todo:
            print(f"{category} is not in your todo categories")
            return (None, None, None)
        
        if not prompt_list[2] :
            sec = (None, None, None)

        if cmd == 'add':
            if sec:
                print("Error")
                return (None, None, None)
            task = prompt_list[2]

            if prompt_list[3:]:
                for word in prompt_list[3:]:
                    task = task + " " + word

            return (cmd, category, task)
        
        elif cmd == 'delete':
            if sec :
                print("Error")
                return (None, None, None)
            if prompt_list[3:]:
                print("Error. Use : delete category Task")
                return (None, None, None)
            id = prompt_list[2]
            return (cmd, category, id)
        
        elif cmd == 'list':
            if not sec :
                return (cmd, None, None)

            return (cmd, category, None)
        
        elif cmd == 'category':
            return (cmd, None, None)
        
        elif cmd == 'done':
            if sec :
                print("Error")
                return (None, None, None)
            if prompt_list[3:]:
                print("Error. Use : delete category Task")
                return (None, None, None)
            id = prompt_list[2]
            return (cmd, category, id)
        
    except Exception:
        print("Error")
        return (None, None, None)

def manage_cmd(todo: dict[str, Any], prompt : str, cond : bool = True):
    while cond:
        try :
            c, x, e = get_cmd(todo, prompt)

            if not c :
                continue

            if c == 'help':
                help()
                continue

            if c == 'quit' :
                save(todo)
                break

            if c == 'add':
                if x != None and e != None:
                    category, task = x, e
                    todo = add(todo, category, task)
                else: continue
                
            if c == 'list':
                if not todo:
                    print("Nothing")
                    return False
                if x == None :
                    x = 'all'
                list(todo, x)
            
            if c == 'delete':
                ret = delete(todo, x, e)
                if not ret :
                    continue
                todo = ret
            
            if c == "category":
                cmd_category(todo, _)

                

                
            
        except Exception:
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

def cmd_category(todo: dict[str, Any], prompt_list : str):
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
                    if not prompt_list[2]:
                        print("Error - commmand not complete. Use : category [create/remove/rename] category_name")
                        return False
                    
                    category = prompt_list[2]

                    if action == 'create':
                        if prompt_list[3:]:
                            print("Category must be one word. Use : category create category_name")
                            return False
                        create_category(todo, category)

                    elif action == 'remove':
                        if prompt_list[3:]:
                            print("Category must be one word. Use : category removecategory_name")
                            return False
                        
                        create_category(todo, category)
                        
                    elif action == 'rename':
                        if prompt_list[4:]:
                            print("Error. Use : category rename old_name new_name")
                            return False
                        new = prompt_list[3]
                        rename_category(todo, category, new)
                        
        else:
            print("Error - command incorrect. Use : category [create/remove/rename] category_name")
            return False
    except:
        pass

def create_category(todo: dict[str, Any], category : str):
    try :
        if category in todo:
            print(f"Category '{category}' already in your todo list")
            return True
        else:
            todo[category] = {}
            print(f"Category {category} created.")
            return True
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
                if todo.pop(category):
                    print(f"Category '{category}' deleted.")
                    return True
                else:
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

            if todo.pop(old):
                print(f"Category {old} renamed to {new}")
                return True
    except Exception:
        print("Error")
        return False
    

def add(todo : dict[str, Any], category : str, task : str):

    position = str(len(todo[category]) + 1)
    todo[category] = {position : {"name": task, "status": "incomplete"}}
    
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

def done(todo: dict[str, Any], prompt_list: list[str]):
    try : 
        if prompt_list[2:]:
            print("Syntax erro. Print only 'done' whith id of task. Eg. : done 1")
            return False
        if not int(prompt_list[1]):
            pass
        if prompt_list[1] not in todo.keys() :
            print(f"Task {prompt_list[1]} doesn't exist.")
            return False

        todo[prompt_list[1]]["status"] = "completed"
        print(f"Task {prompt_list[1]} completed")

        return todo

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
    #clear_screen()
    # todo = {}
    # task = ["category", "non"]
    # print(create_category(todo, task))
    # print(todo)
    todo = load()

    h = False
    while h :
        try:
            prompt = prompt_input()
            if prompt is False: continue

            prompt_list = prompt.split(" ")

            if prompt_list[0] not in ["add", "list", "done", "delete", "quit", "help"] :
                print("Error")
                continue
            
            if prompt_list[0] == 'help':
                help()

            if prompt_list[0] == "quit":
                save(todo)
                clear_screen()
                break

            if prompt_list[0] == "add" :
                todos = add(todo, prompt_list)
                if type(todos) == dict:
                    todo = todos
                else : continue

            if prompt_list[0] == "list" :
                if not lists(todo, "work"): continue
                
            if prompt_list[0] == "done" :

                todos = done(todo, prompt_list)
                if type(todos) == dict:
                    todo = todos
                else : continue

            if prompt_list[0] == "delete":
                todos = delete(todo, prompt_list)
                if type(todos) == dict:
                    todo = todos
                else : continue
        except Exception as e:
            print(e)
            break