## RigUnit_GetTransformItemArray Objects

```python
class RigUnit_GetTransformItemArray(RigUnit)
```

GetTransformArray is used to retrieve an array of transforms from the hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] Defines if the transforms should be retrieved as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``items`` (Array[RigElementKey]):  [Read-Write] The items to retrieve the transforms for
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the transforms should be retrieved in local or global space
- ``transforms`` (Array[Transform]):  [Read-Write] The current transform of the given item - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetTransformItemArray.__init__"></a>

#### __init__

```python
def __init__(items: Array[RigElementKey] = [],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             initial: bool = False,
             transforms: Array[Transform] = []) -> None
```

<a id="unreal.RigUnit_GetTransformItemArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items to retrieve the transforms for

<a id="unreal.RigUnit_GetTransformItemArray.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_GetTransformItemArray.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the transforms should be retrieved in local or global space

<a id="unreal.RigUnit_GetTransformItemArray.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetTransformItemArray.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write] Defines if the transforms should be retrieved as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_GetTransformItemArray.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_GetTransformItemArray.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Only] The current transform of the given item - or identity in case it wasn't found.

<a id="unreal.RigDispatch_MetadataBase"></a>