
def estimate_trip_cost(num_stops: int) -> str:
    if num_stops <= 2:
        return "$ Budget-friendly trip with minimal stops"
    elif num_stops <= 4:
        return "$$ Moderate cost with several points of interest"
    else:
        return "$$$ Premium trip with multiple stops and extended duration"
