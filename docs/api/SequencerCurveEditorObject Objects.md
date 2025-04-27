## SequencerCurveEditorObject Objects

```python
class SequencerCurveEditorObject(Object)
```

* Class to hold sequencer curve editor functions

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScriptingEditor
- **File**: SequencerCurveEditorObject.h

<a id="unreal.SequencerCurveEditorObject.show_curve"></a>

#### show_curve

```python
def show_curve(channel: SequencerChannelProxy, show_curve: bool) -> None
```

x.show_curve(channel, show_curve) -> None
Show curve

Args:
    channel (SequencerChannelProxy): 
    show_curve (bool):

<a id="unreal.SequencerCurveEditorObject.set_random_color_for_channels"></a>

#### set_random_color_for_channels

```python
def set_random_color_for_channels(class_: Class,
                                  identifiers: Array[str]) -> None
```

x.set_random_color_for_channels(class_, identifiers) -> None
Set Random Colors for specified channels idendified by it's class and identifiers. This will be stored in editor user preferences.

Args:
    class_ (type(Class)): 
    identifiers (Array[str]):

<a id="unreal.SequencerCurveEditorObject.set_custom_color_for_channels"></a>

#### set_custom_color_for_channels

```python
def set_custom_color_for_channels(class_: Class, identifiers: Array[str],
                                  new_colors: Array[LinearColor]) -> None
```

x.set_custom_color_for_channels(class_, identifiers, new_colors) -> None
Set Custom Color for specified channels idendified by it's class and identifiers. This will be stored in editor user preferences.

Args:
    class_ (type(Class)): 
    identifiers (Array[str]): 
    new_colors (Array[LinearColor]):

<a id="unreal.SequencerCurveEditorObject.set_custom_color_for_channel"></a>

#### set_custom_color_for_channel

```python
def set_custom_color_for_channel(class_: Class, identifier: str,
                                 new_color: LinearColor) -> None
```

x.set_custom_color_for_channel(class_, identifier, new_color) -> None
Set Custom Color for specified channel idendified by it's class and identifier. This will be stored in editor user preferences.

Args:
    class_ (type(Class)): 
    identifier (str): 
    new_color (LinearColor):

<a id="unreal.SequencerCurveEditorObject.select_keys"></a>

#### select_keys

```python
def select_keys(channel: SequencerChannelProxy, indices: Array[int]) -> None
```

x.select_keys(channel, indices) -> None
Select keys

Args:
    channel (SequencerChannelProxy): 
    indices (Array[int32]):

<a id="unreal.SequencerCurveEditorObject.open_curve_editor"></a>

#### open_curve_editor

```python
def open_curve_editor() -> None
```

x.open_curve_editor() -> None
Open curve editor

<a id="unreal.SequencerCurveEditorObject.is_curve_shown"></a>

#### is_curve_shown

```python
def is_curve_shown(channel: SequencerChannelProxy) -> bool
```

x.is_curve_shown(channel) -> bool
Is the curve displayed

Args:
    channel (SequencerChannelProxy): 

Returns:
    bool:

<a id="unreal.SequencerCurveEditorObject.is_curve_editor_open"></a>

#### is_curve_editor_open

```python
def is_curve_editor_open() -> bool
```

x.is_curve_editor_open() -> bool
Is curve editor open

Returns:
    bool:

<a id="unreal.SequencerCurveEditorObject.has_custom_color_for_channel"></a>

#### has_custom_color_for_channel

```python
def has_custom_color_for_channel(class_: Class, identifier: str) -> bool
```

x.has_custom_color_for_channel(class_, identifier) -> bool
Get if a custom color for specified channel idendified by it's class and identifier exists

Args:
    class_ (type(Class)): 
    identifier (str): 

Returns:
    bool:

<a id="unreal.SequencerCurveEditorObject.get_selected_keys"></a>

#### get_selected_keys

```python
def get_selected_keys(channel_proxy: SequencerChannelProxy) -> Array[int]
```

x.get_selected_keys(channel_proxy) -> Array[int32]
Gets the selected keys with this channel

Args:
    channel_proxy (SequencerChannelProxy): 

Returns:
    Array[int32]:

<a id="unreal.SequencerCurveEditorObject.get_custom_color_for_channel"></a>

#### get_custom_color_for_channel

```python
def get_custom_color_for_channel(class_: Class,
                                 identifier: str) -> LinearColor
```

x.get_custom_color_for_channel(class_, identifier) -> LinearColor
Get custom color for specified channel idendified by it's class and identifier,if none exists will return white

Args:
    class_ (type(Class)): 
    identifier (str): 

Returns:
    LinearColor:

<a id="unreal.SequencerCurveEditorObject.get_channels_with_selected_keys"></a>

#### get_channels_with_selected_keys

```python
def get_channels_with_selected_keys() -> Array[SequencerChannelProxy]
```

x.get_channels_with_selected_keys() -> Array[SequencerChannelProxy]
Gets the channel with selected keys

Returns:
    Array[SequencerChannelProxy]:

<a id="unreal.SequencerCurveEditorObject.empty_selection"></a>

#### empty_selection

```python
def empty_selection() -> None
```

x.empty_selection() -> None
Empties the current selection.

<a id="unreal.SequencerCurveEditorObject.delete_color_for_channels"></a>

#### delete_color_for_channels

```python
def delete_color_for_channels(class_: Class) -> str
```

x.delete_color_for_channels(class_) -> str
Delete for specified channel idendified by it's class and identifier.

Args:
    class_ (type(Class)): 

Returns:
    str: 

    identifier (str):

<a id="unreal.SequencerCurveEditorObject.close_curve_editor"></a>

#### close_curve_editor

```python
def close_curve_editor() -> None
```

x.close_curve_editor() -> None
Close curve editor

<a id="unreal.SequencerCurveEditorObject.apply_filter"></a>

#### apply_filter

```python
def apply_filter(filter: CurveEditorFilterBase) -> None
```

x.apply_filter(filter) -> None
Apply Filter

Args:
    filter (CurveEditorFilterBase):

<a id="unreal.SequencerTools"></a>