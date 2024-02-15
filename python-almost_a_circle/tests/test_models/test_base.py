import unittest
from models.base import Base



class BaseMethods(unittest.TestCase):
    def setUp(self):
        self.obj = Base()
    
    def test_id(self):
        self.assertIsNotNone(self.obj.id)
    
    def test_to_json_string(self):
        self.assertEqual(self.obj.to_json_string(None), "[]")
        self.assertEqual(self.obj.to_json_string(""), "[]")
        result = self.obj.to_json_string([{'id': 1, 'name': 'test'}])
        self.assertEqual(result, '[{"id": 1, "name": "test"}]')



if __name__ == "__main__":
    unittest.main()