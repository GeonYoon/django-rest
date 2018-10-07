import os
import shutil
import tempfile
from PIL import Image 

from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from status.models import Status
from django.conf import settings 

User = get_user_model()

class StatusAPITestCase(APITestCase): #Unittest
    # specific setup(environment) that you want to have to do your tests
    def setUp(self):
        user = User.objects.create(username='testgunuser', email='ssy01013@naver.com')
        user.set_password('django1234')
        user.save()
        status_obj = Status.objects.create(user=user, content="hello there")

    def test_statuses(self):
        # qs = Status.objects.all()
        self.assertEqual(Status.objects.count(),1)
        
    def status_user_token(self):
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username' : 'testgunuser', 
            'password' : 'django1234'
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get("token",0)
        # set my client with this token
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)        
        
    
    def create_item(self):
        self.status_user_token()
        
        url = api_reverse('api-status:list')
        data = {
            'content' : "some cool test content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(),2)  
        return response.data
    
    def test_empty_create_item(self):
        self.status_user_token()
        
        url = api_reverse('api-status:list')
        data = {
            'content' : None,
            'image' : None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        return response.data
    
    def test_status_create_with_image(self):
        self.status_user_token()
        # (w, h) = (800, 1200)
        # (255, 255, 255) hex color
        url = api_reverse('api-status:list')
        image_item  = Image.new('RGB', (800, 1280), (0,124,174))
        tmp_file    = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        with open(tmp_file.name, 'rb') as file_obj :
            data = {
                'content' : "some cool test content",
                'image' : file_obj
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.count(),2) 
            print(response.data)
            img_data = response.data.get('image')
            self.assertNotEqual(img_data, None)
        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', 'testgunuser') 
        # remove entire dir made from the test 
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)
            
    def test_status_create_with_image_and_no_desc(self):
        self.status_user_token()
        # (w, h) = (800, 1200)
        # (255, 255, 255) hex color
        url = api_reverse('api-status:list')
        image_item  = Image.new('RGB', (800, 1280), (0,124,174))
        tmp_file    = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        with open(tmp_file.name, 'rb') as file_obj :
            data = {
                'content' : None,
                'image' : file_obj
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            print(response.data)
            self.assertEqual(Status.objects.count(),2) 
        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', 'testgunuser') 
        # remove entire dir made from the test 
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)
        
    
    def test_status_create(self):
        data = self.create_item()
        
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id" : data_id})
        rud_data = {
            'content' : "some cool test content"
        }
        
        '''
        GET method / retrieve
        '''
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        
    def test_status_update(self):
        data = self.create_item()
        
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id" : data_id})
        rud_data = {
            'content' : "some cool test content"
        }
        
        '''
        PUT / update
        '''
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        rud_response = put_response.data
        self.assertEqual(rud_response['content'], rud_data['content'])
        
    def test_status_delete(self):
        data = self.create_item()
        
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id" : data_id})
        rud_data = {
            'content' : "some cool test content"
        }
        
        '''
        DELETE method / delete
        '''
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        
    
        '''
        NOT FOUND
        '''
        del_response = self.client.get(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_404_NOT_FOUND)        

    def test_status_no_token_create(self):
        url = api_reverse('api-status:list')
        data = {
            'content' : "some cool test content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    

    # def test_register_user_api_fail(self):
    #     url = api_reverse('api-auth:register')
    #     data = {
    #         'username' : 'gunny',
    #         'email' : 'gunny@naver.com',
    #         'password' : 'django1234'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     # if I do dir(response), I can see all of the attribute that I can do (reverse engineering)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data['password2'][0],'This field is required.')
    
    # def test_register_user_api(self):
    #     url = api_reverse('api-auth:register')
    #     data = {
    #         'username' : 'gunny',
    #         'email' : 'gunny@naver.com',
    #         'password' : 'django1234',
    #         'password2' : 'django1234' 
    #     }
    #     response = self.client.post(url, data, format='json')
    #     # if I do dir(response), I can see all of the attribute that I can do (reverse engineering)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     token_len = len(response.data.get("token",0))
    #     self.assertGreater(token_len,0)
        
    # def test_login_user_api(self):
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username' : 'gun',
    #         'password' : 'django1234'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     # if I do dir(response), I can see all of the attribute that I can do (reverse engineering)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     token = response.data.get("token",0)
    #     token_len = 0
    #     if token != 0:
    #         token_len = len(token)
    #     self.assertGreater(token_len,0)
        
    # def test_login_user_api_fail(self):
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username' : 'gunny', # does not exist
    #         'password' : 'django1234'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     # if I do dir(response), I can see all of the attribute that I can do (reverse engineering)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     token = response.data.get("token",0)
    #     token_len = 0
    #     if token != 0:
    #         token_len = len(token)
    #     self.assertEqual(token_len,0)
        
    # def test_token_login_api(self):
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username' : 'gun',
    #         'password' : 'django1234'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     token = response.data.get("token",None)
    #     self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    #     response2 = self.client.post(url, data, format='json')
    #     self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)
        
    # def test_token_register_user_api(self):
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username' : 'gun',
    #         'password' : 'django1234'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     token = response.data.get("token",None)
    #     self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)        
        
    #     url2 = api_reverse('api-auth:register')
    #     data2 = {
    #         'username' : 'gunny',
    #         'email' : 'gunny@naver.com',
    #         'password' : 'django1234',
    #         'password2' : 'django1234' 
    #     }
    #     response = self.client.post(url2, data2, format='json')
    #     # if I do dir(response), I can see all of the attribute that I can do (reverse engineering)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        
        
        
        
        
        