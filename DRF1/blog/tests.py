from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post,Category
# Create your tests here.

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
       test_category = Category.objects.create(name='django')
       testuser1 = User.objects.create_user(
           username='test_user1',password='123456789'
       )
       test_post = Post.objects.create(
           category_id =1,title='post title',
           excerpt ='Post excerpt',content='Post content',
           author_id = 1,status = 'published'
       )

