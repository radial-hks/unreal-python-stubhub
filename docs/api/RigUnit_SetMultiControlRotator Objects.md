## RigUnit_SetMultiControlRotator Objects

```python
class RigUnit_SetMultiControlRotator(RigUnitMutable)
```

SetMultiControlRotator is used to perform a change in the hierarchy by setting multiple controls' rotator value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[RigUnit_SetMultiControlRotator_Entry]):  [Read-Write] The array of control-rotator pairs to be processed
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetMultiControlRotator.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             entries: Array[RigUnit_SetMultiControlRotator_Entry] = [],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator.entries"></a>

#### entries

```python
@property
def entries() -> Array[RigUnit_SetMultiControlRotator_Entry]
```

(Array[RigUnit_SetMultiControlRotator_Entry]):  [Read-Write] The array of control-rotator pairs to be processed

<a id="unreal.RigUnit_SetMultiControlRotator.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[RigUnit_SetMultiControlRotator_Entry]) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetMultiControlRotator.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlTransform"></a>