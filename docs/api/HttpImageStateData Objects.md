## HttpImageStateData Objects

```python
class HttpImageStateData(StructBase)
```

Http Image State Data

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: HttpImageStateSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``image_textrue`` (Texture2DDynamic):  [Read-Write]
- ``state`` (HttpImageState):  [Read-Write]

<a id="unreal.HttpImageStateData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(state: HttpImageState = HttpImageState.NOT_YET,
             image_textrue: Texture2DDynamic = None) -> None
```

<a id="unreal.HttpImageStateData.state"></a>

#### state

```python
@property
def state() -> HttpImageState
```

(HttpImageState):  [Read-Only]

<a id="unreal.HttpImageStateData.image_textrue"></a>

#### image\_textrue

```python
@property
def image_textrue() -> Texture2DDynamic
```

(Texture2DDynamic):  [Read-Only]

<a id="unreal.LidarPointHeatMapData"></a>