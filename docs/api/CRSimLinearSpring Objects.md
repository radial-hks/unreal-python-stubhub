## CRSimLinearSpring Objects

```python
class CRSimLinearSpring(StructBase)
```

CRSim Linear Spring

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: CRSimLinearSpring.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coefficient`` (float):  [Read-Write] The power of this spring
- ``equilibrium`` (float):  [Read-Write] The rest length of this spring.
  A value of lower than zero indicates that the equilibrium
  should be based on the current distance of the two subjects.
- ``subject_a`` (int32):  [Read-Write] The first point affected by this spring
- ``subject_b`` (int32):  [Read-Write] The second point affected by this spring

<a id="unreal.CRSimLinearSpring.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CRSimSoftCollision"></a>