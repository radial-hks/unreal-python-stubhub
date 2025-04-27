## GerstnerWaterWaveGeneratorBase Objects

```python
class GerstnerWaterWaveGeneratorBase(Object)
```

Base class for the gerstner water wave generation. This can be overridden by either C++ classes or Blueprint classes.
Simply implement GenerateGerstnerWaves (or GenerateGerstnerWaves_Implementation in C++) to return the set of waves to be used. Waves will automatically be sorted based on wave length.

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: GerstnerWaterWaves.h

<a id="unreal.GerstnerWaterWaveGeneratorBase.generate_gerstner_waves"></a>

#### generate_gerstner_waves

```python
def generate_gerstner_waves() -> Array[GerstnerWave]
```

x.generate_gerstner_waves() -> Array[GerstnerWave]
Generate Gerstner Waves

Returns:
    Array[GerstnerWave]: 

    out_waves (Array[GerstnerWave]):

<a id="unreal.GerstnerWaterWaveGeneratorSimple"></a>