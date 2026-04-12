## EntitySlotParams Objects

```python
class EntitySlotParams(StructBase)
```

Entity Slot Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (int64):  [Read-Write]
- ``highlight`` (bool):  [Read-Write]
- ``material_index`` (int32):  [Read-Write]
- ``mesh_name`` (Name):  [Read-Write]

<a id="unreal.EntitySlotParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: int = 0,
             mesh_name: Name = "None",
             material_index: int = 0,
             highlight: bool = False) -> None
```

<a id="unreal.EntitySlotParams.eid"></a>

#### eid

```python
@property
def eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.EntitySlotParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: int) -> None
```

<a id="unreal.EntitySlotParams.mesh_name"></a>

#### mesh\_name

```python
@property
def mesh_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EntitySlotParams.mesh_name"></a>

#### mesh\_name

```python
@mesh_name.setter
def mesh_name(value: Name) -> None
```

<a id="unreal.EntitySlotParams.material_index"></a>

#### material\_index

```python
@property
def material_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.EntitySlotParams.material_index"></a>

#### material\_index

```python
@material_index.setter
def material_index(value: int) -> None
```

<a id="unreal.EntitySlotParams.highlight"></a>

#### highlight

```python
@property
def highlight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EntitySlotParams.highlight"></a>

#### highlight

```python
@highlight.setter
def highlight(value: bool) -> None
```

<a id="unreal.EntitySlotParamsArr"></a>