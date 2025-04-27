## LinearConstraint Objects

```python
class LinearConstraint(ConstraintBaseParams)
```

Distance constraint

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``contact_distance`` (float):  [Read-Write] Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.
- ``damping`` (float):  [Read-Write] Damping of the soft constraint. Only used when Soft Constraint is on.
- ``limit`` (float):  [Read-Write] The distance allowed between the two joint reference frames. Distance applies on all axes enabled (one axis means line, two axes implies circle, three axes implies sphere)
- ``restitution`` (float):  [Read-Write] Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
- ``soft_constraint`` (bool):  [Read-Write] Whether we want to use a soft constraint (spring).
- ``stiffness`` (float):  [Read-Write] Stiffness of the soft constraint. Only used when Soft Constraint is on.
- ``x_motion`` (LinearConstraintMotion):  [Read-Write] Indicates the linear constraint applied along the X-axis. Free implies no constraint at all. Locked implies no movement along X is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided.
- ``y_motion`` (LinearConstraintMotion):  [Read-Write] Indicates the linear constraint applied along the Y-axis. Free implies no constraint at all. Locked implies no movement along Y is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided.
- ``z_motion`` (LinearConstraintMotion):  [Read-Write] Indicates the linear constraint applied along theZX-axis. Free implies no constraint at all. Locked implies no movement along Z is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided.

<a id="unreal.LinearConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ConeConstraint"></a>