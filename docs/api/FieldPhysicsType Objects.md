## FieldPhysicsType Objects

```python
class FieldPhysicsType(EnumBase)
```

EField Physics Type

**C++ Source:**

- **Module**: Chaos
- **File**: FieldSystemTypes.h

<a id="unreal.FieldPhysicsType.FIELD_DYNAMIC_STATE"></a>

#### FIELD\_DYNAMIC\_STATE

1: Set the dynamic state of a particle (static, dynamic, kinematic...)

<a id="unreal.FieldPhysicsType.FIELD_LINEAR_FORCE"></a>

#### FIELD\_LINEAR\_FORCE

2: Add a vector field to the particles linear force.

<a id="unreal.FieldPhysicsType.FIELD_EXTERNAL_CLUSTER_STRAIN"></a>

#### FIELD\_EXTERNAL\_CLUSTER\_STRAIN

3: Apply an external strain over the particles. If this strain is over the internal one, the cluster will break.

<a id="unreal.FieldPhysicsType.FIELD_KILL"></a>

#### FIELD\_KILL

4: Disable the particles for which the field will be higher than 0.

<a id="unreal.FieldPhysicsType.FIELD_LINEAR_VELOCITY"></a>

#### FIELD\_LINEAR\_VELOCITY

5: Add a vector field to the particles linear velocity.

<a id="unreal.FieldPhysicsType.FIELD_ANGULAR_VELOCIY"></a>

#### FIELD\_ANGULAR\_VELOCIY

6: Add a vector field to the particles angular velocity.

<a id="unreal.FieldPhysicsType.FIELD_ANGULAR_TORQUE"></a>

#### FIELD\_ANGULAR\_TORQUE

7: Add a vector field to the particles angular torque.

<a id="unreal.FieldPhysicsType.FIELD_INTERNAL_CLUSTER_STRAIN"></a>

#### FIELD\_INTERNAL\_CLUSTER\_STRAIN

8: Add a strain field to the particles internal one.

<a id="unreal.FieldPhysicsType.FIELD_DISABLE_THRESHOLD"></a>

#### FIELD\_DISABLE\_THRESHOLD

9: Disable the particles if their linear and angular velocity are less than the threshold.

<a id="unreal.FieldPhysicsType.FIELD_SLEEPING_THRESHOLD"></a>

#### FIELD\_SLEEPING\_THRESHOLD

10: Set particles in sleeping mode if their linear and angular velocity are less than the threshold.

<a id="unreal.FieldPhysicsType.FIELD_COLLISION_GROUP"></a>

#### FIELD\_COLLISION\_GROUP

15: Set the particles collision group.

<a id="unreal.FieldPhysicsType.FIELD_ACTIVATE_DISABLED"></a>

#### FIELD\_ACTIVATE\_DISABLED

16: Activate all the disabled particles for which the field value will be 0

<a id="unreal.FieldVectorType"></a>