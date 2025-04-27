## GerstnerWaterWaves Objects

```python
class GerstnerWaterWaves(WaterWaves)
```

Waves implementation based off Gerstner waves.
They provide a decent look, are relatively cheap to evaluate and have the advantage of being only dependent on the time variable, which makes them perfect for online simulations.

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: GerstnerWaterWaves.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gerstner_wave_generator`` (GerstnerWaterWaveGeneratorBase):  [Read-Write]
- ``gerstner_waves`` (Array[GerstnerWave]):  [Read-Write]
- ``max_wave_height`` (float):  [Read-Write]

<a id="unreal.GerstnerWaterWaves.gerstner_wave_generator"></a>

#### gerstner_wave_generator

```python
@property
def gerstner_wave_generator() -> GerstnerWaterWaveGeneratorBase
```

(GerstnerWaterWaveGeneratorBase):  [Read-Only]

<a id="unreal.GerstnerWaterWaves.gerstner_waves"></a>

#### gerstner_waves

```python
@property
def gerstner_waves() -> Array[GerstnerWave]
```

(Array[GerstnerWave]):  [Read-Only]

<a id="unreal.GerstnerWaterWaves.max_wave_height"></a>

#### max_wave_height

```python
@property
def max_wave_height() -> float
```

(float):  [Read-Only]

<a id="unreal.LakeCollisionComponent"></a>