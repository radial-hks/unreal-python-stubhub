## RigVMSimPoint Objects

```python
class RigVMSimPoint(StructBase)
```

Rig VMSim Point

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMMathLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inherit_motion`` (float):  [Read-Write] Defines how much the point will inherit motion from its input.
  This does not have an effect on passive (mass == 0.0) points.
  Values can be higher than 1 due to timestep - but they are clamped internally.
- ``linear_damping`` (float):  [Read-Write] The linear damping of the point
- ``linear_velocity`` (Vector):  [Read-Write] The velocity of the point per second
- ``mass`` (float):  [Read-Write] The mass of the point
- ``position`` (Vector):  [Read-Write] The position of the point
- ``size`` (float):  [Read-Write] Size of the point - only used for collision

<a id="unreal.RigVMSimPoint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CRSimPoint"></a>