## RealtimeWeatherData Objects

```python
class RealtimeWeatherData(StructBase)
```

Realtime Weather Data

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherServiceDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``air`` (WeatherAirData):  [Read-Write]
- ``current_weather`` (WeatherCurrentData):  [Read-Write]
- ``location`` (WeatherLocationData):  [Read-Write]

<a id="unreal.RealtimeWeatherData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    location: WeatherLocationData = [
        "WTW3SJ5ZBJUY", "上海", "CN", "上海,上海,中国", "Asia/Shanghai", "+08:00"
    ],
    current_weather: WeatherCurrentData = [
        "晴", 0, 10, 9, 1028.000000, 24, 100.000000, "东", 94, 2.000000, 1.000000
    ],
    air: WeatherAirData = [57, 40, 49, 12, 43, 0.700000, 72, "PM25", "￨ﾉﾯ"]
) -> None
```

<a id="unreal.RealtimeWeatherData.location"></a>

#### location

```python
@property
def location() -> WeatherLocationData
```

(WeatherLocationData):  [Read-Write]

<a id="unreal.RealtimeWeatherData.location"></a>

#### location

```python
@location.setter
def location(value: WeatherLocationData) -> None
```

<a id="unreal.RealtimeWeatherData.current_weather"></a>

#### current\_weather

```python
@property
def current_weather() -> WeatherCurrentData
```

(WeatherCurrentData):  [Read-Write]

<a id="unreal.RealtimeWeatherData.current_weather"></a>

#### current\_weather

```python
@current_weather.setter
def current_weather(value: WeatherCurrentData) -> None
```

<a id="unreal.RealtimeWeatherData.air"></a>

#### air

```python
@property
def air() -> WeatherAirData
```

(WeatherAirData):  [Read-Write]

<a id="unreal.RealtimeWeatherData.air"></a>

#### air

```python
@air.setter
def air(value: WeatherAirData) -> None
```

<a id="unreal.WeatherAirData"></a>