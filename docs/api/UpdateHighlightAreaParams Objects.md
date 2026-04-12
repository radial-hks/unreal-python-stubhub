## UpdateHighlightAreaParams Objects

```python
class UpdateHighlightAreaParams(ParamsBase)
```

Update Highlight Area Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HighlightAreaAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``highlight_area_style`` (HighlightAreaStyle):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``polygon_entity_eid`` (str):  [Read-Write]

<a id="unreal.UpdateHighlightAreaParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    eid: str = "",
    polygon_entity_eid: str = "",
    highlight_area_style: HighlightAreaStyle = [
        "ffffffaa", "595959aa", "000000ff", 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.UpdateHighlightAreaParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateHighlightAreaParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateHighlightAreaParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@property
def polygon_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateHighlightAreaParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@polygon_entity_eid.setter
def polygon_entity_eid(value: str) -> None
```

<a id="unreal.UpdateHighlightAreaParams.highlight_area_style"></a>

#### highlight\_area\_style

```python
@property
def highlight_area_style() -> HighlightAreaStyle
```

(HighlightAreaStyle):  [Read-Write]

<a id="unreal.UpdateHighlightAreaParams.highlight_area_style"></a>

#### highlight\_area\_style

```python
@highlight_area_style.setter
def highlight_area_style(value: HighlightAreaStyle) -> None
```

<a id="unreal.MiniMapSource"></a>