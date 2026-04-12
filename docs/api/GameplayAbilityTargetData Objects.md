## GameplayAbilityTargetData Objects

```python
class GameplayAbilityTargetData(StructBase)
```

A generic structure for targeting data. We want generic functions to produce this data and other generic
functions to consume this data.

We expect this to be able to hold specific actors/object reference and also generic location/direction/origin
information.

Some example producers:
        -Overlap/Hit collision event generates TargetData about who was hit in a melee attack
        -A mouse input causes a hit trace and the actor infront of the crosshair is turned into TargetData
        -A mouse input causes TargetData to be generated from the owner's crosshair view origin/direction
        -An AOE/aura pulses and all actors in a radius around the instigator are added to TargetData
        -Panzer Dragoon style 'painting' targeting mode
        -MMORPG style ground AOE targeting style (potentially both a location on the ground and actors that were targeted)

Some example consumers:
        -Apply a GameplayEffect to all actors in TargetData
        -Find closest actor from all in TargetData
        -Call some function on all actors in TargetData
        -Filter or merge TargetDatas
        -Spawn a new actor at a TargetData location

Maybe it is better to distinguish between actor list targeting vs positional targeting data?
        -AOE/aura type of targeting data blurs the line

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

<a id="unreal.GameplayAbilityTargetData.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GameplayAbilityTargetData_LocationInfo"></a>