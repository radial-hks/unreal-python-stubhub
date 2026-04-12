## EarthTabListWidget\_MeshRegistry Objects

```python
class EarthTabListWidget_MeshRegistry(EarthTabListWidget)
```

Earth Tab List Widget Mesh Registry

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorUI
- **File**: EarthTabList_MeshRegistry.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``button_class`` (type(Class)):  [Read-Write]
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (LinearColor):  [Read-Write] The color and opacity of this widget.  Tints all child widgets.
- ``command_class`` (type(Class)):  [Read-Write]
- ``current_button`` (EarthTabButtonWidget):  [Read-Write]
- ``current_content`` (EarthTabContentWidget):  [Read-Write]
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``desired_focus_widget`` (WidgetChild):  [Read-Write]
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``foreground_color`` (SlateColor):  [Read-Write] The foreground color of the widget, this is inherited by sub widgets.  Any color property
  that is marked as inherit will use this color.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``layer_name`` (Name):  [Read-Write]
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_changed`` (OnEarthTabButtonChanged):  [Read-Write]
- ``on_visibility_changed`` (OnVisibilityChangedEvent):  [Read-Write] Called when the visibility has changed
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The padding area around the content.
- ``panel`` (PanelWidget):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``preview_background`` (Texture2D):  [Read-Write] A preview background that you can use when designing the UI to get a sense of scale on the screen.  Use
  a texture with a screenshot of your game in it, for example if you were designing a HUD.
- ``priority`` (int32):  [Read-Write]
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stop_action`` (bool):  [Read-Write]
- ``tab_buttons`` (Map[int32, EarthTabButtonWidget]):  [Read-Write]
- ``tab_list_info`` (DataTable):  [Read-Write]
- ``tick_frequency`` (WidgetTickFrequency):  [Read-Write] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
  Uncheck this for performance reasons only
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_switcher`` (WidgetSwitcher):  [Read-Write]

<a id="unreal.EarthTabListWidget_MeshRegistry.layer_name"></a>

#### layer\_name

```python
@property
def layer_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EarthTabListWidget_MeshRegistry.layer_name"></a>

#### layer\_name

```python
@layer_name.setter
def layer_name(value: Name) -> None
```

<a id="unreal.EarthTabListWidget_MeshRegistry.button_class"></a>

#### button\_class

```python
@property
def button_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.EarthTabListWidget_MeshRegistry.button_class"></a>

#### button\_class

```python
@button_class.setter
def button_class(value: Class) -> None
```

<a id="unreal.EarthTabListWidget_MeshRegistry.command_class"></a>

#### command\_class

```python
@property
def command_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.EarthTabListWidget_MeshRegistry.command_class"></a>

#### command\_class

```python
@command_class.setter
def command_class(value: Class) -> None
```

<a id="unreal.EarthTabListWidget_MeshRegistry.refresh_button_textures"></a>

#### refresh\_button\_textures

```python
def refresh_button_textures() -> None
```

x.refresh_button_textures() -> None
Refresh Button Textures

<a id="unreal.EarthTabListWidget_MeshRegistry.refresh_buttons"></a>

#### refresh\_buttons

```python
def refresh_buttons() -> None
```

x.refresh_buttons() -> None
Refresh Buttons

<a id="unreal.EarthAnimatedTexture2D"></a>