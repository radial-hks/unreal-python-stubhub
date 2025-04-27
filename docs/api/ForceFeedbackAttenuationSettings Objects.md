## ForceFeedbackAttenuationSettings Objects

```python
class ForceFeedbackAttenuationSettings(BaseAttenuationSettings)
```

The struct for defining the properties used when determining attenuation for a force feedback effect

**C++ Source:**

- **Module**: Engine
- **File**: ForceFeedbackAttenuation.h

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

<a id="unreal.ForceFeedbackAttenuationSettings.__init__"></a>

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

<a id="unreal.PredictProjectilePathParams"></a>