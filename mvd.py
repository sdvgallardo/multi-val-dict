import shlex

# Initialize an empty dictionary
dictionary = { }

def listKeys():
    retval = ""
    if len(dictionary) < 1:
        retval = "No keys"
        print(retval)
    i = 1
    for key in dictionary:
        retval = "%d) %s" % (i, key)
        print (retval)
        i = i + 1
    return retval

def listMembers(key):
    retval = ""
    if key in dictionary:
        i = 1
        for value in dictionary[key]: # Prints numbered list of keys available
            retval = "%d) %s" % (i, value)
            print(retval)
            i = i + 1
    else:
        retval = "ERROR: Key does not exist"
        print(retval)
    return retval # Returns either the error or the last value, for testing

def listAll(keys): 
    retval = ""
    i = 1
    if len(dictionary) < 1:
        retval = "No keys"
        print(retval)
    for key in dictionary:
        for value in dictionary[key]:
            if(keys): # Keys boolean indicates if we include Keys in the output
                retval = "%d) %s: %s" % (i, key, value)
            else:
                retval = "%d) %s" % (i, value)
            print(retval)
            i = i + 1
    return retval # Returns the last value for testing

def addMember(key, value):
    retval = ""
    if key in dictionary: # Checks for existing key
        if value in dictionary[key]:
            retval = "ERROR: Member already exists for key"
        else: 
            dictionary[key].append(value) # Appends member to that list
            retval = "Added"
    else: # Otherwise, starts a new key, value set
        new_dict = {key: [value]} # Initializes the value as part of a list so we can append later
        dictionary.update(new_dict)
        retval = "Added"
    return retval

def removeMember(key, value):
    retval = ""
    if key in dictionary:
        if value in dictionary[key]: 
            dictionary[key].remove(value) # Removes specific value from list
            retval = "Removed"
        else:
            retval = "ERROR: Member does not exist for key"
        if len(dictionary[key]) < 1: 
            del dictionary[key] # Removes key if list goes to 0
    else:
        retval = "ERROR: Key does not exist"
    return retval

def removeAllMembers(key):
    retval = ""
    if key in dictionary:
        del dictionary[key] # Remove the key (and all values) from the dictionary
        retval = "Removed"
    else:
        retval = "ERROR: Key does not exist"
    return retval

def keyOrMemberExists(key, member=None):
    retval = False # Default to False in case the key doesn't exist
    if key in dictionary:
        if member: # If a member is provided, we will check if it exists under the provided key
            retval = True if member in dictionary[key] else False
        else: # If just a key is provided, we will only check if it exists in the dictionary
            retval = True if key in dictionary else False
    return retval

def dictLoop():
    while True:
        user_input = input("Enter a command (or 'HELP' for help): ")    # Get user input

        # Split input into different words
        try:
            words = shlex.split(user_input) # Use a specific split to allow for quoted inputs
        except ValueError:
            print("No closing quotation. Please try again.") # Catch an exception where only one quotation is provided
            continue

        command = words[0].upper()  # Get the desired command

        match command:
            case "KEYS":
                # Returns all keys in the dictionary
                listKeys()
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
                    print(addMember(words[1], words[2]))
            case "REMOVE":
                # Removes a member from a key
                if len(words) != 3:
                    print("ERROR: Must provide a key and a member -- REMOVE [key] [member]")
                else:        
                    print(removeMember(words[1], words[2]))
            case "REMOVEALL":
                # Removes all members for a key and the key from the dictionary
                if len(words) != 2:
                    print("ERROR: Must provide a key -- REMOVEALL [key]")
                else:
                    print(removeAllMembers(words[1]))                
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
                    print(keyOrMemberExists(words[1]))
            case "MEMBEREXISTS":
                # Returns whether a member exists within a key
                if len(words) != 3:
                    print("ERROR: Must provide a key and a member -- MEMBEREXISTS [key] [member]")
                else:        
                    print(keyOrMemberExists(words[1], words[2]))
            case "ALLMEMBERS":
                # Returns all the members in the dictionary
                listAll(False) # Provide False, meaning we don't want keys in this list
            case "ITEMS":
                # Returns all keys in the dictionary and all their members
                listAll(True) # Provide True so keys will be included
            case "HELP":
                # Returns a list of all possible commands
                print("KEYS MEMBERS ADD REMOVE REMOVEALL CLEAR KEYEXISTS MEMBEREXISTS ALLMEMBERS ITEMS HELP QUIT")
            case "QUIT":
                # Quits input
                break
            case _:
                # Default case
                print("Provide a valid command. Type HELP for list.")

if __name__ == '__main__':
    dictLoop()
    # Print the dictionary (mostly for testing)
    print("Your dictionary:", dictionary)