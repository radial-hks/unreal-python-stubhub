## DisplayClusterConfigurationICVFX_LightcardCustomOCIO Objects

```python
class DisplayClusterConfigurationICVFX_LightcardCustomOCIO(StructBase)
```

Display Cluster Configuration ICVFX Lightcard Custom OCIO

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_viewports_ocio_configuration`` (DisplayClusterConfigurationOCIOConfiguration):  [Read-Write] Apply this OpenColorIO configuration to all viewports.
- ``per_viewport_ocio_profiles`` (Array[DisplayClusterConfigurationOCIOProfile]):  [Read-Write] Apply an OpenColorIO configuration on a per-viewport or group-of-viewports basis.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardCustomOCIO.__init__"></a>

#### __init__

```python
def __init__(
    all_viewports_ocio_configuration:
    DisplayClusterConfigurationOCIOConfiguration = [
        False,
        [
            None, ["", -1, ""], ["", -1, ""], ["", ""],
            OpenColorIOViewTransformDirection.FORWARD
        ]
    ],
    per_viewport_ocio_profiles: Array[
        DisplayClusterConfigurationOCIOProfile] = []
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardCustomOCIO.all_viewports_ocio_configuration"></a>

#### all_viewports_ocio_configuration

```python
@property
def all_viewports_ocio_configuration(
) -> DisplayClusterConfigurationOCIOConfiguration
```

(DisplayClusterConfigurationOCIOConfiguration):  [Read-Write] Apply this OpenColorIO configuration to all viewports.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardCustomOCIO.all_viewports_ocio_configuration"></a>

#### all_viewports_ocio_configuration

```python
@all_viewports_ocio_configuration.setter
def all_viewports_ocio_configuration(
        value: DisplayClusterConfigurationOCIOConfiguration) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardCustomOCIO.per_viewport_ocio_profiles"></a>

#### per_viewport_ocio_profiles

```python
@property
def per_viewport_ocio_profiles(
) -> Array[DisplayClusterConfigurationOCIOProfile]
```

(Array[DisplayClusterConfigurationOCIOProfile]):  [Read-Write] Apply an OpenColorIO configuration on a per-viewport or group-of-viewports basis.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardCustomOCIO.per_viewport_ocio_profiles"></a>

#### per_viewport_ocio_profiles

```python
@per_viewport_ocio_profiles.setter
def per_viewport_ocio_profiles(
        value: Array[DisplayClusterConfigurationOCIOProfile]) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOProfile"></a>