## VisualOutlineParams Objects

```python
class VisualOutlineParams(WdpVisualParamBase)
```

Visual Outline Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpVisualAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``outline`` (bool):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.VisualOutlineParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = [],
             style_name: Name = "None",
             outline: bool = False) -> None
```

<a id="unreal.VisualOutlineParams.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write]

<a id="unreal.VisualOutlineParams.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.VisualHighlightParams"></a>