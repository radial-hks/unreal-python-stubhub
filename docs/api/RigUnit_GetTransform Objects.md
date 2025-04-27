## RigUnit_GetTransform Objects

```python
class RigUnit_GetTransform(RigUnit)
```

GetTransform is used to retrieve a single transform from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial`` (bool):  [Read-Write] Defines if the transform should be retrieved as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``item`` (RigElementKey):  [Read-Write] The item to retrieve the transform for
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the transform should be retrieved in local or global space
- ``transform`` (Transform):  [Read-Write] The current transform of the given item - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetTransform.__init__"></a>

#### __init__

```python
def __init__(
    item: RigElementKey = [RigElementType.NONE, "None"],
    space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
    initial: bool = False,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetTransform.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to retrieve the transform for

<a id="unreal.RigUnit_GetTransform.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetTransform.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the transform should be retrieved in local or global space

<a id="unreal.RigUnit_GetTransform.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetTransform.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write] Defines if the transform should be retrieved as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_GetTransform.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_GetTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The current transform of the given item - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetTransformArray"></a>