from unittest import TestCase
from mvd import (
    listMembers,
    listAll,
    addMember,
    removeMember,
    dictionary,
)

class TestProgram(TestCase):
    def test_key_does_not_exist(self):
        # Add a key, then test that another key does not exist
        addMember("foo", "bar")
        val = listMembers("fizz")
        self.assertEqual(val, "ERROR: Key does not exist")

    def test_member_add(self):
        # Add some members
        addMember("color", "red")
        addMember("color", "blue")
        # Add member under another key
        val = addMember("fruit", "apple")
        self.assertEqual(val, "Added")
        # Try to add an already existing member
        val = addMember("color", "red")
        self.assertEqual(val, "ERROR: Member already exists for key")
        # Confirm color key contains two members
        self.assertCountEqual(dictionary["color"], ["red","blue"])

    def test_key_valid_invalid(self):
        # Add member, then check if the the provided key exists
        addMember("color", "blue")
        self.assertTrue(True if "color" in dictionary else False)
        # Check if a different key does not exist
        self.assertFalse(True if "bang" in dictionary else False)
    
    def test_invalid_member_remove(self):
        # Add a member
        addMember("fruit", "apple")
        # Try to remove a member that was never added
        val = removeMember("fruit", "orange")
        self.assertEqual(val, "ERROR: Member does not exist for key")
        # Try to remove a member under a key that was never added
        val = removeMember("fuzz", "buzz")
        self.assertEqual(val, "ERROR: Key does not exist")

    def test_valid_member_remove(self):
        # Add some members
        addMember("color", "red")
        addMember("color", "blue")
        # Remove one member, confirm key only contains last member
        removeMember("color", "blue")
        self.assertCountEqual(dictionary["color"], ["red"])
        # Remove last member, confirm key no longer exists in dict
        removeMember("color", "red")
        self.assertFalse(True if "color" in dictionary else False)

    def test_dictionary_clear(self):
        # Add some members
        addMember("color", "red")
        addMember("color", "blue")
        # Confirm color key contains two members
        self.assertCountEqual(dictionary["color"], ["red","blue"])
        # Clear dictionary, then confirm dictionary is empty
        dictionary.clear()
        self.assertEqual(dictionary, {})
    
    def test_list_members(self):
        # Clear dictionary to start from scratch
        dictionary.clear()
        # Add some members
        addMember("foo", "bar")
        addMember("foo", "bang")
        addMember("baz", "bang")
        addMember("fizz", "buzz")
        val = listAll(False) # We just want members for this one
        # Check that the last output was the last member added
        self.assertEqual(val, "4) buzz")
    
    def test_list_all(self):
        # Clear dictionary to start from scratch
        dictionary.clear()
        # Add some members
        addMember("foo", "bar")
        addMember("foo", "bang")
        addMember("baz", "bang")
        addMember("fizz", "buzz")
        val = listAll(True) # We want both keys and members
        # Check that the last output was the last key and member added
        self.assertEqual(val, "4) fizz: buzz")