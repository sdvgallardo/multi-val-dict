import shlex

# Initialize an empty dictionary
dictionary = { }

def listMembers(key):
    if key in dictionary:
        i = 1
        for value in dictionary[key]: # Prints numbered list of keys available
            print("%d) %s" % (i, value))
            i = i + 1
    else: 
        print("ERROR: Key does not exist")

def listAll(keys): 
    i = 1
    for key in dictionary:
        for value in dictionary[key]:
            if(keys): # Keys boolean indicates if we include Keys in the output
                print("%d) %s: %s" % (i, key, value))
            else:
                print("%d) %s" % (i, value))
            i = i + 1

def addMember(key, value):
    if key in dictionary: # Checks for existing key
        if value in dictionary[key]:
            print("ERROR: Member already exists for key")
        else: 
            dictionary[key].append(value) # Appends member to that list
            print("Added")
    else: # Otherwise, starts a new key, value set
        new_dict = {key: [value]} # Initializes the value as part of a list so we can append later
        dictionary.update(new_dict)
        print("Added")

def removeMember(key, value):
    if key in dictionary:
        if value in dictionary[key]: 
            dictionary[key].remove(value) # Removes specific value from list
            print("Removed")
        else:
            print("ERROR: Member does not exist for key")
        if len(dictionary[key]) < 1: 
            del dictionary[key] # Removes key if list goes to 0
    else:
        print("ERROR: Key does not exist")    

while True:
  # Get user input
  user_input = input("Enter a command (or 'HELP' for help): ")

  # Split input into different words
  words = shlex.split(user_input) # Use a specific split to allow for quoted inputs

  # Get the desired command
  command = words[0].upper()

  match command:
    case "KEYS":
        # Returns all keys in the dictionary
        if len(dictionary) < 1:
            print("No keys")
        i = 1
        for key in dictionary:
            print("%d) %s" % (i, key))
            i = i + 1
    case "MEMBERS":
        # Returns the collection of strings for a given key
        if len(words) != 2:
            print("ERROR: Must provide a key -- MEMBERS [key]")
        else: 
            listMembers(words[1])    
    case "ADD":
        # Adds member to collection with a given key
        if len(words) != 3:
            print("ERROR: Must provide a key and a member -- ADD [key] [member]")
        else:        
            addMember(words[1], words[2])
    case "REMOVE":
        # Removes a member from a key
        if len(words) != 3:
            print("ERROR: Must provide a key and a member -- REMOVE [key] [member]")
        else:        
            removeMember(words[1], words[2])
    case "REMOVEALL":
        # Removes all members for a key and the key from the dictionary
        if len(words) != 2:
            print("ERROR: Must provide a key -- REMOVEALL [key]")
        if words[1] in dictionary:
            del dictionary[words[1]]
        else:
            print("ERROR: Key does not exist")
    case "CLEAR":
        # Removes all keys and all members from the dictionary
        if len(dictionary) < 1:
            print("No keys")
        else:
            dictionary.clear()
            print("Cleared")
    case "KEYEXISTS":
        # Returns whether a key exists or not
        if len(words) != 2:
            print("ERROR: Must provide a key -- KEYEXISTS [key]")
        else:
            print(True if words[1] in dictionary else False)
    case "MEMBEREXISTS":
        # Returns whether a member exists within a key
        if len(words) != 3:
            print("ERROR: Must provide a key and a member -- MEMBEREXISTS [key] [member]")
        else:        
            if words[1] in dictionary:
                print(True if words[2] in dictionary[words[1]] else False)
            else:
                print("False")
    case "ALLMEMBERS":
        # Returns all the members in the dictionary
        if len(dictionary) < 1:
            print("No keys")
        else: 
            listAll(False)
    case "ITEMS":
        # Returns all keys in the dictionary and all their members
        if len(dictionary) < 1:
            print("No keys")
        else: 
            listAll(True)
    case "HELP":
        # Returns a list of all possible commands
        print("KEYS MEMBERS ADD REMOVE REMOVEALL CLEAR KEYEXISTS MEMBEREXISTS ALLMEMBERS ITEMS HELP QUIT")
    case "QUIT":
        # Quits input
        break
    case _:
        # Default case
        print("Provide a valid command. Type HELP for list.")


# Print the dictionary (mostly for testing)
print("Your dictionary:", dictionary)