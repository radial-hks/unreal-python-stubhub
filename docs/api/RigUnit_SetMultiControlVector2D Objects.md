## RigUnit_SetMultiControlVector2D Objects

```python
class RigUnit_SetMultiControlVector2D(RigUnitMutable)
```

SetMultiControlVector2D is used to perform a change in the hierarchy by setting multiple controls' vector2D value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[RigUnit_SetMultiControlVector2D_Entry]):  [Read-Write] The array of control-vector2D pairs to be processed
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetMultiControlVector2D.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             entries: Array[RigUnit_SetMultiControlVector2D_Entry] = [],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SetMultiControlVector2D.entries"></a>

#### entries

```python
@property
def entries() -> Array[RigUnit_SetMultiControlVector2D_Entry]
```

(Array[RigUnit_SetMultiControlVector2D_Entry]):  [Read-Write] The array of control-vector2D pairs to be processed

<a id="unreal.RigUnit_SetMultiControlVector2D.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[RigUnit_SetMultiControlVector2D_Entry]) -> None
```

<a id="unreal.RigUnit_SetMultiControlVector2D.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetMultiControlVector2D.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlVector"></a>