## MeterSettings Objects

```python
class MeterSettings(AudioSynesthesiaSettings)
```

UMeterSettings

Settings for a UMeterAnalyzer.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Meter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analysis_period`` (float):  [Read-Write] Number of seconds between meter measurements
- ``clipping_threshold`` (float):  [Read-Write] What volume threshold to throw clipping detection notifications.
- ``meter_attack_time`` (int32):  [Read-Write] Meter attack time, in milliseconds
- ``meter_release_time`` (int32):  [Read-Write] Meter release time, in milliseconds.
- ``peak_hold_time`` (int32):  [Read-Write] Peak hold time, in milliseconds
- ``peak_mode`` (MeterPeakType):  [Read-Write] Meter envelope type type

<a id="unreal.MeterSettings.analysis_period"></a>

#### analysis_period

```python
@property
def analysis_period() -> float
```

(float):  [Read-Only] Number of seconds between meter measurements

<a id="unreal.MeterSettings.peak_mode"></a>

#### peak_mode

```python
@property
def peak_mode() -> MeterPeakType
```

(MeterPeakType):  [Read-Only] Meter envelope type type

<a id="unreal.MeterSettings.meter_attack_time"></a>

#### meter_attack_time

```python
@property
def meter_attack_time() -> int
```

(int32):  [Read-Only] Meter attack time, in milliseconds

<a id="unreal.MeterSettings.meter_release_time"></a>

#### meter_release_time

```python
@property
def meter_release_time() -> int
```

(int32):  [Read-Only] Meter release time, in milliseconds.

<a id="unreal.MeterSettings.peak_hold_time"></a>

#### peak_hold_time

```python
@property
def peak_hold_time() -> int
```

(int32):  [Read-Only] Peak hold time, in milliseconds

<a id="unreal.MeterSettings.clipping_threshold"></a>

#### clipping_threshold

```python
@property
def clipping_threshold() -> float
```

(float):  [Read-Only] What volume threshold to throw clipping detection notifications.

<a id="unreal.MeterAnalyzer"></a>