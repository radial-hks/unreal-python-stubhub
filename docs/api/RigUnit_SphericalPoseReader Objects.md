## RigUnit_SphericalPoseReader Objects

```python
class RigUnit_SphericalPoseReader(RigUnit_HighlevelBaseMutable)
```

* Outputs a float value between 0-1 based off of the driver item's rotation in a specified region.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SphericalPoseReader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_region_scale_factors`` (RegionScaleFactors):  [Read-Write] The directional scaling parameters for the active region (green).
- ``active_region_size`` (float):  [Read-Write] The size of the active region (green) that outputs the full value (1.0). Range is 0-1. Default is 0.1.
- ``debug`` (SphericalPoseReaderDebugSettings):  [Read-Write]
- ``driver_axis`` (Vector):  [Read-Write] The axis of the driver transform that is compared against the falloff regions. Typically the axis that is pointing at the child; usually X by convention. Default is X-axis (1,0,0).
- ``driver_item`` (RigElementKey):  [Read-Write] The bone that will drive the output parameter when rotated into the active regions of this pose reader.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``falloff_region_scale_factors`` (RegionScaleFactors):  [Read-Write] The directional scaling parameters for the falloff region (yellow).
- ``falloff_size`` (float):  [Read-Write] The size of the falloff region (yellow) that defines the start of the output range. A value of 1 wraps the entire sphere with falloff. Range is 0-1. Default is 0.2.
- ``flip_height_scaling`` (bool):  [Read-Write] Flip the positive / negative directions of the height scale factors.
- ``flip_width_scaling`` (bool):  [Read-Write] Flip the positive / negative directions of the width scale factors.
- ``optional_parent_item`` (RigElementKey):  [Read-Write] An optional parent to use as a stable frame of reference for the active regions (defaults to DriverItem's parent if unset).
- ``output_param`` (float):  [Read-Write] The normalized output parameter; ranges from 0 (when outside yellow region) to 1 (in the green region) and smoothly blends from 0-1 in the yellow region.
- ``rotation_offset`` (Vector):  [Read-Write] Rotate the entire falloff region to align with the desired area of effect.

<a id="unreal.RigUnit_SphericalPoseReader.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    output_param: float = 0.000000,
    driver_item: RigElementKey = [RigElementType.NONE, "None"],
    driver_axis: Vector = [0.000000, 0.000000, 0.000000],
    rotation_offset: Vector = [0.000000, 0.000000, 0.000000],
    active_region_size: float = 0.000000,
    active_region_scale_factors: RegionScaleFactors = [
        1.000000, 1.000000, 1.000000, 1.000000
    ],
    falloff_size: float = 0.000000,
    falloff_region_scale_factors: RegionScaleFactors = [
        1.000000, 1.000000, 1.000000, 1.000000
    ],
    flip_width_scaling: bool = False,
    flip_height_scaling: bool = False,
    optional_parent_item: RigElementKey = [RigElementType.NONE, "None"],
    debug: SphericalPoseReaderDebugSettings = [
        True, False, False, 25.000000, 20, 0.250000
    ]
) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.output_param"></a>

#### output_param

```python
@property
def output_param() -> float
```

(float):  [Read-Only] The normalized output parameter; ranges from 0 (when outside yellow region) to 1 (in the green region) and smoothly blends from 0-1 in the yellow region.

<a id="unreal.RigUnit_SphericalPoseReader.driver_item"></a>

#### driver_item

```python
@property
def driver_item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The bone that will drive the output parameter when rotated into the active regions of this pose reader.

<a id="unreal.RigUnit_SphericalPoseReader.driver_item"></a>

#### driver_item

```python
@driver_item.setter
def driver_item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.driver_axis"></a>

#### driver_axis

```python
@property
def driver_axis() -> Vector
```

(Vector):  [Read-Write] The axis of the driver transform that is compared against the falloff regions. Typically the axis that is pointing at the child; usually X by convention. Default is X-axis (1,0,0).

