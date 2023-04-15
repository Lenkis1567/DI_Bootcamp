 
import requests 
  
# Making a get request 

response = requests.get('http://google.com') 
print("Google: ", response) 
print("Google: ", response.elapsed)

response = requests.get('https://www.imdb.com/') 
print("Imdb: ", response) 
print("Imdb: ", response.elapsed)