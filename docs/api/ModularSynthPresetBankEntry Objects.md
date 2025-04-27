## ModularSynthPresetBankEntry Objects

```python
class ModularSynthPresetBankEntry(StructBase)
```

Modular Synth Preset Bank Entry

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: EpicSynth1Component.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``preset`` (ModularSynthPreset):  [Read-Write]
- ``preset_name`` (str):  [Read-Write]

<a id="unreal.ModularSynthPresetBankEntry.__init__"></a>

#### __init__

```python
def __init__(
    preset_name: str = "",
    preset: ModularSynthPreset = [
        False, Synth1OscType.SAW, 1.000000, 0.000000, 0.000000, 0.000000,
        0.500000, Synth1OscType.SAW, 1.000000, 0.000000, 0.000000, 2.500000,
        0.500000, 0.000000, False, False, 0.500000, 0.000000, 1.000000,
        0.000000, SynthLFOType.SINE, SynthLFOMode.SYNC,
        SynthLFOPatchType.PATCH_TO_NONE, 1.000000, 0.000000, SynthLFOType.SINE,
        SynthLFOMode.SYNC, SynthLFOPatchType.PATCH_TO_NONE, -3.000000,
        10.000000, 100.000000, 0.707000, 5000.000000,
        SynthModEnvPatch.PATCH_TO_NONE, SynthModEnvBiasPatch.PATCH_TO_NONE,
        False, False, 1.000000, 10.000000, 100.000000, 0.707000, 5000.000000,
        True, False, 8000.000000, 2.000000, SynthFilterType.LOW_PASS,
        SynthFilterAlgorithm.LADDER, True, SynthStereoDelayMode.PING_PONG,
        700.000000, 0.700000, 0.300000, 0.200000, False, 0.200000, 0.500000,
        2.000000, []
    ]
) -> None
```

<a id="unreal.ModularSynthPresetBankEntry.preset_name"></a>

#### preset_name

```python
@property
def preset_name() -> str
```

(str):  [Read-Write]

<a id="unreal.ModularSynthPresetBankEntry.preset_name"></a>

#### preset_name

```python
@preset_name.setter
def preset_name(value: str) -> None
```

<a id="unreal.ModularSynthPresetBankEntry.preset"></a>

#### preset

```python
@property
def preset() -> ModularSynthPreset
```

(ModularSynthPreset):  [Read-Write]

<a id="unreal.ModularSynthPresetBankEntry.preset"></a>

#### preset

```python
@preset.setter
def preset(value: ModularSynthPreset) -> None
```

<a id="unreal.SourceEffectBitCrusherBaseSettings"></a>