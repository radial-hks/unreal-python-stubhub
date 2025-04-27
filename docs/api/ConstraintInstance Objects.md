## ConstraintInstance Objects

```python
class ConstraintInstance(ConstraintInstanceBase)
```

Container for a physics representation of an object.

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_rotation_offset`` (Rotator):  [Read-Write] Specifies the angular offset between the two frames of reference. By default limit goes from (-Angle, +Angle)
  This allows you to bias the limit for swing1 swing2 and twist.
- ``constraint_bone1`` (Name):  [Read-Write] Name of first bone (body) that this constraint is connecting.
  This will be the 'child' bone in a PhysicsAsset.
- ``constraint_bone2`` (Name):  [Read-Write] Name of second bone (body) that this constraint is connecting.
  This will be the 'parent' bone in a PhysicsAset.
- ``joint_name`` (Name):  [Read-Only] Name of bone that this joint is associated with.
- ``pos1`` (Vector):  [Read-Write] Location of constraint in Body1 reference frame (usually the "child" body for skeletal meshes).
- ``pos2`` (Vector):  [Read-Write] Location of constraint in Body2 reference frame (usually the "parent" body for skeletal meshes).
- ``pri_axis1`` (Vector):  [Read-Write] Primary (twist) axis in Body1 reference frame.
- ``pri_axis2`` (Vector):  [Read-Write] Primary (twist) axis in Body2 reference frame.
- ``profile_instance`` (ConstraintProfileProperties):  [Read-Write] Constraint Data (properties easily swapped at runtime based on different constraint profiles)
- ``scale_linear_limits`` (bool):  [Read-Write] If true, linear limits scale using the absolute min of the 3d scale of the owning component
- ``sec_axis1`` (Vector):  [Read-Write] Secondary axis in Body1 reference frame. Orthogonal to PriAxis1.
- ``sec_axis2`` (Vector):  [Read-Write] Secondary axis in Body2 reference frame. Orthogonal to PriAxis2.

<a id="unreal.ConstraintInstance.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PhysicsPredictionSettings"></a>