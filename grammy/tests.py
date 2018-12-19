from django.test import TestCase
from .models import Profile,Comment
import datetime as dt
# Create your tests here.
class profileTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.prof = Profile(Bio='Hi guys')
    
    ''' 
    test instance of image
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_profile(self):
        self.prof.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio)>0)

class CommentTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.comment = Comment(name='lovely')
    '''
    test instance of comment
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Commment))
        '''
        test for save instance of comment
        '''
    def test_save_comment(self):
        self.comment.save_comment()
        name= Comment.object.all()
        sel.assertTrue(len(name)>0)