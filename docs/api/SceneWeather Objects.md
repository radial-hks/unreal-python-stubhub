## SceneWeather Objects

```python
class SceneWeather(ParamsBase)
```

Scene Weather

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpEnvironmentAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_seconds`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``realtime`` (bool):  [Read-Write]
- ``scene_weather`` (str):  [Read-Write]

<a id="unreal.SceneWeather.__init__"></a>

#### \_\_init\_\_

```python
def __init__(scene_weather: str = "",
             duration_seconds: float = 0.000000,
             realtime: bool = False) -> None
```

<a id="unreal.SceneWeather.scene_weather"></a>

#### scene\_weather

```python
@property
def scene_weather() -> str
```

(str):  [Read-Write]

<a id="unreal.SceneWeather.scene_weather"></a>

#### scene\_weather

```python
@scene_weather.setter
def scene_weather(value: str) -> None
```

<a id="unreal.SceneWeather.duration_seconds"></a>

#### duration\_seconds

```python
@property
def duration_seconds() -> float
```

(float):  [Read-Write]

<a id="unreal.SceneWeather.duration_seconds"></a>

#### duration\_seconds

```python
@duration_seconds.setter
def duration_seconds(value: float) -> None
```

<a id="unreal.SceneWeather.realtime"></a>

#### realtime

```python
@property
def realtime() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SceneWeather.realtime"></a>

#### realtime

```python
@realtime.setter
def realtime(value: bool) -> None
```

<a id="unreal.SceneWeatherResult"></a>