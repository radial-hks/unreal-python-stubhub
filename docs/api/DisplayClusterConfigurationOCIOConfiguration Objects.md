## DisplayClusterConfigurationOCIOConfiguration Objects

```python
class DisplayClusterConfigurationOCIOConfiguration(StructBase)
```

* OCIO configuration structure.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_OCIO.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_configuration`` (OpenColorIOColorConversionSettings):  [Read-Write] Conversion to apply when this display is enabled
- ``is_enabled`` (bool):  [Read-Write] Enable the application of an OpenColorIO configuration to all viewports.
- ``ocio_configuration`` (OpenColorIODisplayConfiguration):  [Read-Write] "This property has been deprecated.
  deprecated: Use the ColorConfiguration property instead

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.__init__"></a>

#### __init__

```python
def __init__(
    is_enabled: bool = False,
    color_configuration: OpenColorIOColorConversionSettings = [
        None, ["", -1, ""], ["", -1, ""], ["", ""],
        OpenColorIOViewTransformDirection.FORWARD
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Enable the application of an OpenColorIO configuration to all viewports.

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.ocio_configuration"></a>

#### ocio_configuration

```python
@property
def ocio_configuration() -> OpenColorIODisplayConfiguration
```

(OpenColorIODisplayConfiguration):  [Read-Write] "This property has been deprecated.
deprecated: Use the ColorConfiguration property instead

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.ocio_configuration"></a>

#### ocio_configuration

```python
@ocio_configuration.setter
def ocio_configuration(value: OpenColorIODisplayConfiguration) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.color_configuration"></a>

#### color_configuration

```python
@property
def color_configuration() -> OpenColorIOColorConversionSettings
```

(OpenColorIOColorConversionSettings):  [Read-Write] Conversion to apply when this display is enabled

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration.color_configuration"></a>

#### color_configuration

```python
@color_configuration.setter
def color_configuration(value: OpenColorIOColorConversionSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ViewportOCIO"></a>