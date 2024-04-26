from unittest import TestCase
from mvd import (
    listKeys,
    listMembers,
    listAll,
    addMember,
    removeMember,
    removeAllMembers,
    keyOrMemberExists,
    dictionary,
)

class TestProgram(TestCase):
    def test_key_does_not_exist(self):
        addMember("foo", "bar")                     # Add a key, then test that another key does not exist
        val = listMembers("fizz")
        self.assertEqual(val, "ERROR: Key does not exist")

    def test_member_add(self):
        addMember("color", "red")                   # Add some members
        addMember("color", "blue")
        val = listMembers("color")
        self.assertEqual(val, "2) blue")
        val = addMember("fruit", "apple")           # Add member under another key
        self.assertEqual(val, "Added")
        val = addMember("color", "red")             # Try to add an already existing member
        self.assertEqual(val, "ERROR: Member already exists for key")
        self.assertCountEqual(dictionary["color"], ["red","blue"]) # Confirm color key contains two members

    def test_key_member_valid(self):
        addMember("color", "blue")                  # Add member, then check if the the provided key exists
        self.assertTrue(keyOrMemberExists("color"))
        addMember("color", "red")                   # Add another member, then check that the first one still exists
        self.assertTrue(keyOrMemberExists("color", "blue"))

    def test_key_member_invalid(self):
        self.assertFalse(keyOrMemberExists("bang")) # Check for a key that has never existed
        addMember("color", "blue")                  # Check for a member that doesn't exist in a key that does
        self.assertFalse(keyOrMemberExists("color", "gray"))
    
    def test_invalid_member_remove(self):
        addMember("fruit", "apple")                 # Add a member
        val = removeMember("fruit", "kiwi")         # Try to remove a member that was never added
        self.assertEqual(val, "ERROR: Member does not exist for key")
        val = removeMember("fuzz", "buzz")          # Try to remove a member under a key that was never added
        self.assertEqual(val, "ERROR: Key does not exist")

    def test_valid_member_remove(self):
        addMember("color", "red")                   # Add some members
        addMember("color", "blue")
        removeMember("color", "blue")               # Remove one member, confirm key only contains last member
        self.assertCountEqual(dictionary["color"], ["red"])
        removeMember("color", "red")                # Remove last member, confirm key no longer exists in dict
        self.assertFalse(keyOrMemberExists("color"))
    
    def test_remove_all_from_key(self):
        addMember("color", "red")                   # Add some members
        addMember("color", "blue")
        addMember("color", "orange")
        val = addMember("color", "green")
        self.assertEqual(val, "Added")
        val = removeAllMembers("color")             # Call remove all, confirm it succeeded
        self.assertEqual(val, "Removed")
        val = removeAllMembers("color")             # Try to remove it again, confirm error is received
        self.assertEqual(val, "ERROR: Key does not exist")

    def test_dictionary_clear(self):
        addMember("color", "red")                   # Add some members
        addMember("color", "blue")
        self.assertCountEqual(dictionary["color"], ["red","blue"]) # Confirm color key contains two members
        dictionary.clear()                          # Clear dictionary, then confirm dictionary is empty
        self.assertEqual(dictionary, {})

    def test_list_keys(self):
        dictionary.clear()                          # Clear dictionary to start from scratch
        val = listKeys()
        self.assertEqual(val, "No keys")            # Check for no keys message
        addMember("foo", "bar")                     # Add some members
        addMember("fizz", "buzz")
        addMember("color", "red")
        val = addMember("fruit", "apple") 
        self.assertEqual(val, "Added")              # Check that the member was added
        val = listKeys()                            # List all keys, confirm the last one is correct
        self.assertEqual(val, "4) fruit")
    
    def test_list_members(self):
        dictionary.clear()                          # Clear dictionary to start from scratch
        val = listKeys()
        self.assertEqual(val, "No keys")            # Check for no keys message
        addMember("foo", "bar")                     # Add some members
        addMember("foo", "bang")
        addMember("baz", "bang")
        addMember("fizz", "buzz")
        val = listAll(False)                        # We just want members for this one
        self.assertEqual(val, "4) buzz")            # Check that the last output was the last member added
    
    def test_list_all(self):
        dictionary.clear()                          # Clear dictionary to start from scratch
        val = listKeys()
        self.assertEqual(val, "No keys")            # Check for no keys message
        addMember("foo", "bar")                     # Add some members
        addMember("foo", "bang")
        addMember("baz", "bang")
        addMember("fizz", "buzz")
        val = listAll(True)                         # We want both keys and members
        self.assertEqual(val, "4) fizz: buzz")      # Check that the last output was the last key and member added