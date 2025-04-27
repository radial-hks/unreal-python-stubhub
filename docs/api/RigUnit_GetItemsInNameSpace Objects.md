## RigUnit_GetItemsInNameSpace Objects

```python
class RigUnit_GetItemsInNameSpace(RigUnit_RigModulesBase)
```

Returns all items (based on a filter) in the current namespace.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_RigModules.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write] * The items within the namespace
- ``type_to_search`` (RigElementType):  [Read-Write]

<a id="unreal.RigUnit_GetItemsInNameSpace.__init__"></a>

#### __init__

```python
def __init__(type_to_search: RigElementType = RigElementType.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_GetItemsInNameSpace.type_to_search"></a>

#### type_to_search

```python
@property
def type_to_search() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_GetItemsInNameSpace.type_to_search"></a>

#### type_to_search

```python
@type_to_search.setter
def type_to_search(value: RigElementType) -> None
```

<a id="unreal.RigUnit_GetItemsInNameSpace.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] * The items within the namespace

<a id="unreal.RigUnit_SequenceExecution"></a>