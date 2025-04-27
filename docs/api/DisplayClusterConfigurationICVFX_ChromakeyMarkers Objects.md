## DisplayClusterConfigurationICVFX_ChromakeyMarkers Objects

```python
class DisplayClusterConfigurationICVFX_ChromakeyMarkers(StructBase)
```

Display Cluster Configuration ICVFX Chromakey Markers

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Write] True to display Chromakey Markers within the inner frustum.
- ``marker_color`` (LinearColor):  [Read-Write] Marker Color
- ``marker_size_scale`` (float):  [Read-Write] Scale value for the size of each chromakey marker tile.
- ``marker_tile_distance`` (float):  [Read-Write] Distance value between each chromakey marker tile.
- ``marker_tile_offset`` (Vector2D):  [Read-Write] Offset value for the chromakey marker tiles, normalized to the tile distance.  Adjust placement of the chromakey markers within the composition of the camera framing.  Whole numbers will offset chromakey markers by a cyclical amount and have no visual change.
- ``marker_tile_rgba`` (Texture):  [Read-Write] Texture to use as the chromakey marker tile.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.__init__"></a>

#### __init__

```python
def __init__(enable: bool = False,
             marker_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             marker_tile_rgba: Texture = None,
             marker_size_scale: float = 0.000000,
             marker_tile_distance: float = 0.000000,
             marker_tile_offset: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] True to display Chromakey Markers within the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_color"></a>

#### marker_color

```python
@property
def marker_color() -> LinearColor
```

(LinearColor):  [Read-Write] Marker Color

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_color"></a>

#### marker_color

```python
@marker_color.setter
def marker_color(value: LinearColor) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_tile_rgba"></a>

#### marker_tile_rgba

```python
@property
def marker_tile_rgba() -> Texture
```

(Texture):  [Read-Write] Texture to use as the chromakey marker tile.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_tile_rgba"></a>

#### marker_tile_rgba

```python
@marker_tile_rgba.setter
def marker_tile_rgba(value: Texture) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_size_scale"></a>

#### marker_size_scale

```python
@property
def marker_size_scale() -> float
```

(float):  [Read-Write] Scale value for the size of each chromakey marker tile.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_size_scale"></a>

#### marker_size_scale

```python
@marker_size_scale.setter
def marker_size_scale(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_tile_distance"></a>

#### marker_tile_distance

```python
@property
def marker_tile_distance() -> float
```

(float):  [Read-Write] Distance value between each chromakey marker tile.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_tile_distance"></a>

#### marker_tile_distance

```python
@marker_tile_distance.setter
def marker_tile_distance(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_tile_offset"></a>

#### marker_tile_offset

```python
@property
def marker_tile_offset() -> Vector2D
```

(Vector2D):  [Read-Write] Offset value for the chromakey marker tiles, normalized to the tile distance.  Adjust placement of the chromakey markers within the composition of the camera framing.  Whole numbers will offset chromakey markers by a cyclical amount and have no visual change.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers.marker_tile_offset"></a>

#### marker_tile_offset

```python
@marker_tile_offset.setter
def marker_tile_offset(value: Vector2D) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings"></a>