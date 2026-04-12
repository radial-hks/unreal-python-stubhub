## GameplayCueNotify\_LocallyControlledPolicy Objects

```python
class GameplayCueNotify_LocallyControlledPolicy(EnumBase)
```

EGameplayCueNotify_LocallyControlledPolicy

    Specifies if the gameplay cue notify should spawn based on it being locally controlled.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

<a id="unreal.GameplayCueNotify_LocallyControlledPolicy.ALWAYS"></a>

#### ALWAYS

0: Always spawns regardless of locally controlled.

<a id="unreal.GameplayCueNotify_LocallyControlledPolicy.LOCAL_ONLY"></a>

#### LOCAL\_ONLY

1: Only spawn if the source actor is locally controlled.

<a id="unreal.GameplayCueNotify_LocallyControlledPolicy.NOT_LOCAL"></a>

#### NOT\_LOCAL

2: Only spawn if the source actor is NOT locally controlled.

<a id="unreal.GameplayCueNotify_AttachPolicy"></a>