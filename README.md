# Detect-Flare

It is a Flask based restful api that process the metadata requests and determines if there is a possibility of direct glare in the associated image
or not. We assume there is a possibility of direct glare if:

- Azimuthal difference between sun and the direction of the car travel (and hence the
direction of forward- facing camera) is less than 30 degrees AND
- Altitude of the sun is less than 45 degrees.

Please follow the steps below to setup the environment and calling the api.

## Create a conda environment
conda create --name glarenv <br>
conda activate glarenv

## Install libraries
pip install -r requirements.txt

## Start the server
Run the following command to start the server:
python run.py <br>
The server will start on the address http://127.0.0.1:5000 [if port 5000 is not occupied]

## Call REST API
Open a terminal in Linux and type the following command:

curl -H "Content-Type: application/json" -X POST -d '{"lat": 49.2699648, "lon": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2}' http://127.0.0.1:5000/detect_glare

