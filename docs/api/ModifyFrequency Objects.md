## ModifyFrequency Objects

```python
class ModifyFrequency(EnumBase)
```

deprecated: 'ModifyFrequency' was renamed to 'ComponentMobility'.

<a id="unreal.ModifyFrequency.STATIC"></a>

#### STATIC

0: Static objects cannot be moved or changed in game.
- Allows baked lighting
- Fastest rendering

<a id="unreal.ModifyFrequency.STATIONARY"></a>

#### STATIONARY

1: A stationary light will only have its shadowing and bounced lighting from static geometry baked by Lightmass, all other lighting will be dynamic.
- It can change color and intensity in game.
- Can't move
- Allows partial baked lighting
- Dynamic shadows

<a id="unreal.ModifyFrequency.MOVABLE"></a>

#### MOVABLE

2: Movable objects can be moved and changed in game.
- Totally dynamic
- Can cast dynamic shadows
- Slowest rendering

<a id="unreal.CollisionEnabled"></a>