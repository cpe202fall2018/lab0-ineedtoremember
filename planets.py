def weight_on_planets():
    x = int(input("What do you weigh on earth? "))
    mars = x*0.38
    jupiter = x*2.34
    print ("\nOn Mars you would weigh", mars, "pounds.", "\nOn Jupiter you would weigh", jupiter, "pounds.")

if __name__ == '__main__':
   weight_on_planets()