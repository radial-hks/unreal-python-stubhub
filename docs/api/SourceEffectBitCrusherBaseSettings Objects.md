## SourceEffectBitCrusherBaseSettings Objects

```python
class SourceEffectBitCrusherBaseSettings(StructBase)
```

Source Effect Bit Crusher Base Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectBitCrusher.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bit_depth`` (float):  [Read-Write] The reduced bit depth to use for the audio stream
- ``sample_rate`` (float):  [Read-Write] The reduced frequency to use for the audio stream.

<a id="unreal.SourceEffectBitCrusherBaseSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(sample_rate: float = 0.000000,
             bit_depth: float = 0.000000) -> None
```

<a id="unreal.SourceEffectBitCrusherBaseSettings.sample_rate"></a>

#### sample\_rate

```python
@property
def sample_rate() -> float
```

(float):  [Read-Write] The reduced frequency to use for the audio stream.

<a id="unreal.SourceEffectBitCrusherBaseSettings.sample_rate"></a>

#### sample\_rate

```python
@sample_rate.setter
def sample_rate(value: float) -> None
```

<a id="unreal.SourceEffectBitCrusherBaseSettings.asset_sample_rate"></a>

#### asset\_sample\_rate

```python
@property
def asset_sample_rate() -> float
```

deprecated: 'asset_sample_rate' was renamed to 'sample_rate'.

<a id="unreal.SourceEffectBitCrusherBaseSettings.asset_sample_rate"></a>

#### asset\_sample\_rate

```python
@asset_sample_rate.setter
def asset_sample_rate(value: float) -> None
```

<a id="unreal.SourceEffectBitCrusherBaseSettings.bit_depth"></a>

#### bit\_depth

```python
@property
def bit_depth() -> float
```

(float):  [Read-Write] The reduced bit depth to use for the audio stream

<a id="unreal.SourceEffectBitCrusherBaseSettings.bit_depth"></a>

#### bit\_depth

```python
@bit_depth.setter
def bit_depth(value: float) -> None
```

<a id="unreal.SourceEffectBitCrusherSettings"></a>