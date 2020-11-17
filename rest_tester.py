try:
    from run import app
    import unittest 

except Exception as e:
    print("Some modules are missing {} ".format(e))

class TestRestApi(unittest.TestCase):
    """
    This class runs some mandatory unit tests to check the performance of rest api.
    """
    # check valid status code (200) and json response
    def test_response(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
            "lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2
        })
        json_data = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(json_data, {"glare": False})

    # check if content return is application/json
    def test_content_return(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
            "lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2
        })
        data_type = response.content_type
        self.assertEqual(data_type, "application/json")

    # check for invaild latitude (above limit), raise value error
    def test_input_lat_one(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": 91.0, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: lat out of range = [0 to 90]"})

    # check for invaild latitude (below limit), raise value error
    def test_input_lat_two(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": -11.0, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: lat out of range = [0 to 90]"})

    # check for invaild longitude(below limit), raise value error
    def test_input_lon_one(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": 49.2699648, "lon": -181.23, "epoch": 1588704959.321, "orientation": -10.2})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: lon out of range = [-180 to 180]"})

    # check for invaild longitude(above limit), raise value error
    def test_input_lon_two(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": 49.2699648, "lon": 181.23, "epoch": 1588704959.321, "orientation": -10.2})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: lon out of range = [-180 to 180]"})

    # check for invaild epoch (negative value), raise value error
    def test_input_epoch(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": 49.2699648, "lon": -123.1290368, "epoch": -1588704959.321, "orientation": -10.2})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: epoch out of range = [epoch > 0]"})

    # check for invalid orientation(below limit), raise value error
    def test_input_orientation_one(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -181})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: orientation out of range = [-180 to 180]"})

    # check for invalid orientation(above limit), raise value error
    def test_input_orientation_two(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
        "lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": 181})
        json_data = response.get_json()
        self.assertEqual(json_data, {"Error": "ValueError: orientation out of range = [-180 to 180]"})


if __name__ == "__main__":
    unittest.main()