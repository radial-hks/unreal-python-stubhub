## OnsetNRTSettings Objects

```python
class OnsetNRTSettings(AudioSynesthesiaNRTSettings)
```

UOnsetNRTSettings

Settings for a UOnsetNRT analyzer.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: OnsetNRT.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``downmix_to_mono`` (bool):  [Read-Write] If true, multichannel audio is downmixed to mono with equal amplitude scaling. If false, each channel gets it's own onset result.
- ``granularity_in_seconds`` (float):  [Read-Write] Onset timestamp granularity onsets. Lower granularity takes longer to compute.
- ``maximum_frequency`` (float):  [Read-Write] Starting frequency for onset anlaysis.
- ``minimum_frequency`` (float):  [Read-Write] Starting frequency for onset anlaysis.
- ``sensitivity`` (float):  [Read-Write] Sensitivity of onset detector. Higher sensitivity will find more onsets.

<a id="unreal.OnsetNRTSettings.downmix_to_mono"></a>

#### downmix_to_mono

```python
@property
def downmix_to_mono() -> bool
```

(bool):  [Read-Only] If true, multichannel audio is downmixed to mono with equal amplitude scaling. If false, each channel gets it's own onset result.

<a id="unreal.OnsetNRTSettings.granularity_in_seconds"></a>

#### granularity_in_seconds

```python
@property
def granularity_in_seconds() -> float
```

(float):  [Read-Only] Onset timestamp granularity onsets. Lower granularity takes longer to compute.

<a id="unreal.OnsetNRTSettings.sensitivity"></a>

#### sensitivity

```python
@property
def sensitivity() -> float
```

(float):  [Read-Only] Sensitivity of onset detector. Higher sensitivity will find more onsets.

<a id="unreal.OnsetNRTSettings.minimum_frequency"></a>

#### minimum_frequency

```python
@property
def minimum_frequency() -> float
```

(float):  [Read-Only] Starting frequency for onset anlaysis.

<a id="unreal.OnsetNRTSettings.maximum_frequency"></a>

#### maximum_frequency

```python
@property
def maximum_frequency() -> float
```

(float):  [Read-Only] Starting frequency for onset anlaysis.

<a id="unreal.OnsetNRT"></a>