# from django.test import TestCase


# from django.contrib.auth import get_user_model
# from .models import Status

# User = get_user_model()

# class StatusTestCase(TestCase): #Unittest
#     def setUp(self):
#         user = User.objects.create(username='gun', email='ssy01013@naver.com')
#         user.set_password('django1234')
#         user.save()
    
#     def test_creating_status(self):
#         user = User.objects.get(username='gun')
#         obj = Status.objects.create(user=user, content='Some cool new content')   
#         self.assertEqual(obj.id, 1)
#         qs = Status.objects.all()
#         self.assertEqual(qs.count(), 1)
        