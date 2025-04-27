## MovieGraphSetStartEndConsoleCommandsNode Objects

```python
class MovieGraphSetStartEndConsoleCommandsNode(MovieGraphSettingNode)
```

A node which can set console commands to run at the start and end of a render.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSetStartEndConsoleCommandsNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``console_commands`` (MovieGraphStartEndConsoleCommands):  [Read-Only]
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_console_commands`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphSetStartEndConsoleCommandsNode.override_console_commands"></a>

#### override_console_commands

```python
@property
def override_console_commands() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphSetStartEndConsoleCommandsNode.override_console_commands"></a>

#### override_console_commands

```python
@override_console_commands.setter
def override_console_commands(value: bool) -> None
```

<a id="unreal.MovieGraphSetStartEndConsoleCommandsNode.console_commands"></a>

#### console_commands

```python
@property
def console_commands() -> MovieGraphStartEndConsoleCommands
```

(MovieGraphStartEndConsoleCommands):  [Read-Only]

<a id="unreal.MovieGraphShowFlags"></a>