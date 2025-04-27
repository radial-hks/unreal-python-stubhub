## GerstnerWaterWaveGeneratorSpectrum Objects

```python
class GerstnerWaterWaveGeneratorSpectrum(GerstnerWaterWaveGeneratorBase)
```

Default implementation of a gerstner wave generator using known wave spectra from oceanology.
Edited using octaves, where each octave is a set of waves with 2x longer wave length than the previous octave

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: GerstnerWaterWaves.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``octaves`` (Array[GerstnerWaveOctave]):  [Read-Write]
- ``spectrum_type`` (WaveSpectrumType):  [Read-Write]

<a id="unreal.WaterWavesBase"></a>