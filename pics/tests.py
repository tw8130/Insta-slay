from django.test import TestCase
from .models import Comments,Image,Profile
import datetime as dt
# Create your tests here.
class CommentsTestClass(TestCase):
    def setup(self):
        '''
        Method that allows us to create an instance of the Location class before every test.
        '''
        self.nairobi= Location(loc_name = 'Kenya')
        self.nairobi.save_location()

    def test_instance(self):
        '''
        test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def tearDown(self):
        '''
        Method to delete  instance of our location model from the database after each test
        '''
        self.nairobi.delete_location()

class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Method that allows us to create an instance of the Category class before every test.
        '''
        self.travel = Category(cat_name ='Nature')
        self.travel.save_category()

    def test_instance(self):
        '''
        test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.travel,Category))
    
    def tearDown(self):
        '''
        Method to delete  instance of our category model from the database after each test
        '''
        self.travel.delete_category()

class ImageTestClass(TestCase):
   """
   Tests Image class and its functions
   """
   #Set up method
   def setUp(self):
       '''
       Method that allows us to create an instance of the Category class before every test.
       '''
       self.comment = Category(cat_name='Travel')
       self.comment.save_category()

       self.nairobi = Location(loc_name='Kenya')
       self.nairobi.save_location()

       self.image = Image(photo_name='Fashion', photo_caption='cool', =self.nairobi, category=self.travel)
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
