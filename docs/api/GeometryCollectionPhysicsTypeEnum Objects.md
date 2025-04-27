## GeometryCollectionPhysicsTypeEnum Objects

```python
class GeometryCollectionPhysicsTypeEnum(EnumBase)
```

EGeometry Collection Physics Type Enum

**C++ Source:**

- **Module**: Chaos
- **File**: GeometryCollectionSimulationTypes.h

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_ANGULAR_VELOCITY"></a>

#### CHAOS_ANGULAR_VELOCITY

0: Add a vector field to the particles angular velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_DYNAMIC_STATE"></a>

#### CHAOS_DYNAMIC_STATE

1: Set the dynamic state of a particle (static, dynamic, kinematic...)

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_LINEAR_VELOCITY"></a>

#### CHAOS_LINEAR_VELOCITY

2: Add a vector field to the particles linear velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_INITIAL_ANGULAR_VELOCITY"></a>

#### CHAOS_INITIAL_ANGULAR_VELOCITY

3: Initial particles angular velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_INITIAL_LINEAR_VELOCITY"></a>

#### CHAOS_INITIAL_LINEAR_VELOCITY

4: Initial particles linear velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_COLLISION_GROUP"></a>

#### CHAOS_COLLISION_GROUP

5: Set the particles collision group.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_LINEAR_FORCE"></a>

#### CHAOS_LINEAR_FORCE

6: Add a vector field to the particles linear force.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_ANGULAR_TORQUE"></a>

#### CHAOS_ANGULAR_TORQUE

7: Add a vector field to the particles angular torque.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_DISABLE_THRESHOLD"></a>

#### CHAOS_DISABLE_THRESHOLD

8: Disable the particles if their linear and angular velocity are less than the threshold.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_SLEEPING_THRESHOLD"></a>

#### CHAOS_SLEEPING_THRESHOLD

9: Set particles in sleeping mode if their linear and angular velocity are less than the threshold.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_EXTERNAL_CLUSTER_STRAIN"></a>

#### CHAOS_EXTERNAL_CLUSTER_STRAIN

10: Apply an external strain over the particles. If this strain is over the internal one, the cluster will break.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_INTERNAL_CLUSTER_STRAIN"></a>

#### CHAOS_INTERNAL_CLUSTER_STRAIN

11: Add a strain field to the particles internal one.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_LINEAR_IMPULSE"></a>

#### CHAOS_LINEAR_IMPULSE

12: Add a vector field to apply an impulse to the particles.

<a id="unreal.InitialVelocityTypeEnum"></a>