from django.test import TestCase


from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase): #Unittest
    def setUp(self):
        user = User.objects.create(username='gun', email='ssy01013@naver.com')
        user.set_password('django1234')
        user.save()
    
    def test_created_user(self):
        qs = User.objects.filter(username='gun')
        self.assertEqual(qs.count(), 1)
        
        