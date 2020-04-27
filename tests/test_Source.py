import unittest
from models import News, Sources

class TestNews(unittest.TestCase):
  """Defines test for the NewsSource class behaviour
    """
def setUp(self):
      '''
    Set up method that will run before every Test
    '''
    
    self.new_source = News()


def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Sources))

def test_init(self):
      '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_source.author, 'Peter Polle')
    self.assertEqual(self.new_source.title, 'The tech scene in Africa-Is it the next big thing?')
    self.assertEqual(self.new_source.description, 'A look at various tech hubs in Africa and the impact they have on the worlds economy')
    self.assertEqual(self.new_source.url, 'techie.com')
    self.assertEqual(self.new_source.urlToImage, 'techie.com/7643t94.jpg')
    self.assertEqual(self.new_source.content, 'One of the videos shows an incident from 2004, and the other two were recorded in January 2015, according to Sue Gough, a Defense Department spokeswoman. The videos became public after unauthorized leaks in 2007 and 2017, and the Navy previously ')
 

# Article
        
class TestArticle(unittest.TestCase):
    """Defines test for the NewsSource class behaviour
    """
    
def setUp(self):
          '''
        Set up method that will run before every Test
        '''
    self.new_article = Sources('CNN','Georgia starts to reopen but nervous mayors warn that coronavirus crisis isn"t over', 'Maeve Reston', 'edition.cnn.com', 'Global coronavirus pandemic', '2020-04-25T14:15:36Z', 'coronavirus.jpg')
    
def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Articles))

def test_init(self):
      '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_article.id, 'CNN')
    self.assertEqual(self.new_article.name, 'CNN News')
    self.assertEqual(self.new_article.description, 'Cable News Newtork that is a leader in providing news worldwide')
    self.assertEqual(self.new_article.url, 'cnn.com')
    self.assertEqual(self.new_article.category, 'general')