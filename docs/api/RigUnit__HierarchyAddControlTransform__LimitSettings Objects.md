## RigUnit\_HierarchyAddControlTransform\_LimitSettings Objects

```python
class RigUnit_HierarchyAddControlTransform_LimitSettings(StructBase)
```

Rig Unit Hierarchy Add Control Transform Limit Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_limits`` (bool):  [Read-Write]
- ``limit_pitch`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_roll`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_scale_x`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_scale_y`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_scale_z`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_translation_x`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_translation_y`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_translation_z`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_yaw`` (RigControlLimitEnabled):  [Read-Write]
- ``max_value`` (EulerTransform):  [Read-Write]
- ``min_value`` (EulerTransform):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(limit_translation_x: RigControlLimitEnabled = [False, False],
             limit_translation_y: RigControlLimitEnabled = [False, False],
             limit_translation_z: RigControlLimitEnabled = [False, False],
             limit_pitch: RigControlLimitEnabled = [False, False],
             limit_yaw: RigControlLimitEnabled = [False, False],
             limit_roll: RigControlLimitEnabled = [False, False],
             limit_scale_x: RigControlLimitEnabled = [False, False],
             limit_scale_y: RigControlLimitEnabled = [False, False],
             limit_scale_z: RigControlLimitEnabled = [False, False],
             min_value: EulerTransform = [[0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          [1.000000, 1.000000, 1.000000]],
             max_value: EulerTransform = [[0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          [1.000000, 1.000000, 1.000000]],
             draw_limits: bool = False) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_x"></a>

#### limit\_translation\_x

```python
@property
def limit_translation_x() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_x"></a>

#### limit\_translation\_x

```python
@limit_translation_x.setter
def limit_translation_x(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_y"></a>

#### limit\_translation\_y

```python
@property
def limit_translation_y() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_y"></a>

#### limit\_translation\_y

```python
@limit_translation_y.setter
def limit_translation_y(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_z"></a>

#### limit\_translation\_z

```python
@property
def limit_translation_z() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_z"></a>

#### limit\_translation\_z

```python
@limit_translation_z.setter
def limit_translation_z(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_pitch"></a>

#### limit\_pitch

```python
@property
def limit_pitch() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_pitch"></a>

#### limit\_pitch

```python
@limit_pitch.setter
def limit_pitch(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_yaw"></a>

#### limit\_yaw

```python
@property
def limit_yaw() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_yaw"></a>

#### limit\_yaw

```python
@limit_yaw.setter
def limit_yaw(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_roll"></a>

#### limit\_roll

```python
@property
def limit_roll() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_roll"></a>

#### limit\_roll

```python
@limit_roll.setter
def limit_roll(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_x"></a>

#### limit\_scale\_x

```python
@property
def limit_scale_x() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_x"></a>

#### limit\_scale\_x

```python
@limit_scale_x.setter
def limit_scale_x(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_y"></a>

#### limit\_scale\_y

```python
@property
def limit_scale_y() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_y"></a>

#### limit\_scale\_y

```python
@limit_scale_y.setter
def limit_scale_y(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_z"></a>

#### limit\_scale\_z

```python
@property
def limit_scale_z() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_z"></a>

#### limit\_scale\_z

```python
@limit_scale_z.setter
def limit_scale_z(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.min_value"></a>

#### min\_value

```python
@property
def min_value() -> EulerTransform
```

(EulerTransform):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.min_value"></a>

#### min\_value

```python
@min_value.setter
def min_value(value: EulerTransform) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.max_value"></a>

#### max\_value

```python
@property
def max_value() -> EulerTransform
```

(EulerTransform):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.max_value"></a>

#### max\_value

```python
@max_value.setter
def max_value(value: EulerTransform) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.draw_limits"></a>

#### draw\_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.draw_limits"></a>

#### draw\_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings"></a>