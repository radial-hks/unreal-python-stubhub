## AvaViewportSettings Objects

```python
class AvaViewportSettings(DeveloperSettings)
```

Ava Viewport Settings

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheViewport
- **File**: AvaViewportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_bounds_shade_color`` (LinearColor):  [Read-Write]
- ``disabled_guide_color`` (LinearColor):  [Read-Write]
- ``disabled_locked_guide_color`` (LinearColor):  [Read-Write]
- ``dragged_guide_color`` (LinearColor):  [Read-Write]
- ``enable_bounding_boxes`` (bool):  [Read-Write]
- ``enable_shapes_editor_overlay`` (bool):  [Read-Write]
- ``enable_texture_overlay`` (bool):  [Read-Write]
- ``enable_viewport_overlay`` (bool):  [Read-Write]
- ``enabled_guide_color`` (LinearColor):  [Read-Write]
- ``enabled_locked_guide_color`` (LinearColor):  [Read-Write]
- ``grid_always_visible`` (bool):  [Read-Write]
- ``grid_color`` (LinearColor):  [Read-Write]
- ``grid_enabled`` (bool):  [Read-Write]
- ``grid_size`` (int32):  [Read-Write]
- ``grid_thickness`` (float):  [Read-Write]
- ``guide_config_path`` (str):  [Read-Write] Directory used to load and save guide json config files.

  The path will be checked against 3 possible locations:
  - Just itself (/Config/Guides)
  - Project (/Path/To/Project/Config/Guides)
  - Plugin (/Path/To/Plugin/Config/Guides)

  Example values:
  - /Config/Guides
  - D:\UnrealEngine\Config\Guides
- ``guide_thickness`` (float):  [Read-Write]
- ``guides_enabled`` (bool):  [Read-Write]
- ``pixel_grid_color`` (LinearColor):  [Read-Write]
- ``pixel_grid_enabled`` (bool):  [Read-Write]
- ``safe_frames`` (Array[AvaLevelViewportSafeFrame]):  [Read-Write]
- ``safe_frames_enabled`` (bool):  [Read-Write]
- ``shape_editor_overlay_type`` (AvaShapeEditorOverlayType):  [Read-Write] Whether to show or hide the Shapes In-Viewport controls.
- ``snap_indicator_color`` (LinearColor):  [Read-Write]
- ``snap_indicator_thickness`` (float):  [Read-Write]
- ``snap_indicators_enabled`` (bool):  [Read-Write]
- ``snap_state`` (int32):  [Read-Write]
- ``texture_overlay_opacity`` (float):  [Read-Write]
- ``texture_overlay_stretch`` (bool):  [Read-Write]
- ``texture_overlay_texture`` (Texture):  [Read-Write]
- ``viewport_background_material`` (Material):  [Read-Write]
- ``viewport_checkerboard_color0`` (LinearColor):  [Read-Write]
- ``viewport_checkerboard_color1`` (LinearColor):  [Read-Write]
- ``viewport_checkerboard_material`` (Material):  [Read-Write]
- ``viewport_checkerboard_size`` (float):  [Read-Write]

<a id="unreal.AvaViewportSettings.enable_viewport_overlay"></a>

#### enable_viewport_overlay

