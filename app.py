#!flask/bin/python
from flask import Flask, request
from flask_restful import Resource, Api
from date_utils import UtcDateTimeUtils
from glare_utils import CoordinationUtils


app = Flask(__name__)
api = Api(app)

def to_float(input, var_name):
    try:
        return float(input)
    except:
        raise TypeError(str.format("TypeError: %s with value %s can't be converted to float." % (var_name, input)))

class IdentifyGlareImage(Resource):

    def post(self):
        try:
            some_json = request.get_json()
            # import pdb; pdb.set_trace()
            lat = to_float(some_json['lat'], 'lat')
            lon = to_float(some_json['lon'], 'lon')
            epoch = to_float(some_json['epoch'], 'epoch')
            orientation = to_float(some_json['orientation'], 'orientation')

            if (lat < 0 or lat > 90):
                raise ValueError("ValueError: lat out of range = [0 to 90]")
            elif (lon < -180 or lon > 180):
                raise ValueError("ValueError: lon out of range = [-180 to 180")
            elif (orientation < -180 or orientation > 180):
                raise ValueError("ValueError: orientation out of range = [-180 to 180]")
            elif (epoch < 0):
                raise ValueError("ValueError: epoch out of range = [epoch > 0]")
            else:
                # functionality
                date_utils = UtcDateTimeUtils()
                coord_utils = CoordinationUtils(date_utils, lat, lon, epoch, orientation)
                
                return ({'glare': coord_utils.detect_glare()})
        
        except Exception as e:
            print(e)
            return ({'Error': str(e)})

api.add_resource(IdentifyGlareImage, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)



    