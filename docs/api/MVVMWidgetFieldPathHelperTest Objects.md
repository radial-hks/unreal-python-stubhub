## MVVMWidgetFieldPathHelperTest Objects

```python
class MVVMWidgetFieldPathHelperTest(UserWidget)
```

MVVMWidget Field Path Helper Test

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelEditor
- **File**: MVVMFieldPathHelperTest.h

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
- ``color_and_opacity`` (LinearColor):  [Read-Write] The color and opacity of this widget.  Tints all child widgets.
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
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_visibility_changed`` (OnVisibilityChangedEvent):  [Read-Write] Called when the visibility has changed
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The padding area around the content.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``preview_background`` (Texture2D):  [Read-Write] A preview background that you can use when designing the UI to get a sense of scale on the screen.  Use
  a texture with a screenshot of your game in it, for example if you were designing a HUD.
- ``priority`` (int32):  [Read-Write]
- ``property_int_notify`` (int32):  [Read-Write]
- ``property_int_with_bp_getter_setter`` (int32):  [Read-Write]
- ``property_int_with_getter_setter_and_bp`` (int32):  [Read-Write]
- ``property_object_notify`` (MVVMObjectFieldPathHelperTest):  [Read-Write]
- ``property_object_with_bp_getter_setter`` (MVVMObjectFieldPathHelperTest):  [Read-Write]
- ``property_object_with_getter_setter_and_bp`` (MVVMObjectFieldPathHelperTest):  [Read-Write]
- ``property_struct_notify`` (MVVMStructFieldPathHelperTest):  [Read-Write]
- ``property_struct_with_bp_getter_setter`` (MVVMStructFieldPathHelperTest):  [Read-Write]
- ``property_struct_with_getter_setter_and_bp`` (MVVMStructFieldPathHelperTest):  [Read-Write]
- ``property_vector_notify`` (Vector):  [Read-Write]
- ``property_vector_with_bp_getter_setter`` (Vector):  [Read-Write]
- ``property_vector_with_getter_setter_and_bp`` (Vector):  [Read-Write]
- ``property_view_model_notify`` (MVVMViewModelFieldPathHelperTest):  [Read-Write]
- ``property_view_model_with_bp_getter_setter`` (MVVMViewModelFieldPathHelperTest):  [Read-Write]
- ``property_view_model_with_getter_setter_and_bp`` (MVVMViewModelFieldPathHelperTest):  [Read-Write]
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stop_action`` (bool):  [Read-Write]
- ``tick_frequency`` (WidgetTickFrequency):  [Read-Write] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
  Uncheck this for performance reasons only
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_int_with_getter_setter_and_bp"></a>

#### property_int_with_getter_setter_and_bp

```python
@property
def property_int_with_getter_setter_and_bp() -> int
```

(int32):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_int_with_getter_setter_and_bp"></a>

#### property_int_with_getter_setter_and_bp

```python
@property_int_with_getter_setter_and_bp.setter
def property_int_with_getter_setter_and_bp(value: int) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_int_with_bp_getter_setter"></a>

#### property_int_with_bp_getter_setter

```python
@property
def property_int_with_bp_getter_setter() -> int
```

(int32):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_int_with_bp_getter_setter"></a>

#### property_int_with_bp_getter_setter

```python
@property_int_with_bp_getter_setter.setter
def property_int_with_bp_getter_setter(value: int) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_int_notify"></a>

#### property_int_notify

```python
@property
def property_int_notify() -> int
```

(int32):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_int_notify"></a>

#### property_int_notify

```python
@property_int_notify.setter
def property_int_notify(value: int) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_vector_with_getter_setter_and_bp"></a>

#### property_vector_with_getter_setter_and_bp

```python
@property
def property_vector_with_getter_setter_and_bp() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_vector_with_getter_setter_and_bp"></a>

#### property_vector_with_getter_setter_and_bp

```python
@property_vector_with_getter_setter_and_bp.setter
def property_vector_with_getter_setter_and_bp(value: Vector) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_vector_with_bp_getter_setter"></a>

#### property_vector_with_bp_getter_setter

```python
@property
def property_vector_with_bp_getter_setter() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_vector_with_bp_getter_setter"></a>

