## GerstnerWaterWaveGeneratorSimple Objects

```python
class GerstnerWaterWaveGeneratorSimple(GerstnerWaterWaveGeneratorBase)
```

Default implementation of a gerstner wave generator using a simple custom range based set of parameters to generate waves.

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: GerstnerWaterWaves.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude_falloff`` (float):  [Read-Write]
- ``direction_angular_spread_deg`` (float):  [Read-Write]
- ``large_wave_steepness`` (float):  [Read-Write]
- ``max_amplitude`` (float):  [Read-Write]
- ``max_wavelength`` (float):  [Read-Write]
- ``min_amplitude`` (float):  [Read-Write]
- ``min_wavelength`` (float):  [Read-Write]
- ``num_waves`` (int32):  [Read-Write]
- ``randomness`` (float):  [Read-Write]
- ``seed`` (int32):  [Read-Write]
- ``small_wave_steepness`` (float):  [Read-Write]
- ``steepness_falloff`` (float):  [Read-Write]
- ``wavelength_falloff`` (float):  [Read-Write]
- ``wind_angle_deg`` (float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.num_waves"></a>

#### num_waves

```python
@property
def num_waves() -> int
```

(int32):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.num_waves"></a>

#### num_waves

```python
@num_waves.setter
def num_waves(value: int) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.randomness"></a>

#### randomness

```python
@property
def randomness() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.randomness"></a>

#### randomness

```python
@randomness.setter
def randomness(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.min_wavelength"></a>

#### min_wavelength

```python
@property
def min_wavelength() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.min_wavelength"></a>

#### min_wavelength

```python
@min_wavelength.setter
def min_wavelength(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.max_wavelength"></a>

#### max_wavelength

```python
@property
def max_wavelength() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.max_wavelength"></a>

#### max_wavelength

```python
@max_wavelength.setter
def max_wavelength(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.wavelength_falloff"></a>

#### wavelength_falloff

```python
@property
def wavelength_falloff() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.wavelength_falloff"></a>

#### wavelength_falloff

```python
@wavelength_falloff.setter
def wavelength_falloff(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.min_amplitude"></a>

#### min_amplitude

```python
@property
def min_amplitude() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.min_amplitude"></a>

#### min_amplitude

```python
@min_amplitude.setter
def min_amplitude(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.max_amplitude"></a>

#### max_amplitude

```python
@property
def max_amplitude() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.max_amplitude"></a>

#### max_amplitude

```python
@max_amplitude.setter
def max_amplitude(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.amplitude_falloff"></a>

#### amplitude_falloff

```python
@property
def amplitude_falloff() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.amplitude_falloff"></a>

#### amplitude_falloff

```python
@amplitude_falloff.setter
def amplitude_falloff(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.wind_angle_deg"></a>

#### wind_angle_deg

```python
@property
def wind_angle_deg() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.wind_angle_deg"></a>

#### wind_angle_deg

```python
@wind_angle_deg.setter
def wind_angle_deg(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.direction_angular_spread_deg"></a>

#### direction_angular_spread_deg

```python
@property
def direction_angular_spread_deg() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.direction_angular_spread_deg"></a>

#### direction_angular_spread_deg

```python
@direction_angular_spread_deg.setter
def direction_angular_spread_deg(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.small_wave_steepness"></a>

#### small_wave_steepness

```python
@property
def small_wave_steepness() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.small_wave_steepness"></a>

#### small_wave_steepness

```python
@small_wave_steepness.setter
def small_wave_steepness(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.large_wave_steepness"></a>

#### large_wave_steepness

```python
@property
def large_wave_steepness() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.large_wave_steepness"></a>

#### large_wave_steepness

```python
@large_wave_steepness.setter
def large_wave_steepness(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSimple.steepness_falloff"></a>

#### steepness_falloff

```python
@property
def steepness_falloff() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaterWaveGeneratorSimple.steepness_falloff"></a>

#### steepness_falloff

```python
@steepness_falloff.setter
def steepness_falloff(value: float) -> None
```

<a id="unreal.GerstnerWaterWaveGeneratorSpectrum"></a>