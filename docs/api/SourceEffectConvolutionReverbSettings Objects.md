## SourceEffectConvolutionReverbSettings Objects

```python
class SourceEffectConvolutionReverbSettings(StructBase)
```

Source Effect Convolution Reverb Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectConvolutionReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bypass`` (bool):  [Read-Write] If true, input audio is directly routed to output audio with applying any effect.
- ``dry_volume_db`` (float):  [Read-Write] Controls how much of the dry signal is mixed into the output, in Decibels
- ``wet_volume_db`` (float):  [Read-Write] Controls how much of the wet signal is mixed into the output, in Decibels

<a id="unreal.SourceEffectConvolutionReverbSettings.__init__"></a>

#### __init__

```python
def __init__(wet_volume_db: float = 0.000000,
             dry_volume_db: float = 0.000000,
             bypass: bool = False) -> None
```

<a id="unreal.SourceEffectConvolutionReverbSettings.wet_volume_db"></a>

#### wet_volume_db

```python
@property
def wet_volume_db() -> float
```

(float):  [Read-Write] Controls how much of the wet signal is mixed into the output, in Decibels

<a id="unreal.SourceEffectConvolutionReverbSettings.wet_volume_db"></a>

#### wet_volume_db

```python
@wet_volume_db.setter
def wet_volume_db(value: float) -> None
```

<a id="unreal.SourceEffectConvolutionReverbSettings.dry_volume_db"></a>

#### dry_volume_db

```python
@property
def dry_volume_db() -> float
```

(float):  [Read-Write] Controls how much of the dry signal is mixed into the output, in Decibels

<a id="unreal.SourceEffectConvolutionReverbSettings.dry_volume_db"></a>

#### dry_volume_db

```python
@dry_volume_db.setter
def dry_volume_db(value: float) -> None
```

<a id="unreal.SourceEffectConvolutionReverbSettings.bypass"></a>

#### bypass

```python
@property
def bypass() -> bool
```

(bool):  [Read-Write] If true, input audio is directly routed to output audio with applying any effect.

<a id="unreal.SourceEffectConvolutionReverbSettings.bypass"></a>

#### bypass

```python
@bypass.setter
def bypass(value: bool) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings"></a>