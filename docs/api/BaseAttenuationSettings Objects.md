## BaseAttenuationSettings Objects

```python
class BaseAttenuationSettings(StructBase)
```

* Base class for attenuation settings.

**C++ Source:**

- **Module**: Engine
- **File**: Attenuation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attenuation_shape`` (AttenuationShape):  [Read-Write] The shape of the non-custom attenuation method.
- ``attenuation_shape_extents`` (Vector):  [Read-Write] The dimensions to use for the attenuation shape. Interpretation of the values differ per shape.
           Sphere  - X is Sphere Radius. Y and Z are unused
           Capsule - X is Capsule Half Height, Y is Capsule Radius, Z is unused
           Box     - X, Y, and Z are the Box's dimensions
           Cone    - X is Cone Radius, Y is Cone Angle, Z is Cone Falloff Angle
- ``cone_offset`` (float):  [Read-Write] The distance back from the sound's origin to begin the cone when using the cone attenuation shape.
- ``cone_sphere_falloff_distance`` (float):  [Read-Write] The distance over which volume attenuation occurs for the optional sphere shape.
- ``cone_sphere_radius`` (float):  [Read-Write] An optional attenuation radius (sphere) that extends from the cone origin.
- ``custom_attenuation_curve`` (RuntimeFloatCurve):  [Read-Write] The custom volume attenuation curve to use.
- ``d_b_attenuation_at_max`` (float):  [Read-Write] The attenuation volume at the falloff distance in decibels (Only for 'Natural Sound' Distance Algorithm).
- ``distance_algorithm`` (AttenuationDistanceModel):  [Read-Write] The type of attenuation as a function of distance to use.
- ``falloff_distance`` (float):  [Read-Write] The distance over which volume attenuation occurs.
- ``falloff_mode`` (NaturalSoundFalloffMode):  [Read-Write] Whether to continue attenuating, go silent, or hold last volume value when beyond falloff bounds and
  'Attenuation At Max (dB)' is set to a value greater than -60dB.
  (Only for 'Natural Sound' Distance Algorithm). */

<a id="unreal.BaseAttenuationSettings.__init__"></a>

#### __init__

```python
def __init__(
        distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel
    .LINEAR,
        attenuation_shape: AttenuationShape = AttenuationShape.SPHERE,
        falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.
    CONTINUES,
        d_b_attenuation_at_max: float = 0.000000,
        attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000],
        cone_offset: float = 0.000000,
        falloff_distance: float = 0.000000,
        cone_sphere_radius: float = 0.000000,
        cone_sphere_falloff_distance: float = 0.000000,
        custom_attenuation_curve: RuntimeFloatCurve = []) -> None
```

<a id="unreal.BaseAttenuationSettings.distance_algorithm"></a>

#### distance_algorithm

```python
@property
def distance_algorithm() -> AttenuationDistanceModel
```

(AttenuationDistanceModel):  [Read-Write] The type of attenuation as a function of distance to use.

<a id="unreal.BaseAttenuationSettings.distance_algorithm"></a>

#### distance_algorithm

```python
@distance_algorithm.setter
def distance_algorithm(value: AttenuationDistanceModel) -> None
```

<a id="unreal.BaseAttenuationSettings.attenuation_shape"></a>

#### attenuation_shape

```python
@property
def attenuation_shape() -> AttenuationShape
```

(AttenuationShape):  [Read-Write] The shape of the non-custom attenuation method.

<a id="unreal.BaseAttenuationSettings.attenuation_shape"></a>

#### attenuation_shape

```python
@attenuation_shape.setter
def attenuation_shape(value: AttenuationShape) -> None
```

<a id="unreal.BaseAttenuationSettings.falloff_mode"></a>

#### falloff_mode

```python
@property
def falloff_mode() -> NaturalSoundFalloffMode
```

(NaturalSoundFalloffMode):  [Read-Write] Whether to continue attenuating, go silent, or hold last volume value when beyond falloff bounds and
'Attenuation At Max (dB)' is set to a value greater than -60dB.
(Only for 'Natural Sound' Distance Algorithm). */

