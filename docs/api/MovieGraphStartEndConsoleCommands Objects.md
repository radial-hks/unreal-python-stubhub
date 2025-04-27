## MovieGraphStartEndConsoleCommands Objects

```python
class MovieGraphStartEndConsoleCommands(Object)
```

Console commands that can execute within the UMovieGraphSetStartEndConsoleCommandsNode.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSetStartEndConsoleCommandsNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_end_commands`` (Array[str]):  [Read-Write] Console commands to execute when this shot finishes rendering. Used to restore changes made by Add Console Commands.
- ``add_start_commands`` (Array[str]):  [Read-Write] Console commands to execute when this shot starts rendering. If the command(s) need to be undone after the shot finishes rendering, add a
  matching entry to Add End Commands.
- ``remove_end_commands`` (Array[str]):  [Read-Write] End commands that should be removed from upstream nodes. Commands entered here must be an exact match to upstream command(s) in order to be removed.
- ``remove_start_commands`` (Array[str]):  [Read-Write] Start commands that should be removed from upstream nodes. Commands entered here must be an exact match to upstream command(s) in order to be removed.

<a id="unreal.MovieGraphStartEndConsoleCommands.add_start_commands"></a>

#### add_start_commands

```python
@property
def add_start_commands() -> Array[str]
```

(Array[str]):  [Read-Write] Console commands to execute when this shot starts rendering. If the command(s) need to be undone after the shot finishes rendering, add a
matching entry to Add End Commands.

<a id="unreal.MovieGraphStartEndConsoleCommands.add_start_commands"></a>

#### add_start_commands

```python
@add_start_commands.setter
def add_start_commands(value: Array[str]) -> None
```

<a id="unreal.MovieGraphStartEndConsoleCommands.add_end_commands"></a>

#### add_end_commands

```python
@property
def add_end_commands() -> Array[str]
```

(Array[str]):  [Read-Write] Console commands to execute when this shot finishes rendering. Used to restore changes made by Add Console Commands.

<a id="unreal.MovieGraphStartEndConsoleCommands.add_end_commands"></a>

#### add_end_commands

```python
@add_end_commands.setter
def add_end_commands(value: Array[str]) -> None
```

<a id="unreal.MovieGraphStartEndConsoleCommands.remove_start_commands"></a>

#### remove_start_commands

```python
@property
def remove_start_commands() -> Array[str]
```

(Array[str]):  [Read-Write] Start commands that should be removed from upstream nodes. Commands entered here must be an exact match to upstream command(s) in order to be removed.

<a id="unreal.MovieGraphStartEndConsoleCommands.remove_start_commands"></a>

#### remove_start_commands

```python
@remove_start_commands.setter
def remove_start_commands(value: Array[str]) -> None
```

<a id="unreal.MovieGraphStartEndConsoleCommands.remove_end_commands"></a>

#### remove_end_commands

```python
@property
def remove_end_commands() -> Array[str]
```

(Array[str]):  [Read-Write] End commands that should be removed from upstream nodes. Commands entered here must be an exact match to upstream command(s) in order to be removed.

<a id="unreal.MovieGraphStartEndConsoleCommands.remove_end_commands"></a>

#### remove_end_commands

```python
@remove_end_commands.setter
def remove_end_commands(value: Array[str]) -> None
```

<a id="unreal.MovieGraphSetStartEndConsoleCommandsNode"></a>