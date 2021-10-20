"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) 
formed between the hour and the minute hand.

Input: hour = 12, minutes = 30
Output: 165

Idea:
Clock has 360degrees divided by 60 minutes = each minute has 6 degrees
for 360degrees hours = 12 so each hour has 360/12 = 30 degrees

Initialize the constants: one_min_angle = 6, one_hour_angle = 30.

The angle between minute hand and 0-minutes vertical line is minutes_angle = one_min_angle * minutes.

The angle between hour hand and 12-hour vertical line is hour_angle = (hour % 12 + minutes / 60) * one_hour_angle.

Find the difference: diff = abs(hour_angle - minutes_angle).

Return the smallest angle: min(diff, 360 - diff).
"""

def angleClock(hour: int, minutes: int) -> float:
    one_min_angle = 6
    one_hour_angle = 30
    
    minutes_angle = one_min_angle * minutes
    hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
    
    diff = abs(hour_angle - minutes_angle)
    return min(diff, 360 - diff)