<a id="unreal.BaseAttenuationSettings.falloff_mode"></a>

#### falloff_mode

```python
@falloff_mode.setter
def falloff_mode(value: NaturalSoundFalloffMode) -> None
```

<a id="unreal.BaseAttenuationSettings.d_b_attenuation_at_max"></a>

#### d_b_attenuation_at_max

```python
@property
def d_b_attenuation_at_max() -> float
```

(float):  [Read-Write] The attenuation volume at the falloff distance in decibels (Only for 'Natural Sound' Distance Algorithm).

<a id="unreal.BaseAttenuationSettings.d_b_attenuation_at_max"></a>

#### d_b_attenuation_at_max

```python
@d_b_attenuation_at_max.setter
def d_b_attenuation_at_max(value: float) -> None
```

<a id="unreal.BaseAttenuationSettings.attenuation_shape_extents"></a>

#### attenuation_shape_extents

```python
@property
def attenuation_shape_extents() -> Vector
```

(Vector):  [Read-Write] The dimensions to use for the attenuation shape. Interpretation of the values differ per shape.
         Sphere  - X is Sphere Radius. Y and Z are unused
         Capsule - X is Capsule Half Height, Y is Capsule Radius, Z is unused
         Box     - X, Y, and Z are the Box's dimensions
         Cone    - X is Cone Radius, Y is Cone Angle, Z is Cone Falloff Angle

<a id="unreal.BaseAttenuationSettings.attenuation_shape_extents"></a>

#### attenuation_shape_extents

```python
@attenuation_shape_extents.setter
def attenuation_shape_extents(value: Vector) -> None
```

<a id="unreal.BaseAttenuationSettings.cone_offset"></a>

#### cone_offset

```python
@property
def cone_offset() -> float
```

(float):  [Read-Write] The distance back from the sound's origin to begin the cone when using the cone attenuation shape.

<a id="unreal.BaseAttenuationSettings.cone_offset"></a>

#### cone_offset

```python
@cone_offset.setter
def cone_offset(value: float) -> None
```

<a id="unreal.BaseAttenuationSettings.falloff_distance"></a>

#### falloff_distance

```python
@property
def falloff_distance() -> float
```

(float):  [Read-Write] The distance over which volume attenuation occurs.

<a id="unreal.BaseAttenuationSettings.falloff_distance"></a>

#### falloff_distance

```python
@falloff_distance.setter
def falloff_distance(value: float) -> None
```

<a id="unreal.BaseAttenuationSettings.cone_sphere_radius"></a>

#### cone_sphere_radius

```python
@property
def cone_sphere_radius() -> float
```

(float):  [Read-Write] An optional attenuation radius (sphere) that extends from the cone origin.

<a id="unreal.BaseAttenuationSettings.cone_sphere_radius"></a>

#### cone_sphere_radius

```python
@cone_sphere_radius.setter
def cone_sphere_radius(value: float) -> None
```

<a id="unreal.BaseAttenuationSettings.cone_sphere_falloff_distance"></a>

#### cone_sphere_falloff_distance

```python
@property
def cone_sphere_falloff_distance() -> float
```

(float):  [Read-Write] The distance over which volume attenuation occurs for the optional sphere shape.

<a id="unreal.BaseAttenuationSettings.cone_sphere_falloff_distance"></a>

#### cone_sphere_falloff_distance

```python
@cone_sphere_falloff_distance.setter
def cone_sphere_falloff_distance(value: float) -> None
```

<a id="unreal.BaseAttenuationSettings.custom_attenuation_curve"></a>

#### custom_attenuation_curve

```python
@property
def custom_attenuation_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The custom volume attenuation curve to use.

<a id="unreal.BaseAttenuationSettings.custom_attenuation_curve"></a>

#### custom_attenuation_curve

```python
@custom_attenuation_curve.setter
def custom_attenuation_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.ForceFeedbackAttenuationSettings"></a>