## SoundEffectPresetWidgetInterface Objects

```python
class SoundEffectPresetWidgetInterface(AudioPanelWidgetInterface)
```

Sound Effect Preset Widget Interface

**C++ Source:**

- **Module**: Engine
- **File**: SoundEffectPresetWidgetInterface.h

<a id="unreal.SoundEffectPresetWidgetInterface.on_property_changed"></a>

#### on_property_changed

```python
def on_property_changed(preset: SoundEffectPreset,
                        property_name: Name) -> None
```

x.on_property_changed(preset, property_name) -> None
Called when the preset object is changed

Args:
    preset (SoundEffectPreset): 
    property_name (Name):

<a id="unreal.SoundEffectPresetWidgetInterface.on_constructed"></a>

#### on_constructed

```python
def on_constructed(preset: SoundEffectPreset) -> None
```

x.on_constructed(preset) -> None
Called when the preset widget is constructed

Args:
    preset (SoundEffectPreset):

<a id="unreal.SoundEffectPresetWidgetInterface.get_class"></a>

#### get_class

```python
def get_class() -> Class
```

x.get_class() -> type(Class)
Returns the class of Preset the widget supports

Returns:
    type(Class):

<a id="unreal.SoundEffectSourcePreset"></a>