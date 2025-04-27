## RetainerBox Objects

```python
class RetainerBox(ContentWidget)
```

The Retainer Box renders children widgets to a render target first before
later rendering that render target to the screen.  This allows both frequency
and phase to be controlled so that the UI can actually render less often than the
frequency of the main game render.  It also has the side benefit of allow materials
to be applied to the render target after drawing the widgets to apply a simple post process.

* Single Child
* Caching / Performance

**C++ Source:**

- **Module**: UMG
- **File**: RetainerBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``effect_material`` (MaterialInterface):  [Read-Write] The effect to optionally apply to the render target.  We will set the texture sampler based on the name
  set in the
  TextureParameter: property. If you want to adjust transparency of the final image, make sure you set Blend Mode to AlphaComposite (Pre-Multiplied Alpha) and make sure to multiply the alpha you're apply across the surface to the color and the alpha of the render target, otherwise you won't see the expected color.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``phase`` (int32):  [Read-Write] The Phase this widget will draw on.

  If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.
  If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every
  other frame.  So in a 60Hz game, the UI would render at 30Hz.
- ``phase_count`` (int32):  [Read-Write] The PhaseCount controls how many phases are possible know what to modulus the current frame
  count by to determine if this is the current frame to draw the widget on.

  If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.
  If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every
  other frame.  So in a 60Hz game, the UI would render at 30Hz.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_on_invalidation`` (bool):  [Read-Write] Should this widget redraw the contents it has every time it receives an invalidation request
  from it's children, similar to the invalidation panel.
- ``render_on_phase`` (bool):  [Read-Write] Should this widget redraw the contents it has every time the phase occurs.
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``retain_render`` (bool):  [Read-Write]
- ``show_effects_in_designer`` (bool):  [Read-Write] If true, retained rendering occurs in designer
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``texture_parameter`` (Name):  [Read-Write] The texture sampler parameter of the
  EffectMaterial,: that we'll set to the render target.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.RetainerBox.retain_render"></a>

#### retain_render

```python
@property
def retain_render() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RetainerBox.retain_render"></a>

#### retain_render

```python
@retain_render.setter
def retain_render(value: bool) -> None
```

<a id="unreal.RetainerBox.render_on_invalidation"></a>

#### render_on_invalidation

```python
@property
def render_on_invalidation() -> bool
```

(bool):  [Read-Only] Should this widget redraw the contents it has every time it receives an invalidation request
from it's children, similar to the invalidation panel.

<a id="unreal.RetainerBox.render_on_phase"></a>

#### render_on_phase

```python
@property
def render_on_phase() -> bool
```

(bool):  [Read-Only] Should this widget redraw the contents it has every time the phase occurs.

<a id="unreal.RetainerBox.phase"></a>

#### phase

```python
@property
def phase() -> int
```

(int32):  [Read-Only] The Phase this widget will draw on.

If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.
If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every
other frame.  So in a 60Hz game, the UI would render at 30Hz.

<a id="unreal.RetainerBox.phase_count"></a>

#### phase_count

```python
@property
def phase_count() -> int
```

(int32):  [Read-Only] The PhaseCount controls how many phases are possible know what to modulus the current frame
count by to determine if this is the current frame to draw the widget on.

If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.
If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every
other frame.  So in a 60Hz game, the UI would render at 30Hz.

<a id="unreal.RetainerBox.effect_material"></a>

#### effect_material

```python
@property
def effect_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] The effect to optionally apply to the render target.  We will set the texture sampler based on the name
set in the
TextureParameter: property. If you want to adjust transparency of the final image, make sure you set Blend Mode to AlphaComposite (Pre-Multiplied Alpha) and make sure to multiply the alpha you're apply across the surface to the color and the alpha of the render target, otherwise you won't see the expected color.

<a id="unreal.RetainerBox.effect_material"></a>

#### effect_material

```python
@effect_material.setter
def effect_material(value: MaterialInterface) -> None
```

<a id="unreal.RetainerBox.texture_parameter"></a>

#### texture_parameter

```python
@property
def texture_parameter() -> Name
```

(Name):  [Read-Write] The texture sampler parameter of the
EffectMaterial,: that we'll set to the render target.

<a id="unreal.RetainerBox.texture_parameter"></a>

#### texture_parameter

```python
@texture_parameter.setter
def texture_parameter(value: Name) -> None
```

<a id="unreal.RetainerBox.show_effects_in_designer"></a>

#### show_effects_in_designer

```python
@property
def show_effects_in_designer() -> bool
```

(bool):  [Read-Only] If true, retained rendering occurs in designer

<a id="unreal.RetainerBox.set_texture_parameter"></a>

#### set_texture_parameter

```python
def set_texture_parameter(texture_parameter: Name) -> None
```

x.set_texture_parameter(texture_parameter) -> None
Sets the name of the texture parameter to set the render target to on the material.

Args:
    texture_parameter (Name):

<a id="unreal.RetainerBox.set_retain_rendering"></a>

#### set_retain_rendering

```python
def set_retain_rendering(retain_rendering: bool) -> None
```

x.set_retain_rendering(retain_rendering) -> None
Set the flag for if we retain the render or pass-through

Args:
    retain_rendering (bool):

<a id="unreal.RetainerBox.set_rendering_phase"></a>

#### set_rendering_phase

```python
def set_rendering_phase(render_phase: int, total_phases: int) -> None
```

x.set_rendering_phase(render_phase, total_phases) -> None
Requests the retainer redrawn the contents it has.

Args:
    render_phase (int32): 
    total_phases (int32):

<a id="unreal.RetainerBox.set_effect_material"></a>

#### set_effect_material

```python
def set_effect_material(effect_material: MaterialInterface) -> None
```

x.set_effect_material(effect_material) -> None
Set a new effect material to the retainer widget.

Args:
    effect_material (MaterialInterface):

<a id="unreal.RetainerBox.request_render"></a>

#### request_render

```python
def request_render() -> None
```

x.request_render() -> None
Requests the retainer redrawn the contents it has.

<a id="unreal.RetainerBox.get_effect_material"></a>

#### get_effect_material

```python
def get_effect_material() -> MaterialInstanceDynamic
```

x.get_effect_material() -> MaterialInstanceDynamic
Get the current dynamic effect material applied to the retainer box.

Returns:
    MaterialInstanceDynamic:

<a id="unreal.RichTextBlock"></a>