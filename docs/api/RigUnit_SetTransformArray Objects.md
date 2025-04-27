## RigUnit_SetTransformArray Objects

```python
class RigUnit_SetTransformArray(RigUnitMutable)
```

SetTransformArray is used to set an array of transforms on the hierarchy.

Note: For Controls when setting the initial transform this node
actually sets the Control's offset transform and resets the local
values to (0, 0, 0).

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``initial`` (bool):  [Read-Write] Defines if the transform should be set as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``items`` (RigElementKeyCollection):  [Read-Write] The item to set the transform for
- ``propagate_to_children`` (bool):  [Read-Write] If set to true children of affected items in the hierarchy
  will follow the transform change - otherwise only the parent will move.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the transform should be set in local or global space
- ``transforms`` (Array[Transform]):  [Read-Write] The new transform of the given item
- ``weight`` (float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_SetTransformArray.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             items: RigElementKeyCollection = [[]],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             initial: bool = False,
             transforms: Array[Transform] = [],
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SetTransformArray.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] The item to set the transform for

<a id="unreal.RigUnit_SetTransformArray.items"></a>

#### items

```python
@items.setter
def items(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_SetTransformArray.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the transform should be set in local or global space

<a id="unreal.RigUnit_SetTransformArray.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetTransformArray.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write] Defines if the transform should be set as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_SetTransformArray.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_SetTransformArray.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] The new transform of the given item

<a id="unreal.RigUnit_SetTransformArray.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigUnit_SetTransformArray.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_SetTransformArray.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetTransformArray.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Write] If set to true children of affected items in the hierarchy
will follow the transform change - otherwise only the parent will move.

<a id="unreal.RigUnit_SetTransformArray.propagate_to_children"></a>

#### propagate_to_children

```python
@propagate_to_children.setter
def propagate_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_SetTransformItemArray"></a>