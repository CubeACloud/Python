clean_city = ["karachi", "lahore", "multan", "islamabad", "pindi"]
cleanest_city = ["khan"]
one_of_the_most_cleasent_city = []
for x in clean_city: 
  for y in cleanest_city:
    one_of_the_most_cleasent_city.append(x + y)
    print(one_of_the_most_cleasent_city)
    

    mobile_name_in_pakistan = ["samsung", "Qmobile", "huwaei", "docomo", "techno", "honor"]
lowest_price_in_pakistan = input("")
pakistan = lowest_price_in_pakistan.lower()
for x in mobile_name_in_pakistan:
  if pakistan ==x:
    print("we are appriciated")
    break
  else:
     print("wrong")

     imtiaz =  ["techno", "honor", "infinix"]
for x in imtiaz:
    if "honor" == x:
        print("as")

        firstName = ["maaz", "musab", "usman", "shuraim", "sudais", "ausaf"]
lastName = ["khan"]
fullName = []
for x in firstName:
 for y in lastName:
    fullName.append(x + y)
    print(fullName)


animals = ["MONKEY", "RABIT", "Elephant", "Lion", "elegator", "cow", "goat", "camel", "turttle", "sheep", "snake"]
humans = input("")
l = humans.title()
for x in animals:
  if l ==x:
    print("we are humans")

    customer_care_centre_data = {1: "maaz",
                             6: "furqan", 
                             3: "s2 204"}
print(customer_care_centre_data[6])customer_care_centre = {1: "maaz",
                             2: "furqan", 
                             3: "s2 204"}
customer_care_centre["8"] = "meow"
print(customer_care_centre)

