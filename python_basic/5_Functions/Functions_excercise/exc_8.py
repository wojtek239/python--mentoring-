def get_angle(**kwargs: float) -> float:
    """
    to calculate angle between clock hands
    """
    hour = kwargs.get("hour", 0)
    minute = kwargs.get("minute", 0)

    hour_angle = (hour % 12 + minute / 60) * 30
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)

    return angle


angle = get_angle(hour=9, minute=45)
print(f'angle between hands is: {angle}')
