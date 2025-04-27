## SunPositionFunctionLibrary Objects

```python
class SunPositionFunctionLibrary(BlueprintFunctionLibrary)
```

Sun Position Function Library

**C++ Source:**

- **Plugin**: SunPosition
- **Module**: SunPosition
- **File**: SunPosition.h

<a id="unreal.SunPositionFunctionLibrary.get_sun_position"></a>

#### get_sun_position

```python
@classmethod
def get_sun_position(cls, latitude: float, longitude: float, time_zone: float,
                     is_daylight_saving_time: bool, year: int, month: int,
                     day: int, hours: int, minutes: int,
                     seconds: int) -> SunPositionData
```

X.get_sun_position(latitude, longitude, time_zone, is_daylight_saving_time, year, month, day, hours, minutes, seconds) -> SunPositionData
Get the sun's position data based on position, date and time

Args:
    latitude (float): 
    longitude (float): 
    time_zone (float): 
    is_daylight_saving_time (bool): 
    year (int32): 
    month (int32): 
    day (int32): 
    hours (int32): 
    minutes (int32): 
    seconds (int32): 

Returns:
    SunPositionData: 

    sun_position_data (SunPositionData):

<a id="unreal.WaveTableBankFactory"></a>