weather = input("What's the weather like today? (sunny/rainy/cold):"
).lower()
if weather == "cold":
    print ("Make sure to wear a warm coat and a scarf.")
if weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
else:  
  print("Sorry, I don't have recommendations for this weather.")
