## SourceEffectStereoDelaySettings Objects

```python
class SourceEffectStereoDelaySettings(StructBase)
```

Source Effect Stereo Delay Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectStereoDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delay_mode`` (StereoDelaySourceEffect):  [Read-Write] What mode to set the stereo delay effect.
- ``delay_ratio`` (float):  [Read-Write] Delay spread for left and right channels. Allows left and right channels to have differential delay amounts. Useful for stereo channel decorrelation.
- ``delay_time_msec`` (float):  [Read-Write] The base amount of delay in the left and right channels of the delay line.
- ``dry_level`` (float):  [Read-Write] The dry level of the effect
- ``feedback`` (float):  [Read-Write] The amount of audio to feedback into the delay line once the delay has been tapped.
- ``filter_enabled`` (bool):  [Read-Write] Whether or not to enable filtering
- ``filter_frequency`` (float):  [Read-Write] Cutoff frequency of the filter
- ``filter_q`` (float):  [Read-Write] Q of the filter
- ``filter_type`` (StereoDelayFiltertype):  [Read-Write] Filter type to feed feedback audio to
- ``wet_level`` (float):  [Read-Write] The amount of delay effect to mix with the dry input signal into the effect.

<a id="unreal.SourceEffectStereoDelaySettings.__init__"></a>

#### __init__

```python
def __init__(
        delay_mode: StereoDelaySourceEffect = StereoDelaySourceEffect.NORMAL,
        delay_time_msec: float = 0.000000,
        feedback: float = 0.000000,
        delay_ratio: float = 0.000000,
        wet_level: float = 0.000000,
        dry_level: float = 0.000000,
        filter_enabled: bool = False,
        filter_type: StereoDelayFiltertype = StereoDelayFiltertype.LOWPASS,
        filter_frequency: float = 0.000000,
        filter_q: float = 0.000000) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.delay_mode"></a>

#### delay_mode

```python
@property
def delay_mode() -> StereoDelaySourceEffect
```

(StereoDelaySourceEffect):  [Read-Write] What mode to set the stereo delay effect.

<a id="unreal.SourceEffectStereoDelaySettings.delay_mode"></a>

#### delay_mode

```python
@delay_mode.setter
def delay_mode(value: StereoDelaySourceEffect) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.delay_time_msec"></a>

#### delay_time_msec

```python
@property
def delay_time_msec() -> float
```

(float):  [Read-Write] The base amount of delay in the left and right channels of the delay line.

<a id="unreal.SourceEffectStereoDelaySettings.delay_time_msec"></a>

#### delay_time_msec

```python
@delay_time_msec.setter
def delay_time_msec(value: float) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.feedback"></a>

#### feedback

```python
@property
def feedback() -> float
```

(float):  [Read-Write] The amount of audio to feedback into the delay line once the delay has been tapped.

<a id="unreal.SourceEffectStereoDelaySettings.feedback"></a>

#### feedback

```python
@feedback.setter
def feedback(value: float) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.delay_ratio"></a>

#### delay_ratio

```python
@property
def delay_ratio() -> float
```

(float):  [Read-Write] Delay spread for left and right channels. Allows left and right channels to have differential delay amounts. Useful for stereo channel decorrelation.

<a id="unreal.SourceEffectStereoDelaySettings.delay_ratio"></a>

#### delay_ratio

```python
@delay_ratio.setter
def delay_ratio(value: float) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.wet_level"></a>

#### wet_level

```python
@property
def wet_level() -> float
```

(float):  [Read-Write] The amount of delay effect to mix with the dry input signal into the effect.

<a id="unreal.SourceEffectStereoDelaySettings.wet_level"></a>

#### wet_level

```python
@wet_level.setter
def wet_level(value: float) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.dry_level"></a>

#### dry_level

```python
@property
def dry_level() -> float
```

(float):  [Read-Write] The dry level of the effect

<a id="unreal.SourceEffectStereoDelaySettings.dry_level"></a>

#### dry_level

```python
@dry_level.setter
def dry_level(value: float) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.filter_enabled"></a>

#### filter_enabled

```python
@property
def filter_enabled() -> bool
```

(bool):  [Read-Write] Whether or not to enable filtering

<a id="unreal.SourceEffectStereoDelaySettings.filter_enabled"></a>

#### filter_enabled

```python
@filter_enabled.setter
def filter_enabled(value: bool) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.filter_type"></a>

#### filter_type

```python
@property
def filter_type() -> StereoDelayFiltertype
```

(StereoDelayFiltertype):  [Read-Write] Filter type to feed feedback audio to

<a id="unreal.SourceEffectStereoDelaySettings.filter_type"></a>

#### filter_type

```python
@filter_type.setter
def filter_type(value: StereoDelayFiltertype) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.filter_frequency"></a>

#### filter_frequency

```python
@property
def filter_frequency() -> float
```

(float):  [Read-Write] Cutoff frequency of the filter

<a id="unreal.SourceEffectStereoDelaySettings.filter_frequency"></a>

#### filter_frequency

```python
@filter_frequency.setter
def filter_frequency(value: float) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings.filter_q"></a>

#### filter_q

```python
@property
def filter_q() -> float
```

(float):  [Read-Write] Q of the filter

<a id="unreal.SourceEffectStereoDelaySettings.filter_q"></a>

#### filter_q

```python
@filter_q.setter
def filter_q(value: float) -> None
```

<a id="unreal.SourceEffectWaveShaperSettings"></a>