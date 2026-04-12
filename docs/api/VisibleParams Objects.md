## VisibleParams Objects

```python
class VisibleParams(ParamsBase)
```

Visible

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.VisibleParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = [], visible: bool = False) -> None
```

<a id="unreal.VisibleParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.VisibleParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[int]) -> None
```

<a id="unreal.VisibleParams.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.VisibleParams.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.VisibleByTypeParams"></a>