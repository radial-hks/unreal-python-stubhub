## WdpVisualParamBase Objects

```python
class WdpVisualParamBase(ParamsBase)
```

Model

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpVisualAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.WdpVisualParamBase.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = [], style_name: Name = "None") -> None
```

<a id="unreal.WdpVisualParamBase.eids"></a>

#### eids

```python
@property
def eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.WdpVisualParamBase.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[int]) -> None
```

<a id="unreal.WdpVisualParamBase.style_name"></a>

#### style\_name

```python
@property
def style_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.WdpVisualParamBase.style_name"></a>

#### style\_name

```python
@style_name.setter
def style_name(value: Name) -> None
```

<a id="unreal.VisualOutlineParams"></a>