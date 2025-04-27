## MovieGraphNamedResolution Objects

```python
class MovieGraphNamedResolution(StructBase)
```

Holds information about a screen resolution to be used for rendering.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphNamedResolution.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write] The description text for this screen resolution.
- ``profile_name`` (Name):  [Read-Write] The name of the resolution this links to
- ``resolution`` (IntPoint):  [Read-Write] The screen resolution (in pixels).

<a id="unreal.MovieGraphNamedResolution.__init__"></a>

#### __init__

```python
def __init__(profile_name: Name = "None",
             resolution: IntPoint = [0, 0],
             description: str = "") -> None
```

<a id="unreal.MovieGraphNamedResolution.profile_name"></a>

#### profile_name

```python
@property
def profile_name() -> Name
```

(Name):  [Read-Write] The name of the resolution this links to

<a id="unreal.MovieGraphNamedResolution.profile_name"></a>

#### profile_name

```python
@profile_name.setter
def profile_name(value: Name) -> None
```

<a id="unreal.MovieGraphNamedResolution.resolution"></a>

#### resolution

```python
@property
def resolution() -> IntPoint
```

(IntPoint):  [Read-Write] The screen resolution (in pixels).

<a id="unreal.MovieGraphNamedResolution.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: IntPoint) -> None
```

<a id="unreal.MovieGraphNamedResolution.description"></a>

#### description

```python
@property
def description() -> str
```

(str):  [Read-Write] The description text for this screen resolution.

<a id="unreal.MovieGraphNamedResolution.description"></a>

#### description

```python
@description.setter
def description(value: str) -> None
```

<a id="unreal.MovieGraphPropertyInfo"></a>