## ResonanceAudioBlueprintFunctionLibrary Objects

```python
class ResonanceAudioBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Resonance Audio Blueprint Function Library

**C++ Source:**

- **Plugin**: ResonanceAudio
- **Module**: ResonanceAudio
- **File**: ResonanceAudioBlueprintFunctionLibrary.h

<a id="unreal.ResonanceAudioBlueprintFunctionLibrary.set_global_reverb_preset"></a>

#### set_global_reverb_preset

```python
@classmethod
def set_global_reverb_preset(cls,
                             preset: ResonanceAudioReverbPluginPreset) -> None
```

X.set_global_reverb_preset(preset) -> None
This function overrides the Global Reverb Preset for Resonance Audio

Args:
    preset (ResonanceAudioReverbPluginPreset):

<a id="unreal.ResonanceAudioBlueprintFunctionLibrary.get_global_reverb_preset"></a>

#### get_global_reverb_preset

```python
@classmethod
def get_global_reverb_preset(cls) -> ResonanceAudioReverbPluginPreset
```

X.get_global_reverb_preset() -> ResonanceAudioReverbPluginPreset
This function retrieves the Global Reverb Preset for Resonance Audio

Returns:
    ResonanceAudioReverbPluginPreset:

<a id="unreal.ResonanceAudioDirectivityVisualizer"></a>