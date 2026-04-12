## WeatherControlManager Objects

```python
class WeatherControlManager(Object)
```

brief: 注意这里的WeatherTime主要用来控制天空光照，同时天空光照又受天气影响

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherControlManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current_time_of_day_notify_event`` (CurrentTimeOfDayNotifyEvent):  [Read-Write] 当前天空球环境对应时间事件，主要用于天空球环境渐变过程中通知其他对象，当前环境对应的实际时间
- ``current_time_section_notify_event`` (CurrentTimeSectionNotifyEvent):  [Read-Write] 当前天空球环境对应时间段事件，主要用于天空球环境渐变过程中通知其他对象，当前环境对应的实际时间段
- ``target_weather_description_update_event`` (TargetWeatherDescriptionUpdateEvent):  [Read-Write] 目标天气描述 更新事件
- ``target_weather_index_update_event`` (TargetWeatherIndexUpdateEvent):  [Read-Write] 目标天气序号 更新事件
- ``target_weather_time_of_day_update_event`` (TargetWeatherTimeOfDayUpdateEvent):  [Read-Write] 目标时间 更新事件

<a id="unreal.WeatherControlManager.target_weather_time_of_day_update_event"></a>

#### target\_weather\_time\_of\_day\_update\_event

```python
@property
def target_weather_time_of_day_update_event(
) -> TargetWeatherTimeOfDayUpdateEvent
```

(TargetWeatherTimeOfDayUpdateEvent):  [Read-Write] 目标时间 更新事件

<a id="unreal.WeatherControlManager.target_weather_time_of_day_update_event"></a>

#### target\_weather\_time\_of\_day\_update\_event

```python
@target_weather_time_of_day_update_event.setter
def target_weather_time_of_day_update_event(
        value: TargetWeatherTimeOfDayUpdateEvent) -> None
```

<a id="unreal.WeatherControlManager.target_weather_index_update_event"></a>

#### target\_weather\_index\_update\_event

```python
@property
def target_weather_index_update_event() -> TargetWeatherIndexUpdateEvent
```

(TargetWeatherIndexUpdateEvent):  [Read-Write] 目标天气序号 更新事件

<a id="unreal.WeatherControlManager.target_weather_index_update_event"></a>

#### target\_weather\_index\_update\_event

```python
@target_weather_index_update_event.setter
def target_weather_index_update_event(
        value: TargetWeatherIndexUpdateEvent) -> None
```

<a id="unreal.WeatherControlManager.target_weather_description_update_event"></a>

#### target\_weather\_description\_update\_event

```python
@property
def target_weather_description_update_event(
) -> TargetWeatherDescriptionUpdateEvent
```

(TargetWeatherDescriptionUpdateEvent):  [Read-Write] 目标天气描述 更新事件

<a id="unreal.WeatherControlManager.target_weather_description_update_event"></a>

#### target\_weather\_description\_update\_event

```python
@target_weather_description_update_event.setter
def target_weather_description_update_event(
        value: TargetWeatherDescriptionUpdateEvent) -> None
```

<a id="unreal.WeatherControlManager.current_time_of_day_notify_event"></a>

#### current\_time\_of\_day\_notify\_event

```python
@property
def current_time_of_day_notify_event() -> CurrentTimeOfDayNotifyEvent
```

(CurrentTimeOfDayNotifyEvent):  [Read-Write] 当前天空球环境对应时间事件，主要用于天空球环境渐变过程中通知其他对象，当前环境对应的实际时间

<a id="unreal.WeatherControlManager.current_time_of_day_notify_event"></a>

#### current\_time\_of\_day\_notify\_event

```python
@current_time_of_day_notify_event.setter
def current_time_of_day_notify_event(
        value: CurrentTimeOfDayNotifyEvent) -> None
```

<a id="unreal.WeatherControlManager.current_time_section_notify_event"></a>

#### current\_time\_section\_notify\_event

```python
@property
def current_time_section_notify_event() -> CurrentTimeSectionNotifyEvent
```

(CurrentTimeSectionNotifyEvent):  [Read-Write] 当前天空球环境对应时间段事件，主要用于天空球环境渐变过程中通知其他对象，当前环境对应的实际时间段

<a id="unreal.WeatherControlManager.current_time_section_notify_event"></a>

#### current\_time\_section\_notify\_event

```python
@current_time_section_notify_event.setter
def current_time_section_notify_event(
        value: CurrentTimeSectionNotifyEvent) -> None
```

<a id="unreal.WeatherControlManager.set_target_weather_time_of_day"></a>

#### set\_target\_weather\_time\_of\_day

```python
def set_target_weather_time_of_day(time: DateTime,
                                   duration_seconds: float = 0.000000) -> None
```

x.set_target_weather_time_of_day(time, duration_seconds=0.000000) -> None
设置目标时间和时间切换持续时间， 持续时间以秒为单位

Args:
    time (DateTime): 
    duration_seconds (float):

