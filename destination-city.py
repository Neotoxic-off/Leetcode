class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        destinations = set()
        outgoing_cities = set()

        for path in paths:
            destinations.add(path[1])
            outgoing_cities.add(path[0])

        for destination in destinations:
            if destination not in outgoing_cities:
                return destination
