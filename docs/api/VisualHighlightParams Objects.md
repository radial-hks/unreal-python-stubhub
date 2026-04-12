## VisualHighlightParams Objects

```python
class VisualHighlightParams(WdpVisualParamBase)
```

Visual Highlight Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpVisualAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``highlight`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.VisualHighlightParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = [],
             style_name: Name = "None",
             highlight: bool = False) -> None
```

<a id="unreal.VisualHighlightParams.highlight"></a>

#### highlight

```python
@property
def highlight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.VisualHighlightParams.highlight"></a>

#### highlight

```python
@highlight.setter
def highlight(value: bool) -> None
```

<a id="unreal.EntityTypeParams"></a>