<a id="unreal.WeatherControlManager.set_target_weather_index"></a>

#### set\_target\_weather\_index

```python
def set_target_weather_index(index: int,
                             duration_seconds: float = 0.000000) -> None
```

x.set_target_weather_index(index, duration_seconds=0.000000) -> None
设置目标天气序号，序号按照天光模板定义的标准天气列表

Args:
    index (int32): 
    duration_seconds (float):

<a id="unreal.WeatherControlManager.set_target_weather_description"></a>

#### set\_target\_weather\_description

```python
def set_target_weather_description(description: str,
                                   duration_seconds: float = 0.000000) -> None
```

x.set_target_weather_description(description, duration_seconds=0.000000) -> None
设置当前目标天气描述，描述参照标准天气列表

Args:
    description (str): 
    duration_seconds (float):

<a id="unreal.WeatherControlManager.set_real_weather_time_enabled"></a>

#### set\_real\_weather\_time\_enabled

```python
def set_real_weather_time_enabled(real_time: bool) -> None
```

x.set_real_weather_time_enabled(real_time) -> None
设置是否开启实时光照时间

Args:
    real_time (bool):

<a id="unreal.WeatherControlManager.set_define_time_section_map"></a>

#### set\_define\_time\_section\_map

```python
def set_define_time_section_map(
        new_time_section_define_map: Map[TimeSection,
                                         TimeSectionDefine]) -> None
```

x.set_define_time_section_map(new_time_section_define_map) -> None
直接设置定义时间段起止时间映射表

Args:
    new_time_section_define_map (Map[TimeSection, TimeSectionDefine]):

<a id="unreal.WeatherControlManager.set_current_weather_time_of_day"></a>

#### set\_current\_weather\_time\_of\_day

```python
def set_current_weather_time_of_day(time: DateTime) -> None
```

x.set_current_weather_time_of_day(time) -> None
设置当前时间，该函数为天空球插件更新时间状态时调用

Args:
    time (DateTime):

<a id="unreal.WeatherControlManager.get_time_section_define"></a>

#### get\_time\_section\_define

```python
def get_time_section_define(time_section: TimeSection) -> TimeSectionDefine
```

x.get_time_section_define(time_section) -> TimeSectionDefine
定义时间段起止时间

Args:
    time_section (TimeSection): 

Returns:
    TimeSectionDefine:

<a id="unreal.WeatherControlManager.get_time_section_by_date_time"></a>

#### get\_time\_section\_by\_date\_time

```python
def get_time_section_by_date_time(time: DateTime) -> TimeSection
```

x.get_time_section_by_date_time(time) -> TimeSection
根据时间获取对应的时间段

Args:
    time (DateTime): 

Returns:
    TimeSection:

<a id="unreal.WeatherControlManager.get_target_weather_time_of_day"></a>

#### get\_target\_weather\_time\_of\_day

```python
def get_target_weather_time_of_day() -> DateTime
```

x.get_target_weather_time_of_day() -> DateTime
获取目标时间

Returns:
    DateTime:

<a id="unreal.WeatherControlManager.get_target_weather_index"></a>

#### get\_target\_weather\_index

```python
def get_target_weather_index() -> int
```

x.get_target_weather_index() -> int32
获取目标天气序号

Returns:
    int32:

<a id="unreal.WeatherControlManager.get_target_weather_description"></a>

#### get\_target\_weather\_description

```python
def get_target_weather_description() -> str
```

x.get_target_weather_description() -> str
获取当前目标天气描述

Returns:
    str:

<a id="unreal.WeatherControlManager.get_real_time_weather_enabled"></a>

#### get\_real\_time\_weather\_enabled

```python
def get_real_time_weather_enabled() -> bool
```

x.get_real_time_weather_enabled() -> bool
获取是否开启实时光照时间

Returns:
    bool:

<a id="unreal.WeatherControlManager.get_current_weather_time_of_day"></a>

#### get\_current\_weather\_time\_of\_day

```python
def get_current_weather_time_of_day() -> DateTime
```

x.get_current_weather_time_of_day() -> DateTime
获取当前天空球实际对应时间

Returns:
    DateTime:

<a id="unreal.WeatherControlManager.get_current_time_section"></a>

#### get\_current\_time\_section

```python
def get_current_time_section() -> TimeSection
```

x.get_current_time_section() -> TimeSection
获取当前天空球实际对应时间段

Returns:
    TimeSection:

<a id="unreal.WeatherControlManager.define_time_section_start_end"></a>

#### define\_time\_section\_start\_end

```python
def define_time_section_start_end(time_section: TimeSection,
                                  define_data: TimeSectionDefine) -> None
```

x.define_time_section_start_end(time_section, define_data) -> None
定义时间段起止时间

Args:
    time_section (TimeSection): 
    define_data (TimeSectionDefine):

<a id="unreal.AnimationCompressionLibraryDatabaseFactory"></a>