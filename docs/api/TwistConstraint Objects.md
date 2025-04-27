## TwistConstraint Objects

```python
class TwistConstraint(ConstraintBaseParams)
```

Angular roll constraint

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``contact_distance`` (float):  [Read-Write] Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.
- ``damping`` (float):  [Read-Write] Damping of the soft constraint. Only used when Soft Constraint is on.
- ``restitution`` (float):  [Read-Write] Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
- ``soft_constraint`` (bool):  [Read-Write] Whether we want to use a soft constraint (spring).
- ``stiffness`` (float):  [Read-Write] Stiffness of the soft constraint. Only used when Soft Constraint is on.
- ``twist_limit_degrees`` (float):  [Read-Write] Symmetric angle of roll along the X-axis.
- ``twist_motion`` (AngularConstraintMotion):  [Read-Write] Indicates whether the Twist limit is used.

<a id="unreal.TwistConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.LinearDriveConstraint"></a>