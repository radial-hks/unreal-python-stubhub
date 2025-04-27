## DisplayClusterConfigurationICVFX_CustomSize Objects

```python
class DisplayClusterConfigurationICVFX_CustomSize(StructBase)
```

Custom resolution settings for ICVFX.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adapt_size`` (bool):  [Read-Write] Automatically adapts resolution to be proportional
  to the filmback aspect ratio for the ICVFX Camera
  while continuing to render the same total amount of
  pixels as specified by the size. Enabling this can help
  avoid visual artifacts without affecting the
  performance budget.
- ``custom_height`` (int32):  [Read-Write] Custom Height, in pixels.
- ``custom_width`` (int32):  [Read-Write] Custom Width, in pixels.
- ``use_custom_size`` (bool):  [Read-Write] Enabling this option will allow these custom settings to be used instead of the default settings.

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.__init__"></a>

#### __init__

```python
def __init__(use_custom_size: bool = False,
             custom_width: int = 0,
             custom_height: int = 0,
             adapt_size: bool = False) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.use_custom_size"></a>

#### use_custom_size

```python
@property
def use_custom_size() -> bool
```

(bool):  [Read-Write] Enabling this option will allow these custom settings to be used instead of the default settings.

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.use_custom_size"></a>

#### use_custom_size

```python
@use_custom_size.setter
def use_custom_size(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.custom_width"></a>

#### custom_width

```python
@property
def custom_width() -> int
```

(int32):  [Read-Write] Custom Width, in pixels.

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.custom_width"></a>

#### custom_width

```python
@custom_width.setter
def custom_width(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.custom_height"></a>

#### custom_height

```python
@property
def custom_height() -> int
```

(int32):  [Read-Write] Custom Height, in pixels.

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.custom_height"></a>

#### custom_height

```python
@custom_height.setter
def custom_height(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.adapt_size"></a>

#### adapt_size

```python
@property
def adapt_size() -> bool
```

(bool):  [Read-Write] Automatically adapts resolution to be proportional
to the filmback aspect ratio for the ICVFX Camera
while continuing to render the same total amount of
pixels as specified by the size. Enabling this can help
avoid visual artifacts without affecting the
performance budget.

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize.adapt_size"></a>

#### adapt_size

```python
@adapt_size.setter
def adapt_size(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_Size"></a>