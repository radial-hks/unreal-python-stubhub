## AvaEditorSettings Objects

```python
class AvaEditorSettings(DeveloperSettings)
```

Motion Design Editor Settings

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheEditor
- **File**: AvaEditorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_activate_motion_design_viewport`` (bool):  [Read-Write] Whether to automatically switch to the Motion Design viewport when the mode is activated
  or a Motion Design level is opened.
- ``auto_include_attached_actors_in_edit_actions`` (bool):  [Read-Write] Whether to Automatically Include the Attached Actors when performing Edit Actions such as Cut, Copy, Duplicate.
- ``camera_distance`` (float):  [Read-Write] * Distance from the camera that new actors are created via the toolbox or drag and drop.
  * Also sets the distance from the origin that new Camera Preview Viewport cameras are created.
- ``default_viewport_quality_settings`` (AvaViewportQualitySettings):  [Read-Write] Default viewport quality settings for all newly created Motion Design blueprints.
- ``enable_level_context_switching`` (bool):  [Read-Write] Whether to allow the Motion Design Interface to show the current selected level rather than fixed at the persistent level
- ``keep_relative_transform_when_grouping`` (bool):  [Read-Write] When Grouping Actors with a Null Actor, whether to keep the relative transform of these Actors
- ``viewport_quality_presets`` (Map[Name, AvaViewportQualitySettings]):  [Read-Write] Viewport quality settings user presets.

<a id="unreal.AvaEditorSettings.enable_level_context_switching"></a>

#### enable_level_context_switching

```python
@property
def enable_level_context_switching() -> bool
```

(bool):  [Read-Write] Whether to allow the Motion Design Interface to show the current selected level rather than fixed at the persistent level

<a id="unreal.AvaEditorSettings.enable_level_context_switching"></a>

#### enable_level_context_switching

```python
@enable_level_context_switching.setter
def enable_level_context_switching(value: bool) -> None
```

<a id="unreal.AvaEditorSettings.auto_include_attached_actors_in_edit_actions"></a>

#### auto_include_attached_actors_in_edit_actions

```python
@property
def auto_include_attached_actors_in_edit_actions() -> bool
```

(bool):  [Read-Write] Whether to Automatically Include the Attached Actors when performing Edit Actions such as Cut, Copy, Duplicate.

<a id="unreal.AvaEditorSettings.auto_include_attached_actors_in_edit_actions"></a>

#### auto_include_attached_actors_in_edit_actions

```python
@auto_include_attached_actors_in_edit_actions.setter
def auto_include_attached_actors_in_edit_actions(value: bool) -> None
```

<a id="unreal.AvaEditorSettings.keep_relative_transform_when_grouping"></a>

#### keep_relative_transform_when_grouping

```python
@property
def keep_relative_transform_when_grouping() -> bool
```

(bool):  [Read-Write] When Grouping Actors with a Null Actor, whether to keep the relative transform of these Actors

<a id="unreal.AvaEditorSettings.keep_relative_transform_when_grouping"></a>

#### keep_relative_transform_when_grouping

```python
@keep_relative_transform_when_grouping.setter
def keep_relative_transform_when_grouping(value: bool) -> None
```

<a id="unreal.AvaEditorSettings.camera_distance"></a>

#### camera_distance

```python
@property
def camera_distance() -> float
```

(float):  [Read-Write] * Distance from the camera that new actors are created via the toolbox or drag and drop.
* Also sets the distance from the origin that new Camera Preview Viewport cameras are created.

<a id="unreal.AvaEditorSettings.camera_distance"></a>

#### camera_distance

```python
@camera_distance.setter
def camera_distance(value: float) -> None
```

<a id="unreal.AvaEditorSettings.auto_activate_motion_design_viewport"></a>

#### auto_activate_motion_design_viewport

```python
@property
def auto_activate_motion_design_viewport() -> bool
```

(bool):  [Read-Write] Whether to automatically switch to the Motion Design viewport when the mode is activated
or a Motion Design level is opened.

<a id="unreal.AvaEditorSettings.auto_activate_motion_design_viewport"></a>

#### auto_activate_motion_design_viewport

```python
@auto_activate_motion_design_viewport.setter
def auto_activate_motion_design_viewport(value: bool) -> None
```

<a id="unreal.AvaEditorSettings.default_viewport_quality_settings"></a>

#### default_viewport_quality_settings

```python
@property
def default_viewport_quality_settings() -> AvaViewportQualitySettings
```

(AvaViewportQualitySettings):  [Read-Write] Default viewport quality settings for all newly created Motion Design blueprints.

<a id="unreal.AvaEditorSettings.default_viewport_quality_settings"></a>

#### default_viewport_quality_settings

```python
@default_viewport_quality_settings.setter
def default_viewport_quality_settings(
        value: AvaViewportQualitySettings) -> None
```

<a id="unreal.AvaEditorSettings.viewport_quality_presets"></a>

#### viewport_quality_presets

```python
@property
def viewport_quality_presets() -> Map[Name, AvaViewportQualitySettings]
```

(Map[Name, AvaViewportQualitySettings]):  [Read-Write] Viewport quality settings user presets.

<a id="unreal.AvaEditorSettings.viewport_quality_presets"></a>

#### viewport_quality_presets

```python
@viewport_quality_presets.setter
def viewport_quality_presets(
        value: Map[Name, AvaViewportQualitySettings]) -> None
```

<a id="unreal.AvalancheEditorSettings"></a>