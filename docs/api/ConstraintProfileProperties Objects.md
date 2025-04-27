## ConstraintProfileProperties Objects

```python
class ConstraintProfileProperties(StructBase)
```

Container for properties of a physics constraint that can be easily swapped at runtime. This is useful for switching different setups when going from ragdoll to standup for example

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_break_threshold`` (float):  [Read-Write] Torque needed to break the joint.
- ``angular_breakable`` (bool):  [Read-Write] Whether it is possible to break the joint with angular force.
- ``angular_drive`` (AngularDriveConstraint):  [Read-Write]
- ``angular_plasticity`` (bool):  [Read-Write] Whether it is possible to reset target rotations from the angular displacement.
- ``angular_plasticity_threshold`` (float):  [Read-Write] [Chaos Only] Degree threshold from target angle needed to reset the target angle.
- ``cone_limit`` (ConeConstraint):  [Read-Write]
- ``contact_transfer_scale`` (float):  [Read-Write] [Chaos Only] Colliison transfer on parent from the joints child. Range is 0.0-MAX
- ``disable_collision`` (bool):  [Read-Write] Disable collision between bodies joined by this constraint.
- ``enable_mass_conditioning`` (bool):  [Read-Write] Whether mass conditioning is enabled for this joint. Mass conditioning applies a non-physical scale to the mass and inertia of the two
  bodies that only affects this joint, so that the mass and inertia ratios are smaller. This helps stabilize joints where the bodies
  are very different sizes, and especially when the parent body is heavier than the child. However, it can lead to unrealistic
  behaviour, especially when collisions are involved.
- ``enable_projection`` (bool):  [Read-Write] Projection is a post-solve position and angular fixup consisting of two correction procedures. First, if the constraint limits are exceeded
  by more that the Linear or Angular Tolerance, the bodies are teleported to eliminate the error. Second, if the constraint limits are exceeded
  by less than the tolerance, a semi-physical correction is applied,  with the parent body in the constraint is treated as having infinite mass.
  The teleport tolerance are controlled by ProjectionLinearTolerance and ProjectionAngularTolerance. The semi-physical correction is controlled
  by ProjectionLinearAlpha and ProjectionAnguilarAlpha. You may have one, none, or both systems enabled at the same time.

  Projection only works well if the chain is not interacting with other objects (e.g., through collisions) because the projection of the bodies in
  the chain will cause other constraints to be violated. Likewise, if a body is influenced by multiple constraints, then enabling projection on more
  than one constraint may lead to unexpected results - the  "last" constraint would win but the order in which constraints are solved cannot be directly controlled.

  Note that the semi-physical projection (ProjectionLinearAlpha and ProjectionAngularAlpha) is only applied to hard-limit constraints and not those with
  soft limits because the soft limit is the point at which the soft-constraint (spring) kicks in, and not really a limit on how far the joint can be separated.
- ``enable_shock_propagation`` (bool):  [Read-Write] Shock propagation increases the mass of the parent body for the last iteration of the position and velocity solve phases.
  This can help stiffen up joint chains, but is also prone to introducing energy down the chain especially at high alpha.
  It also does not work well if there are collisions on the bodies preventing the joints from correctly resolving - this
  can lead to jitter, especially if collision shock propagation is also enabled.
- ``linear_break_threshold`` (float):  [Read-Write] Force needed to break the distance constraint.
- ``linear_breakable`` (bool):  [Read-Write] Whether it is possible to break the joint with linear force.
- ``linear_drive`` (LinearDriveConstraint):  [Read-Write]
- ``linear_limit`` (LinearConstraint):  [Read-Write]
- ``linear_plasticity`` (bool):  [Read-Write] Whether it is possible to reset spring rest length from the linear deformation.
- ``linear_plasticity_threshold`` (float):  [Read-Write] [Chaos Only] Percent threshold from center of mass distance needed to reset the linear drive position target. This value can be greater than 1.
- ``linear_plasticity_type`` (ConstraintPlasticityType):  [Read-Write] Whether linear plasticity has a operation mode [free]
- ``parent_dominates`` (bool):  [Read-Write] When set, the parent body in a constraint will not be affected by the motion of the child
- ``projection_angular_alpha`` (float):  [Read-Write] How much semi-physical angular projection correction to apply [0-1]. Only used if bEnableProjection is true and if hard limits are used.
- ``projection_angular_tolerance`` (float):  [Read-Write] If the joint error is above this distance after the solve phase, the child body will be teleported to fix the error. Only used if bEnableProjection is true.
- ``projection_linear_alpha`` (float):  [Read-Write] How much semi-physical linear projection correction to apply [0-1]. Only used if bEnableProjection is true and if hard limits are used.
- ``projection_linear_tolerance`` (float):  [Read-Write] If the joint error is above this distance after the solve phase, the child body will be teleported to fix the error. Only used if bEnableProjection is true.
- ``shock_propagation_alpha`` (float):  [Read-Write] How much shock propagation to apply [0-1]. Shock propagation increases the mass of the parent body for the last iteration of the
  position and velocity solve phases. This can help stiffen up joint chains, but is also prone to introducing energy down the chain
  especially at high alpha. Only used in bEnableShockPropagation is true.
- ``twist_limit`` (TwistConstraint):  [Read-Write]

<a id="unreal.ConstraintProfileProperties.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PhysicsReplicationResimulationSettings"></a>