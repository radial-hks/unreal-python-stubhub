## PhysicsAsset Objects

```python
class PhysicsAsset(Object)
```

PhysicsAsset contains a set of rigid bodies and constraints that make up a single ragdoll.
The asset is not limited to human ragdolls, and can be used for any physical simulation using bodies and constraints.
A SkeletalMesh has a single PhysicsAsset, which allows for easily turning ragdoll physics on or off for many SkeletalMeshComponents
The asset can be configured inside the Physics Asset Editor.
see: https://docs.unrealengine.com/InteractiveExperiences/Physics/PhysicsAssetEditor
see: USkeletalMesh

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constraint_profiles`` (Array[Name]):  [Read-Write]
- ``not_for_dedicated_server`` (bool):  [Read-Write] If true, we skip instancing bodies for this PhysicsAsset on dedicated servers
- ``physical_animation_profiles`` (Array[Name]):  [Read-Write]
- ``solver_iterations`` (SolverIterations):  [Read-Only] Old solver settings shown for reference. These will be removed at some point.
  When you open an old asset you should see that the settings were transferred to "SolverSettings" above.
  You should usually see:
  SolverSettings.PositionIterations = OldSettings.SolverIterations * OldSetting.JointIterations;
  SolverSettings.VelocityIterations = 1;
  SolverSettings.ProjectionIterations = 1;
- ``solver_settings`` (PhysicsAssetSolverSettings):  [Read-Write] Solver settings when the asset is used with a RigidBody Anim Node (RBAN).
- ``solver_type`` (PhysicsAssetSolverType):  [Read-Write] Solver type used in physics asset editor. This can be used to make what you see in the asset editor more closely resembles what you
  see in game (though there will be differences owing to framerate variation etc). If your asset will primarily be used as a ragdoll
  select "World", but if it will be used in the AnimGraph select "RBAN".
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.PhysicsAsset.get_constraints"></a>

#### get_constraints

```python
def get_constraints(
        includes_terminated: bool) -> Array[ConstraintInstanceAccessor]
```

x.get_constraints(includes_terminated) -> Array[ConstraintInstanceAccessor]
Gets all constraints

Args:
    includes_terminated (bool): 

Returns:
    Array[ConstraintInstanceAccessor]: 

    out_constraints (Array[ConstraintInstanceAccessor]): returned list of constraints matching the parameters

<a id="unreal.PhysicsAsset.get_constraint_by_name"></a>

#### get_constraint_by_name

```python
def get_constraint_by_name(
        constraint_name: Name) -> ConstraintInstanceAccessor
```

x.get_constraint_by_name(constraint_name) -> ConstraintInstanceAccessor
Gets a constraint by its joint name

Args:
    constraint_name (Name): name of the constraint

Returns:
    ConstraintInstanceAccessor: ConstraintInstance accessor to the constraint data

<a id="unreal.PhysicsAsset.get_constraint_by_bone_names"></a>

#### get_constraint_by_bone_names

```python
def get_constraint_by_bone_names(
        bone1_name: Name, bone2_name: Name) -> ConstraintInstanceAccessor
```

x.get_constraint_by_bone_names(bone1_name, bone2_name) -> ConstraintInstanceAccessor
Gets a constraint by its joint name

Args:
    bone1_name (Name): name of the first bone in the joint
    bone2_name (Name): name of the second bone in the joint

Returns:
    ConstraintInstanceAccessor: ConstraintInstance accessor to the constraint data

<a id="unreal.PhysicsCollisionHandler"></a>