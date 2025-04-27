## RigUnit_SetTranslation Objects

```python
class RigUnit_SetTranslation(RigUnitMutable)
```

SetTranslation is used to set a single translation on hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``initial`` (bool):  [Read-Write] Defines if the transform should be set as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``item`` (RigElementKey):  [Read-Write] The item to set the translation for
- ``propagate_to_children`` (bool):  [Read-Write] If set to true children of affected items in the hierarchy
  will follow the transform change - otherwise only the parent will move.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the translation should be set in local or global space
- ``value`` (Vector):  [Read-Write] The new translation of the given item
- ``weight`` (float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_SetTranslation.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             initial: bool = False,
             value: Vector = [0.000000, 0.000000, 0.000000],
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SetTranslation.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to set the translation for

<a id="unreal.RigUnit_SetTranslation.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetTranslation.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the translation should be set in local or global space

<a id="unreal.RigUnit_SetTranslation.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetTranslation.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write] Defines if the transform should be set as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_SetTranslation.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_SetTranslation.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write] The new translation of the given item

<a id="unreal.RigUnit_SetTranslation.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigUnit_SetTranslation.translation"></a>

#### translation

```python
@property
def translation() -> Vector
```

deprecated: 'translation' was renamed to 'value'.

<a id="unreal.RigUnit_SetTranslation.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector) -> None
```

<a id="unreal.RigUnit_SetTranslation.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] Defines how much the change will be applied

<a id="unreal.RigUnit_SetTranslation.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetTranslation.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Write] If set to true children of affected items in the hierarchy
will follow the transform change - otherwise only the parent will move.

<a id="unreal.RigUnit_SetTranslation.propagate_to_children"></a>

#### propagate_to_children

```python
@propagate_to_children.setter
def propagate_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_SetRotation"></a>