```python
@property
def enable_viewport_overlay() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.enable_viewport_overlay"></a>

#### enable_viewport_overlay

```python
@enable_viewport_overlay.setter
def enable_viewport_overlay(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.enable_bounding_boxes"></a>

#### enable_bounding_boxes

```python
@property
def enable_bounding_boxes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.enable_bounding_boxes"></a>

#### enable_bounding_boxes

```python
@enable_bounding_boxes.setter
def enable_bounding_boxes(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.viewport_background_material"></a>

#### viewport_background_material

```python
@property
def viewport_background_material() -> Material
```

(Material):  [Read-Write]

<a id="unreal.AvaViewportSettings.viewport_background_material"></a>

#### viewport_background_material

```python
@viewport_background_material.setter
def viewport_background_material(value: Material) -> None
```

<a id="unreal.AvaViewportSettings.viewport_checkerboard_material"></a>

#### viewport_checkerboard_material

```python
@property
def viewport_checkerboard_material() -> Material
```

(Material):  [Read-Write]

<a id="unreal.AvaViewportSettings.viewport_checkerboard_material"></a>

#### viewport_checkerboard_material

```python
@viewport_checkerboard_material.setter
def viewport_checkerboard_material(value: Material) -> None
```

<a id="unreal.AvaViewportSettings.viewport_checkerboard_color0"></a>

#### viewport_checkerboard_color0

```python
@property
def viewport_checkerboard_color0() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.viewport_checkerboard_color0"></a>

#### viewport_checkerboard_color0

```python
@viewport_checkerboard_color0.setter
def viewport_checkerboard_color0(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.viewport_checkerboard_color1"></a>

#### viewport_checkerboard_color1

```python
@property
def viewport_checkerboard_color1() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.viewport_checkerboard_color1"></a>

#### viewport_checkerboard_color1

```python
@viewport_checkerboard_color1.setter
def viewport_checkerboard_color1(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.viewport_checkerboard_size"></a>

#### viewport_checkerboard_size

```python
@property
def viewport_checkerboard_size() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaViewportSettings.viewport_checkerboard_size"></a>

#### viewport_checkerboard_size

```python
@viewport_checkerboard_size.setter
def viewport_checkerboard_size(value: float) -> None
```

<a id="unreal.AvaViewportSettings.enable_shapes_editor_overlay"></a>

#### enable_shapes_editor_overlay

```python
@property
def enable_shapes_editor_overlay() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.enable_shapes_editor_overlay"></a>

#### enable_shapes_editor_overlay

```python
@enable_shapes_editor_overlay.setter
def enable_shapes_editor_overlay(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.shape_editor_overlay_type"></a>

#### shape_editor_overlay_type

```python
@property
def shape_editor_overlay_type() -> AvaShapeEditorOverlayType
```

(AvaShapeEditorOverlayType):  [Read-Write] Whether to show or hide the Shapes In-Viewport controls.

<a id="unreal.AvaViewportSettings.shape_editor_overlay_type"></a>

#### shape_editor_overlay_type

```python
@shape_editor_overlay_type.setter
def shape_editor_overlay_type(value: AvaShapeEditorOverlayType) -> None
```

<a id="unreal.AvaViewportSettings.grid_enabled"></a>

#### grid_enabled

```python
@property
def grid_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.grid_enabled"></a>

#### grid_enabled

```python
@grid_enabled.setter
def grid_enabled(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.grid_always_visible"></a>

#### grid_always_visible

```python
@property
def grid_always_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.grid_always_visible"></a>

#### grid_always_visible

```python
@grid_always_visible.setter
def grid_always_visible(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.grid_size"></a>

#### grid_size

```python
@property
def grid_size() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaViewportSettings.grid_size"></a>

#### grid_size

```python
@grid_size.setter
def grid_size(value: int) -> None
```

<a id="unreal.AvaViewportSettings.grid_color"></a>

#### grid_color

```python
@property
def grid_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.grid_color"></a>

#### grid_color

```python
@grid_color.setter
def grid_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.grid_thickness"></a>

#### grid_thickness

```python
@property
def grid_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaViewportSettings.grid_thickness"></a>

#### grid_thickness

```python
@grid_thickness.setter
def grid_thickness(value: float) -> None
```

<a id="unreal.AvaViewportSettings.pixel_grid_enabled"></a>

#### pixel_grid_enabled

```python
@property
def pixel_grid_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.pixel_grid_enabled"></a>

#### pixel_grid_enabled

```python
@pixel_grid_enabled.setter
def pixel_grid_enabled(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.pixel_grid_color"></a>

#### pixel_grid_color

```python
@property
def pixel_grid_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.pixel_grid_color"></a>

#### pixel_grid_color

```python
@pixel_grid_color.setter
def pixel_grid_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.snap_state"></a>

#### snap_state

```python
@property
def snap_state() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaViewportSettings.snap_state"></a>

#### snap_state

```python
@snap_state.setter
def snap_state(value: int) -> None
```

<a id="unreal.AvaViewportSettings.snap_indicators_enabled"></a>

#### snap_indicators_enabled

```python
@property
def snap_indicators_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.snap_indicators_enabled"></a>

#### snap_indicators_enabled

```python
@snap_indicators_enabled.setter
def snap_indicators_enabled(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.snap_indicator_color"></a>

#### snap_indicator_color

```python
@property
def snap_indicator_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.snap_indicator_color"></a>

#### snap_indicator_color

```python
@snap_indicator_color.setter
def snap_indicator_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.snap_indicator_thickness"></a>

#### snap_indicator_thickness

```python
@property
def snap_indicator_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaViewportSettings.snap_indicator_thickness"></a>

#### snap_indicator_thickness

```python
@snap_indicator_thickness.setter
def snap_indicator_thickness(value: float) -> None
```

<a id="unreal.AvaViewportSettings.guides_enabled"></a>

#### guides_enabled

```python
@property
def guides_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.guides_enabled"></a>

#### guides_enabled

```python
@guides_enabled.setter
def guides_enabled(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.guide_config_path"></a>

#### guide_config_path

```python
@property
def guide_config_path() -> str
```

(str):  [Read-Write] Directory used to load and save guide json config files.

The path will be checked against 3 possible locations:
- Just itself (/Config/Guides)
- Project (/Path/To/Project/Config/Guides)
- Plugin (/Path/To/Plugin/Config/Guides)

Example values:
- /Config/Guides
- D:\UnrealEngine\Config\Guides

<a id="unreal.AvaViewportSettings.guide_config_path"></a>

#### guide_config_path

```python
@guide_config_path.setter
def guide_config_path(value: str) -> None
```

<a id="unreal.AvaViewportSettings.enabled_guide_color"></a>

#### enabled_guide_color

```python
@property
def enabled_guide_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.enabled_guide_color"></a>

#### enabled_guide_color

```python
@enabled_guide_color.setter
def enabled_guide_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.enabled_locked_guide_color"></a>

#### enabled_locked_guide_color

```python
@property
def enabled_locked_guide_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.enabled_locked_guide_color"></a>

#### enabled_locked_guide_color

```python
@enabled_locked_guide_color.setter
def enabled_locked_guide_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.disabled_guide_color"></a>

#### disabled_guide_color

```python
@property
def disabled_guide_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.disabled_guide_color"></a>

#### disabled_guide_color

```python
@disabled_guide_color.setter
def disabled_guide_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.disabled_locked_guide_color"></a>

#### disabled_locked_guide_color

```python
@property
def disabled_locked_guide_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.disabled_locked_guide_color"></a>

#### disabled_locked_guide_color

```python
@disabled_locked_guide_color.setter
def disabled_locked_guide_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.dragged_guide_color"></a>

#### dragged_guide_color

```python
@property
def dragged_guide_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.dragged_guide_color"></a>

#### dragged_guide_color

```python
@dragged_guide_color.setter
def dragged_guide_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.guide_thickness"></a>

#### guide_thickness

```python
@property
def guide_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaViewportSettings.guide_thickness"></a>

#### guide_thickness

```python
@guide_thickness.setter
def guide_thickness(value: float) -> None
```

<a id="unreal.AvaViewportSettings.safe_frames_enabled"></a>

#### safe_frames_enabled

```python
@property
def safe_frames_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.safe_frames_enabled"></a>

#### safe_frames_enabled

```python
@safe_frames_enabled.setter
def safe_frames_enabled(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.safe_frames"></a>

#### safe_frames

```python
@property
def safe_frames() -> Array[AvaLevelViewportSafeFrame]
```

(Array[AvaLevelViewportSafeFrame]):  [Read-Write]

<a id="unreal.AvaViewportSettings.safe_frames"></a>

#### safe_frames

```python
@safe_frames.setter
def safe_frames(value: Array[AvaLevelViewportSafeFrame]) -> None
```

<a id="unreal.AvaViewportSettings.camera_bounds_shade_color"></a>

#### camera_bounds_shade_color

```python
@property
def camera_bounds_shade_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaViewportSettings.camera_bounds_shade_color"></a>

#### camera_bounds_shade_color

```python
@camera_bounds_shade_color.setter
def camera_bounds_shade_color(value: LinearColor) -> None
```

<a id="unreal.AvaViewportSettings.enable_texture_overlay"></a>

#### enable_texture_overlay

```python
@property
def enable_texture_overlay() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.enable_texture_overlay"></a>

#### enable_texture_overlay

```python
@enable_texture_overlay.setter
def enable_texture_overlay(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.texture_overlay_texture"></a>

#### texture_overlay_texture

```python
@property
def texture_overlay_texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.AvaViewportSettings.texture_overlay_texture"></a>

#### texture_overlay_texture

```python
@texture_overlay_texture.setter
def texture_overlay_texture(value: Texture) -> None
```

<a id="unreal.AvaViewportSettings.texture_overlay_opacity"></a>

#### texture_overlay_opacity

```python
@property
def texture_overlay_opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaViewportSettings.texture_overlay_opacity"></a>

#### texture_overlay_opacity

```python
@texture_overlay_opacity.setter
def texture_overlay_opacity(value: float) -> None
```

<a id="unreal.AvaViewportSettings.texture_overlay_stretch"></a>

#### texture_overlay_stretch

```python
@property
def texture_overlay_stretch() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaViewportSettings.texture_overlay_stretch"></a>

#### texture_overlay_stretch

```python
@texture_overlay_stretch.setter
def texture_overlay_stretch(value: bool) -> None
```

<a id="unreal.AvaViewportSettings.set_snap_state"></a>

#### set_snap_state

```python
def set_snap_state(snap_state: AvaViewportSnapState) -> None
```

x.set_snap_state(snap_state) -> None
Set Snap State

Args:
    snap_state (AvaViewportSnapState):

<a id="unreal.AvaViewportSettings.has_snap_state"></a>

#### has_snap_state

```python
def has_snap_state(snap_state: AvaViewportSnapState) -> bool
```

x.has_snap_state(snap_state) -> bool
Has Snap State

Args:
    snap_state (AvaViewportSnapState): 

Returns:
    bool:

<a id="unreal.AvaViewportSettings.get_snap_state"></a>

#### get_snap_state

```python
def get_snap_state() -> AvaViewportSnapState
```

x.get_snap_state() -> AvaViewportSnapState
Get Snap State

Returns:
    AvaViewportSnapState:

<a id="unreal.AvaInteractiveToolsToolViewportPlanner"></a>