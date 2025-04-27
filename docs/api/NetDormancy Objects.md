## NetDormancy Objects

```python
class NetDormancy(EnumBase)
```

Describes if an actor can enter a low network bandwidth dormant mode

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.NetDormancy.DORM_NEVER"></a>

#### DORM_NEVER

0: This actor can never go network dormant.

<a id="unreal.NetDormancy.DORM_AWAKE"></a>

#### DORM_AWAKE

1: This actor can go dormant, but is not currently dormant. Game code will tell it when it go dormant.

<a id="unreal.NetDormancy.DORM_DORMANT_ALL"></a>

#### DORM_DORMANT_ALL

2: This actor wants to go fully dormant for all connections.

<a id="unreal.NetDormancy.DORM_DORMANT_PARTIAL"></a>

#### DORM_DORMANT_PARTIAL

3: This actor may want to go dormant for some connections, GetNetDormancy() will be called to find out which.

<a id="unreal.NetDormancy.DORM_INITIAL"></a>

#### DORM_INITIAL

4: This actor is initially dormant for all connection if it was placed in map.

<a id="unreal.PhysicsReplicationMode"></a>