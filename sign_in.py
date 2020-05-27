import tweepy
import json

with open("token.json","r") as f:
  tokens = json.load(f)

ck = tokens["API_key"]
cks = tokens["API_key_secret"]
at = tokens["Access_token"]
ats = tokens["Access_token_secret"]

def sign_in():
  auth = tweepy.OAuthHandler(ck,cks)
  auth.set_access_token(at,ats)
  return tweepy.API(auth)
