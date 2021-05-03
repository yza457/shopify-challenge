import tornado.ioloop
import tornado.web
import requests
import os
from db import MockDb

# covert a list of dictionaries to a list of list
def to_product_list(db_connection, product_images):
  res = []

  for one_product in product_images:
    one_product_list = []
    for key in db_connection.columns:
      one_product_list.append(one_product[key])
    res.append(one_product_list)
  
  return res

# get keywords in input image and return relevant product images
def find_simiar_products(input_url):
  # use an external API to recognize product from the image with input_url
  # the credentials should be stored somewhere safe if this is not a coding challenge 
  api_id = '1jnMGJikcuIDtXePwMrFkM5V'
  api_key = 'QRYLBB7IwLo7QrVwOw64tXNCKt8DvfApoSA3OcFzaoClwBFv'
  params = {'url': input_url, 'num_keywords': 10}
  keywords = requests.get('https://api.everypixel.com/v1/keywords', params=params, auth=(api_id, api_key)).json()

  # return empty list if api request returns error
  if ("keywords" not in keywords):
    return []
  
  # extract recognition result from keywords
  recognition_result = [one_keyword["keyword"] for one_keyword in keywords["keywords"]]

  # query the database to get simiar product images
  db_connection = MockDb()
  product_images = db_connection.select_category(recognition_result)

  # Tornado templating language only support python lists
  product_images_list = to_product_list(db_connection, product_images)

  return product_images_list

class MainHandler(tornado.web.RequestHandler):
  # inital render
  def get(self):
    self.render("index.html", input_url="")

  # render page after hitting search button
  def post(self):
    input = self.get_argument("input", None)
    if input is not None:
      print("input is " + input)
      products = find_simiar_products(input)
      self.render("index.html", input_url=input, result=products, cwd = os.getcwd())

if __name__ == "__main__":
  # map handler for index.html and static file handler
  app = tornado.web.Application([
    (r"/", MainHandler),
    (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {"path": "./images/"}),
  ], debug = True)

  app.listen(8888)
  print("Server started!")
  tornado.ioloop.IOLoop.current().start()