<a id="unreal.RigUnit_SphericalPoseReader.driver_axis"></a>

#### driver_axis

```python
@driver_axis.setter
def driver_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Vector
```

(Vector):  [Read-Write] Rotate the entire falloff region to align with the desired area of effect.

<a id="unreal.RigUnit_SphericalPoseReader.rotation_offset"></a>

#### rotation_offset

```python
@rotation_offset.setter
def rotation_offset(value: Vector) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.active_region_size"></a>

#### active_region_size

```python
@property
def active_region_size() -> float
```

(float):  [Read-Write] The size of the active region (green) that outputs the full value (1.0). Range is 0-1. Default is 0.1.

<a id="unreal.RigUnit_SphericalPoseReader.active_region_size"></a>

#### active_region_size

```python
@active_region_size.setter
def active_region_size(value: float) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.active_region_scale_factors"></a>

#### active_region_scale_factors

```python
@property
def active_region_scale_factors() -> RegionScaleFactors
```

(RegionScaleFactors):  [Read-Write] The directional scaling parameters for the active region (green).

<a id="unreal.RigUnit_SphericalPoseReader.active_region_scale_factors"></a>

#### active_region_scale_factors

```python
@active_region_scale_factors.setter
def active_region_scale_factors(value: RegionScaleFactors) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.falloff_size"></a>

#### falloff_size

```python
@property
def falloff_size() -> float
```

(float):  [Read-Write] The size of the falloff region (yellow) that defines the start of the output range. A value of 1 wraps the entire sphere with falloff. Range is 0-1. Default is 0.2.

<a id="unreal.RigUnit_SphericalPoseReader.falloff_size"></a>

#### falloff_size

```python
@falloff_size.setter
def falloff_size(value: float) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.falloff_region_scale_factors"></a>

#### falloff_region_scale_factors

```python
@property
def falloff_region_scale_factors() -> RegionScaleFactors
```

(RegionScaleFactors):  [Read-Write] The directional scaling parameters for the falloff region (yellow).

<a id="unreal.RigUnit_SphericalPoseReader.falloff_region_scale_factors"></a>

#### falloff_region_scale_factors

```python
@falloff_region_scale_factors.setter
def falloff_region_scale_factors(value: RegionScaleFactors) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.flip_width_scaling"></a>

#### flip_width_scaling

```python
@property
def flip_width_scaling() -> bool
```

(bool):  [Read-Write] Flip the positive / negative directions of the width scale factors.

<a id="unreal.RigUnit_SphericalPoseReader.flip_width_scaling"></a>

#### flip_width_scaling

```python
@flip_width_scaling.setter
def flip_width_scaling(value: bool) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.flip_height_scaling"></a>

#### flip_height_scaling

```python
@property
def flip_height_scaling() -> bool
```

(bool):  [Read-Write] Flip the positive / negative directions of the height scale factors.

<a id="unreal.RigUnit_SphericalPoseReader.flip_height_scaling"></a>

#### flip_height_scaling

```python
@flip_height_scaling.setter
def flip_height_scaling(value: bool) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.optional_parent_item"></a>

#### optional_parent_item

```python
@property
def optional_parent_item() -> RigElementKey
```

(RigElementKey):  [Read-Write] An optional parent to use as a stable frame of reference for the active regions (defaults to DriverItem's parent if unset).

<a id="unreal.RigUnit_SphericalPoseReader.optional_parent_item"></a>

#### optional_parent_item

```python
@optional_parent_item.setter
def optional_parent_item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader.debug"></a>

#### debug

```python
@property
def debug() -> SphericalPoseReaderDebugSettings
```

(SphericalPoseReaderDebugSettings):  [Read-Write]

<a id="unreal.RigUnit_SphericalPoseReader.debug"></a>

#### debug

```python
@debug.setter
def debug(value: SphericalPoseReaderDebugSettings) -> None
```

<a id="unreal.RigUnit_SpringIK_DebugSettings"></a>