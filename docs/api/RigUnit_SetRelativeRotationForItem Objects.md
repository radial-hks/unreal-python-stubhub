## RigUnit_SetRelativeRotationForItem Objects

```python
class RigUnit_SetRelativeRotationForItem(RigUnitMutable)
```

SetRelativeRotation is used to set a single rotation from a hierarchy in the space of another item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetRelativeTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] The child item to set the transform for
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``parent`` (RigElementKey):  [Read-Write] The parent item to use.
  The child transform will be set in the space of the parent.
- ``parent_initial`` (bool):  [Read-Write] Defines if the parent's transform should be determined as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``propagate_to_children`` (bool):  [Read-Write] If set to true children of affected items in the hierarchy
  will follow the transform change - otherwise only the parent will move.
- ``value`` (Quat):  [Read-Write] The transform of the child item relative to the provided parent
- ``weight`` (float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_SetRelativeRotationForItem.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             parent: RigElementKey = [RigElementType.NONE, "None"],
             parent_initial: bool = False,
             value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SetRelativeRotationForItem.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] The child item to set the transform for

<a id="unreal.RigUnit_SetRelativeRotationForItem.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetRelativeRotationForItem.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] The parent item to use.
The child transform will be set in the space of the parent.

<a id="unreal.RigUnit_SetRelativeRotationForItem.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetRelativeRotationForItem.parent_initial"></a>

#### parent_initial

```python
@property
def parent_initial() -> bool
```

(bool):  [Read-Write] Defines if the parent's transform should be determined as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_SetRelativeRotationForItem.parent_initial"></a>

#### parent_initial

```python
@parent_initial.setter
def parent_initial(value: bool) -> None
```

<a id="unreal.RigUnit_SetRelativeRotationForItem.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write] The transform of the child item relative to the provided parent

<a id="unreal.RigUnit_SetRelativeRotationForItem.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigUnit_SetRelativeRotationForItem.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_SetRelativeRotationForItem.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetRelativeRotationForItem.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Write] If set to true children of affected items in the hierarchy
will follow the transform change - otherwise only the parent will move.

<a id="unreal.RigUnit_SetRelativeRotationForItem.propagate_to_children"></a>

#### propagate_to_children

```python
@propagate_to_children.setter
def propagate_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_SetSpaceInitialTransform"></a>