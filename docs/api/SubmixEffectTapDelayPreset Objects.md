## SubmixEffectTapDelayPreset Objects

```python
class SubmixEffectTapDelayPreset(SoundEffectSubmixPreset)
```

UTapDelaySubmixPreset
Class which processes audio streams and uses parameters defined in the preset class.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectTapDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectTapDelaySettings):  [Read-Write]

<a id="unreal.SubmixEffectTapDelayPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectTapDelaySettings
```

(SubmixEffectTapDelaySettings):  [Read-Write]

<a id="unreal.SubmixEffectTapDelayPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectTapDelaySettings) -> None
```

<a id="unreal.SubmixEffectTapDelayPreset.set_tap"></a>

#### set_tap

```python
def set_tap(tap_id: int, tap_info: TapDelayInfo) -> None
```

x.set_tap(tap_id, tap_info) -> None
Modify a specific tap.

Args:
    tap_id (int32): 
    tap_info (TapDelayInfo):

<a id="unreal.SubmixEffectTapDelayPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectTapDelaySettings) -> None
```

x.set_settings(settings) -> None
Set all tap delay setting. This will replace any dynamically added or modified taps.

Args:
    settings (SubmixEffectTapDelaySettings):

<a id="unreal.SubmixEffectTapDelayPreset.set_interpolation_time"></a>

#### set_interpolation_time

```python
def set_interpolation_time(time: float) -> None
```

x.set_interpolation_time(time) -> None
Set the time it takes to interpolate between parameters, in milliseconds.

Args:
    time (float):

<a id="unreal.SubmixEffectTapDelayPreset.remove_tap"></a>

#### remove_tap

```python
def remove_tap(tap_id: int) -> None
```

x.remove_tap(tap_id) -> None
Remove the tap from the preset.

Args:
    tap_id (int32):

<a id="unreal.SubmixEffectTapDelayPreset.get_tap_ids"></a>

#### get_tap_ids

```python
def get_tap_ids() -> Array[int]
```

x.get_tap_ids() -> Array[int32]
Retrieve an array of all tap ids for the submix effect.

Returns:
    Array[int32]: 

    tap_ids (Array[int32]):

<a id="unreal.SubmixEffectTapDelayPreset.get_tap"></a>

#### get_tap

```python
def get_tap(tap_id: int) -> TapDelayInfo
```

x.get_tap(tap_id) -> TapDelayInfo
Get the current info about a specific tap.

Args:
    tap_id (int32): 

Returns:
    TapDelayInfo: 

    tap_info (TapDelayInfo):

<a id="unreal.SubmixEffectTapDelayPreset.get_max_delay_in_milliseconds"></a>

#### get_max_delay_in_milliseconds

```python
def get_max_delay_in_milliseconds() -> float
```

x.get_max_delay_in_milliseconds() -> float
Get the maximum delay possible.

Returns:
    float:

<a id="unreal.SubmixEffectTapDelayPreset.add_tap"></a>

#### add_tap

```python
def add_tap() -> int
```

x.add_tap() -> int32
Adds a dynamic tap delay with the given settings. Returns the tap id.

Returns:
    int32: 

    tap_id (int32):

<a id="unreal.GranularSynth"></a>