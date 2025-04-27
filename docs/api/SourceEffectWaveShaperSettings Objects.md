## SourceEffectWaveShaperSettings Objects

```python
class SourceEffectWaveShaperSettings(StructBase)
```

Source Effect Wave Shaper Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectWaveShaper.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amount`` (float):  [Read-Write] The amount of wave shaping. 0.0 = no wave shaping.
- ``output_gain_db`` (float):  [Read-Write] The amount of wave shaping. 0.0 = no wave shaping.

<a id="unreal.SourceEffectWaveShaperSettings.__init__"></a>

#### __init__

```python
def __init__(amount: float = 0.000000,
             output_gain_db: float = 0.000000) -> None
```

<a id="unreal.SourceEffectWaveShaperSettings.amount"></a>

#### amount

```python
@property
def amount() -> float
```

(float):  [Read-Write] The amount of wave shaping. 0.0 = no wave shaping.

<a id="unreal.SourceEffectWaveShaperSettings.amount"></a>

#### amount

```python
@amount.setter
def amount(value: float) -> None
```

<a id="unreal.SourceEffectWaveShaperSettings.output_gain_db"></a>

#### output_gain_db

```python
@property
def output_gain_db() -> float
```

(float):  [Read-Write] The amount of wave shaping. 0.0 = no wave shaping.

<a id="unreal.SourceEffectWaveShaperSettings.output_gain_db"></a>

#### output_gain_db

```python
@output_gain_db.setter
def output_gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings"></a>