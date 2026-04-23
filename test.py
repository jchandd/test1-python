# Robot Delivery Team
# Collect 3 robot names and three delivery zones(Downtown, Suburbs, Industrial) from the user. Then, assign each robot to a delivery zone and print out the assignments.
# Robot names, Nova, Apex, and Bolt
# Check the total distance to be covered (integer between 5 and 500 km) if more distance then 400km then print "Distance too long, cannot assign to robot"
# Collect the weight if each robot's carge (between 1 and 50kg) (if over 50 kg then print "Overweight cargo, cannot assign to robot")
# Check if the weather conditions between Clear, Rain, and Storm are safe.( If storm is selected print unsafe conditions and do not assign to robot)
# Other wise print a summary of robot names, zones, and cargo weights with the message "Robots ready for delivery")


def get_robot_names():
    robot_names = []
    for i in range(3):  #
        name = input(f"Enter the name of robot {i+1}: ")  # Loop to collect robot names
        robot_names.append(name)
    return robot_names


def get_delivery_zones():
    zones = []
    for i in range(3):  # Loop to collect delivery zones for each robot
        zone = input(
            f"Enter the delivery zone for robot {i+1} (Downtown, Suburbs, Industrial): "
        )
        zones.append(zone)
    return zones


def get_distance():
    distance = int(input("Enter the total distance to be covered (5-500 km): "))
    if distance > 400:
        print("Distance too long, cannot assign to robot")
        return None
    return distance
