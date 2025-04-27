## ModularSynthLibrary Objects

```python
class ModularSynthLibrary(BlueprintFunctionLibrary)
```

Modular Synth Library

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: EpicSynth1Component.h

<a id="unreal.ModularSynthLibrary.add_modular_synth_preset_to_bank_asset"></a>

#### add_modular_synth_preset_to_bank_asset

```python
@classmethod
def add_modular_synth_preset_to_bank_asset(cls, bank: ModularSynthPresetBank,
                                           preset: ModularSynthPreset,
                                           preset_name: str) -> None
```

X.add_modular_synth_preset_to_bank_asset(bank, preset, preset_name) -> None
Adds the modular synth preset to the bank asset in the content browser. Only call during editor.

Args:
    bank (ModularSynthPresetBank): 
    preset (ModularSynthPreset): 
    preset_name (str):

<a id="unreal.ModularSynthComponent"></a>