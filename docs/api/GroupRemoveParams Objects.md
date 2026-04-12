## GroupRemoveParams Objects

```python
class GroupRemoveParams(ParamsBase)
```

Group Remove Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpGroupAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``remove_eids`` (Array[int64]):  [Read-Write]

<a id="unreal.GroupRemoveParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(group_eid: int = 0, remove_eids: Array[int] = []) -> None
```

<a id="unreal.GroupRemoveParams.group_eid"></a>

#### group\_eid

```python
@property
def group_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.GroupRemoveParams.group_eid"></a>

#### group\_eid

```python
@group_eid.setter
def group_eid(value: int) -> None
```

<a id="unreal.GroupRemoveParams.remove_eids"></a>

#### remove\_eids

```python
@property
def remove_eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.GroupRemoveParams.remove_eids"></a>

#### remove\_eids

```python
@remove_eids.setter
def remove_eids(value: Array[int]) -> None
```

<a id="unreal.OutlineComponentParams"></a>