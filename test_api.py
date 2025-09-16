import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Basic tests
assert response.status_code == 200, "Expected status code 200"
data = response.json()

# Check expected content
assert "title" in data, "Response should contain a 'title' key"

print("All tests passed.")

