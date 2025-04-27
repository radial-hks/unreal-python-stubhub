## PhysicsReplicationMode Objects

```python
class PhysicsReplicationMode(EnumBase)
```

EPhysics Replication Mode

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.PhysicsReplicationMode.DEFAULT"></a>

#### DEFAULT

0: Default physics replication.

<a id="unreal.PhysicsReplicationMode.PREDICTIVE_INTERPOLATION"></a>

#### PREDICTIVE_INTERPOLATION

1: Work In Progress. Physics replication performing velocity interpolation.
Recommendation: Set on actors with a local role of ENetRole::ROLE_SimulatedProxy.
Designed to handle local predictive interactions with other actors, especially actors of the local role ENetRole::ROLE_AutonomousProxy.

<a id="unreal.PhysicsReplicationMode.RESIMULATION"></a>

#### RESIMULATION

2: Work In Progress. Forward predicted replication by simulating physics and correcting errors through resimulating physics from a correct state in the past.
Recommendation: Set on actors with a local role of ENetRole::ROLE_AutonomousProxy.
Can be used for both ROLE_AutonomousProxy and ROLE_SimulatedProxy, though not recommended for ROLE_SimulatedProxy due to CPU performance.
Available when Project Settings > Physics Prediction is enabled.

<a id="unreal.PhysicalMaterialMaskColor"></a>