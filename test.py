import unittest
from unittest.mock import patch
from main import app
from health.routes.health import health_bp

class TestPingRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_ping_route(self):
        response = self.app.get('/ping')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Status'], 'Up 👍')

class TestHealthzRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_ping_route(self):
        response = self.app.get('/healthz')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(data['Status'], 'Up 👍')

# class TestHealthzRoute(unittest.TestCase):
#     def setUp(self):
#         self.app = app.test_client()

#     @patch('health.routes.health.psutil')
#     def test_healthz_route_memory_zero(self, mock_psutil):
#         mock_psutil.cpu_percent.return_value = 10.0
#         # Set total memory to 0
#         mock_psutil.virtual_memory.return_value = (0, 0, 0, 0)

#         response = self.app.get('/healthz')
#         data = response.get_json()
#         print(response)

#         # Assert that the response status code is 500
#         self.assertEqual(response.status_code, 500)

#         # self.assertTrue(any([
#         #     data['cpu_usage'] == 0,
#         #     data['memory']['total'] == 0,
#         #     data['memory']['used'] == 0,
#         #     data['memory']['free'] == 0,
#         #     data['memory']['percent'] == 0,
#         #     data['disk_space']['total'] == 0,
#         #     data['disk_space']['used'] == 0,
#         #     data['disk_space']['free'] == 0,
#         #     data['disk_space']['percent'] == 0,
#         # ]))

if __name__ == '__main__':
    unittest.main()
