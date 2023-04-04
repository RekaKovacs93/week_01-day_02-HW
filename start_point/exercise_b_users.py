users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return a list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary

users["Jonathan"]["twitter"]
users["Erik"]["home_town"]
users["Erik"]["lottery_numbers"]
users["Avril"]["pets"][0]["species"]
users["Erik"]["lottery_numbers"][2]


list_of_nums = users["Avril"]["lottery_numbers"]
list_of_even_nums = []

for num in list_of_nums:
    if num % 2 == 0:
        list_of_even_nums.append(num)
        

users["Erik"]["lottery_numbers"].append(7)
users["Erik"]["home_town"] = "Edinburgh"
users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})
users["Jenny"] = {
    "twitter": "jens",
    "lottery_numbers": [15, 11, 38, 30, 5, 2],
    "home_town": "Newcastle",
    "pets": [
      {
        "name": "fiffy",
        "species": "hamster"
      }
    ]
  }
print(users["Jenny"])
