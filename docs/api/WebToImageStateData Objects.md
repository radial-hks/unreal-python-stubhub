## WebToImageStateData Objects

```python
class WebToImageStateData(StructBase)
```

Web to Image State Data

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: WebToImage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``state`` (WebToImageState):  [Read-Write]
- ``texture`` (Texture2DDynamic):  [Read-Write]

<a id="unreal.WebToImageStateData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(state: WebToImageState = WebToImageState.NOT_YET,
             texture: Texture2DDynamic = None) -> None
```

<a id="unreal.WebToImageStateData.state"></a>

#### state

```python
@property
def state() -> WebToImageState
```

(WebToImageState):  [Read-Only]

<a id="unreal.WebToImageStateData.texture"></a>

#### texture

```python
@property
def texture() -> Texture2DDynamic
```

(Texture2DDynamic):  [Read-Only]

<a id="unreal.ChinaMapSwitchModeParams"></a>