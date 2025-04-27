## SoundConcurrencySettings Objects

```python
class SoundConcurrencySettings(StructBase)
```

Sound Concurrency Settings

**C++ Source:**

- **Module**: Engine
- **File**: SoundConcurrency.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``limit_to_owner`` (bool):  [Read-Write] Whether or not to limit the concurrency to per sound owner (i.e. the actor that plays the sound). If the sound doesn't have an owner, it falls back to global concurrency.
- ``max_count`` (int32):  [Read-Write] The max number of allowable concurrent active voices for voices playing in this concurrency group.
- ``resolution_rule`` (MaxConcurrentResolutionRule):  [Read-Write] Which concurrency resolution policy to use if max voice count is reached.
- ``retrigger_time`` (float):  [Read-Write] Amount of time to wait (in seconds) between different sounds which play with this concurrency. Sounds rejected from this will ignore virtualization settings.
- ``voice_steal_release_time`` (float):  [Read-Write] Time taken to fade out if voice is evicted or culled due to another voice in the group starting.
- ``volume_scale`` (float):  [Read-Write] Ducking factor to apply per older voice instance (generation), which compounds based on scaling mode
  and (optionally) revives them as they stop according to the provided attack/release times.

  Note: This is not applied until after StopQuietest rules are evaluated, in order to avoid thrashing sounds.

  AppliedVolumeScale = Math.Pow(DuckingScale, VoiceGeneration)
- ``volume_scale_attack_time`` (float):  [Read-Write] Time taken to apply duck using volume scalar.
- ``volume_scale_can_release`` (bool):  [Read-Write] Whether or not volume scaling can recover volume ducking behavior when concurrency group sounds stop (default scale mode only).
- ``volume_scale_mode`` (ConcurrencyVolumeScaleMode):  [Read-Write] Volume Scale mode designating how to scale voice volume based on number of member sounds active in group.
- ``volume_scale_release_time`` (float):  [Read-Write] Time taken to recover volume scalar duck.

<a id="unreal.SoundConcurrencySettings.__init__"></a>

#### __init__

```python
def __init__(
        max_count: int = 0,
        limit_to_owner: bool = False,
        volume_scale_can_release: bool = False,
        resolution_rule:
    MaxConcurrentResolutionRule = MaxConcurrentResolutionRule.PREVENT_NEW,
        retrigger_time: float = 0.000000,
        volume_scale_mode:
    ConcurrencyVolumeScaleMode = ConcurrencyVolumeScaleMode.DEFAULT,
        volume_scale_attack_time: float = 0.000000,
        volume_scale_release_time: float = 0.000000,
        voice_steal_release_time: float = 0.000000) -> None
```

<a id="unreal.SoundConcurrencySettings.max_count"></a>

#### max_count

```python
@property
def max_count() -> int
```

(int32):  [Read-Write] The max number of allowable concurrent active voices for voices playing in this concurrency group.

<a id="unreal.SoundConcurrencySettings.max_count"></a>

#### max_count

```python
@max_count.setter
def max_count(value: int) -> None
```

<a id="unreal.SoundConcurrencySettings.limit_to_owner"></a>

#### limit_to_owner

```python
@property
def limit_to_owner() -> bool
```

(bool):  [Read-Write] Whether or not to limit the concurrency to per sound owner (i.e. the actor that plays the sound). If the sound doesn't have an owner, it falls back to global concurrency.

<a id="unreal.SoundConcurrencySettings.limit_to_owner"></a>

#### limit_to_owner

```python
@limit_to_owner.setter
def limit_to_owner(value: bool) -> None
```

<a id="unreal.SoundConcurrencySettings.volume_scale_can_release"></a>

#### volume_scale_can_release

```python
@property
def volume_scale_can_release() -> bool
```

(bool):  [Read-Write] Whether or not volume scaling can recover volume ducking behavior when concurrency group sounds stop (default scale mode only).

<a id="unreal.SoundConcurrencySettings.volume_scale_can_release"></a>

#### volume_scale_can_release

```python
@volume_scale_can_release.setter
def volume_scale_can_release(value: bool) -> None
```

<a id="unreal.SoundConcurrencySettings.resolution_rule"></a>

#### resolution_rule

```python
@property
def resolution_rule() -> MaxConcurrentResolutionRule
```

(MaxConcurrentResolutionRule):  [Read-Write] Which concurrency resolution policy to use if max voice count is reached.

<a id="unreal.SoundConcurrencySettings.resolution_rule"></a>

#### resolution_rule

```python
@resolution_rule.setter
def resolution_rule(value: MaxConcurrentResolutionRule) -> None
```

<a id="unreal.SoundConcurrencySettings.retrigger_time"></a>

#### retrigger_time

```python
@property
def retrigger_time() -> float
```

(float):  [Read-Write] Amount of time to wait (in seconds) between different sounds which play with this concurrency. Sounds rejected from this will ignore virtualization settings.

<a id="unreal.SoundConcurrencySettings.retrigger_time"></a>

#### retrigger_time

```python
@retrigger_time.setter
def retrigger_time(value: float) -> None
```

<a id="unreal.SoundConcurrencySettings.volume_scale_mode"></a>

#### volume_scale_mode

```python
@property
def volume_scale_mode() -> ConcurrencyVolumeScaleMode
```

(ConcurrencyVolumeScaleMode):  [Read-Write] Volume Scale mode designating how to scale voice volume based on number of member sounds active in group.

<a id="unreal.SoundConcurrencySettings.volume_scale_mode"></a>

#### volume_scale_mode

```python
@volume_scale_mode.setter
def volume_scale_mode(value: ConcurrencyVolumeScaleMode) -> None
```

<a id="unreal.SoundConcurrencySettings.volume_scale_attack_time"></a>

#### volume_scale_attack_time

```python
@property
def volume_scale_attack_time() -> float
```

(float):  [Read-Write] Time taken to apply duck using volume scalar.

<a id="unreal.SoundConcurrencySettings.volume_scale_attack_time"></a>

#### volume_scale_attack_time

```python
@volume_scale_attack_time.setter
def volume_scale_attack_time(value: float) -> None
```

<a id="unreal.SoundConcurrencySettings.volume_scale_release_time"></a>

#### volume_scale_release_time

```python
@property
def volume_scale_release_time() -> float
```

(float):  [Read-Write] Time taken to recover volume scalar duck.

<a id="unreal.SoundConcurrencySettings.volume_scale_release_time"></a>

#### volume_scale_release_time

```python
@volume_scale_release_time.setter
def volume_scale_release_time(value: float) -> None
```

<a id="unreal.SoundConcurrencySettings.voice_steal_release_time"></a>

#### voice_steal_release_time

```python
@property
def voice_steal_release_time() -> float
```

(float):  [Read-Write] Time taken to fade out if voice is evicted or culled due to another voice in the group starting.

<a id="unreal.SoundConcurrencySettings.voice_steal_release_time"></a>

#### voice_steal_release_time

```python
@voice_steal_release_time.setter
def voice_steal_release_time(value: float) -> None
```

<a id="unreal.SoundClassAdjuster"></a>