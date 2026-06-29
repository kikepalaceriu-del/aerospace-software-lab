def analyze_flight(flight):
    result = {
        "max_altitude": flight["altitude"].max(),
        "max_speed": flight["speed"].max(),
        "avg_speed": flight["speed"].mean(),
        "total_time": flight["time"].max(),
        "altitude_gain": flight["altitude"].iloc[-1] - flight["altitude"].iloc[0],
    }

    return result


    
    

    