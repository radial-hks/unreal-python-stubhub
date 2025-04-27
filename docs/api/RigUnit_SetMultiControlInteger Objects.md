## RigUnit_SetMultiControlInteger Objects

```python
class RigUnit_SetMultiControlInteger(RigUnitMutable)
```

SetMultiControlInteger is used to perform a change in the hierarchy by setting multiple controls' integer value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[RigUnit_SetMultiControlInteger_Entry]):  [Read-Write] The array of control-integer pairs to be processed
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetMultiControlInteger.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             entries: Array[RigUnit_SetMultiControlInteger_Entry] = [],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SetMultiControlInteger.entries"></a>

#### entries

```python
@property
def entries() -> Array[RigUnit_SetMultiControlInteger_Entry]
```

(Array[RigUnit_SetMultiControlInteger_Entry]):  [Read-Write] The array of control-integer pairs to be processed

<a id="unreal.RigUnit_SetMultiControlInteger.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[RigUnit_SetMultiControlInteger_Entry]) -> None
```

<a id="unreal.RigUnit_SetMultiControlInteger.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetMultiControlInteger.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlVector2D"></a>