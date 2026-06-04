class Driver:
    def __init__(self,name,distance):
        self.name=name
        self.distance=distance
drivers=[
    Driver("Driver1",5),
    Driver("Driver2",2),
    Driver("Driver3",8),
    Driver("Driver4",3)
]
nearest=drivers[0]
for driver in drivers:
    if driver.distance< nearest.distance:
        nearest=driver
print("Nearest Driver:",nearest.name)
print("Distance:",nearest.distance,"km")