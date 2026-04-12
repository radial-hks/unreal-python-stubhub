## GroupAddParams Objects

```python
class GroupAddParams(ParamsBase)
```

Group Add Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpGroupAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_eids`` (Array[int64]):  [Read-Write]
- ``add_to_group_position`` (int32):  [Read-Write]
- ``group_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GroupAddParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(group_eid: int = 0,
             add_eids: Array[int] = [],
             add_to_group_position: int = 0) -> None
```

<a id="unreal.GroupAddParams.group_eid"></a>

#### group\_eid

```python
@property
def group_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.GroupAddParams.group_eid"></a>

#### group\_eid

```python
@group_eid.setter
def group_eid(value: int) -> None
```

<a id="unreal.GroupAddParams.add_eids"></a>

#### add\_eids

```python
@property
def add_eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.GroupAddParams.add_eids"></a>

#### add\_eids

```python
@add_eids.setter
def add_eids(value: Array[int]) -> None
```

<a id="unreal.GroupAddParams.add_to_group_position"></a>

#### add\_to\_group\_position

```python
@property
def add_to_group_position() -> int
```

(int32):  [Read-Write]

<a id="unreal.GroupAddParams.add_to_group_position"></a>

#### add\_to\_group\_position

```python
@add_to_group_position.setter
def add_to_group_position(value: int) -> None
```

<a id="unreal.GroupRemoveParams"></a>