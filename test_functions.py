import pytest
from db import MockDb
from server import to_product_list

test_db_connection = MockDb()

def test_server_to_product_list():
  # the order of the keys in input_dict should be preserved
  input_dict = [
    {
      "id" : 0,
      "name" : "awesome brand 1",
      "category" : "blender",
      "url" : "blender_1.jpg"
    },
    {
      "id" : 2,
      "name" : "awesome brand 3",
      "category" : "blender",
      "url" : "blender_3.jpg"
    }
  ]
  expected = [
    [0, "awesome brand 1", "blender", "blender_1.jpg"],
    [2, "awesome brand 3", "blender", "blender_3.jpg"],
  ]
  assert to_product_list(test_db_connection, input_dict) == expected

  # empty input_dict should return empty list
  input_dict = []
  expected = []
  assert to_product_list(test_db_connection, input_dict) == expected

def test_db_select_category():
  # nonexisting category name should return empty list
  input_categories = ["nonexisting"]
  expected = []
  assert test_db_connection.select_category(input_categories) == expected

  # products of the same category should be returned
  input_categories = ["blender"]
  expected = [
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
    }
  ]
  assert test_db_connection.select_category(input_categories) == expected

  # if multiple categories are provided, corresponding products should be returned
  input_categories = ["blender", "toaster"]
  expected =  [
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
  assert test_db_connection.select_category(input_categories) == expected