#local test
import json
import requests
import os

AUTH_ENDPOINT = "https://django-geonyoon.c9users.io/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"


img_path = os.path.join(os.getcwd(), "cds.jpg")

headers= {
    "Content-Type" : "application/json",
}

data = {
    'username': 'gun',
    'password': 'django1234',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)

BASE_ENDPOINT = "https://django-geonyoon.c9users.io/api/status/"
ENDPOINT = BASE_ENDPOINT + "25/"

headers2= {
    # "Content-Type" : "application/json",
    "Authorization" : "JWT " + token
}

data2 = {
    'content': 'new'
} 

with open(img_path, 'rb') as image:
    file_data = {
        'image' : image
    }    
    r = requests.get(ENDPOINT, headers=headers2)
    print(r.text)

# AUTH_ENDPOINT = "https://django-geonyoon.c9users.io/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
# ENDPOINT = "https://django-geonyoon.c9users.io/api/status/"

# image_path = os.path.join(os.getcwd(), "cds.jpg")

# headers= {
#     "Content-Type" : "application/json",
#     "Authorization": "JWT " + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmlnX2lhdCI6MTUzODc0ODY4NywidXNlcm5hbWUiOiJndW4xMiIsImV4cCI6MTUzODc0ODk4NywidXNlcl9pZCI6MTQsImVtYWlsIjoiZ3VuMTJAbmF2ZXIuY29tIn0.aywg0ePDO9bh6bKVK2QUn13fVmIFXySqwWipeQruUU0'
# }

# data = {
#     'username': 'gun13',
#     'email': 'gun13@naver.com',
#     'password': 'django1234',
#     'password2': 'django1234'
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json() 
# print(token)


# print(token)

# refresh_data = {
#     'token' : token
# }
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token'] 

# print(new_token)

# headers= {
#     # "Content-Type" : "application/json",    
#     "Authorization": "JWT " + token
# }

# with open(image_path, 'rb') as image:
#     file_data = {
#         'image' : image
#     }  
#     data = {
#         "content": "new content-type"
#     }
#     post_data = json.dumps(data)
#     posted_response = requests.post(ENDPOINT, data = data, headers=headers, files=file_data)
#     print(posted_response.text)

# get_endpoint = ENDPOINT + str(5)

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)




# post_headers = {
#     'content-type' : 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers = post_headers)
# print(post_response.text)





# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image' : image
#             }    
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else :    
#         r = requests.request(method, ENDPOINT,  data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r 
    
# do_img(method='put',
#     data={'id' : 19, 'user' : 1, "content" : "This is New"},
#     is_json=False,
#     img_path=image_path
#     )




# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT,  data=data, headers=headers)
#     # print(r.text)
#     # print(r.status_code)
#     return r 
    
# do(data={'id':500})

# do(method='delete', data={'id':4})

# do(method='delete', data={'id':5})

# do(method='put', data={'id':6, "content" : 'some noew cool content', 'user' : 1})

# do(method='post', data={"content" : 'some noew cool content', 'user' : 1})