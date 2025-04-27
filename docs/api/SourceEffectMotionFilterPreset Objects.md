## SourceEffectMotionFilterPreset Objects

```python
class SourceEffectMotionFilterPreset(SoundEffectSourcePreset)
```

USourceEffectMotionFilterPreset
This code exposes your preset settings and effect class to the editor.
And allows for a handle to setting/updating effect settings dynamically.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMotionFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SourceEffectMotionFilterSettings):  [Read-Write] The copy of the settings struct. Can't be written to in BP, but can be read.
  Note that the value read in BP is the serialized settings, will not reflect dynamic changes made in BP.

<a id="unreal.SourceEffectMotionFilterPreset.settings"></a>

#### settings

```python
@property
def settings() -> SourceEffectMotionFilterSettings
```

(SourceEffectMotionFilterSettings):  [Read-Only] The copy of the settings struct. Can't be written to in BP, but can be read.
Note that the value read in BP is the serialized settings, will not reflect dynamic changes made in BP.

<a id="unreal.SourceEffectMotionFilterPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SourceEffectMotionFilterSettings) -> None
```

x.set_settings(settings) -> None
Change settings of your effect from blueprints. Will broadcast changes to active instances.

Args:
    settings (SourceEffectMotionFilterSettings):

<a id="unreal.SourceEffectPannerPreset"></a>