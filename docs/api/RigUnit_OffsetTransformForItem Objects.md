## RigUnit_OffsetTransformForItem Objects

```python
class RigUnit_OffsetTransformForItem(RigUnitMutable)
```

Offset Transform is used to add an offset to an existing transform in the hierarchy. The offset is post multiplied.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_OffsetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The item to offset the transform for
- ``offset_transform`` (Transform):  [Read-Write] The transform of the item relative to its previous transform
- ``propagate_to_children`` (bool):  [Read-Write] If set to true children of affected items in the hierarchy
  will follow the transform change - otherwise only the parent will move.
- ``weight`` (float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_OffsetTransformForItem.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             offset_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                            [-0.000000, 0.000000, 0.000000],
                                            [1.000000, 1.000000, 1.000000]],
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_OffsetTransformForItem.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to offset the transform for

<a id="unreal.RigUnit_OffsetTransformForItem.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_OffsetTransformForItem.offset_transform"></a>

#### offset_transform

```python
@property
def offset_transform() -> Transform
```

(Transform):  [Read-Write] The transform of the item relative to its previous transform

<a id="unreal.RigUnit_OffsetTransformForItem.offset_transform"></a>

#### offset_transform

```python
@offset_transform.setter
def offset_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_OffsetTransformForItem.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_OffsetTransformForItem.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_OffsetTransformForItem.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Write] If set to true children of affected items in the hierarchy
will follow the transform change - otherwise only the parent will move.

<a id="unreal.RigUnit_OffsetTransformForItem.propagate_to_children"></a>

#### propagate_to_children

```python
@propagate_to_children.setter
def propagate_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint"></a>