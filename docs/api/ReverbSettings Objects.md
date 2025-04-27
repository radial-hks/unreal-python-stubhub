## ReverbSettings Objects

```python
class ReverbSettings(StructBase)
```

Struct encapsulating settings for reverb effects.

**C++ Source:**

- **Module**: Engine
- **File**: ReverbSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_reverb`` (bool):  [Read-Write] Whether to apply the reverb settings below.
- ``fade_time`` (float):  [Read-Write] Time to fade from the current reverb settings into this setting, in seconds.
- ``reverb_effect`` (ReverbEffect):  [Read-Write] The reverb asset to employ.
- ``reverb_plugin_effect`` (SoundEffectSubmixPreset):  [Read-Write] This is used to apply plugin-specific settings when a Reverb Plugin is being used.
- ``volume`` (float):  [Read-Write] Volume level of the reverb effect.

<a id="unreal.ReverbSettings.__init__"></a>

#### __init__

```python
def __init__(apply_reverb: bool = False,
             reverb_effect: ReverbEffect = None,
             reverb_plugin_effect: SoundEffectSubmixPreset = None,
             volume: float = 0.000000,
             fade_time: float = 0.000000) -> None
```

<a id="unreal.ReverbSettings.apply_reverb"></a>

#### apply_reverb

```python
@property
def apply_reverb() -> bool
```

(bool):  [Read-Write] Whether to apply the reverb settings below.

<a id="unreal.ReverbSettings.apply_reverb"></a>

#### apply_reverb

```python
@apply_reverb.setter
def apply_reverb(value: bool) -> None
```

<a id="unreal.ReverbSettings.reverb_effect"></a>

#### reverb_effect

```python
@property
def reverb_effect() -> ReverbEffect
```

(ReverbEffect):  [Read-Write] The reverb asset to employ.

<a id="unreal.ReverbSettings.reverb_effect"></a>

#### reverb_effect

```python
@reverb_effect.setter
def reverb_effect(value: ReverbEffect) -> None
```

<a id="unreal.ReverbSettings.reverb_plugin_effect"></a>

#### reverb_plugin_effect

```python
@property
def reverb_plugin_effect() -> SoundEffectSubmixPreset
```

(SoundEffectSubmixPreset):  [Read-Write] This is used to apply plugin-specific settings when a Reverb Plugin is being used.

<a id="unreal.ReverbSettings.reverb_plugin_effect"></a>

#### reverb_plugin_effect

```python
@reverb_plugin_effect.setter
def reverb_plugin_effect(value: SoundEffectSubmixPreset) -> None
```

<a id="unreal.ReverbSettings.volume"></a>

#### volume

```python
@property
def volume() -> float
```

(float):  [Read-Write] Volume level of the reverb effect.

<a id="unreal.ReverbSettings.volume"></a>

#### volume

```python
@volume.setter
def volume(value: float) -> None
```

<a id="unreal.ReverbSettings.fade_time"></a>

#### fade_time

```python
@property
def fade_time() -> float
```

(float):  [Read-Write] Time to fade from the current reverb settings into this setting, in seconds.

<a id="unreal.ReverbSettings.fade_time"></a>

#### fade_time

```python
@fade_time.setter
def fade_time(value: float) -> None
```

<a id="unreal.ColorGradePerRangeSettings"></a>