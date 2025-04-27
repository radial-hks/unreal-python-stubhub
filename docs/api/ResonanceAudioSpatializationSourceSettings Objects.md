## ResonanceAudioSpatializationSourceSettings Objects

```python
class ResonanceAudioSpatializationSourceSettings(
        SpatializationPluginSourceSettingsBase)
```

Resonance Audio Spatialization Source Settings

**C++ Source:**

- **Plugin**: ResonanceAudio
- **Module**: ResonanceAudio
- **File**: ResonanceAudioSpatializationSourceSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_distance`` (float):  [Read-Write] Maximum distance to apply the chosen attenuation method ((default = 50000.0 cm)
- ``min_distance`` (float):  [Read-Write] Minimum distance to apply the chosen attenuation method (default = 100.0 cm)
- ``pattern`` (float):  [Read-Write] Directivity pattern: 0.0 (omnidirectional), 0.5 (cardioid), 1.0 (figure-of-8)
- ``rolloff`` (RaDistanceRolloffModel):  [Read-Write] Roll-off model to use for sound source distance attenuation. Select 'None' (default) to use Unreal attenuation settings
- ``scale`` (float):  [Read-Write] Scale (for directivity pattern visualization only).
- ``sharpness`` (float):  [Read-Write] Sharpness of the directivity pattern. Higher values result in a narrower sound emission beam
- ``spatialization_method`` (RaSpatializationMethod):  [Read-Write] Spatialization method to use for sound object(s). NOTE: Has no effect if 'Stereo Panning' global quality mode is selected for the project
- ``spread`` (float):  [Read-Write] Spread (width) of the sound source (in degrees). Note: spread control is not available if 'Stereo Panning' global quality mode is enabled for the project and / or 'Stereo Panning' spatialization mode is enabled for the sound source
- ``toggle_visualization`` (bool):  [Read-Write] Whether to visualize directivity pattern in the viewport.

<a id="unreal.ResonanceAudioSpatializationSourceSettings.set_sound_source_spread"></a>

#### set_sound_source_spread

```python
def set_sound_source_spread(spread: float) -> None
```

x.set_sound_source_spread(spread) -> None
Sets the sound source spread (width), applies, and updates

Args:
    spread (float):

<a id="unreal.ResonanceAudioSpatializationSourceSettings.set_sound_source_directivity"></a>

#### set_sound_source_directivity

```python
def set_sound_source_directivity(pattern: float, sharpness: float) -> None
```

x.set_sound_source_directivity(pattern, sharpness) -> None
Sets the sound source directivity, applies, and updates

Args:
    pattern (float): 
    sharpness (float):

<a id="unreal.StateTreeEditorData"></a>