from django.test import TestCase
from .models import Comments,Image,Profile
import datetime as dt
# Create your tests here.
class CommentsTestClass(TestCase):
    def setup(self):
        '''
        Method that allows us to create an instance of the Comments class before every test.
        '''
        self.comment= Comments(text = 'amazing')
        self.comment.save_comments()

    def test_instance(self):
        '''
        test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.comment,Comments))
    
    def tearDown(self):
        '''
        Method to delete  instance of our comments model from the database after each test
        '''
        self.comment.delete_comments()

class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Method that allows us to create an instance of the Profile class before every test.
        '''
        self.photo = Profile(profile_photo ='image4.jpg')
        self.photo.save_photo()

    def test_instance(self):
        '''
        test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.photo,Profile))
    
    def tearDown(self):
        '''
        Method to delete  instance of our profile model from the database after each test
        '''
        self.photo.delete_photo()

class ImageTestClass(TestCase):
   """
   Tests Image class and its functions
   """
   #Set up method
   def setUp(self):
       '''
       Method that allows us to create an instance of the Image class before every test.
       '''

       self.image = Image(photo_name='Fashion', photo_caption='cool',photo_comments ='fansy', pub_date='2020.06.12')
       self.image.save_image()


   def test_instance(self):
       '''
       test to confirm that the object is being instantiated correctly
       '''
       self.assertTrue(isinstance(self.image, Image))

   def test_save_method(self):
       """
       Function to test an image and its details is being saved
       """
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

   def test_delete_method(self):
       """
       Function to test if an image can be deleted
       """
       self.image.save_image()
       self.image.delete_image()

   def test_update_method(self):
       """
       Function to test that an image's details can be updated
       """
       self.image.save_image()
       new_image = Image.objects.filter(image='image1.jpg').update(image='download.jpg')
       images = Image.objects.get(image='download.jpg')
       self.assertTrue(images.image, 'download.jpg')

   def test_get_image_by_id(self):
       """
       Function to test if you can get an image by its id
       """
       self.image.save_image()
       this_img= self.image.get_image_by_id(self.image.id)
       image = Image.objects.get(id=self.image.id)
       self.assertTrue(this_img, image)
