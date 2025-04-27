## RigUnit_SetControlVector2D Objects

```python
class RigUnit_SetControlVector2D(RigUnitMutable)
```

SetControlVector2D is used to perform a change in the hierarchy by setting a single control's Vector2D value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``vector`` (Vector2D):  [Read-Write] The transform value to set for the given Control.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlVector2D.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             control: Name = "None",
             weight: float = 0.000000,
             vector: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SetControlVector2D.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetControlVector2D.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlVector2D.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlVector2D.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlVector2D.vector"></a>

#### vector

```python
@property
def vector() -> Vector2D
```

(Vector2D):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetControlVector2D.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector2D) -> None
```

<a id="unreal.RigUnit_SetMultiControlVector2D_Entry"></a>