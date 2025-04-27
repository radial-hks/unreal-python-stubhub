## CRSimPointForce Objects

```python
class CRSimPointForce(StructBase)
```

CRSim Point Force

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: CRSimPointForce.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coefficient`` (float):  [Read-Write] The strength of the force (a multiplier for direction based forces)
- ``force_type`` (CRSimPointForceType):  [Read-Write] The type of force.
- ``normalize`` (bool):  [Read-Write] If set to true the input vector will be normalized.
- ``vector`` (Vector):  [Read-Write] The point / direction to use for the force.
  This is a direction for direction based forces,
  while this is a position for attractor / repel based forces.

<a id="unreal.CRSimPointForce.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigModuleReference"></a>