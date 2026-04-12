## WdpEnvironmentAPI Objects

```python
class WdpEnvironmentAPI(StandardApiClassBase)
```

Wdp Environment API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpEnvironmentAPI.h

<a id="unreal.WdpEnvironmentAPI.set_skylight_time"></a>

#### set\_skylight\_time

```python
def set_skylight_time(time_of_day_param: SkylightTime) -> Optional[ResultBase]
```

x.set_skylight_time(time_of_day_param) -> ResultBase or None
APIs

Args:
    time_of_day_param (SkylightTime): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpEnvironmentAPI.set_scene_weather"></a>

#### set\_scene\_weather

```python
def set_scene_weather(weather_param: SceneWeather) -> Optional[ResultBase]
```

x.set_scene_weather(weather_param) -> ResultBase or None
Set Scene Weather

Args:
    weather_param (SceneWeather): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpEnvironmentAPI.process_weather_update"></a>

#### process\_weather\_update

```python
def process_weather_update(realtime_weather_data: RealtimeWeatherData) -> None
```

x.process_weather_update(realtime_weather_data) -> None
Process Weather Update

Args:
    realtime_weather_data (RealtimeWeatherData):

<a id="unreal.WdpEnvironmentAPI.get_skylight_time"></a>

#### get\_skylight\_time

```python
def get_skylight_time(param: ParamsBase) -> Optional[SkylightTimeResult]
```

x.get_skylight_time(param) -> SkylightTimeResult or None
Get Skylight Time

Args:
    param (ParamsBase): 

Returns:
    SkylightTimeResult or None: 

    out_result (SkylightTimeResult):

<a id="unreal.WdpEnvironmentAPI.get_scene_weather"></a>

#### get\_scene\_weather

```python
def get_scene_weather(param: ParamsBase) -> Optional[SceneWeatherResult]
```

x.get_scene_weather(param) -> SceneWeatherResult or None
Get Scene Weather

Args:
    param (ParamsBase): 

Returns:
    SceneWeatherResult or None: 

    out_result (SceneWeatherResult):

<a id="unreal.WdpEnvironmentEntity"></a>