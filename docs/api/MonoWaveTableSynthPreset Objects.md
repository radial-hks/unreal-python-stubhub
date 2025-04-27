## MonoWaveTableSynthPreset Objects

```python
class MonoWaveTableSynthPreset(Object)
```

UStruct Mono Wave Table Synth Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SynthComponentMonoWaveTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lock_keyframes_to_grid`` (int32):  [Read-Write] How many evenly-spaced keyframes to use when LockKeyframesToGrid is true
- ``lock_keyframes_to_grid_bool`` (bool):  [Read-Write] Lock wavetables to evenly spaced keyframes that can be edited vertically only (will re-sample)
- ``normalize_wave_tables`` (bool):  [Read-Write] Normalize the WaveTable data? False will allow clipping, True will normalize the tables when sent to the synth for rendering
- ``preset_name`` (str):  [Read-Write] Name the preset
- ``wave_table`` (Array[RuntimeFloatCurve]):  [Read-Write] Wave Table Editor
- ``wave_table_resolution`` (int32):  [Read-Write] How many samples will be taken of the curve from time = [0.0, 1.0]

<a id="unreal.MonoWaveTableSynthPreset.preset_name"></a>

#### preset_name

```python
@property
def preset_name() -> str
```

(str):  [Read-Write] Name the preset

<a id="unreal.MonoWaveTableSynthPreset.preset_name"></a>

#### preset_name

```python
@preset_name.setter
def preset_name(value: str) -> None
```

<a id="unreal.MonoWaveTableSynthPreset.lock_keyframes_to_grid_bool"></a>

#### lock_keyframes_to_grid_bool

```python
@property
def lock_keyframes_to_grid_bool() -> bool
```

(bool):  [Read-Only] Lock wavetables to evenly spaced keyframes that can be edited vertically only (will re-sample)

<a id="unreal.MonoWaveTableSynthPreset.lock_keyframes_to_grid"></a>

#### lock_keyframes_to_grid

```python
@property
def lock_keyframes_to_grid() -> int
```

(int32):  [Read-Only] How many evenly-spaced keyframes to use when LockKeyframesToGrid is true

<a id="unreal.MonoWaveTableSynthPreset.wave_table_resolution"></a>

#### wave_table_resolution

```python
@property
def wave_table_resolution() -> int
```

(int32):  [Read-Only] How many samples will be taken of the curve from time = [0.0, 1.0]

<a id="unreal.MonoWaveTableSynthPreset.wave_table"></a>

#### wave_table

```python
@property
def wave_table() -> Array[RuntimeFloatCurve]
```

(Array[RuntimeFloatCurve]):  [Read-Only] Wave Table Editor

<a id="unreal.MonoWaveTableSynthPreset.normalize_wave_tables"></a>

#### normalize_wave_tables

```python
@property
def normalize_wave_tables() -> bool
```

(bool):  [Read-Write] Normalize the WaveTable data? False will allow clipping, True will normalize the tables when sent to the synth for rendering

<a id="unreal.MonoWaveTableSynthPreset.normalize_wave_tables"></a>

#### normalize_wave_tables

```python
@normalize_wave_tables.setter
def normalize_wave_tables(value: bool) -> None
```

<a id="unreal.SynthComponentMonoWaveTable"></a>