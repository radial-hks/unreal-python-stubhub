## AudioVectorscope Objects

```python
class AudioVectorscope(Widget)
```

A vectorscope UMG widget.

Supports displaying waveforms in 2D (Left channel X axis, Right channel Y axis) from incoming audio samples.

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioVectorscopeUMG.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``audio_bus`` (AudioBus):  [Read-Write] The audio bus used to obtain audio samples for the vectorscope
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``display_persistence_ms`` (float):  [Read-Write] For how long the audio samples should persist in the screen (in milliseconds).
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``grid_divisions`` (int32):  [Read-Write] The number of grid divisions.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``max_display_persistence_ms`` (float):  [Read-Write] The max where the audio samples should persist in the screen (in milliseconds).
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``panel_layout_type`` (AudioPanelLayoutType):  [Read-Write] Show/Hide advanced panel layout.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``scale`` (float):  [Read-Write] The scale for the displayed audio samples.
- ``show_grid`` (bool):  [Read-Write] Show/Hide the vectorscope grid.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``vectorscope_style`` (AudioVectorscopePanelStyle):  [Read-Write] The vectorscope panel style
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.AudioVectorscope.vectorscope_style"></a>

#### vectorscope_style

```python
@property
def vectorscope_style() -> AudioVectorscopePanelStyle
```

(AudioVectorscopePanelStyle):  [Read-Only] The vectorscope panel style

<a id="unreal.AudioVectorscope.audio_bus"></a>

#### audio_bus

```python
@property
def audio_bus() -> AudioBus
```

(AudioBus):  [Read-Only] The audio bus used to obtain audio samples for the vectorscope

<a id="unreal.AudioVectorscope.show_grid"></a>

#### show_grid

```python
@property
def show_grid() -> bool
```

(bool):  [Read-Only] Show/Hide the vectorscope grid.

<a id="unreal.AudioVectorscope.grid_divisions"></a>

#### grid_divisions

```python
@property
def grid_divisions() -> int
```

(int32):  [Read-Only] The number of grid divisions.

<a id="unreal.AudioVectorscope.max_display_persistence_ms"></a>

#### max_display_persistence_ms

```python
@property
def max_display_persistence_ms() -> float
```

(float):  [Read-Only] The max where the audio samples should persist in the screen (in milliseconds).

<a id="unreal.AudioVectorscope.display_persistence_ms"></a>

#### display_persistence_ms

```python
@property
def display_persistence_ms() -> float
```

(float):  [Read-Only] For how long the audio samples should persist in the screen (in milliseconds).

<a id="unreal.AudioVectorscope.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Only] The scale for the displayed audio samples.

<a id="unreal.AudioVectorscope.panel_layout_type"></a>

#### panel_layout_type

```python
@property
def panel_layout_type() -> AudioPanelLayoutType
```

(AudioPanelLayoutType):  [Read-Only] Show/Hide advanced panel layout.

<a id="unreal.AudioVectorscope.stop_processing"></a>

#### stop_processing

```python
def stop_processing() -> None
```

x.stop_processing() -> None
Stops the vectorscope processing.

<a id="unreal.AudioVectorscope.start_processing"></a>

#### start_processing

```python
def start_processing() -> None
```

x.start_processing() -> None
Starts the vectorscope processing.

<a id="unreal.MetaSoundEditorSubsystem"></a>