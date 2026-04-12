## AesEditorUISubsystem Objects

```python
class AesEditorUISubsystem(WorldSubsystem)
```

Aes Editor UISubsystem

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorUI
- **File**: AesEditorUISubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_editor_main_ui`` (UserWidget):  [Read-Write]
- ``aes_editor_ui_hide_event`` (AesEditorUIHideEvent):  [Read-Write]
- ``aes_editor_ui_show_event`` (AesEditorUIShowEvent):  [Read-Write]
- ``aes_probe_ui`` (UserWidget):  [Read-Write]

<a id="unreal.AesEditorUISubsystem.aes_editor_ui_show_event"></a>

#### aes\_editor\_ui\_show\_event

```python
@property
def aes_editor_ui_show_event() -> AesEditorUIShowEvent
```

(AesEditorUIShowEvent):  [Read-Write]

<a id="unreal.AesEditorUISubsystem.aes_editor_ui_show_event"></a>

#### aes\_editor\_ui\_show\_event

```python
@aes_editor_ui_show_event.setter
def aes_editor_ui_show_event(value: AesEditorUIShowEvent) -> None
```

<a id="unreal.AesEditorUISubsystem.aes_editor_ui_hide_event"></a>

#### aes\_editor\_ui\_hide\_event

```python
@property
def aes_editor_ui_hide_event() -> AesEditorUIHideEvent
```

(AesEditorUIHideEvent):  [Read-Write]

<a id="unreal.AesEditorUISubsystem.aes_editor_ui_hide_event"></a>

#### aes\_editor\_ui\_hide\_event

```python
@aes_editor_ui_hide_event.setter
def aes_editor_ui_hide_event(value: AesEditorUIHideEvent) -> None
```

<a id="unreal.AesEditorUISubsystem.aes_editor_main_ui"></a>

#### aes\_editor\_main\_ui

```python
@property
def aes_editor_main_ui() -> UserWidget
```

(UserWidget):  [Read-Only]

<a id="unreal.AesEditorUISubsystem.aes_probe_ui"></a>

#### aes\_probe\_ui

```python
@property
def aes_probe_ui() -> UserWidget
```

(UserWidget):  [Read-Only]

<a id="unreal.AesEditorUISubsystem.set_aes_editor_main_ui_enabled"></a>

#### set\_aes\_editor\_main\_ui\_enabled

```python
def set_aes_editor_main_ui_enabled(enabled: bool) -> None
```

x.set_aes_editor_main_ui_enabled(enabled) -> None
Set Aes Editor Main UIEnabled

Args:
    enabled (bool):

<a id="unreal.AesEditorUISubsystem.open_ui"></a>

#### open\_ui

```python
def open_ui() -> None
```

x.open_ui() -> None
Open UI

<a id="unreal.AesEditorUISubsystem.open_probe_ui"></a>

#### open\_probe\_ui

```python
def open_probe_ui() -> None
```

x.open_probe_ui() -> None
Open Probe UI

<a id="unreal.AesEditorUISubsystem.is_aes_editor_main_ui_enabled"></a>

#### is\_aes\_editor\_main\_ui\_enabled

```python
def is_aes_editor_main_ui_enabled() -> bool
```

x.is_aes_editor_main_ui_enabled() -> bool
Is Aes Editor Main UIEnabled

Returns:
    bool:

<a id="unreal.AesEditorUISubsystem.get_asset_tooltip_texture"></a>

#### get\_asset\_tooltip\_texture

```python
def get_asset_tooltip_texture(guid: str) -> Texture2D
```

x.get_asset_tooltip_texture(guid) -> Texture2D
Get Asset Tooltip Texture

Args:
    guid (str): 

Returns:
    Texture2D:

<a id="unreal.AesEditorUISubsystem.enter_free_mode"></a>

#### enter\_free\_mode

```python
def enter_free_mode() -> None
```

x.enter_free_mode() -> None
Enter Free Mode

<a id="unreal.AesEditorUISubsystem.close_ui"></a>

#### close\_ui

```python
def close_ui() -> None
```

x.close_ui() -> None
Close UI

<a id="unreal.AesEditorWindowWidget"></a>