import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):
    
    def test_website_loading(self):
        url = "https://atg.world"
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            print("Website loaded successfully!")
        except requests.exceptions.RequestException as e:
            print("Failed to connect to the website:", e)
            self.fail("Failed to connect to the website.")

if __name__ == '__main__':
    unittest.main()