## RealtimeWeatherManager Objects

```python
class RealtimeWeatherManager(Object)
```

Realtime Weather Manager

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: RealTimeWeatherManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``city_info_event`` (CityInfoEvent):  [Read-Write]
- ``weather_update_event`` (WeatherUpdateEvent):  [Read-Write] 天气更新事件

<a id="unreal.RealtimeWeatherManager.weather_update_event"></a>

#### weather\_update\_event

```python
@property
def weather_update_event() -> WeatherUpdateEvent
```

(WeatherUpdateEvent):  [Read-Write] 天气更新事件

<a id="unreal.RealtimeWeatherManager.weather_update_event"></a>

#### weather\_update\_event

```python
@weather_update_event.setter
def weather_update_event(value: WeatherUpdateEvent) -> None
```

<a id="unreal.RealtimeWeatherManager.city_info_event"></a>

#### city\_info\_event

```python
@property
def city_info_event() -> CityInfoEvent
```

(CityInfoEvent):  [Read-Write]

<a id="unreal.RealtimeWeatherManager.city_info_event"></a>

#### city\_info\_event

```python
@city_info_event.setter
def city_info_event(value: CityInfoEvent) -> None
```

<a id="unreal.RealtimeWeatherManager.set_sky_weather_sync_is_allowed"></a>

#### set\_sky\_weather\_sync\_is\_allowed

```python
def set_sky_weather_sync_is_allowed(is_allowed: bool) -> None
```

x.set_sky_weather_sync_is_allowed(is_allowed) -> None
设置是否开启天气与天空球同步

Args:
    is_allowed (bool):

<a id="unreal.RealtimeWeatherManager.set_realtime_weather_timer_is_allowed"></a>

#### set\_realtime\_weather\_timer\_is\_allowed

```python
def set_realtime_weather_timer_is_allowed(is_allowed: bool) -> None
```

x.set_realtime_weather_timer_is_allowed(is_allowed) -> None
设置是否开启定时获取实时天气

Args:
    is_allowed (bool):

<a id="unreal.RealtimeWeatherManager.set_realtime_request_url"></a>

#### set\_realtime\_request\_url

```python
def set_realtime_request_url(url: str) -> None
```

x.set_realtime_request_url(url) -> None
设置实时天气获取基础URL

Args:
    url (str):

<a id="unreal.RealtimeWeatherManager.set_realtime_request_gap_in_seconds"></a>

#### set\_realtime\_request\_gap\_in\_seconds

```python
def set_realtime_request_gap_in_seconds(seconds: float) -> None
```

x.set_realtime_request_gap_in_seconds(seconds) -> None
设置实时天气获取间隔时间，单位：秒

Args:
    seconds (float):

<a id="unreal.RealtimeWeatherManager.set_realtime_city"></a>

#### set\_realtime\_city

```python
def set_realtime_city(city: str) -> None
```

x.set_realtime_city(city) -> None
设置实时天气获取对应城市

Args:
    city (str):

<a id="unreal.RealtimeWeatherManager.set_city_id_list_request_url"></a>

#### set\_city\_id\_list\_request\_url

```python
def set_city_id_list_request_url(url: str) -> None
```

x.set_city_id_list_request_url(url) -> None
设置获取城市Id列表基础URL

Args:
    url (str):

<a id="unreal.RealtimeWeatherManager.request_current_weather"></a>

#### request\_current\_weather

```python
def request_current_weather(city: str = "") -> None
```

x.request_current_weather(city="") -> None
请求实时天气

Args:
    city (str):

<a id="unreal.RealtimeWeatherManager.request_city_info"></a>

#### request\_city\_info

```python
def request_city_info(city: str = "") -> None
```

x.request_city_info(city="") -> None
请求城市Id

Args:
    city (str):

<a id="unreal.RealtimeWeatherManager.get_sky_weather_sync_is_allowed"></a>

#### get\_sky\_weather\_sync\_is\_allowed

```python
def get_sky_weather_sync_is_allowed() -> bool
```

x.get_sky_weather_sync_is_allowed() -> bool
获取是否开启天气与天空球同步

Returns:
    bool:

<a id="unreal.RealtimeWeatherManager.get_realtime_weather_timer_is_allowed"></a>

#### get\_realtime\_weather\_timer\_is\_allowed

```python
def get_realtime_weather_timer_is_allowed() -> bool
```

x.get_realtime_weather_timer_is_allowed() -> bool
获取是否开启定时获取实时天气

Returns:
    bool:

<a id="unreal.RealtimeWeatherManager.get_realtime_request_url"></a>

#### get\_realtime\_request\_url

```python
def get_realtime_request_url() -> str
```

x.get_realtime_request_url() -> str
获取实时天气获取基础URL

Returns:
    str:

<a id="unreal.RealtimeWeatherManager.get_realtime_request_gap_in_seconds"></a>

#### get\_realtime\_request\_gap\_in\_seconds

```python
def get_realtime_request_gap_in_seconds() -> float
```

x.get_realtime_request_gap_in_seconds() -> float
获取实时天气获取间隔时间，单位：秒

Returns:
    float:

<a id="unreal.RealtimeWeatherManager.get_realtime_city"></a>

#### get\_realtime\_city

```python
def get_realtime_city() -> str
```

x.get_realtime_city() -> str
获取实时天气获取对应城市

Returns:
    str:

<a id="unreal.RealtimeWeatherManager.get_city_info_request_url"></a>

#### get\_city\_info\_request\_url

```python
def get_city_info_request_url() -> str
```

x.get_city_info_request_url() -> str
获取城市Id列表基础URL

Returns:
    str:

<a id="unreal.WdpEnvironmentFunctionLibrary"></a>