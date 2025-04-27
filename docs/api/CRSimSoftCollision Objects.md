## CRSimSoftCollision Objects

```python
class CRSimSoftCollision(StructBase)
```

CRSim Soft Collision

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: CRSimSoftCollision.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coefficient`` (float):  [Read-Write] The strength of the collision force
- ``falloff_type`` (RigVMAnimEasingType):  [Read-Write] The type of falloff to use
- ``inverted`` (bool):  [Read-Write] If set to true the collision volume will be inverted
- ``maximum_distance`` (float):  [Read-Write] The maximum distance for the collision.
  If this is equal or lower than the minimum there's no falloff.
  For a cone shape this represents the maximum angle in degrees.
- ``minimum_distance`` (float):  [Read-Write] The minimum distance for the collision.
  If this is equal or higher than the maximum there's no falloff.
  For a cone shape this represents the minimum angle in degrees.
- ``shape_type`` (CRSimSoftCollisionType):  [Read-Write] The type of collision shape
- ``transform`` (Transform):  [Read-Write] The world / global transform of the collisoin

<a id="unreal.CRSimSoftCollision.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CRSimPointForce"></a>