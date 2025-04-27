## SourceEffectMidSideSpreaderPreset Objects

```python
class SourceEffectMidSideSpreaderPreset(SoundEffectSourcePreset)
```

USourceEffectMidSideSpreaderPreset
This code exposes your preset settings and effect class to the editor.
And allows for a handle to setting/updating effect settings dynamically.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMidSideSpreader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SourceEffectMidSideSpreaderSettings):  [Read-Write] The copy of the settings struct. Can't be written to in BP, but can be read.
  Note that the value read in BP is the serialized settings, will not reflect dynamic changes made in BP.

<a id="unreal.SourceEffectMidSideSpreaderPreset.settings"></a>

#### settings

```python
@property
def settings() -> SourceEffectMidSideSpreaderSettings
```

(SourceEffectMidSideSpreaderSettings):  [Read-Only] The copy of the settings struct. Can't be written to in BP, but can be read.
Note that the value read in BP is the serialized settings, will not reflect dynamic changes made in BP.

<a id="unreal.SourceEffectMidSideSpreaderPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SourceEffectMidSideSpreaderSettings) -> None
```

x.set_settings(settings) -> None
Change settings of your effect from blueprints. Will broadcast changes to active instances.

Args:
    settings (SourceEffectMidSideSpreaderSettings):

<a id="unreal.SourceEffectMotionFilterPreset"></a>