# a mock of database
class MockDb:
  def __init__(self):
    self.storage = storage
    self.columns = ["id", "name", "category", "url"]

  # retrieve product images in storage
  # if product categories is in input_categories
  def select_category(self, input_categories):
    res = []
    for category in input_categories:
      for product in self.storage:
        if product["category"] == category:
          res.append(product)
    
    return res

# storage of product images
storage = [
  {
    "id" : 0,
    "name" : "awesome brand 1",
    "category" : "blender",
    "url" : "blender_1.jpg"
  },
  {
    "id" : 1,
    "name" : "awesome brand 2",
    "category" : "blender",
    "url" : "blender_2.jpg"
  },
  {
    "id" : 2,
    "name" : "awesome brand 3",
    "category" : "blender",
    "url" : "blender_3.jpg"
  },
  {
    "id" : 3,
    "name" : "coffee maker brand 1",
    "category" : "coffee maker",
    "url" : "coffee_maker_1.jpg"
  },
  {
    "id" : 4,
    "name" : "coffee maker brand 2",
    "category" : "coffee maker",
    "url" : "coffee_maker_2.jpg"
  },
  {
    "id" : 5,
    "name" : "coffee maker brand 3",
    "category" : "coffee maker",
    "url" : "coffee_maker_3.jpg"
  },
    {
    "id" : 6,
    "name" : "smart toaster brand 1",
    "category" : "toaster",
    "url" : "toaster_1.jpg"
  },
  {
    "id" : 7,
    "name" : "smart toaster brand 2",
    "category" : "toaster",
    "url" : "toaster_2.jpg"
  },
  {
    "id" : 8,
    "name" : "smart toaster brand 3",
    "category" : "toaster",
    "url" : "toaster_3.jpg"
  }
]