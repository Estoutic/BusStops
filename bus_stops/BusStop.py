class BusStop:
    def __init__(self) -> None:
        super().__init__()

    def get_bus_stop(self):
        bus_stop_distance = int(input())
        sveta_distance = int(input())
        next_of_bus_stop = max(sveta_distance // bus_stop_distance, 1)
        distance_of_near_bus_stop = bus_stop_distance * next_of_bus_stop
        previous_bus_stop = (next_of_bus_stop - 1)
        distance_of_previous_bus_stop = previous_bus_stop * bus_stop_distance
        print(min(distance_of_near_bus_stop - sveta_distance,sveta_distance - distance_of_previous_bus_stop))




