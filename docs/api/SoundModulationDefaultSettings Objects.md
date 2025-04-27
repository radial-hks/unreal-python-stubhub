## SoundModulationDefaultSettings Objects

```python
class SoundModulationDefaultSettings(StructBase)
```

Default parameter destination settings for source audio object.

**C++ Source:**

- **Module**: Engine
- **File**: SoundModulationDestination.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``highpass_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Highpass modulation
- ``lowpass_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Lowpass modulation
- ``pitch_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Pitch modulation
- ``volume_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Volume modulation

<a id="unreal.SoundModulationDefaultSettings.__init__"></a>

#### __init__

```python
def __init__(
    volume_modulation_destination: SoundModulationDestinationSettings = [
        1.000000, []
    ],
    pitch_modulation_destination: SoundModulationDestinationSettings = [
        1.000000, []
    ],
    highpass_modulation_destination: SoundModulationDestinationSettings = [
        1.000000, []
    ],
    lowpass_modulation_destination: SoundModulationDestinationSettings = [
        1.000000, []
    ]
) -> None
```

<a id="unreal.SoundModulationDefaultSettings.volume_modulation_destination"></a>

#### volume_modulation_destination

```python
@property
def volume_modulation_destination() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] Volume modulation

<a id="unreal.SoundModulationDefaultSettings.volume_modulation_destination"></a>

#### volume_modulation_destination

```python
@volume_modulation_destination.setter
def volume_modulation_destination(
        value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundModulationDefaultSettings.pitch_modulation_destination"></a>

#### pitch_modulation_destination

```python
@property
def pitch_modulation_destination() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] Pitch modulation

<a id="unreal.SoundModulationDefaultSettings.pitch_modulation_destination"></a>

#### pitch_modulation_destination

```python
@pitch_modulation_destination.setter
def pitch_modulation_destination(
        value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundModulationDefaultSettings.highpass_modulation_destination"></a>

#### highpass_modulation_destination

```python
@property
def highpass_modulation_destination() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] Highpass modulation

<a id="unreal.SoundModulationDefaultSettings.highpass_modulation_destination"></a>

#### highpass_modulation_destination

```python
@highpass_modulation_destination.setter
def highpass_modulation_destination(
        value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundModulationDefaultSettings.lowpass_modulation_destination"></a>

#### lowpass_modulation_destination

```python
@property
def lowpass_modulation_destination() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] Lowpass modulation

<a id="unreal.SoundModulationDefaultSettings.lowpass_modulation_destination"></a>

#### lowpass_modulation_destination

```python
@lowpass_modulation_destination.setter
def lowpass_modulation_destination(
        value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundModulationDestinationSettings"></a>