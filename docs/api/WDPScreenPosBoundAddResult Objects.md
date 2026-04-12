## WDPScreenPosBoundAddResult Objects

```python
class WDPScreenPosBoundAddResult(ResultBase)
```

WDPScreen Pos Bound Add Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ids`` (Array[Guid]):  [Read-Write]
- ``locations`` (Array[Vector]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WDPScreenPosBoundAddResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             ids: Array[Guid] = [],
             locations: Array[Vector] = []) -> None
```

<a id="unreal.WDPScreenPosBoundAddResult.ids"></a>

#### ids

```python
@property
def ids() -> Array[Guid]
```

(Array[Guid]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundAddResult.ids"></a>

#### ids

```python
@ids.setter
def ids(value: Array[Guid]) -> None
```

<a id="unreal.WDPScreenPosBoundAddResult.locations"></a>

#### locations

```python
@property
def locations() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundAddResult.locations"></a>

#### locations

```python
@locations.setter
def locations(value: Array[Vector]) -> None
```

<a id="unreal.WDPUpdateScreenPosBoundResult"></a>