import argparse

from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import pymongo
import pandas as pd

db = pymongo.MongoClient('localhost', 27017)
parser = argparse.ArgumentParser()
parser.add_argument("hotelId", help="Enter the name of location or city you want to insert")
args = parser.parse_args()
hotel_Id = int(args.hotelId)
print hotel_Id


def data_convertion():
    # print hotel_Id
    # location_for_hotelid = ()
    location_based_on_hotelId = list(db.CT.Hotels.find({'hotel_id': int(hotel_Id)}, {'loc_id': 1, '_id': 0}))
    # print location_based_on_hotelId[0]['loc_id']
    # hoteldetails = list(
    #     db.CT.Hotels.find({'loc_id': location_based_on_hotelId[0]['loc_id']}, {'hotel_id': 1, 'lat_lng': 1, '_id': 0}))
    # for i in range(0, len(hoteldetails)):
    #     if hoteldetails[i]['hotel_id'] == hotel_Id:
    #         location_for_hotelid = (float(hoteldetails[i]['lat_lng'][0]), float(hoteldetails[i]['lat_lng'][1]))
    #     locations_allhotels = (float(hoteldetails[i]['lat_lng'][0]), float(hoteldetails[i]['lat_lng'][1]))
    #     distance = vincenty(location_for_hotelid, locations_allhotels).kilometers
    #     db.CT.Hotels.update({"hotel_id": hoteldetails[i]['hotel_id']}, {"$set": {"Distance": distance}})
    # print "end of the data_covertion"
    hoteldetails_updated = db.CT.Hotels.find({'loc_id': location_based_on_hotelId[0]['loc_id']},
                                             {'hotel_id':1,'hotel_name':1,'capacity':1,'Distance':1,'_id':0})
    read_data(hoteldetails_updated)


def read_data(hoteldetails):
    df = pd.DataFrame(list(hoteldetails))
    print df.head()
    print "read data function called with updated data "


if __name__ == "__main__":
    data_convertion()
