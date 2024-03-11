import unittest
from unittest.mock import patch, MagicMock
from src.main import App


class TestMain(unittest.TestCase):
    URL = "http://159.203.50.162"
    TOKEN = "e7026c64578833bfc1ba"
    TICKS = 10
    T_MAX = 20
    T_MIN = 10

    def setUp(self):
        self.app = App()
        # Mock the hub connection
        self.app.HOST = self.URL
        self.app.TOKEN = self.TOKEN
        self.app.TICKS = self.TICKS
        self.app.T_MAX = self.T_MAX
        self.app.T_MIN = self.T_MIN

    @patch("requests.get")
    def test_send_action_to_hvac(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.text = '{"detail": "success"}'
        mock_get.return_value = mock_response

        # Test send_action_to_hvac
        self.app.send_action_to_hvac("TurnOnAc")
        mock_get.assert_called_once_with(
            self.URL + "/api/hvac/" + self.TOKEN + "/TurnOnAc/10"
        )

    # Does not work
    @patch("psycopg2.connect")
    def test_save_event_to_database(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        self.app._db_connection = mock_connect
        self.app._db_connection is not None

        # Test save_event_to_database
        self.app.save_event_to_database("2014-01-01", "10")
        mock_cursor.execute.compare(
            "INSERT INTO sensor_data (timestamp, temperature, action) VALUES (%s, %s, %s)",
            ("timestamp", "temperature", "TurnOnAc"),
        )
        mock_connect.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
