## SoundAttenuationPluginSettings Objects

```python
class SoundAttenuationPluginSettings(StructBase)
```

Sound Attenuation Plugin Settings

**C++ Source:**

- **Module**: Engine
- **File**: SoundAttenuation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``occlusion_plugin_settings_array`` (Array[OcclusionPluginSourceSettingsBase]):  [Read-Write] Settings to use with occlusion audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.
- ``reverb_plugin_settings_array`` (Array[ReverbPluginSourceSettingsBase]):  [Read-Write] Settings to use with reverb audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.
- ``source_data_override_plugin_settings_array`` (Array[SourceDataOverridePluginSourceSettingsBase]):  [Read-Write] Settings to use with source data override audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.
- ``spatialization_plugin_settings_array`` (Array[SpatializationPluginSourceSettingsBase]):  [Read-Write] Settings to use with spatialization audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.

<a id="unreal.SoundAttenuationPluginSettings.__init__"></a>

#### __init__

```python
def __init__(
    spatialization_plugin_settings_array: Array[
        SpatializationPluginSourceSettingsBase] = [],
    occlusion_plugin_settings_array: Array[
        OcclusionPluginSourceSettingsBase] = [],
    reverb_plugin_settings_array: Array[ReverbPluginSourceSettingsBase] = [],
    source_data_override_plugin_settings_array: Array[
        SourceDataOverridePluginSourceSettingsBase] = []
) -> None
```

<a id="unreal.SoundAttenuationPluginSettings.spatialization_plugin_settings_array"></a>

#### spatialization_plugin_settings_array

```python
@property
def spatialization_plugin_settings_array(
) -> Array[SpatializationPluginSourceSettingsBase]
```

(Array[SpatializationPluginSourceSettingsBase]):  [Read-Write] Settings to use with spatialization audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.

<a id="unreal.SoundAttenuationPluginSettings.spatialization_plugin_settings_array"></a>

#### spatialization_plugin_settings_array

```python
@spatialization_plugin_settings_array.setter
def spatialization_plugin_settings_array(
        value: Array[SpatializationPluginSourceSettingsBase]) -> None
```

<a id="unreal.SoundAttenuationPluginSettings.occlusion_plugin_settings_array"></a>

#### occlusion_plugin_settings_array

```python
@property
def occlusion_plugin_settings_array(
) -> Array[OcclusionPluginSourceSettingsBase]
```

(Array[OcclusionPluginSourceSettingsBase]):  [Read-Write] Settings to use with occlusion audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.

<a id="unreal.SoundAttenuationPluginSettings.occlusion_plugin_settings_array"></a>

#### occlusion_plugin_settings_array

```python
@occlusion_plugin_settings_array.setter
def occlusion_plugin_settings_array(
        value: Array[OcclusionPluginSourceSettingsBase]) -> None
```

<a id="unreal.SoundAttenuationPluginSettings.reverb_plugin_settings_array"></a>

#### reverb_plugin_settings_array

```python
@property
def reverb_plugin_settings_array() -> Array[ReverbPluginSourceSettingsBase]
```

(Array[ReverbPluginSourceSettingsBase]):  [Read-Write] Settings to use with reverb audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.

<a id="unreal.SoundAttenuationPluginSettings.reverb_plugin_settings_array"></a>

#### reverb_plugin_settings_array

```python
@reverb_plugin_settings_array.setter
def reverb_plugin_settings_array(
        value: Array[ReverbPluginSourceSettingsBase]) -> None
```

<a id="unreal.SoundAttenuationPluginSettings.source_data_override_plugin_settings_array"></a>

#### source_data_override_plugin_settings_array

```python
@property
def source_data_override_plugin_settings_array(
) -> Array[SourceDataOverridePluginSourceSettingsBase]
```

(Array[SourceDataOverridePluginSourceSettingsBase]):  [Read-Write] Settings to use with source data override audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. This is an array so multiple plugins can have settings.

<a id="unreal.SoundAttenuationPluginSettings.source_data_override_plugin_settings_array"></a>

#### source_data_override_plugin_settings_array

```python
@source_data_override_plugin_settings_array.setter
def source_data_override_plugin_settings_array(
        value: Array[SourceDataOverridePluginSourceSettingsBase]) -> None
```

<a id="unreal.SoundSubmixSendInfoBase"></a>