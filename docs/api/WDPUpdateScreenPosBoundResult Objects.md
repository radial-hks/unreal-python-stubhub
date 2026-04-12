## WDPUpdateScreenPosBoundResult Objects

```python
class WDPUpdateScreenPosBoundResult(ResultBase)
```

WDPUpdate Screen Pos Bound Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WDPUpdateScreenPosBoundResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WDPUpdateScreenPosBoundResult.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPUpdateScreenPosBoundResult.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPScreenPosBoundChange"></a>