## WorldPositionIncludedOffsets Objects

```python
class WorldPositionIncludedOffsets(EnumBase)
```

Specifies which shader generated offsets should included in the world position (displacement/WPO etc.)

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionWorldPosition.h

<a id="unreal.WorldPositionIncludedOffsets.WPT_DEFAULT"></a>

#### WPT_DEFAULT

0: Absolute world position with all material shader offsets applied

<a id="unreal.WorldPositionIncludedOffsets.WPT_EXCLUDE_ALL_SHADER_OFFSETS"></a>

#### WPT_EXCLUDE_ALL_SHADER_OFFSETS

1: Absolute world position with no material shader offsets applied

<a id="unreal.WorldPositionIncludedOffsets.WPT_CAMERA_RELATIVE"></a>

#### WPT_CAMERA_RELATIVE

2: Camera relative world position with all material shader offsets applied

<a id="unreal.WorldPositionIncludedOffsets.WPT_CAMERA_RELATIVE_NO_OFFSETS"></a>

#### WPT_CAMERA_RELATIVE_NO_OFFSETS

3: Camera relative world position with no material shader offsets applied

<a id="unreal.ParticleSystemUpdateMode"></a>