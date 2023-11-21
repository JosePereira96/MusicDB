import os
import googleapiclient.discovery

from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
data = config['youtube']


def connect():
	# Disable OAuthlib's HTTPS verification when running locally.
	# *DO NOT* leave this option enabled in production.
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

	api_service_name = "youtube"
	api_version = "v3"
	DEVELOPER_KEY = data['developerKey']

	youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

	return youtube

