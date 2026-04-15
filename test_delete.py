import requests  
s=requests.Session()  
r=s.post('http://127.0.0.1:5000/', data={'username':'admin','password':'admin123','role':'admin'}, allow_redirects=True)  
print('login', r.status_code, r.url)  
r=s.post('http://127.0.0.1:5000/delete_faculty_none', allow_redirects=True)  
print('delete', r.status_code, r.url)  
print('dashboard redirected', '/dashboard' in r.url)  
