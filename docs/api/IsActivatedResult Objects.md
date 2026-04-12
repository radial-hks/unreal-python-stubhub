## IsActivatedResult Objects

```python
class IsActivatedResult(ResultBase)
```

Is Activated Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_activated`` (bool):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.IsActivatedResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             is_activated: bool = False) -> None
```

<a id="unreal.IsActivatedResult.is_activated"></a>

#### is\_activated

```python
@property
def is_activated() -> bool
```

(bool):  [Read-Write]

<a id="unreal.IsActivatedResult.is_activated"></a>

#### is\_activated

```python
@is_activated.setter
def is_activated(value: bool) -> None
```

<a id="unreal.AesTilesVisualApiParamBase"></a>