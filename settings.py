# import several components
from components.article import article
from components.collection import collection
from components.people import people
from components.photo import photo
from components.tag import tag

# env variables
from env import ENV

MONGO_HOST = ENV['MONGO_HOST']
MONGO_PORT = ENV['MONGO_PORT']
MONGO_USERNAME = ENV['MONGO_USERNAME']
MONGO_PASSWORD = ENV['MONGO_PASSWORD']
MONGO_DBNAME = ENV['MONGO_DBNAME']

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
  'article': article,
  'collection': collection,
  'people': people,
  'photo': photo,
  'tag': tag
}