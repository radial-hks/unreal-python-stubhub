## PerlinNoiseCameraShakePattern Objects

```python
class PerlinNoiseCameraShakePattern(SimpleCameraShakePattern)
```

A camera shake that uses Perlin noise to shake the camera.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: PerlinNoiseCameraShakePattern.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_in_time`` (float):  [Read-Write] Blend-in time for this shake. Zero or less means no blend-in.
- ``blend_out_time`` (float):  [Read-Write] Blend-out time for this shake. Zero or less means no blend-out.
- ``duration`` (float):  [Read-Write] Duration in seconds of this shake. Zero or less means infinite.
- ``fov`` (PerlinNoiseShaker):  [Read-Write] FOV shake.
- ``location_amplitude_multiplier`` (float):  [Read-Write] Amplitude multiplier for all location shake
- ``location_frequency_multiplier`` (float):  [Read-Write] Frequency multiplier for all location shake
- ``pitch`` (PerlinNoiseShaker):  [Read-Write] Pitch shake.
- ``roll`` (PerlinNoiseShaker):  [Read-Write] Roll shake.
- ``rotation_amplitude_multiplier`` (float):  [Read-Write] Amplitude multiplier for all rotation shake
- ``rotation_frequency_multiplier`` (float):  [Read-Write] Frequency multiplier for all rotation shake
- ``x`` (PerlinNoiseShaker):  [Read-Write] Shake in the X axis.
- ``y`` (PerlinNoiseShaker):  [Read-Write] Shake in the Y axis.
- ``yaw`` (PerlinNoiseShaker):  [Read-Write] Yaw shake.
- ``z`` (PerlinNoiseShaker):  [Read-Write] Shake in the Z axis.

<a id="unreal.PerlinNoiseCameraShakePattern.location_amplitude_multiplier"></a>

#### location_amplitude_multiplier

```python
@property
def location_amplitude_multiplier() -> float
```

(float):  [Read-Write] Amplitude multiplier for all location shake

<a id="unreal.PerlinNoiseCameraShakePattern.location_amplitude_multiplier"></a>

#### location_amplitude_multiplier

```python
@location_amplitude_multiplier.setter
def location_amplitude_multiplier(value: float) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.location_frequency_multiplier"></a>

#### location_frequency_multiplier

```python
@property
def location_frequency_multiplier() -> float
```

(float):  [Read-Write] Frequency multiplier for all location shake

<a id="unreal.PerlinNoiseCameraShakePattern.location_frequency_multiplier"></a>

#### location_frequency_multiplier

```python
@location_frequency_multiplier.setter
def location_frequency_multiplier(value: float) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.x"></a>

#### x

```python
@property
def x() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] Shake in the X axis.

<a id="unreal.PerlinNoiseCameraShakePattern.x"></a>

#### x

```python
@x.setter
def x(value: PerlinNoiseShaker) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.y"></a>

#### y

```python
@property
def y() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] Shake in the Y axis.

<a id="unreal.PerlinNoiseCameraShakePattern.y"></a>

#### y

```python
@y.setter
def y(value: PerlinNoiseShaker) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.z"></a>

#### z

```python
@property
def z() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] Shake in the Z axis.

<a id="unreal.PerlinNoiseCameraShakePattern.z"></a>

#### z

```python
@z.setter
def z(value: PerlinNoiseShaker) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.rotation_amplitude_multiplier"></a>

#### rotation_amplitude_multiplier

```python
@property
def rotation_amplitude_multiplier() -> float
```

(float):  [Read-Write] Amplitude multiplier for all rotation shake

<a id="unreal.PerlinNoiseCameraShakePattern.rotation_amplitude_multiplier"></a>

#### rotation_amplitude_multiplier

```python
@rotation_amplitude_multiplier.setter
def rotation_amplitude_multiplier(value: float) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.rotation_frequency_multiplier"></a>

#### rotation_frequency_multiplier

```python
@property
def rotation_frequency_multiplier() -> float
```

(float):  [Read-Write] Frequency multiplier for all rotation shake

<a id="unreal.PerlinNoiseCameraShakePattern.rotation_frequency_multiplier"></a>

#### rotation_frequency_multiplier

```python
@rotation_frequency_multiplier.setter
def rotation_frequency_multiplier(value: float) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.pitch"></a>

#### pitch

```python
@property
def pitch() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] Pitch shake.

<a id="unreal.PerlinNoiseCameraShakePattern.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: PerlinNoiseShaker) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.yaw"></a>

#### yaw

```python
@property
def yaw() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] Yaw shake.

<a id="unreal.PerlinNoiseCameraShakePattern.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: PerlinNoiseShaker) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.roll"></a>

#### roll

```python
@property
def roll() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] Roll shake.

<a id="unreal.PerlinNoiseCameraShakePattern.roll"></a>

#### roll

```python
@roll.setter
def roll(value: PerlinNoiseShaker) -> None
```

<a id="unreal.PerlinNoiseCameraShakePattern.fov"></a>

#### fov

```python
@property
def fov() -> PerlinNoiseShaker
```

(PerlinNoiseShaker):  [Read-Write] FOV shake.

<a id="unreal.PerlinNoiseCameraShakePattern.fov"></a>

#### fov

```python
@fov.setter
def fov(value: PerlinNoiseShaker) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern"></a>