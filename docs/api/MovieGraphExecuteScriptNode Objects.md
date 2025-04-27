## MovieGraphExecuteScriptNode Objects

```python
class MovieGraphExecuteScriptNode(MovieGraphSettingNode)
```

This node allows users to run code before and after a movie graph is being executed. Example use cases
would be to run custom logic that overrides the output directory, or to trigger an event after a shot finishes.
These bits of script can be implemented in either C++, or in Python (as a UClass) because we don't serialize the
object and only create it at runtime during the render. See UMovieGraphScriptBase for details.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphExecuteScriptNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_script`` (bool):  [Read-Write]
- ``script`` (SoftClassPath):  [Read-Write] Which script should this node instantiate? The class will be instantiated when the job starts,
  and then different functions will be called on that instance throughout the life-time of the
  movie render. Scripts can be implemented in Python or C++, see MovieGraphExecuteScriptNode.h
  for more details.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphExecuteScriptNode.override_script"></a>

#### override_script

```python
@property
def override_script() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphExecuteScriptNode.override_script"></a>

#### override_script

```python
@override_script.setter
def override_script(value: bool) -> None
```

<a id="unreal.MovieGraphExecuteScriptNode.script"></a>

#### script

```python
@property
def script() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] Which script should this node instantiate? The class will be instantiated when the job starts,
and then different functions will be called on that instance throughout the life-time of the
movie render. Scripts can be implemented in Python or C++, see MovieGraphExecuteScriptNode.h
for more details.

<a id="unreal.MovieGraphExecuteScriptNode.script"></a>

#### script

```python
@script.setter
def script(value: SoftClassPath) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode"></a>