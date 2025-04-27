## DisplayClusterConfigurationViewport_RemapData Objects

```python
class DisplayClusterConfigurationViewport_RemapData(StructBase)
```

Remapping configuration for a single remapped region, which can be any subregion of a viewport, and can be remapped to any
part of the screen, and can be rotated or flipped

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ViewportRemap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write] The angle in degrees to rotate the remapped region by; rotation is performed around the center of the output region
- ``flip_h`` (bool):  [Read-Write] Flips the remapped region horizontally
- ``flip_v`` (bool):  [Read-Write] Flips the remapped region vertically
- ``output_region`` (DisplayClusterConfigurationRectangle):  [Read-Write] The region in screen space to output the remapped region to
- ``viewport_region`` (DisplayClusterConfigurationRectangle):  [Read-Write] The subregion of the viewport to remap; (0,0) x (W, H) will remap the entire viewport

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.__init__"></a>

#### __init__

```python
def __init__(viewport_region: DisplayClusterConfigurationRectangle = [
    0, 0, 0, 0
],
             output_region: DisplayClusterConfigurationRectangle = [
                 0, 0, 0, 0
             ],
             angle: float = 0.000000,
             flip_h: bool = False,
             flip_v: bool = False) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.viewport_region"></a>

#### viewport_region

```python
@property
def viewport_region() -> DisplayClusterConfigurationRectangle
```

(DisplayClusterConfigurationRectangle):  [Read-Write] The subregion of the viewport to remap; (0,0) x (W, H) will remap the entire viewport

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.viewport_region"></a>

#### viewport_region

```python
@viewport_region.setter
def viewport_region(value: DisplayClusterConfigurationRectangle) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.output_region"></a>

#### output_region

```python
@property
def output_region() -> DisplayClusterConfigurationRectangle
```

(DisplayClusterConfigurationRectangle):  [Read-Write] The region in screen space to output the remapped region to

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.output_region"></a>

#### output_region

```python
@output_region.setter
def output_region(value: DisplayClusterConfigurationRectangle) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write] The angle in degrees to rotate the remapped region by; rotation is performed around the center of the output region

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.flip_h"></a>

#### flip_h

```python
@property
def flip_h() -> bool
```

(bool):  [Read-Write] Flips the remapped region horizontally

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.flip_h"></a>

#### flip_h

```python
@flip_h.setter
def flip_h(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.flip_v"></a>

#### flip_v

```python
@property
def flip_v() -> bool
```

(bool):  [Read-Write] Flips the remapped region vertically

<a id="unreal.DisplayClusterConfigurationViewport_RemapData.flip_v"></a>

#### flip_v

```python
@flip_v.setter
def flip_v(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Remap"></a>