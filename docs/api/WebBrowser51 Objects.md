## WebBrowser51 Objects

```python
class WebBrowser51(Widget)
```

Web Browser 51

**C++ Source:**

- **Plugin**: WebUI51World
- **Module**: WebBrowser51
- **File**: WebBrowser51.h

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
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``initial_url`` (str):  [Read-Write] URL that the browser will initially navigate to. The URL should include the protocol, eg http://
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_screen_shot_mode`` (bool):  [Read-Write] Should the browser window support screenshot.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_before_popup`` (OnBeforePopup):  [Read-Write] Called when a popup is about to spawn.
- ``on_clicked`` (OnClicked):  [Read-Write] Called when the webbrowser is clicked
- ``on_console_message`` (OnConsoleMessage):  [Read-Write] Called when the browser has console spew to print
- ``on_double_clicked`` (OnClicked):  [Read-Write] Called when the webbrowser is clicked
- ``on_hovered`` (OnHovered):  [Read-Write] Called when the webbrowser is hovered
- ``on_java_script_event_bp`` (OnJavaScriptEvent_Bp):  [Read-Write]
- ``on_load_completed`` (OnLoadCompleted):  [Read-Write]
- ``on_load_started`` (OnLoadStarted):  [Read-Write]
- ``on_screen_shot_completed`` (OnScreenShotCompleted):  [Read-Write]
- ``on_unhovered`` (OnHovered):  [Read-Write] Called when the webbrowser is unhovered
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
- ``supports_hud`` (bool):  [Read-Write] Should the browser window support HUD.
- ``supports_transparency`` (bool):  [Read-Write] Should the browser window support transparency.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.WebBrowser51.on_url_changed"></a>

#### on\_url\_changed

```python
@property
def on_url_changed() -> OnUrlChanged
```

(OnUrlChanged):  [Read-Write] Called when the Url changes.

<a id="unreal.WebBrowser51.on_url_changed"></a>

#### on\_url\_changed

```python
@on_url_changed.setter
def on_url_changed(value: OnUrlChanged) -> None
```

<a id="unreal.WebBrowser51.on_before_popup"></a>

#### on\_before\_popup

```python
@property
def on_before_popup() -> OnBeforePopup
```

(OnBeforePopup):  [Read-Write] Called when a popup is about to spawn.

<a id="unreal.WebBrowser51.on_before_popup"></a>

#### on\_before\_popup

```python
@on_before_popup.setter
def on_before_popup(value: OnBeforePopup) -> None
```

<a id="unreal.WebBrowser51.on_console_message"></a>

#### on\_console\_message

```python
@property
def on_console_message() -> OnConsoleMessage
```

(OnConsoleMessage):  [Read-Write] Called when the browser has console spew to print

<a id="unreal.WebBrowser51.on_console_message"></a>

#### on\_console\_message

```python
@on_console_message.setter
def on_console_message(value: OnConsoleMessage) -> None
```

<a id="unreal.WebBrowser51.on_java_script_event_bp"></a>

#### on\_java\_script\_event\_bp

```python
@property
def on_java_script_event_bp() -> OnJavaScriptEvent_Bp
```

(OnJavaScriptEvent_Bp):  [Read-Write]

<a id="unreal.WebBrowser51.on_java_script_event_bp"></a>

#### on\_java\_script\_event\_bp

```python
@on_java_script_event_bp.setter
def on_java_script_event_bp(value: OnJavaScriptEvent_Bp) -> None
```

<a id="unreal.WebBrowser51.on_load_started"></a>

#### on\_load\_started

```python
@property
def on_load_started() -> OnLoadStarted
```

(OnLoadStarted):  [Read-Write]

<a id="unreal.WebBrowser51.on_load_started"></a>

#### on\_load\_started

```python
@on_load_started.setter
def on_load_started(value: OnLoadStarted) -> None
```

<a id="unreal.WebBrowser51.on_load_completed"></a>

#### on\_load\_completed

```python
@property
def on_load_completed() -> OnLoadCompleted
```

(OnLoadCompleted):  [Read-Write]

<a id="unreal.WebBrowser51.on_load_completed"></a>

#### on\_load\_completed

```python
@on_load_completed.setter
def on_load_completed(value: OnLoadCompleted) -> None
```

<a id="unreal.WebBrowser51.on_screen_shot_completed"></a>

#### on\_screen\_shot\_completed

```python
@property
def on_screen_shot_completed() -> OnScreenShotCompleted
```

(OnScreenShotCompleted):  [Read-Write]

<a id="unreal.WebBrowser51.on_screen_shot_completed"></a>

#### on\_screen\_shot\_completed

```python
@on_screen_shot_completed.setter
def on_screen_shot_completed(value: OnScreenShotCompleted) -> None
```

