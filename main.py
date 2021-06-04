from plexapi.server import PlexServer
import credentials
import json
import requests

def post_sensor(sensor,data):
    headers = {"Authorization": "Bearer "+credentials.api_token,
               'content-type': 'application/json'}

    url = credentials.api_url+"/api/states/"+sensor
    #data = '{"state": "1", "attributes": {"unit_of_measurement": "Miles"}}'
    response = requests.post(url, headers=headers, data=data)
    print("Posting Sensor: ",sensor)
    #print(response.text)



baseurl = credentials.plex_host+":"+credentials.plex_port
token = credentials.plex_token
plex = PlexServer(baseurl, token)


tv_shows = plex.library.section('TV Shows')
movies = plex.library.section('Movies')

sensor = {}
sensor['attributes'] = {}
sensor['state'] = tv_shows.totalViewSize(libtype='episode')
sensor['attributes']['show_count'] = tv_shows.totalSize
post_sensor("sensor.plex_tv_count",json.dumps(sensor))

sensor = {}
sensor['attributes'] = {}
sensor['state'] = movies.totalSize
post_sensor("sensor.plex_movies_count",json.dumps(sensor))
