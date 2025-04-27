## SourceEffectMidSideSpreaderSettings Objects

```python
class SourceEffectMidSideSpreaderSettings(StructBase)
```

FSourceEffectMidSideSpreaderSettings
This is the source effect's setting struct.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMidSideSpreader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``equal_power`` (bool):  [Read-Write] Indicate whether an equal power relationship between the mid and side channels should be maintained
- ``input_mode`` (StereoChannelMode):  [Read-Write] Indicate the channel mode of the input signal
- ``output_mode`` (StereoChannelMode):  [Read-Write] Indicate the channel mode of the output signal
- ``spread_amount`` (float):  [Read-Write] Amount of Mid/Side Spread. 0.0 is no spread, 1.0 is full wide.

<a id="unreal.SourceEffectMidSideSpreaderSettings.__init__"></a>

#### __init__

```python
def __init__(spread_amount: float = 0.000000,
             input_mode: StereoChannelMode = StereoChannelMode.MID_SIDE,
             output_mode: StereoChannelMode = StereoChannelMode.MID_SIDE,
             equal_power: bool = False) -> None
```

<a id="unreal.SourceEffectMidSideSpreaderSettings.spread_amount"></a>

#### spread_amount

```python
@property
def spread_amount() -> float
```

(float):  [Read-Write] Amount of Mid/Side Spread. 0.0 is no spread, 1.0 is full wide.

<a id="unreal.SourceEffectMidSideSpreaderSettings.spread_amount"></a>

#### spread_amount

```python
@spread_amount.setter
def spread_amount(value: float) -> None
```

<a id="unreal.SourceEffectMidSideSpreaderSettings.input_mode"></a>

#### input_mode

```python
@property
def input_mode() -> StereoChannelMode
```

(StereoChannelMode):  [Read-Write] Indicate the channel mode of the input signal

<a id="unreal.SourceEffectMidSideSpreaderSettings.input_mode"></a>

#### input_mode

```python
@input_mode.setter
def input_mode(value: StereoChannelMode) -> None
```

<a id="unreal.SourceEffectMidSideSpreaderSettings.output_mode"></a>

#### output_mode

```python
@property
def output_mode() -> StereoChannelMode
```

(StereoChannelMode):  [Read-Write] Indicate the channel mode of the output signal

<a id="unreal.SourceEffectMidSideSpreaderSettings.output_mode"></a>

#### output_mode

```python
@output_mode.setter
def output_mode(value: StereoChannelMode) -> None
```

<a id="unreal.SourceEffectMidSideSpreaderSettings.equal_power"></a>

#### equal_power

```python
@property
def equal_power() -> bool
```

(bool):  [Read-Write] Indicate whether an equal power relationship between the mid and side channels should be maintained

<a id="unreal.SourceEffectMidSideSpreaderSettings.equal_power"></a>

#### equal_power

```python
@equal_power.setter
def equal_power(value: bool) -> None
```

<a id="unreal.SourceEffectIndividualFilterSettings"></a>