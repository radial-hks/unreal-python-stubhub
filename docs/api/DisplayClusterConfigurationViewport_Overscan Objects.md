## DisplayClusterConfigurationViewport_Overscan Objects

```python
class DisplayClusterConfigurationViewport_Overscan(StructBase)
```

Display Cluster Configuration Viewport Overscan

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ViewportOverscan.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bottom`` (float):  [Read-Write] Bottom
- ``enabled`` (bool):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.
- ``left`` (float):  [Read-Write] Left
- ``mode`` (DisplayClusterConfigurationViewportOverscanMode):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.
- ``oversize`` (bool):  [Read-Write] Set to True to render at the overscan resolution, set to false to render at the resolution in the configuration and scale for overscan.
- ``right`` (float):  [Read-Write] Right
- ``top`` (float):  [Read-Write] Top

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.__init__"></a>

#### __init__

```python
def __init__(
        enabled: bool = False,
        mode:
    DisplayClusterConfigurationViewportOverscanMode = DisplayClusterConfigurationViewportOverscanMode
    .PIXELS,
        left: float = 0.000000,
        right: float = 0.000000,
        top: float = 0.000000,
        bottom: float = 0.000000,
        oversize: bool = False) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.mode"></a>

#### mode

```python
@property
def mode() -> DisplayClusterConfigurationViewportOverscanMode
```

(DisplayClusterConfigurationViewportOverscanMode):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.mode"></a>

#### mode

```python
@mode.setter
def mode(value: DisplayClusterConfigurationViewportOverscanMode) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.left"></a>

#### left

```python
@property
def left() -> float
```

(float):  [Read-Write] Left

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.left"></a>

#### left

```python
@left.setter
def left(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.right"></a>

#### right

```python
@property
def right() -> float
```

(float):  [Read-Write] Right

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.right"></a>

#### right

```python
@right.setter
def right(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.top"></a>

#### top

```python
@property
def top() -> float
```

(float):  [Read-Write] Top

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.top"></a>

#### top

```python
@top.setter
def top(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.bottom"></a>

#### bottom

```python
@property
def bottom() -> float
```

(float):  [Read-Write] Bottom

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.bottom"></a>

#### bottom

```python
@bottom.setter
def bottom(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.oversize"></a>

#### oversize

```python
@property
def oversize() -> bool
```

(bool):  [Read-Write] Set to True to render at the overscan resolution, set to false to render at the resolution in the configuration and scale for overscan.

<a id="unreal.DisplayClusterConfigurationViewport_Overscan.oversize"></a>

#### oversize

```python
@oversize.setter
def oversize(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame"></a>