class BusStop:
    def __init__(self) -> None:
        super().__init__()

    def get_bus_stop(self):
        bus_stop_distance = int(input())
        sveta_distance = int(input())
        count_of_bus_stop = sveta_distance // bus_stop_distance
        distance_of_near_bus_stop = bus_stop_distance * count_of_bus_stop
        distance_from_sveta_to_near_bus_stop = distance_of_near_bus_stop - sveta_distance
        print(abs(distance_from_sveta_to_near_bus_stop))


