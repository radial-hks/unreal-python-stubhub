## SourceEffectDynamicsProcessorSettings Objects

```python
class SourceEffectDynamicsProcessorSettings(StructBase)
```

Source Effect Dynamics Processor Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectDynamicsProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analog_mode`` (bool):  [Read-Write]
- ``attack_time_msec`` (float):  [Read-Write]
- ``dynamics_processor_type`` (SourceEffectDynamicsProcessorType):  [Read-Write]
- ``input_gain_db`` (float):  [Read-Write]
- ``knee_bandwidth_db`` (float):  [Read-Write]
- ``look_ahead_msec`` (float):  [Read-Write]
- ``output_gain_db`` (float):  [Read-Write]
- ``peak_mode`` (SourceEffectDynamicsPeakMode):  [Read-Write]
- ``ratio`` (float):  [Read-Write]
- ``release_time_msec`` (float):  [Read-Write]
- ``stereo_linked`` (bool):  [Read-Write]
- ``threshold_db`` (float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.__init__"></a>

#### __init__

```python
def __init__(
        dynamics_processor_type:
    SourceEffectDynamicsProcessorType = SourceEffectDynamicsProcessorType.
    COMPRESSOR,
        peak_mode: SourceEffectDynamicsPeakMode = SourceEffectDynamicsPeakMode.
    MEAN_SQUARED,
        look_ahead_msec: float = 0.000000,
        attack_time_msec: float = 0.000000,
        release_time_msec: float = 0.000000,
        threshold_db: float = 0.000000,
        ratio: float = 0.000000,
        knee_bandwidth_db: float = 0.000000,
        input_gain_db: float = 0.000000,
        output_gain_db: float = 0.000000,
        stereo_linked: bool = False,
        analog_mode: bool = False) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.dynamics_processor_type"></a>

#### dynamics_processor_type

```python
@property
def dynamics_processor_type() -> SourceEffectDynamicsProcessorType
```

(SourceEffectDynamicsProcessorType):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.dynamics_processor_type"></a>

#### dynamics_processor_type

```python
@dynamics_processor_type.setter
def dynamics_processor_type(value: SourceEffectDynamicsProcessorType) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.peak_mode"></a>

#### peak_mode

```python
@property
def peak_mode() -> SourceEffectDynamicsPeakMode
```

(SourceEffectDynamicsPeakMode):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.peak_mode"></a>

#### peak_mode

```python
@peak_mode.setter
def peak_mode(value: SourceEffectDynamicsPeakMode) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.look_ahead_msec"></a>

#### look_ahead_msec

```python
@property
def look_ahead_msec() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.look_ahead_msec"></a>

#### look_ahead_msec

```python
@look_ahead_msec.setter
def look_ahead_msec(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@property
def attack_time_msec() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@attack_time_msec.setter
def attack_time_msec(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.release_time_msec"></a>

#### release_time_msec

```python
@property
def release_time_msec() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.release_time_msec"></a>

#### release_time_msec

```python
@release_time_msec.setter
def release_time_msec(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.threshold_db"></a>

#### threshold_db

```python
@property
def threshold_db() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.threshold_db"></a>

#### threshold_db

```python
@threshold_db.setter
def threshold_db(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.knee_bandwidth_db"></a>

#### knee_bandwidth_db

```python
@property
def knee_bandwidth_db() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.knee_bandwidth_db"></a>

#### knee_bandwidth_db

```python
@knee_bandwidth_db.setter
def knee_bandwidth_db(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.input_gain_db"></a>

#### input_gain_db

```python
@property
def input_gain_db() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.input_gain_db"></a>

#### input_gain_db

```python
@input_gain_db.setter
def input_gain_db(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.output_gain_db"></a>

#### output_gain_db

```python
@property
def output_gain_db() -> float
```

(float):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.output_gain_db"></a>

#### output_gain_db

```python
@output_gain_db.setter
def output_gain_db(value: float) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.stereo_linked"></a>

#### stereo_linked

```python
@property
def stereo_linked() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.stereo_linked"></a>

#### stereo_linked

```python
@stereo_linked.setter
def stereo_linked(value: bool) -> None
```

<a id="unreal.SourceEffectDynamicsProcessorSettings.analog_mode"></a>

#### analog_mode

```python
@property
def analog_mode() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SourceEffectDynamicsProcessorSettings.analog_mode"></a>

#### analog_mode

```python
@analog_mode.setter
def analog_mode(value: bool) -> None
```

<a id="unreal.SourceEffectEnvelopeFollowerSettings"></a>