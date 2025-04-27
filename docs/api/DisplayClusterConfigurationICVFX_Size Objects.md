## DisplayClusterConfigurationICVFX_Size Objects

```python
class DisplayClusterConfigurationICVFX_Size(StructBase)
```

Default resolution settings for ICVFX.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adapt_size`` (bool):  [Read-Write] Automatically adapts the default frame resolution to be proportional
  to the filmback aspect ratio for the ICVFX Camera
  while continuing to render the same total amount of
  pixels as specified by the size. Enabling this can help
  avoid visual artifacts without affecting the
  performance budget.
- ``height`` (int32):  [Read-Write] The default height of In-Cameras, in pixels.
- ``width`` (int32):  [Read-Write] The default width of In-Cameras, in pixels.

<a id="unreal.DisplayClusterConfigurationICVFX_Size.__init__"></a>

#### __init__

```python
def __init__(width: int = 0,
             height: int = 0,
             adapt_size: bool = False) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_Size.width"></a>

#### width

```python
@property
def width() -> int
```

(int32):  [Read-Write] The default width of In-Cameras, in pixels.

<a id="unreal.DisplayClusterConfigurationICVFX_Size.width"></a>

#### width

```python
@width.setter
def width(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_Size.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Write] The default height of In-Cameras, in pixels.

<a id="unreal.DisplayClusterConfigurationICVFX_Size.height"></a>

#### height

```python
@height.setter
def height(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_Size.adapt_size"></a>

#### adapt_size

```python
@property
def adapt_size() -> bool
```

(bool):  [Read-Write] Automatically adapts the default frame resolution to be proportional
to the filmback aspect ratio for the ICVFX Camera
while continuing to render the same total amount of
pixels as specified by the size. Enabling this can help
avoid visual artifacts without affecting the
performance budget.

<a id="unreal.DisplayClusterConfigurationICVFX_Size.adapt_size"></a>

#### adapt_size

```python
@adapt_size.setter
def adapt_size(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings"></a>