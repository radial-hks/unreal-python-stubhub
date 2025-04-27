## FOVScalingType Objects

```python
class FOVScalingType(EnumBase)
```

EFOVScaling Type

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

<a id="unreal.FOVScalingType.STANDARD"></a>

#### STANDARD

0: FOV scaling to apply scaled movement deltas to inputs dependent upon the player's selected FOV

<a id="unreal.FOVScalingType.UE4_BACK_COMPAT"></a>

#### UE4_BACK_COMPAT

1: FOV scaling was incorrectly calculated in UE4's UPlayerInput::MassageAxisInput. This implementation is intended to aid backwards compatibility, but should not be used by new projects.

<a id="unreal.InputAxisSwizzle"></a>