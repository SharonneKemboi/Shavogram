from django.test import TestCase
from django.contrib.auth.models import User
from .models import Photo,Comments,Profile

# Create your tests here.


class ImageTestCase(TestCase):
    """
    This is the class will test the photos
    """
    def setUp(self):
        """
        This will create a new photo before each test
        """
        self.new_user = User(username = "Sharonne", email = "sharonne@gmail.com",password = "Atara123")
        self.new_user.save()
        self.new_photo = Photo(name = 'Sharonne', user = self.new_user)
        self.new_photo.save()

    def tearDown(self):
        """  
        This will clear the db after each test
        """
        Photo.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the new photo created is an instance of the Photo class
        """
        self.assertTrue(isinstance(self.new_photo, Photo))

    def test_init(self):
        """
        This will test whether the new photo is instantiated correctly
        """

        self.assertTrue(self.new_photo.name == "Sharonne")

    def test_save_photo(self):
        """
        This will test whether the new photo is added to the db
        """
        self.new_photo.save_photo()    
        self.assertTrue(len(Photo.objects.all()) > 0)


    def test_photo_delete(self):
        """
        This will test whether the photo is deleted from the db
        """
        self.new_photo.save_photo()
        self.assertTrue(len(Photo.objects.all()) > 0)
        self.new_photo.delete_photo()
        self.assertTrue(len(Photo.objects.all()) == 0)

    def test_edit_caption(self):
        """
        This will test the edit caption function
        """
        self.new_photo.save_photo()
        image = Photo.objects.get(id = 1)
        image.update_caption("Hello world")
        self.assertTrue(image.caption == "Hello world")    



class CommentTestCases(TestCase):
    """
    This is the class to test the comments
    """
    def setUp(self):
        """
        This will create a new comment before every test
        """
        self.new_user = User(username = "Sharonne")
        self.new_user.save()
        self.new_photo = Photo(name = 'Sharonne', user = self.new_user)
        self.new_photo.save_photo()
        self.new_comment = Comments(comment = "waddup", image = self.new_photo)

    def tearDown(self):
        """
        This will clear the dbs after each test
        """
        User.objects.all().delete()
        Photo.objects.all().delete()
        Comments.objects.all().delete()

    def test_is_instance(self):
        """
        This will test whether the new comment created is an instance of the comment class
        """
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_init(self):
        """
        This will test whether the new comment is instantiated correctly
        """
        self.assertTrue(self.new_comment.comment == "waddup")

    def test_save_comment(self):
        """
        This will test whether the new comment is added to the db
        """
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.objects.all()) > 0)

    def test_delete_comment(self):
        """
        This will test whether the comment is deleted
        """
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.objects.all()) > 0)
        self.new_comment.delete_comment()
        self.assertTrue(len(Comments.objects.all()) == 0)

    def test_edit_comment(self):
        """
        This will test whether the new comment can be edited
        """
        self.new_comment.save_comment()
        mycomments = Comments.objects.get(id = 1)
        mycomments.update_comment("New one")
        self.assertTrue(self.objects.get(id =1).comment == "New one")

class ProfileTestCases(TestCase):
    """
    This will test the profiles
    """
    def setUp(self):
        """
        This will add a new profile before each test
        """
        self.new_user = User(username = "Sharonne")
        self.new_user.save()

        

    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.new_user.profile, Profile))

  
    def test_search_users(self):
        """
        This will test whether the search function works
        """
        users = Profile.search_user("Sharonne")
        self.assertTrue(len(users) == 1)
