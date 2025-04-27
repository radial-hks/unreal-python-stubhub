## DynamicsBandSettings Objects

```python
class DynamicsBandSettings(StructBase)
```

Dynamics Band Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectMultiBandCompressor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attack_time_msec`` (float):  [Read-Write] The amount of time to ramp into any dynamics processing effect in milliseconds.
- ``crossover_top_frequency`` (float):  [Read-Write] Frequency of the crossover between this band and the next. The last band will have this property ignored
- ``input_gain_db`` (float):  [Read-Write] The input gain of the dynamics processor in dB
- ``knee_bandwidth_db`` (float):  [Read-Write] The knee bandwidth of the compressor to use in dB
- ``output_gain_db`` (float):  [Read-Write] The output gain of the dynamics processor in dB
- ``ratio`` (float):  [Read-Write] The dynamics processor ratio -- has different meaning depending on the processor type.
- ``release_time_msec`` (float):  [Read-Write] The amount of time to release the dynamics processing effect in milliseconds
- ``threshold_db`` (float):  [Read-Write] The threshold at which to perform a dynamics processing operation

<a id="unreal.DynamicsBandSettings.__init__"></a>

#### __init__

```python
def __init__(crossover_top_frequency: float = 0.000000,
             attack_time_msec: float = 0.000000,
             release_time_msec: float = 0.000000,
             threshold_db: float = 0.000000,
             ratio: float = 0.000000,
             knee_bandwidth_db: float = 0.000000,
             input_gain_db: float = 0.000000,
             output_gain_db: float = 0.000000) -> None
```

<a id="unreal.DynamicsBandSettings.crossover_top_frequency"></a>

#### crossover_top_frequency

```python
@property
def crossover_top_frequency() -> float
```

(float):  [Read-Write] Frequency of the crossover between this band and the next. The last band will have this property ignored

<a id="unreal.DynamicsBandSettings.crossover_top_frequency"></a>

#### crossover_top_frequency

```python
@crossover_top_frequency.setter
def crossover_top_frequency(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@property
def attack_time_msec() -> float
```

(float):  [Read-Write] The amount of time to ramp into any dynamics processing effect in milliseconds.

<a id="unreal.DynamicsBandSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@attack_time_msec.setter
def attack_time_msec(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.release_time_msec"></a>

#### release_time_msec

```python
@property
def release_time_msec() -> float
```

(float):  [Read-Write] The amount of time to release the dynamics processing effect in milliseconds

<a id="unreal.DynamicsBandSettings.release_time_msec"></a>

#### release_time_msec

```python
@release_time_msec.setter
def release_time_msec(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.threshold_db"></a>

#### threshold_db

```python
@property
def threshold_db() -> float
```

(float):  [Read-Write] The threshold at which to perform a dynamics processing operation

<a id="unreal.DynamicsBandSettings.threshold_db"></a>

#### threshold_db

```python
@threshold_db.setter
def threshold_db(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write] The dynamics processor ratio -- has different meaning depending on the processor type.

<a id="unreal.DynamicsBandSettings.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.knee_bandwidth_db"></a>

#### knee_bandwidth_db

```python
@property
def knee_bandwidth_db() -> float
```

(float):  [Read-Write] The knee bandwidth of the compressor to use in dB

<a id="unreal.DynamicsBandSettings.knee_bandwidth_db"></a>

#### knee_bandwidth_db

```python
@knee_bandwidth_db.setter
def knee_bandwidth_db(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.input_gain_db"></a>

#### input_gain_db

```python
@property
def input_gain_db() -> float
```

(float):  [Read-Write] The input gain of the dynamics processor in dB

<a id="unreal.DynamicsBandSettings.input_gain_db"></a>

#### input_gain_db

```python
@input_gain_db.setter
def input_gain_db(value: float) -> None
```

<a id="unreal.DynamicsBandSettings.output_gain_db"></a>

#### output_gain_db

```python
@property
def output_gain_db() -> float
```

(float):  [Read-Write] The output gain of the dynamics processor in dB

<a id="unreal.DynamicsBandSettings.output_gain_db"></a>

#### output_gain_db

```python
@output_gain_db.setter
def output_gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings"></a>