## SkylightTimeResult Objects

```python
class SkylightTimeResult(ResultBase)
```

Skylight Time Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpEnvironmentAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``realtime`` (bool):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``skylight_time`` (str):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.SkylightTimeResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             skylight_time: str = "",
             realtime: bool = False) -> None
```

<a id="unreal.SkylightTimeResult.skylight_time"></a>

#### skylight\_time

```python
@property
def skylight_time() -> str
```

(str):  [Read-Write]

<a id="unreal.SkylightTimeResult.skylight_time"></a>

#### skylight\_time

```python
@skylight_time.setter
def skylight_time(value: str) -> None
```

<a id="unreal.SkylightTimeResult.realtime"></a>

#### realtime

```python
@property
def realtime() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkylightTimeResult.realtime"></a>

#### realtime

```python
@realtime.setter
def realtime(value: bool) -> None
```

<a id="unreal.SceneWeather"></a>