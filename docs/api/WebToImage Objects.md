## WebToImage Objects

```python
class WebToImage(Image)
```

Web to Image

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: WebToImage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``brush`` (SlateBrush):  [Read-Write] Image to draw
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (LinearColor):  [Read-Write] Color and opacity
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flip_for_right_to_left_flow_direction`` (bool):  [Read-Write] Flips the image if the localization's flow direction is RightToLeft
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_load_completed`` (OnLoadCompleted):  [Read-Write]
- ``on_load_started`` (OnLoadStarted):  [Read-Write]
- ``on_mouse_button_down_event`` (OnPointerEvent):  [Read-Write]
- ``on_screen_shot_completed`` (OnScreenShotCompleted):  [Read-Write]
- ``on_url_changed`` (OnUrlChanged):  [Read-Write] Called when the Url changes.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``screen_shot_delay_ms`` (int32):  [Read-Write]
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.WebToImage.on_url_changed"></a>

#### on\_url\_changed

```python
@property
def on_url_changed() -> OnUrlChanged
```

(OnUrlChanged):  [Read-Write] Called when the Url changes.

<a id="unreal.WebToImage.on_url_changed"></a>

#### on\_url\_changed

```python
@on_url_changed.setter
def on_url_changed(value: OnUrlChanged) -> None
```

<a id="unreal.WebToImage.on_load_started"></a>

#### on\_load\_started

```python
@property
def on_load_started() -> OnLoadStarted
```

(OnLoadStarted):  [Read-Write]

<a id="unreal.WebToImage.on_load_started"></a>

#### on\_load\_started

```python
@on_load_started.setter
def on_load_started(value: OnLoadStarted) -> None
```

<a id="unreal.WebToImage.on_load_completed"></a>

#### on\_load\_completed

```python
@property
def on_load_completed() -> OnLoadCompleted
```

(OnLoadCompleted):  [Read-Write]

<a id="unreal.WebToImage.on_load_completed"></a>

#### on\_load\_completed

```python
@on_load_completed.setter
def on_load_completed(value: OnLoadCompleted) -> None
```

<a id="unreal.WebToImage.on_screen_shot_completed"></a>

#### on\_screen\_shot\_completed

```python
@property
def on_screen_shot_completed() -> OnScreenShotCompleted
```

(OnScreenShotCompleted):  [Read-Write]

<a id="unreal.WebToImage.on_screen_shot_completed"></a>

#### on\_screen\_shot\_completed

```python
@on_screen_shot_completed.setter
def on_screen_shot_completed(value: OnScreenShotCompleted) -> None
```

<a id="unreal.WebToImage.set_screen_shot_delay"></a>

#### set\_screen\_shot\_delay

```python
def set_screen_shot_delay(delay_ms: int) -> None
```

x.set_screen_shot_delay(delay_ms) -> None
Set Screen Shot Delay

Args:
    delay_ms (int32):

<a id="unreal.WebToImage.open_browser"></a>

#### open\_browser

```python
def open_browser() -> None
```

x.open_browser() -> None
Open a new browser.

<a id="unreal.WebToImage.load_url"></a>

#### load\_url

```python
def load_url(url: str) -> None
```

x.load_url(url) -> None
Load Url

Args:
    url (str):

<a id="unreal.WebToImage.load_texture"></a>

#### load\_texture

```python
def load_texture(texture: Texture2DDynamic) -> None
```

x.load_texture(texture) -> None
Load Texture

Args:
    texture (Texture2DDynamic):

<a id="unreal.WebToImage.dettach"></a>

#### dettach

```python
def dettach() -> None
```

x.dettach() -> None
Dettach

<a id="unreal.WebToImage.create_texture2d_from_image_buffer"></a>

#### create\_texture2d\_from\_image\_buffer

```python
def create_texture2d_from_image_buffer(
        buffer: Array[int],
        width: int,
        height: int,
        alpha_threshold: int = 0) -> Texture2DDynamic
```

x.create_texture2d_from_image_buffer(buffer, width, height, alpha_threshold=0) -> Texture2DDynamic
Create Texture 2DFrom Image Buffer

Args:
    buffer (Array[uint8]): 
    width (int32): 
    height (int32): 
    alpha_threshold (uint8): 

Returns:
    Texture2DDynamic:

<a id="unreal.WebToImage.close_browser"></a>

#### close\_browser

```python
def close_browser(force: bool, block_till_closed: bool) -> None
```

x.close_browser(force, block_till_closed) -> None
Close the browser.

Args:
    force (bool): 
    block_till_closed (bool):

<a id="unreal.WebToImage.attach"></a>

#### attach

```python
def attach(browser: WebBrowser51) -> None
```

x.attach(browser) -> None
Attach

Args:
    browser (WebBrowser51):

<a id="unreal.WindowEntity"></a>