## TeleportType Objects

```python
class TeleportType(EnumBase)
```

Whether to teleport physics body or not

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.TeleportType.NONE"></a>

#### NONE

0: Do not teleport physics body. This means velocity will reflect the movement between initial and final position, and collisions along the way will occur

<a id="unreal.TeleportType.TELEPORT_PHYSICS"></a>

#### TELEPORT_PHYSICS

1: Teleport physics body so that velocity remains the same and no collision occurs

<a id="unreal.TeleportType.RESET_PHYSICS"></a>

#### RESET_PHYSICS

2: Teleport physics body and reset physics state completely

<a id="unreal.CustomBoneAttributeLookup"></a>