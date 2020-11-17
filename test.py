try:
    from run import app
    import unittest 

except Exception as e:
    print("Some modules are missing {} ".format(e))

class FlaskTestApi(unittest.TestCase):
    """
    This class runs some unit tests to check the performance of rest api.
    """
    # check for the status code and json response
    def test_response(self):
        tester = app.test_client(self)
        response = tester.post("/detect_glare", json = {
            "lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2
        })
        json_data = response.get_json()
        statuscode = response.status_code
        self.assertEquals(statuscode, 200)
        self.assertEquals(json_data, {"glare": False})


if __name__ == "__main__":
    unittest.main()