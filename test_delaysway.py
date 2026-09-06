# test_delaysway.py
"""
Tests for DelaySway module.
"""

import unittest
from delaysway import DelaySway

class TestDelaySway(unittest.TestCase):
    """Test cases for DelaySway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DelaySway()
        self.assertIsInstance(instance, DelaySway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DelaySway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
