## RootMotionMode Objects

```python
class RootMotionMode(EnumBase)
```

ERoot Motion Mode

**C++ Source:**

- **Module**: Engine
- **File**: AnimEnums.h

<a id="unreal.RootMotionMode.NO_ROOT_MOTION_EXTRACTION"></a>

#### NO\_ROOT\_MOTION\_EXTRACTION

0: Leave root motion in animation.

<a id="unreal.RootMotionMode.IGNORE_ROOT_MOTION"></a>

#### IGNORE\_ROOT\_MOTION

1: Extract root motion but do not apply it.

<a id="unreal.RootMotionMode.ROOT_MOTION_FROM_EVERYTHING"></a>

#### ROOT\_MOTION\_FROM\_EVERYTHING

2: Root motion is taken from all animations contributing to the final pose, not suitable for network multiplayer setups.

<a id="unreal.RootMotionMode.ROOT_MOTION_FROM_MONTAGES_ONLY"></a>

#### ROOT\_MOTION\_FROM\_MONTAGES\_ONLY

3: Root motion is only taken from montages, suitable for network multiplayer setups.

<a id="unreal.MontagePlayReturnType"></a>