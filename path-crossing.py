class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        x = 0
        y = 0
        mapping = {
            "N": {
                "x": 0,
                "y": 1
            },
            "S": {
                "x": 0,
                "y": -1
            },
            "E": {
                "x": 1,
                "y": 0
            },
            "W": {
                "x": -1,
                "y": 0
            }
        }

        seen.add((x, y))
        for i in path:
            x += mapping[i]["x"]
            y += mapping[i]["y"]

            point = (x, y)

            if (point in seen):
                return True
            seen.add(point)
        return (False)
