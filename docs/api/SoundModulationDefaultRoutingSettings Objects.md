## SoundModulationDefaultRoutingSettings Objects

```python
class SoundModulationDefaultRoutingSettings(SoundModulationDefaultSettings)
```

Default parameter destination settings for source audio object.

**C++ Source:**

- **Module**: Engine
- **File**: SoundModulationDestination.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``highpass_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Highpass modulation
- ``highpass_routing`` (ModulationRouting):  [Read-Write] What high-pass modulation settings to use
- ``lowpass_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Lowpass modulation
- ``lowpass_routing`` (ModulationRouting):  [Read-Write] What low-pass modulation settings to use
- ``pitch_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Pitch modulation
- ``pitch_routing`` (ModulationRouting):  [Read-Write] What pitch modulation settings to use
- ``volume_modulation_destination`` (SoundModulationDestinationSettings):  [Read-Write] Volume modulation
- ``volume_routing`` (ModulationRouting):  [Read-Write] What volume modulation settings to use

<a id="unreal.SoundModulationDefaultRoutingSettings.__init__"></a>

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
        ],
        volume_routing: ModulationRouting = ModulationRouting.DISABLE,
        pitch_routing: ModulationRouting = ModulationRouting.DISABLE,
        highpass_routing: ModulationRouting = ModulationRouting.DISABLE,
        lowpass_routing: ModulationRouting = ModulationRouting.DISABLE
) -> None
```

<a id="unreal.SoundModulationDefaultRoutingSettings.volume_routing"></a>

#### volume_routing

```python
@property
def volume_routing() -> ModulationRouting
```

(ModulationRouting):  [Read-Write] What volume modulation settings to use

<a id="unreal.SoundModulationDefaultRoutingSettings.volume_routing"></a>

#### volume_routing

```python
@volume_routing.setter
def volume_routing(value: ModulationRouting) -> None
```

<a id="unreal.SoundModulationDefaultRoutingSettings.pitch_routing"></a>

#### pitch_routing

```python
@property
def pitch_routing() -> ModulationRouting
```

(ModulationRouting):  [Read-Write] What pitch modulation settings to use

<a id="unreal.SoundModulationDefaultRoutingSettings.pitch_routing"></a>

#### pitch_routing

```python
@pitch_routing.setter
def pitch_routing(value: ModulationRouting) -> None
```

<a id="unreal.SoundModulationDefaultRoutingSettings.highpass_routing"></a>

#### highpass_routing

```python
@property
def highpass_routing() -> ModulationRouting
```

(ModulationRouting):  [Read-Write] What high-pass modulation settings to use

<a id="unreal.SoundModulationDefaultRoutingSettings.highpass_routing"></a>

#### highpass_routing

```python
@highpass_routing.setter
def highpass_routing(value: ModulationRouting) -> None
```

<a id="unreal.SoundModulationDefaultRoutingSettings.lowpass_routing"></a>

#### lowpass_routing

```python
@property
def lowpass_routing() -> ModulationRouting
```

(ModulationRouting):  [Read-Write] What low-pass modulation settings to use

<a id="unreal.SoundModulationDefaultRoutingSettings.lowpass_routing"></a>

#### lowpass_routing

```python
@lowpass_routing.setter
def lowpass_routing(value: ModulationRouting) -> None
```

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings"></a>