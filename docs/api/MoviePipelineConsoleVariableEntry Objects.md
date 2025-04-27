## MoviePipelineConsoleVariableEntry Objects

```python
class MoviePipelineConsoleVariableEntry(StructBase)
```

Represents a console variable override that can be enabled/disabled.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write] Enable state. If disabled, this cvar entry will be ignored when resolving the final value of the cvar.
- ``name`` (str):  [Read-Write] The name of the console variable.
- ``value`` (float):  [Read-Write] The value of the console variable.

<a id="unreal.MoviePipelineConsoleVariableEntry.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             value: float = 0.000000,
             is_enabled: bool = False) -> None
```

<a id="unreal.MoviePipelineConsoleVariableEntry.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Only] The name of the console variable.

<a id="unreal.MoviePipelineConsoleVariableEntry.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Only] The value of the console variable.

<a id="unreal.MoviePipelineConsoleVariableEntry.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Only] Enable state. If disabled, this cvar entry will be ignored when resolving the final value of the cvar.

<a id="unreal.MoviePipelineSegmentWorkMetrics"></a>