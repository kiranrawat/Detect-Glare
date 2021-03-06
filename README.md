# Detect-Flare

Flask based restful api that process the metadata requests and determines if there is a possibility of direct glare in the associated image or not. We assume there is a possibility of direct glare if:

1. Azimuthal difference between sun and the direction of the car travel (and hence the
direction of forward- facing camera) is less than 30 degrees AND <br>
2. Altitude of the sun is less than 45 degrees.

Please follow the steps below to setup the environment,calling and testing the rest api.

## Assumption

I have not considered negative altitudes as glare because a negative value means below the horizon, so the sun wouldn't even be there to have a glare condition.

## Create a conda environment
conda create --name glarenv <br>
conda activate glarenv

## Install libraries
pip install -r requirements.txt

## Start the server
Start flask rest server (rest server run on localhost:5000): `python run.py`
The server will start on the address http://127.0.0.1:5000 [if port 5000 is not occupied]

## Call REST API
Open a terminal in Linux and type the following command:

curl -H "Content-Type: application/json" -X POST -d '{"lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2}' http://127.0.0.1:5000/detect_glare

## To execute unit tests:

1. Start flask rest server (rest server run on localhost:5000): `python run.py` <br>
2. Run unittest: `python rest_tester.py`

