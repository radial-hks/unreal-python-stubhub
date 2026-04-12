## GetHighlightAreaParams Objects

```python
class GetHighlightAreaParams(ResultBase)
```

Get Highlight Area Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HighlightAreaAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``highlight_area_style`` (HighlightAreaStyle):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``polygon_entity_eid`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetHighlightAreaParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    message: str = "",
    scene_change_info: WdpSceneChangeInfo = [[], [], []],
    success: bool = False,
    polygon_entity_eid: str = "",
    highlight_area_style: HighlightAreaStyle = [
        "ffffffaa", "595959aa", "000000ff", 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.GetHighlightAreaParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@property
def polygon_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GetHighlightAreaParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@polygon_entity_eid.setter
def polygon_entity_eid(value: str) -> None
```

<a id="unreal.GetHighlightAreaParams.highlight_area_style"></a>

#### highlight\_area\_style

```python
@property
def highlight_area_style() -> HighlightAreaStyle
```

(HighlightAreaStyle):  [Read-Write]

<a id="unreal.GetHighlightAreaParams.highlight_area_style"></a>

#### highlight\_area\_style

```python
@highlight_area_style.setter
def highlight_area_style(value: HighlightAreaStyle) -> None
```

<a id="unreal.UpdateHighlightAreaParams"></a>