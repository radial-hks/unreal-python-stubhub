## HairExternalForces Objects

```python
class HairExternalForces(StructBase)
```

Hair External Forces

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``air_drag`` (float):  [Read-Write] Coefficient between 0 and 1 to be used for the air drag
- ``air_velocity`` (Vector):  [Read-Write] Velocity of the surrounding air in cm/s
- ``gravity_vector`` (Vector):  [Read-Write] Acceleration vector in cm/s2 to be used for the gravity

<a id="unreal.HairExternalForces.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairBendConstraint"></a>