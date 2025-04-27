## WaveOscillatorCameraShakePattern Objects

```python
class WaveOscillatorCameraShakePattern(SimpleCameraShakePattern)
```

A camera shake that uses oscillations to move the camera.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: WaveOscillatorCameraShakePattern.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_in_time`` (float):  [Read-Write] Blend-in time for this shake. Zero or less means no blend-in.
- ``blend_out_time`` (float):  [Read-Write] Blend-out time for this shake. Zero or less means no blend-out.
- ``duration`` (float):  [Read-Write] Duration in seconds of this shake. Zero or less means infinite.
- ``fov`` (WaveOscillator):  [Read-Write] FOV oscillation.
- ``location_amplitude_multiplier`` (float):  [Read-Write] Amplitude multiplier for all location oscillation
- ``location_frequency_multiplier`` (float):  [Read-Write] Frequency multiplier for all location oscillation
- ``pitch`` (WaveOscillator):  [Read-Write] Pitch oscillation.
- ``roll`` (WaveOscillator):  [Read-Write] Roll oscillation.
- ``rotation_amplitude_multiplier`` (float):  [Read-Write] Amplitude multiplier for all rotation oscillation
- ``rotation_frequency_multiplier`` (float):  [Read-Write] Frequency multiplier for all rotation oscillation
- ``x`` (WaveOscillator):  [Read-Write] Oscillation in the X axis.
- ``y`` (WaveOscillator):  [Read-Write] Oscillation in the Y axis.
- ``yaw`` (WaveOscillator):  [Read-Write] Yaw oscillation.
- ``z`` (WaveOscillator):  [Read-Write] Oscillation in the Z axis.

<a id="unreal.WaveOscillatorCameraShakePattern.location_amplitude_multiplier"></a>

#### location_amplitude_multiplier

```python
@property
def location_amplitude_multiplier() -> float
```

(float):  [Read-Write] Amplitude multiplier for all location oscillation

<a id="unreal.WaveOscillatorCameraShakePattern.location_amplitude_multiplier"></a>

#### location_amplitude_multiplier

```python
@location_amplitude_multiplier.setter
def location_amplitude_multiplier(value: float) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.location_frequency_multiplier"></a>

#### location_frequency_multiplier

```python
@property
def location_frequency_multiplier() -> float
```

(float):  [Read-Write] Frequency multiplier for all location oscillation

<a id="unreal.WaveOscillatorCameraShakePattern.location_frequency_multiplier"></a>

#### location_frequency_multiplier

```python
@location_frequency_multiplier.setter
def location_frequency_multiplier(value: float) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.x"></a>

#### x

```python
@property
def x() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] Oscillation in the X axis.

<a id="unreal.WaveOscillatorCameraShakePattern.x"></a>

#### x

```python
@x.setter
def x(value: WaveOscillator) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.y"></a>

#### y

```python
@property
def y() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] Oscillation in the Y axis.

<a id="unreal.WaveOscillatorCameraShakePattern.y"></a>

#### y

```python
@y.setter
def y(value: WaveOscillator) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.z"></a>

#### z

```python
@property
def z() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] Oscillation in the Z axis.

<a id="unreal.WaveOscillatorCameraShakePattern.z"></a>

#### z

```python
@z.setter
def z(value: WaveOscillator) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.rotation_amplitude_multiplier"></a>

#### rotation_amplitude_multiplier

```python
@property
def rotation_amplitude_multiplier() -> float
```

(float):  [Read-Write] Amplitude multiplier for all rotation oscillation

<a id="unreal.WaveOscillatorCameraShakePattern.rotation_amplitude_multiplier"></a>

#### rotation_amplitude_multiplier

```python
@rotation_amplitude_multiplier.setter
def rotation_amplitude_multiplier(value: float) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.rotation_frequency_multiplier"></a>

#### rotation_frequency_multiplier

```python
@property
def rotation_frequency_multiplier() -> float
```

(float):  [Read-Write] Frequency multiplier for all rotation oscillation

<a id="unreal.WaveOscillatorCameraShakePattern.rotation_frequency_multiplier"></a>

#### rotation_frequency_multiplier

```python
@rotation_frequency_multiplier.setter
def rotation_frequency_multiplier(value: float) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.pitch"></a>

#### pitch

```python
@property
def pitch() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] Pitch oscillation.

<a id="unreal.WaveOscillatorCameraShakePattern.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: WaveOscillator) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.yaw"></a>

#### yaw

```python
@property
def yaw() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] Yaw oscillation.

<a id="unreal.WaveOscillatorCameraShakePattern.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: WaveOscillator) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.roll"></a>

#### roll

```python
@property
def roll() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] Roll oscillation.

<a id="unreal.WaveOscillatorCameraShakePattern.roll"></a>

#### roll

```python
@roll.setter
def roll(value: WaveOscillator) -> None
```

<a id="unreal.WaveOscillatorCameraShakePattern.fov"></a>

#### fov

```python
@property
def fov() -> WaveOscillator
```

(WaveOscillator):  [Read-Write] FOV oscillation.

<a id="unreal.WaveOscillatorCameraShakePattern.fov"></a>

#### fov

```python
@fov.setter
def fov(value: WaveOscillator) -> None
```

<a id="unreal.TestCameraShake"></a>