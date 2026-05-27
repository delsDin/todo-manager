import json
import os

def help():
    clear_screnn()
    if os.path.exists('help.txt'):
        with open('help.txt', 'r') as file:
            for row in file:
                print(row)
    else:
        print("Help not available !")

def save(data : dict, file = "todo.json"):
    """
    Save data to json format

    Args :
        data (dict) : the data
        file (str)
    
    """
    with open(file, "w", encoding="utf-8") as fichier:

        json.dump(data, fichier, indent=4, ensure_ascii=False)

def load(file="todo.json"):
    """
    Load data from json

    Args:
        file (str)
    """

    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as fichier:
            todo = json.load(fichier)
    else:
        todo = {}
    return todo

def clear_screnn():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    clear_screnn()
    todo = load()

    clear_screnn()
    h = True
    while h :
        try:
            try :
                prompt = input("todo=# ")
            except KeyboardInterrupt:
                print("\n")
                continue

            prompt_list = prompt.split(" ")

            if prompt_list[0] not in ["add", "list", "done", "delete", "quit", "help"] :
                print("Error")
                continue
            
            if prompt_list[0] == 'help':
                help()

            if prompt_list[0] == "quit":
                save(todo)
                clear_screnn()
                break

            if prompt_list[0] == "add" :

                if not prompt_list[1:]:
                    print("Require task name")
                    continue
                if len(prompt_list[1]) == 1:
                    print("Invalide task")

                task = prompt_list[1]
                for num, word in enumerate(prompt_list[1:]):
                    if num == 0:
                        continue
                    task = task + " " + word
                position = str(len(todo) + 1)
                todo[position] = {"name": task, "status": "incomplete"}
                
                print(f"Task added: \"{task}\" (ID: {position})")

            if prompt_list[0] == "list" :

                if prompt_list[1:]:
                    print("Syntaxe error. Print only the key word 'list'")
                    continue

                if not todo:
                    print("Nothing")
                    continue
                
                for id, task in todo.items():
                    print(f"{id}. {task["name"]} [{task["status"]}]")

            if prompt_list[0] == "done" :
                
                try : 
                    if prompt_list[2:]:
                        print("Syntax erro. Print only 'done' whith id of task. Eg. : done 1")
                        continue
                    if not int(prompt_list[1]):
                        pass
                    if prompt_list[1] not in todo.keys() :
                        print(f"Task {prompt_list[1]} doesn't exist.")
                        continue

                    todo[prompt_list[1]]["status"] = "completed"
                    print(f"Task {prompt_list[1]} completed")

                except Exception as e :
                    print("Second argument must be integer")
                # finally :
                #     print("Second argument must be integer")
            
            if prompt_list[0] == "delete":
                try : 
                    if prompt_list[2:]:
                        print("Syntax erro. Print only 'done' whith id of task. Eg. : done 1")
                        continue

                    if not int(prompt_list[1]):
                        pass

                    if prompt_list[1] not in todo.keys() :
                        print(f"Task {prompt_list[1]} doesn't exist.")
                        continue

                    todo.pop(prompt_list[1])
                    
                    
                    todo = {str(i) : value for i, (key, value) in enumerate(todo.items(), start=1)}

                    print(f"Task deleted")

                except ValueError :
                    print("Second argument must be integer")
        
        except Exception as e:
            print(e)
            break