import astropy.coordinates as SkyCoord
import astropy.units as u
from astropy.time import Time
# from astropy.utils import iers

# constants
AZIMUTHAL_DIFF_LIMIT = 30
SUN_ALTITUDE_LIMIT = 45


class CoordinatesUtils():
    """
    This class is created to compute glare detection
    """
    def __init__(self, date_utils, lat, long, epoch, orientation):
        try:
            # set mirror for astropy library
            # iers.Conf.iers_auto_url.set('ftp://cddis.gsfc.nasa.gov/pub/products/iers/finals2000A.all')

            # injecting dateutils library to the class
            self.date_utils = date_utils

            # set location and datetime of the picture in astropy format
            self.image_location = SkyCoord.EarthLocation(lat=lat * u.deg, lon=long * u.deg)
            self.image_datetime = Time(self.date_utils.fetch_utc_datetime(epoch))
            # default values
            self.azimuth = 0
            self.altitude = 0
            self.orientation = orientation

            # Determines the location of the sun at a given time (or times, if the input is an array Time object), in geocentric coordinates.
            self.sun = SkyCoord.get_sun(self.image_datetime)
           
        except Exception as e:
            raise e

    def __calculate_azimuth_and_altitude(self):
        """
        calculate azimuth and altitude based on earth location and datetime of the image
        """
        try:
            alt_and_az = SkyCoord.AltAz(location=self.image_location, obstime=self.image_datetime)
            self.altitude = self.sun.transform_to(alt_and_az).alt.degree
            self.azimuth = self.sun.transform_to(alt_and_az).az.degree
        except Exception as e:
            raise e

    # this function is used to compute if glare exist or not
    def detect_glare(self):
        """
        Returns True if glare is detected in the image.
        """
        try:
            self.__calculate_azimuth_and_altitude()

            # convert orientation to [0-360] degree format
            temp_orientation = (self.orientation + 360) % 360         

            # compute the minimum difference between azimuth and orientation
            phi = abs(self.azimuth - temp_orientation) % 360 
            if (phi > 180):
                azimuth_distance = 360 - phi
            else:
                azimuth_distance = phi

            # Return True if condition satisfies
            if (azimuth_distance <= AZIMUTHAL_DIFF_LIMIT and self.altitude <= SUN_ALTITUDE_LIMIT and self.altitude > 0):
                return True

            return False
        except Exception as e:
            raise e