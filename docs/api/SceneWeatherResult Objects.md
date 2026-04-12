## SceneWeatherResult Objects

```python
class SceneWeatherResult(ResultBase)
```

Scene Weather Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpEnvironmentAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``realtime`` (bool):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``scene_weather`` (str):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.SceneWeatherResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             scene_weather: str = "",
             realtime: bool = False) -> None
```

<a id="unreal.SceneWeatherResult.scene_weather"></a>

#### scene\_weather

```python
@property
def scene_weather() -> str
```

(str):  [Read-Write]

<a id="unreal.SceneWeatherResult.scene_weather"></a>

#### scene\_weather

```python
@scene_weather.setter
def scene_weather(value: str) -> None
```

<a id="unreal.SceneWeatherResult.realtime"></a>

#### realtime

```python
@property
def realtime() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SceneWeatherResult.realtime"></a>

#### realtime

```python
@realtime.setter
def realtime(value: bool) -> None
```

<a id="unreal.WeatherUpdateEventArgs"></a>