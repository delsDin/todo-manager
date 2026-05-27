import os
import json
import subprocess
from pathlib import Path
from typing import Any, Dict

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

def save(data: Dict[str, Any], file: str = "todo.json") -> None:
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

def load(file: str ="todo.json") -> dict[str, Any]:
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

def add(todo : dict[str, Any], prompt_list : list[str]):
    if not prompt_list[1:]:
        print("Require task name")
        return False
    if len(prompt_list[1]) == 1 or prompt_list[1] == "":
        print("Invalide task")
        return False

    task = prompt_list[1]

    for num, word in enumerate(prompt_list[1:]):
        if num == 0:
            continue
        
        task = task + " " + word

    position = str(len(todo) + 1)
    todo[position] = {"name": task, "status": "incomplete"}
    
    print(f"Task added: \"{task}\" (ID: {position})")

    return todo

def lists(todo : dict[str, Any]):
    if prompt_list[1:]:
        print("Syntaxe error. Print only the key word 'list'")
        return False

    if not todo:
        print("Nothing")
        return False

    for id, task in todo.items():
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

def delete(todo: dict[str, Any], prompt_list : list[str]):
    try : 
        if prompt_list[2:]:
            print("Syntax erro. Print only 'done' whith id of task. Eg. : done 1")
            return False

        if not int(prompt_list[1]):
            pass

        if prompt_list[1] not in todo.keys() :
            print(f"Task {prompt_list[1]} doesn't exist.")
            return False

        todo.pop(prompt_list[1])
        
        todo = {str(i) : value for i, (_, value) in enumerate(todo.items(), start=1)}

        print(f"Task deleted")

        return todo

    except ValueError :
        print("Second argument must be integer")
        

if __name__ == '__main__':
    clear_screen()
    todo = load()

    h = True
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
                if not lists(todo): continue
                
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