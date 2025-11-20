#grma1075 94731
class Aufgabe_6:
    todos = []
    todos.append("SWE Übungsblatt machen")
    todos.append("Einkaufen gehen")
    todos.append("Python lernen")
    
    print("--- gesamte Liste Todos ---")
    print(todos)

    print("--- alle Einträge in der Liste ---")
    for i in todos: 
        print(i)

    print("--- erster Eintrag der Liste ---")    
    print(todos[0])

    print("--- letzter Eintrag der Liste ---")
    print(todos[-1])

    print("--- die letzten beiden Einträge mit [:]-Notation ---")
    print(todos[1:3])
    
