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
        