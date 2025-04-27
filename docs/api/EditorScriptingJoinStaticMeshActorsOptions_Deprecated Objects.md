## EditorScriptingJoinStaticMeshActorsOptions_Deprecated Objects

```python
class EditorScriptingJoinStaticMeshActorsOptions_Deprecated(StructBase)
```

Editor Scripting Join Static Mesh Actors Options Deprecated

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorLevelLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``destroy_source_actors`` (bool):  [Read-Write] Destroy the provided Actors after the operation.
- ``new_actor_label`` (str):  [Read-Write] Name of the new spawned Actor to replace the provided Actors.
- ``rename_components_from_source`` (bool):  [Read-Write] Rename StaticMeshComponents based on source Actor's name.

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.__init__"></a>

#### __init__

```python
def __init__(destroy_source_actors: bool = False,
             new_actor_label: str = "",
             rename_components_from_source: bool = False) -> None
```

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.destroy_source_actors"></a>

#### destroy_source_actors

```python
@property
def destroy_source_actors() -> bool
```

(bool):  [Read-Write] Destroy the provided Actors after the operation.

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.destroy_source_actors"></a>

#### destroy_source_actors

```python
@destroy_source_actors.setter
def destroy_source_actors(value: bool) -> None
```

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.new_actor_label"></a>

#### new_actor_label

```python
@property
def new_actor_label() -> str
```

(str):  [Read-Write] Name of the new spawned Actor to replace the provided Actors.

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.new_actor_label"></a>

#### new_actor_label

```python
@new_actor_label.setter
def new_actor_label(value: str) -> None
```

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.rename_components_from_source"></a>

#### rename_components_from_source

```python
@property
def rename_components_from_source() -> bool
```

(bool):  [Read-Write] Rename StaticMeshComponents based on source Actor's name.

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.rename_components_from_source"></a>

#### rename_components_from_source

```python
@rename_components_from_source.setter
def rename_components_from_source(value: bool) -> None
```

<a id="unreal.EditorScriptingMergeStaticMeshActorsOptions_Deprecated"></a>