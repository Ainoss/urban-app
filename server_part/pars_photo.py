from instagram.client import InstagramAPI
from string import find
from time import time
from record import *
import requests
import urllib2
import json
#access_token = "1693106172.b2eb1f7.1182a054c2854a8cb7487ad39f19ef7d"
#api = InstagramAPI(access_token=access_token)
#https://api.instagram.com/v1/media/search?lat=55.756168&lng=37.621852&count=100000&min_timestamp=1429992000&max_timestamp=1430006400&access_token=1693106172.b2eb1f7.1182a054c2854a8cb7487ad39f19ef7d


#def coverage_area(lat1,lng1,lat2,lng2):

one_meter_in_degrees = 0.000014


def from_degrees_to_meters( degree):
    return float(degree)/one_meter_in_degrees

def from_meters_to_degrees( meters):
    return float(meters)*one_meter_in_degrees

def get_effective_radius(radius):
    return 0.7071*radius

def is_no_out_of_range(lat, lng, center_lat, center_lng, radius):
    shift = from_meters_to_degrees(get_effective_radius(radius))
    min_lat = float(center_lat) - shift
    max_lat = float(center_lat) + shift
    min_lng = float(center_lng )- shift
    max_lng = float(center_lng) + shift
    boole = ( float(min_lat) < float(lat)) and ( float(max_lat) > float(lat)) and ( float(min_lng) < float(lng)) and ( float(max_lng) > float(lng))
    return boole

def step(radius):
    return 2*from_meters_to_degrees(get_effective_radius(radius))

def get_lat(string):
    i = find( string, '(')
    j = find(string,',')
    lat = string[i + 1:j]
    return lat

def get_lng(string):
    i = find(string,',')
    j = find(string,")")
    lng = string[i+2:j]
    return lng

def send_to_server(post, weight):
    record = Record()
    record.latitude = post["location"]["latitude"]
    record.longitude = post["location"]["longitude"]
    if post.caption:
        record.message = post["caption"]["text"].encode('utf-8')
    record.url = post["images"]["standard_resolution"]["url"]
    record.time = time()
    record.weight = weight
    set_record(record)


def parse_info2(center_lat, center_lng, resent_media, radius, i):
    instagram_url = "https://api.instagram.com/v1/media/search?"
    instagram_url = instagram_url + "lng=" + str(center_lng)
    instagram_url = instagram_url + "&lat=" + str(center_lat)
    instagram_url = instagram_url + "&count=" + str(100000)
    instagram_url = instagram_url + "&min_timestamp=" + str(1429992000)
    instagram_url = instagram_url + "&access_token=" + str("1693106172.b2eb1f7.1182a054c2854a8cb7487ad39f19ef7d")
    encoded_data = urllib2.urlopen(instagram_url).read()
    data = json.loads(encoded_data)["data"]
    print data
    for post in data:
        print "--------"
        print post["created_time"]
        print post["images"]["standard_resolution"]["url"]
        #print "likes = "+ str(media.likes) + " count = " + str(len(media.likes)) + "\n"
        if post["location"]:
            lat = post["location"]["latitude"]
            lng = post["location"]["longitude"]
            weight = 300.0/(data[-1]["created_time"] - data[0]["created_time"])*100
            if weight < 0:
                weight = -weight
            send_to_server(post, weight)

def parse_info(center_lat, center_lng, resent_media, radius, i):
    for media in resent_media:
        if media.location:
            lat = get_lat(str(media.location.point))
            lng = get_lng(str(media.location.point))
            if is_no_out_of_range(lat, lng, center_lat, center_lng, radius):
                send_to_server(media)
                if media.caption:
                    hashtags = media.caption.text.encode("utf-8")


def cover_area( lat1,lng1,lat2,lng2,radius,min_timestamp,max_timestamp):
    i = 0
    api = InstagramAPI(client_id='b2eb1f7863244ca2b8ae463810be93c7', client_secret='0c0f0f2bc28c4181a188d006243a0679')
    tmp_lat = lat1
    tmp_lng = lng1
    while ( tmp_lng < lng2 ):
        while( tmp_lat < lat2):
            resent_media = api.media_search(count="100", lat=str(tmp_lat), lng=str(tmp_lng), min_timestamp=str(min_timestamp), max_timestamp=str(max_timestamp),distance=str(radius))
            parse_info2(tmp_lat, tmp_lng, resent_media, radius, i)
            tmp_lat = tmp_lat + step(radius)
            i = i + 1
        tmp_lat = lat1
        tmp_lng = tmp_lng + step(radius)


def start_getting_photos():
    lat1 = 55.589650 
    lng1 = 37.401545
    lat2 = 55.911938
    lng2 = 37.842371
    radius = 5000

    min_timestamp = 1429920000
    max_timestamp = 1430000300
    while ( min_timestamp < max_timestamp ):
        print "PHOTO"
        cover_area( lat1,lng1,lat2,lng2,radius,min_timestamp,min_timestamp + 300)
        min_timestamp = min_timestamp + 300


#if __name__ == '__main__':
#    start_getting_photos()


