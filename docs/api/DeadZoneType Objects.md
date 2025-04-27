## DeadZoneType Objects

```python
class DeadZoneType(EnumBase)
```

EDead Zone Type

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

<a id="unreal.DeadZoneType.AXIAL"></a>

#### AXIAL

0: Apply dead zone to axes individually. This will result in input being chamfered at the corners for
2d/3d axis inputs, and matches the original UE4 deadzone logic.

<a id="unreal.DeadZoneType.RADIAL"></a>

#### RADIAL

1: Apply dead zone logic to all axes simultaneously. This gives smooth input (circular/spherical coverage).
On a 1d axis input this works identically to Axial.

For most games, this will give the smoothest feeling analog values. The input is smoothed to avoid
"jumpiness" when you are moving the analog axis.

<a id="unreal.DeadZoneType.UNSCALED_RADIAL"></a>

#### UNSCALED_RADIAL

2: Apply dead zone logic to all axes simultaneously without any smooth input
which the normal "Radial" deadzone applies.

The behavior of this deadzone type is as follows:
If the magnitude of the input is less then the lower threshold, ignore it.
Clamp the magnitude of the input to the upper threshold value.

For some games, this may result in feeling "jumpy", because the value goes from 0.0 to
the lower threshold immediately instead of being smoothed, like the normal "Radial" deadzone option.

<a id="unreal.FOVScalingType"></a>