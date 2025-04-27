## OpenColorIODisplayConfiguration Objects

```python
class OpenColorIODisplayConfiguration(StructBase)
```

Identifies an OCIO Display look configuration

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIO
- **File**: OpenColorIOColorSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_configuration`` (OpenColorIOColorConversionSettings):  [Read-Write] Conversion to apply when this display is enabled
- ``is_enabled`` (bool):  [Read-Write] Whether or not this display configuration is enabled
  Since display look are applied on viewports, this will
  dictate whether it's applied or not to it

<a id="unreal.OpenColorIODisplayConfiguration.__init__"></a>

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

<a id="unreal.OpenColorIODisplayConfiguration.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Whether or not this display configuration is enabled
Since display look are applied on viewports, this will
dictate whether it's applied or not to it

<a id="unreal.OpenColorIODisplayConfiguration.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.OpenColorIODisplayConfiguration.color_configuration"></a>

#### color_configuration

```python
@property
def color_configuration() -> OpenColorIOColorConversionSettings
```

(OpenColorIOColorConversionSettings):  [Read-Write] Conversion to apply when this display is enabled

<a id="unreal.OpenColorIODisplayConfiguration.color_configuration"></a>

#### color_configuration

```python
@color_configuration.setter
def color_configuration(value: OpenColorIOColorConversionSettings) -> None
```

<a id="unreal.MediaCaptureOptions"></a>