## DisplayClusterConfigurationOCIOProfile Objects

```python
class DisplayClusterConfigurationOCIOProfile(StructBase)
```

* OCIO profile structure. Can be configured for viewports or cluster nodes.
* To enable viewport configuration when using as a UPROPERTY set meta = (ConfigurationMode = "Viewports")
* To enable cluster node configuration when using as a UPROPERTY set meta = (ConfigurationMode = "ClusterNodes")

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_OCIO.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_ocio_to_objects`` (Array[str]):  [Read-Write] Specify the viewports to apply this OpenColorIO configuration.
- ``color_configuration`` (OpenColorIOColorConversionSettings):  [Read-Write] Conversion to apply when this display is enabled
- ``is_enabled`` (bool):  [Read-Write] Enable the application of an OpenColorIO configuration for the viewport(s) specified.
- ``ocio_configuration`` (OpenColorIODisplayConfiguration):  [Read-Write] "This property has been deprecated.
  deprecated: Use the ColorConfiguration property instead

<a id="unreal.DisplayClusterConfigurationOCIOProfile.__init__"></a>

#### __init__

```python
def __init__(
    is_enabled: bool = False,
    apply_ocio_to_objects: Array[str] = [],
    color_configuration: OpenColorIOColorConversionSettings = [
        None, ["", -1, ""], ["", -1, ""], ["", ""],
        OpenColorIOViewTransformDirection.FORWARD
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOProfile.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Enable the application of an OpenColorIO configuration for the viewport(s) specified.

<a id="unreal.DisplayClusterConfigurationOCIOProfile.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOProfile.ocio_configuration"></a>

#### ocio_configuration

```python
@property
def ocio_configuration() -> OpenColorIODisplayConfiguration
```

(OpenColorIODisplayConfiguration):  [Read-Write] "This property has been deprecated.
deprecated: Use the ColorConfiguration property instead

<a id="unreal.DisplayClusterConfigurationOCIOProfile.ocio_configuration"></a>

#### ocio_configuration

```python
@ocio_configuration.setter
def ocio_configuration(value: OpenColorIODisplayConfiguration) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOProfile.apply_ocio_to_objects"></a>

#### apply_ocio_to_objects

```python
@property
def apply_ocio_to_objects() -> Array[str]
```

(Array[str]):  [Read-Only] Specify the viewports to apply this OpenColorIO configuration.

<a id="unreal.DisplayClusterConfigurationOCIOProfile.color_configuration"></a>

#### color_configuration

```python
@property
def color_configuration() -> OpenColorIOColorConversionSettings
```

(OpenColorIOColorConversionSettings):  [Read-Write] Conversion to apply when this display is enabled

<a id="unreal.DisplayClusterConfigurationOCIOProfile.color_configuration"></a>

#### color_configuration

```python
@color_configuration.setter
def color_configuration(value: OpenColorIOColorConversionSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationOCIOConfiguration"></a>