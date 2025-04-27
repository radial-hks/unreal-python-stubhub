## CEClonerCollisionRadiusMode Objects

```python
class CEClonerCollisionRadiusMode(EnumBase)
```

Enumerates all modes for how clones radius are calculed

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerEffectorShared.h

<a id="unreal.CEClonerCollisionRadiusMode.MANUAL"></a>

#### MANUAL

0: Input collision radius manually

<a id="unreal.CEClonerCollisionRadiusMode.MIN_EXTENT"></a>

#### MIN_EXTENT

1: Collision radius will be calculated automatically based on the min extent value, mesh scale included

<a id="unreal.CEClonerCollisionRadiusMode.MAX_EXTENT"></a>

#### MAX_EXTENT

2: Collision radius will be calculated automatically based on the max extent value, mesh scale included

<a id="unreal.CEClonerCollisionRadiusMode.EXTENT_LENGTH"></a>

#### EXTENT_LENGTH

3: Collision radius will be calculated automatically based on the extent length, mesh scale included

<a id="unreal.CEClonerSpawnLoopMode"></a>