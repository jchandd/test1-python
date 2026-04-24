# Robot Delivery Team

# Collect 3 robot names and three delivery zones(Downtown, Suburbs, Industrial) from the user. Then, assign each robot to a delivery zone and print out the assignments.

# Robot names, Nova, Apex, and Bolt

# Check the total distance to be covered (integer between 5 and 500 km) if more distance then 400km then print "Distance too long, cannot assign to robot"

# Collect the weight if each robot's carge (between 1 and 50kg) (if over 50 kg then print "Overweight cargo, cannot assign to robot")

# Check if the weather conditions between Clear, Rain, and Storm are safe.( If storm is selected print unsafe conditions and do not assign to robot)

# Other wise print a summary of robot names, zones, and cargo weights with the message "Robots ready for delivery")


def get_robot_names():
    robot_names = []  # Defined robot names
    for i in range(3):
        name = input(f"Enter the name of robot {i+1}: ")  # Loop to collect robot names
        robot_names.append(name)
    return robot_names


def get_delivery_zones():
    valid_zones = ["downtown", "suburbs", "industrial"]  # Valid delivery zones
    delivery_zones = []
    for i in range(3):
        while True:
            zone = (
                input(
                    f"Enter the delivery zone for robot {i+1} (Downtown, Suburbs, Industrial): "
                )
                .strip()
                .lower()
            )  # Loop to collect delivery zones
            if zone in valid_zones:
                delivery_zones.append(
                    zone.capitalize()
                )  # Store the zone with the first letter capitalized
                break
            else:
                print("Invalid zone. Please enter Downtown, Suburbs, or Industrial.")
    return delivery_zones


def get_distance():
    while True:
        distance = int(input("Enter the total distance to be covered (1-500km): "))
        if distance > 500:
            print(
                "Distance too long, cannot assign to robot. Please enter a valid distance."
            )
        else:
            return distance


def get_cargo_weights():
    cargo_weights = []
    for i in range(3):
        while True:
            weight = int(input(f"Enter the cargo weight for robot {i+1} (1-50 kg): "))
            if weight > 50:
                print(
                    "Overweight cargo, cannot assign to robot. Please enter a valid weight."
                )
            else:
                cargo_weights.append(weight)
                break
    return cargo_weights


def get_weather_conditions():
    while True:
        condition = (
            input("Enter the weather condition (Clear, Rain, Storm): ").strip().lower()
        )
        if condition == "storm":
            print(
                "Unsafe conditions, cannot assign to robot. Please enter a valid weather condition."
            )
            exit()
        elif condition in ["clear", "rain"]:
            return condition
        else:
            print("Invalid weather condition. Please enter Clear, Rain, or Storm.")


def main():
    robot_names = get_robot_names()
    delivery_zones = get_delivery_zones()
    distance = get_distance()
    cargo_weights = get_cargo_weights()
    weather_condition = get_weather_conditions()

    print("\nSummary of Assignments:")
    for i in range(3):
        print(
            f"Robot: {robot_names[i]}, Zone: {delivery_zones[i]}, Cargo Weight: {cargo_weights[i]} kg"
        )
    print("Robots ready for delivery!")


if __name__ == "__main__":
    main()
