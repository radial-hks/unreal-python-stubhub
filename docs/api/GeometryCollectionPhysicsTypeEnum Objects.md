## GeometryCollectionPhysicsTypeEnum Objects

```python
class GeometryCollectionPhysicsTypeEnum(EnumBase)
```

EGeometry Collection Physics Type Enum

**C++ Source:**

- **Module**: Chaos
- **File**: GeometryCollectionSimulationTypes.h

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_ANGULAR_VELOCITY"></a>

#### CHAOS\_ANGULAR\_VELOCITY

0: Add a vector field to the particles angular velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_DYNAMIC_STATE"></a>

#### CHAOS\_DYNAMIC\_STATE

1: Set the dynamic state of a particle (static, dynamic, kinematic...)

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_LINEAR_VELOCITY"></a>

#### CHAOS\_LINEAR\_VELOCITY

2: Add a vector field to the particles linear velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_INITIAL_ANGULAR_VELOCITY"></a>

#### CHAOS\_INITIAL\_ANGULAR\_VELOCITY

3: Initial particles angular velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_INITIAL_LINEAR_VELOCITY"></a>

#### CHAOS\_INITIAL\_LINEAR\_VELOCITY

4: Initial particles linear velocity.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_COLLISION_GROUP"></a>

#### CHAOS\_COLLISION\_GROUP

5: Set the particles collision group.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_LINEAR_FORCE"></a>

#### CHAOS\_LINEAR\_FORCE

6: Add a vector field to the particles linear force.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_ANGULAR_TORQUE"></a>

#### CHAOS\_ANGULAR\_TORQUE

7: Add a vector field to the particles angular torque.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_DISABLE_THRESHOLD"></a>

#### CHAOS\_DISABLE\_THRESHOLD

8: Disable the particles if their linear and angular velocity are less than the threshold.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_SLEEPING_THRESHOLD"></a>

#### CHAOS\_SLEEPING\_THRESHOLD

9: Set particles in sleeping mode if their linear and angular velocity are less than the threshold.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_EXTERNAL_CLUSTER_STRAIN"></a>

#### CHAOS\_EXTERNAL\_CLUSTER\_STRAIN

10: Apply an external strain over the particles. If this strain is over the internal one, the cluster will break.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_INTERNAL_CLUSTER_STRAIN"></a>

#### CHAOS\_INTERNAL\_CLUSTER\_STRAIN

11: Add a strain field to the particles internal one.

<a id="unreal.GeometryCollectionPhysicsTypeEnum.CHAOS_LINEAR_IMPULSE"></a>

#### CHAOS\_LINEAR\_IMPULSE

12: Add a vector field to apply an impulse to the particles.

<a id="unreal.InitialVelocityTypeEnum"></a>