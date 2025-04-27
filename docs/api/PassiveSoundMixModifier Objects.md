## PassiveSoundMixModifier Objects

```python
class PassiveSoundMixModifier(StructBase)
```

Structure containing information on a SoundMix to activate passively.

**C++ Source:**

- **Module**: Engine
- **File**: SoundClass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_volume_threshold`` (float):  [Read-Write] Maximum volume level required to activate SoundMix. Above this value the SoundMix will not be active.
- ``min_volume_threshold`` (float):  [Read-Write] Minimum volume level required to activate SoundMix. Below this value the SoundMix will not be active.
- ``sound_mix`` (SoundMix):  [Read-Write] The SoundMix to activate

<a id="unreal.PassiveSoundMixModifier.__init__"></a>

#### __init__

```python
def __init__(sound_mix: SoundMix = None,
             min_volume_threshold: float = 0.000000,
             max_volume_threshold: float = 0.000000) -> None
```

<a id="unreal.PassiveSoundMixModifier.sound_mix"></a>

#### sound_mix

```python
@property
def sound_mix() -> SoundMix
```

(SoundMix):  [Read-Only] The SoundMix to activate

<a id="unreal.PassiveSoundMixModifier.min_volume_threshold"></a>

#### min_volume_threshold

```python
@property
def min_volume_threshold() -> float
```

(float):  [Read-Only] Minimum volume level required to activate SoundMix. Below this value the SoundMix will not be active.

<a id="unreal.PassiveSoundMixModifier.volume_threshold"></a>

#### volume_threshold

```python
@property
def volume_threshold() -> float
```

deprecated: 'volume_threshold' was renamed to 'min_volume_threshold'.

<a id="unreal.PassiveSoundMixModifier.max_volume_threshold"></a>

#### max_volume_threshold

```python
@property
def max_volume_threshold() -> float
```

(float):  [Read-Only] Maximum volume level required to activate SoundMix. Above this value the SoundMix will not be active.

<a id="unreal.SoundConcurrencySettings"></a>