#### property_vector_with_bp_getter_setter

```python
@property_vector_with_bp_getter_setter.setter
def property_vector_with_bp_getter_setter(value: Vector) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_vector_notify"></a>

#### property_vector_notify

```python
@property
def property_vector_notify() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_vector_notify"></a>

#### property_vector_notify

```python
@property_vector_notify.setter
def property_vector_notify(value: Vector) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_struct_with_getter_setter_and_bp"></a>

#### property_struct_with_getter_setter_and_bp

```python
@property
def property_struct_with_getter_setter_and_bp(
) -> MVVMStructFieldPathHelperTest
```

(MVVMStructFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_struct_with_getter_setter_and_bp"></a>

#### property_struct_with_getter_setter_and_bp

```python
@property_struct_with_getter_setter_and_bp.setter
def property_struct_with_getter_setter_and_bp(
        value: MVVMStructFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_struct_with_bp_getter_setter"></a>

#### property_struct_with_bp_getter_setter

```python
@property
def property_struct_with_bp_getter_setter() -> MVVMStructFieldPathHelperTest
```

(MVVMStructFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_struct_with_bp_getter_setter"></a>

#### property_struct_with_bp_getter_setter

```python
@property_struct_with_bp_getter_setter.setter
def property_struct_with_bp_getter_setter(
        value: MVVMStructFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_struct_notify"></a>

#### property_struct_notify

```python
@property
def property_struct_notify() -> MVVMStructFieldPathHelperTest
```

(MVVMStructFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_struct_notify"></a>

#### property_struct_notify

```python
@property_struct_notify.setter
def property_struct_notify(value: MVVMStructFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_object_with_getter_setter_and_bp"></a>

#### property_object_with_getter_setter_and_bp

```python
@property
def property_object_with_getter_setter_and_bp(
) -> MVVMObjectFieldPathHelperTest
```

(MVVMObjectFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_object_with_getter_setter_and_bp"></a>

#### property_object_with_getter_setter_and_bp

```python
@property_object_with_getter_setter_and_bp.setter
def property_object_with_getter_setter_and_bp(
        value: MVVMObjectFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_object_with_bp_getter_setter"></a>

#### property_object_with_bp_getter_setter

```python
@property
def property_object_with_bp_getter_setter() -> MVVMObjectFieldPathHelperTest
```

(MVVMObjectFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_object_with_bp_getter_setter"></a>

#### property_object_with_bp_getter_setter

```python
@property_object_with_bp_getter_setter.setter
def property_object_with_bp_getter_setter(
        value: MVVMObjectFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_object_notify"></a>

#### property_object_notify

```python
@property
def property_object_notify() -> MVVMObjectFieldPathHelperTest
```

(MVVMObjectFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_object_notify"></a>

#### property_object_notify

```python
@property_object_notify.setter
def property_object_notify(value: MVVMObjectFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_view_model_with_getter_setter_and_bp"></a>

#### property_view_model_with_getter_setter_and_bp

```python
@property
def property_view_model_with_getter_setter_and_bp(
) -> MVVMViewModelFieldPathHelperTest
```

(MVVMViewModelFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_view_model_with_getter_setter_and_bp"></a>

#### property_view_model_with_getter_setter_and_bp

```python
@property_view_model_with_getter_setter_and_bp.setter
def property_view_model_with_getter_setter_and_bp(
        value: MVVMViewModelFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_view_model_with_bp_getter_setter"></a>

#### property_view_model_with_bp_getter_setter

```python
@property
def property_view_model_with_bp_getter_setter(
) -> MVVMViewModelFieldPathHelperTest
```

(MVVMViewModelFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_view_model_with_bp_getter_setter"></a>

#### property_view_model_with_bp_getter_setter

```python
@property_view_model_with_bp_getter_setter.setter
def property_view_model_with_bp_getter_setter(
        value: MVVMViewModelFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_view_model_notify"></a>

#### property_view_model_notify

```python
@property
def property_view_model_notify() -> MVVMViewModelFieldPathHelperTest
```

(MVVMViewModelFieldPathHelperTest):  [Read-Write]

<a id="unreal.MVVMWidgetFieldPathHelperTest.property_view_model_notify"></a>

#### property_view_model_notify

```python
@property_view_model_notify.setter
def property_view_model_notify(
        value: MVVMViewModelFieldPathHelperTest) -> None
```

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_view_model_with_getter_setter_and_bp"></a>

#### set_property_view_model_with_getter_setter_and_bp

```python
def set_property_view_model_with_getter_setter_and_bp(
        value: MVVMViewModelFieldPathHelperTest) -> None
```

x.set_property_view_model_with_getter_setter_and_bp(value) -> None
Set Property View Model with Getter Setter and BP

Args:
    value (MVVMViewModelFieldPathHelperTest):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_view_model_with_bp_getter_setter"></a>

#### set_property_view_model_with_bp_getter_setter

```python
def set_property_view_model_with_bp_getter_setter(
        value: MVVMViewModelFieldPathHelperTest) -> None
```

x.set_property_view_model_with_bp_getter_setter(value) -> None
Set Property View Model with BPGetter Setter

Args:
    value (MVVMViewModelFieldPathHelperTest):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_vector_with_getter_setter_and_bp"></a>

#### set_property_vector_with_getter_setter_and_bp

```python
def set_property_vector_with_getter_setter_and_bp(value: Vector) -> None
```

x.set_property_vector_with_getter_setter_and_bp(value) -> None
Set Property Vector with Getter Setter and BP

Args:
    value (Vector):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_vector_with_bp_getter_setter"></a>

#### set_property_vector_with_bp_getter_setter

```python
def set_property_vector_with_bp_getter_setter(value: Vector) -> None
```

x.set_property_vector_with_bp_getter_setter(value) -> None
Set Property Vector with BPGetter Setter

Args:
    value (Vector):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_struct_with_getter_setter_and_bp"></a>

#### set_property_struct_with_getter_setter_and_bp

```python
def set_property_struct_with_getter_setter_and_bp(
        value: MVVMStructFieldPathHelperTest) -> None
```

x.set_property_struct_with_getter_setter_and_bp(value) -> None
Set Property Struct with Getter Setter and BP

Args:
    value (MVVMStructFieldPathHelperTest):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_struct_with_bp_getter_setter"></a>

#### set_property_struct_with_bp_getter_setter

```python
def set_property_struct_with_bp_getter_setter(
        value: MVVMStructFieldPathHelperTest) -> None
```

x.set_property_struct_with_bp_getter_setter(value) -> None
Set Property Struct with BPGetter Setter

Args:
    value (MVVMStructFieldPathHelperTest):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_object_with_getter_setter_and_bp"></a>

#### set_property_object_with_getter_setter_and_bp

```python
def set_property_object_with_getter_setter_and_bp(
        value: MVVMObjectFieldPathHelperTest) -> None
```

x.set_property_object_with_getter_setter_and_bp(value) -> None
Set Property Object with Getter Setter and BP

Args:
    value (MVVMObjectFieldPathHelperTest):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_object_with_bp_getter_setter"></a>

#### set_property_object_with_bp_getter_setter

```python
def set_property_object_with_bp_getter_setter(
        value: MVVMObjectFieldPathHelperTest) -> None
```

x.set_property_object_with_bp_getter_setter(value) -> None
Set Property Object with BPGetter Setter

Args:
    value (MVVMObjectFieldPathHelperTest):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_int_with_getter_setter_and_bp"></a>

#### set_property_int_with_getter_setter_and_bp

```python
def set_property_int_with_getter_setter_and_bp(value: int) -> None
```

x.set_property_int_with_getter_setter_and_bp(value) -> None
Set Property Int with Getter Setter and BP

Args:
    value (int32):

<a id="unreal.MVVMWidgetFieldPathHelperTest.set_property_int_with_bp_getter_setter"></a>

#### set_property_int_with_bp_getter_setter

```python
def set_property_int_with_bp_getter_setter(value: int) -> None
```

x.set_property_int_with_bp_getter_setter(value) -> None
Set Property Int with BPGetter Setter

Args:
    value (int32):

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_view_model_with_getter_setter_and_bp"></a>

#### get_property_view_model_with_getter_setter_and_bp

```python
def get_property_view_model_with_getter_setter_and_bp(
) -> MVVMViewModelFieldPathHelperTest
```

x.get_property_view_model_with_getter_setter_and_bp() -> MVVMViewModelFieldPathHelperTest
Get Property View Model with Getter Setter and BP

Returns:
    MVVMViewModelFieldPathHelperTest:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_view_model_with_bp_getter_setter"></a>

#### get_property_view_model_with_bp_getter_setter

```python
def get_property_view_model_with_bp_getter_setter(
) -> MVVMViewModelFieldPathHelperTest
```

x.get_property_view_model_with_bp_getter_setter() -> MVVMViewModelFieldPathHelperTest
Get Property View Model with BPGetter Setter

Returns:
    MVVMViewModelFieldPathHelperTest:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_vector_with_getter_setter_and_bp"></a>

#### get_property_vector_with_getter_setter_and_bp

```python
def get_property_vector_with_getter_setter_and_bp() -> Vector
```

x.get_property_vector_with_getter_setter_and_bp() -> Vector
Get Property Vector with Getter Setter and BP

Returns:
    Vector:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_vector_with_bp_getter_setter"></a>

#### get_property_vector_with_bp_getter_setter

```python
def get_property_vector_with_bp_getter_setter() -> Vector
```

x.get_property_vector_with_bp_getter_setter() -> Vector
Get Property Vector with BPGetter Setter

Returns:
    Vector:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_struct_with_getter_setter_and_bp"></a>

#### get_property_struct_with_getter_setter_and_bp

```python
def get_property_struct_with_getter_setter_and_bp(
) -> MVVMStructFieldPathHelperTest
```

x.get_property_struct_with_getter_setter_and_bp() -> MVVMStructFieldPathHelperTest
Get Property Struct with Getter Setter and BP

Returns:
    MVVMStructFieldPathHelperTest:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_struct_with_bp_getter_setter"></a>

#### get_property_struct_with_bp_getter_setter

```python
def get_property_struct_with_bp_getter_setter(
) -> MVVMStructFieldPathHelperTest
```

x.get_property_struct_with_bp_getter_setter() -> MVVMStructFieldPathHelperTest
Get Property Struct with BPGetter Setter

Returns:
    MVVMStructFieldPathHelperTest:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_object_with_getter_setter_and_bp"></a>

#### get_property_object_with_getter_setter_and_bp

```python
def get_property_object_with_getter_setter_and_bp(
) -> MVVMObjectFieldPathHelperTest
```

x.get_property_object_with_getter_setter_and_bp() -> MVVMObjectFieldPathHelperTest
Get Property Object with Getter Setter and BP

Returns:
    MVVMObjectFieldPathHelperTest:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_object_with_bp_getter_setter"></a>

#### get_property_object_with_bp_getter_setter

```python
def get_property_object_with_bp_getter_setter(
) -> MVVMObjectFieldPathHelperTest
```

x.get_property_object_with_bp_getter_setter() -> MVVMObjectFieldPathHelperTest
Get Property Object with BPGetter Setter

Returns:
    MVVMObjectFieldPathHelperTest:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_int_with_getter_setter_and_bp"></a>

#### get_property_int_with_getter_setter_and_bp

```python
def get_property_int_with_getter_setter_and_bp() -> int
```

x.get_property_int_with_getter_setter_and_bp() -> int32
Get Property Int with Getter Setter and BP

Returns:
    int32:

<a id="unreal.MVVMWidgetFieldPathHelperTest.get_property_int_with_bp_getter_setter"></a>

#### get_property_int_with_bp_getter_setter

```python
def get_property_int_with_bp_getter_setter() -> int
```

x.get_property_int_with_bp_getter_setter() -> int32
Get Property Int with BPGetter Setter

Returns:
    int32:

<a id="unreal.MVVMFieldValueChangedTest"></a>