<a id="unreal.WebBrowser51.on_clicked"></a>

#### on\_clicked

```python
@property
def on_clicked() -> OnClicked
```

(OnClicked):  [Read-Write] Called when the webbrowser is clicked

<a id="unreal.WebBrowser51.on_clicked"></a>

#### on\_clicked

```python
@on_clicked.setter
def on_clicked(value: OnClicked) -> None
```

<a id="unreal.WebBrowser51.on_double_clicked"></a>

#### on\_double\_clicked

```python
@property
def on_double_clicked() -> OnClicked
```

(OnClicked):  [Read-Write] Called when the webbrowser is clicked

<a id="unreal.WebBrowser51.on_double_clicked"></a>

#### on\_double\_clicked

```python
@on_double_clicked.setter
def on_double_clicked(value: OnClicked) -> None
```

<a id="unreal.WebBrowser51.on_hovered"></a>

#### on\_hovered

```python
@property
def on_hovered() -> OnHovered
```

(OnHovered):  [Read-Write] Called when the webbrowser is hovered

<a id="unreal.WebBrowser51.on_hovered"></a>

#### on\_hovered

```python
@on_hovered.setter
def on_hovered(value: OnHovered) -> None
```

<a id="unreal.WebBrowser51.on_unhovered"></a>

#### on\_unhovered

```python
@property
def on_unhovered() -> OnHovered
```

(OnHovered):  [Read-Write] Called when the webbrowser is unhovered

<a id="unreal.WebBrowser51.on_unhovered"></a>

#### on\_unhovered

```python
@on_unhovered.setter
def on_unhovered(value: OnHovered) -> None
```

<a id="unreal.WebBrowser51.set_screen_shot_delay"></a>

#### set\_screen\_shot\_delay

```python
def set_screen_shot_delay(delay_ms: int) -> None
```

x.set_screen_shot_delay(delay_ms) -> None
Set Screen Shot Delay

Args:
    delay_ms (int32):

<a id="unreal.WebBrowser51.open_browser"></a>

#### open\_browser

```python
def open_browser() -> None
```

x.open_browser() -> None
Open a new browser.

<a id="unreal.WebBrowser51.load_url"></a>

#### load\_url

```python
def load_url(new_url: str) -> None
```

x.load_url(new_url) -> None
Load the specified URL

Args:
    new_url (str): New URL to load

<a id="unreal.WebBrowser51.load_string"></a>

#### load\_string

```python
def load_string(contents: str, dummy_url: str) -> None
```

x.load_string(contents, dummy_url) -> None
Load a string as data to create a web page

Args:
    contents (str): String to load
    dummy_url (str): Dummy URL for the page

<a id="unreal.WebBrowser51.is_browser_closed"></a>

#### is\_browser\_closed

```python
def is_browser_closed() -> bool
```

x.is_browser_closed() -> bool
whether the browser is closed.

Returns:
    bool:

<a id="unreal.WebBrowser51.invalidate_browser_view"></a>

#### invalidate\_browser\_view

```python
def invalidate_browser_view() -> None
```

x.invalidate_browser_view() -> None
Invalidate Browser View

<a id="unreal.WebBrowser51.init_browser_view_size"></a>

#### init\_browser\_view\_size

```python
def init_browser_view_size(size: Vector2D) -> None
```

x.init_browser_view_size(size) -> None
Init Browser View Size

Args:
    size (Vector2D):

<a id="unreal.WebBrowser51.get_url"></a>

#### get\_url

```python
def get_url() -> str
```

x.get_url() -> str
Gets the currently loaded URL.

Returns:
    str: The URL, or empty string if no document is loaded.

<a id="unreal.WebBrowser51.get_title_text"></a>

#### get\_title\_text

```python
def get_title_text() -> Text
```

x.get_title_text() -> Text
Get the current title of the web page

Returns:
    Text:

<a id="unreal.WebBrowser51.execute_javascript"></a>

#### execute\_javascript

```python
def execute_javascript(script_text: str) -> None
```

x.execute_javascript(script_text) -> None
Executes a JavaScript string in the context of the web page

Args:
    script_text (str): JavaScript string to execute

<a id="unreal.WebBrowser51.close_web_browser"></a>

#### close\_web\_browser

```python
def close_web_browser() -> None
```

x.close_web_browser() -> None
Close Web Browser

<a id="unreal.WebBrowser51.close_browser"></a>

#### close\_browser

```python
def close_browser(force: bool, block_till_closed: bool) -> None
```

x.close_browser(force, block_till_closed) -> None
Close the browser.

Args:
    force (bool): 
    block_till_closed (bool):

<a id="unreal.ComputeDataProvider"></a>