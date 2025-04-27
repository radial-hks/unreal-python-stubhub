## ClothingTeleportMode Objects

```python
class ClothingTeleportMode(EnumBase)
```

EClothing Teleport Mode

**C++ Source:**

- **Module**: ClothingSystemRuntimeInterface
- **File**: ClothingSystemRuntimeTypes.h

<a id="unreal.ClothingTeleportMode.NONE"></a>

#### NONE

0: No teleport, simulate as normal

<a id="unreal.ClothingTeleportMode.TELEPORT"></a>

#### TELEPORT

1: Teleport the simulation, causing no intertial effects but keep the sim mesh shape

<a id="unreal.ClothingTeleportMode.TELEPORT_AND_RESET"></a>

#### TELEPORT_AND_RESET

2: Teleport the simulation, causing no intertial effects and reset the sim mesh shape

<a id="unreal.ClothingTeleportMode.HARD_RESET"></a>

#### HARD_RESET

3: Hard reset the simulation by refreshing the cloth config

<a id="unreal.AnimationMode"></a>