## CreateHighlightAreaParams Objects

```python
class CreateHighlightAreaParams(ParamsBase)
```

Create Highlight Area Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HighlightAreaAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``highlight_area_style`` (HighlightAreaStyle):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``polygon_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreateHighlightAreaParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    polygon_entity_eid: str = "",
    highlight_area_style: HighlightAreaStyle = [
        "ffffffaa", "595959aa", "000000ff", 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.CreateHighlightAreaParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@property
def polygon_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateHighlightAreaParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@polygon_entity_eid.setter
def polygon_entity_eid(value: str) -> None
```

<a id="unreal.CreateHighlightAreaParams.highlight_area_style"></a>

#### highlight\_area\_style

```python
@property
def highlight_area_style() -> HighlightAreaStyle
```

(HighlightAreaStyle):  [Read-Write]

<a id="unreal.CreateHighlightAreaParams.highlight_area_style"></a>

#### highlight\_area\_style

```python
@highlight_area_style.setter
def highlight_area_style(value: HighlightAreaStyle) -> None
```

<a id="unreal.GetHighlightAreaParams"></a>