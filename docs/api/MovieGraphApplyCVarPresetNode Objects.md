## MovieGraphApplyCVarPresetNode Objects

```python
class MovieGraphApplyCVarPresetNode(MovieGraphSettingNode)
```

A node which can apply a console variable preset.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphApplyCVarPresetNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``console_variable_preset`` (MovieSceneConsoleVariableTrackInterface):  [Read-Write] The console variable preset that should be applied.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_console_variable_preset`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphApplyCVarPresetNode.override_console_variable_preset"></a>

#### override_console_variable_preset

```python
@property
def override_console_variable_preset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphApplyCVarPresetNode.override_console_variable_preset"></a>

#### override_console_variable_preset

```python
@override_console_variable_preset.setter
def override_console_variable_preset(value: bool) -> None
```

<a id="unreal.MovieGraphApplyCVarPresetNode.console_variable_preset"></a>

#### console_variable_preset

```python
@property
def console_variable_preset() -> MovieSceneConsoleVariableTrackInterface
```

(MovieSceneConsoleVariableTrackInterface):  [Read-Write] The console variable preset that should be applied.

<a id="unreal.MovieGraphApplyCVarPresetNode.console_variable_preset"></a>

#### console_variable_preset

```python
@console_variable_preset.setter
def console_variable_preset(
        value: MovieSceneConsoleVariableTrackInterface) -> None
```

<a id="unreal.MovieGraphFileOutputNode"></a>