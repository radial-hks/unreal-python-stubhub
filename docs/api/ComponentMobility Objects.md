## ComponentMobility Objects

```python
class ComponentMobility(EnumBase)
```

Describes how often this component is allowed to move.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.ComponentMobility.STATIC"></a>

#### STATIC

0: Static objects cannot be moved or changed in game.
- Allows baked lighting
- Fastest rendering

<a id="unreal.ComponentMobility.STATIONARY"></a>

#### STATIONARY

1: A stationary light will only have its shadowing and bounced lighting from static geometry baked by Lightmass, all other lighting will be dynamic.
- It can change color and intensity in game.
- Can't move
- Allows partial baked lighting
- Dynamic shadows

<a id="unreal.ComponentMobility.MOVABLE"></a>

#### MOVABLE

2: Movable objects can be moved and changed in game.
- Totally dynamic
- Can cast dynamic shadows
- Slowest rendering

<a id="unreal.ModifyFrequency"></a>