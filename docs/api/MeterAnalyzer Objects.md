## MeterAnalyzer Objects

```python
class MeterAnalyzer(AudioAnalyzer)
```

UMeterAnalyzer

UMeterAnalyzer calculates the current amplitude of an
audio bus in real-time.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Meter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_latest_overall_meter_results`` (OnLatestOverallMeterResults):  [Read-Write] Delegate to receive the latest overall meter results.
- ``on_latest_per_channel_meter_results`` (OnLatestPerChannelMeterResults):  [Read-Write] Delegate to receive the latest per-channel meter results.
- ``on_overall_meter_results`` (OnOverallMeterResults):  [Read-Write] Delegate to receive all overall meter results since last delegate call.
- ``on_per_channel_meter_results`` (OnPerChannelMeterResults):  [Read-Write] Delegate to receive all meter results, per-channel, since last delegate call.
- ``settings`` (MeterSettings):  [Read-Write] The settings for the meter audio analyzer.

<a id="unreal.MeterAnalyzer.settings"></a>

#### settings

```python
@property
def settings() -> MeterSettings
```

(MeterSettings):  [Read-Write] The settings for the meter audio analyzer.

<a id="unreal.MeterAnalyzer.settings"></a>

#### settings

```python
@settings.setter
def settings(value: MeterSettings) -> None
```

<a id="unreal.MeterAnalyzer.on_overall_meter_results"></a>

#### on_overall_meter_results

```python
@property
def on_overall_meter_results() -> OnOverallMeterResults
```

(OnOverallMeterResults):  [Read-Write] Delegate to receive all overall meter results since last delegate call.

<a id="unreal.MeterAnalyzer.on_overall_meter_results"></a>

#### on_overall_meter_results

```python
@on_overall_meter_results.setter
def on_overall_meter_results(value: OnOverallMeterResults) -> None
```

<a id="unreal.MeterAnalyzer.on_per_channel_meter_results"></a>

#### on_per_channel_meter_results

```python
@property
def on_per_channel_meter_results() -> OnPerChannelMeterResults
```

(OnPerChannelMeterResults):  [Read-Write] Delegate to receive all meter results, per-channel, since last delegate call.

<a id="unreal.MeterAnalyzer.on_per_channel_meter_results"></a>

#### on_per_channel_meter_results

```python
@on_per_channel_meter_results.setter
def on_per_channel_meter_results(value: OnPerChannelMeterResults) -> None
```

<a id="unreal.MeterAnalyzer.on_latest_overall_meter_results"></a>

#### on_latest_overall_meter_results

```python
@property
def on_latest_overall_meter_results() -> OnLatestOverallMeterResults
```

(OnLatestOverallMeterResults):  [Read-Write] Delegate to receive the latest overall meter results.

<a id="unreal.MeterAnalyzer.on_latest_overall_meter_results"></a>

#### on_latest_overall_meter_results

```python
@on_latest_overall_meter_results.setter
def on_latest_overall_meter_results(
        value: OnLatestOverallMeterResults) -> None
```

<a id="unreal.MeterAnalyzer.on_latest_per_channel_meter_results"></a>

#### on_latest_per_channel_meter_results

```python
@property
def on_latest_per_channel_meter_results() -> OnLatestPerChannelMeterResults
```

(OnLatestPerChannelMeterResults):  [Read-Write] Delegate to receive the latest per-channel meter results.

<a id="unreal.MeterAnalyzer.on_latest_per_channel_meter_results"></a>

#### on_latest_per_channel_meter_results

```python
@on_latest_per_channel_meter_results.setter
def on_latest_per_channel_meter_results(
        value: OnLatestPerChannelMeterResults) -> None
```

<a id="unreal.OnsetNRTSettings"></a>