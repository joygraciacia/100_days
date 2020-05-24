moon_multiple = 16.5/100

def main():
 	
    earth_weight = input("Enter a weight on earth:")

    earth_weight = float(earth_weight)

    moon_weight = round((earth_weight * moon_multiple),1)

    moon_weight = str(moon_weight)
		

    print('Equivalent weight on the moon:' + moon_weight)


main();


# def main():

#     dictionary = {}

#     dictionary["learning"] = "awesome"

#     dictionary["coding"] = "fun"

#     for i in dictionary:
#     	print(dictionary[i])


# main();