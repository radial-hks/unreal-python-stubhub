## RootMotionMode Objects

```python
class RootMotionMode(EnumBase)
```

ERoot Motion Mode

**C++ Source:**

- **Module**: Engine
- **File**: AnimEnums.h

<a id="unreal.RootMotionMode.NO_ROOT_MOTION_EXTRACTION"></a>

#### NO_ROOT_MOTION_EXTRACTION

0: Leave root motion in animation.

<a id="unreal.RootMotionMode.IGNORE_ROOT_MOTION"></a>

#### IGNORE_ROOT_MOTION

1: Extract root motion but do not apply it.

<a id="unreal.RootMotionMode.ROOT_MOTION_FROM_EVERYTHING"></a>

#### ROOT_MOTION_FROM_EVERYTHING

2: Root motion is taken from all animations contributing to the final pose, not suitable for network multiplayer setups.

<a id="unreal.RootMotionMode.ROOT_MOTION_FROM_MONTAGES_ONLY"></a>

#### ROOT_MOTION_FROM_MONTAGES_ONLY

3: Root motion is only taken from montages, suitable for network multiplayer setups.

<a id="unreal.MontagePlayReturnType"></a>