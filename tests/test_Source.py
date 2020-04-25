import unittest
from models import Sources, Articles

class TestSource(unittest.TestCase):
  """Defines test for the NewsSource class behaviour
    """
    def setUp(self):
          '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('CNN','Cable News Newtork that is a leader in providing news worldwide', 'cnn.com', 'general', 'CNN News', 'U.S.A', 'en')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))
    
    def test_init(self):
          '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.id, 'CNN')
        self.assertEqual(self.new_source.description, 'Cable News Newtork that is a leader in providing news worldwide')
        self.assertEqual(self.new_source.url, 'cnn.com')
        self.assertEqual(self.new_source.category, 'general')
        self.assertEqual(self.new_source.name, 'CNN News')
        self.assertEqual(self.new_source.country, 'U.S.A')
        self.assertEqual(self.new_source.language, 'en')
        