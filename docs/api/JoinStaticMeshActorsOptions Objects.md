## JoinStaticMeshActorsOptions Objects

```python
class JoinStaticMeshActorsOptions(StructBase)
```

Join Static Mesh Actors Options

**C++ Source:**

- **Module**: StaticMeshEditor
- **File**: StaticMeshEditorSubsystemHelpers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``destroy_source_actors`` (bool):  [Read-Write] Destroy the provided Actors after the operation.
- ``new_actor_label`` (str):  [Read-Write] Name of the new spawned Actor to replace the provided Actors.
- ``rename_components_from_source`` (bool):  [Read-Write] Rename StaticMeshComponents based on source Actor's name.

<a id="unreal.JoinStaticMeshActorsOptions.__init__"></a>

#### __init__

```python
def __init__(destroy_source_actors: bool = False,
             new_actor_label: str = "",
             rename_components_from_source: bool = False) -> None
```

<a id="unreal.JoinStaticMeshActorsOptions.destroy_source_actors"></a>

#### destroy_source_actors

```python
@property
def destroy_source_actors() -> bool
```

(bool):  [Read-Write] Destroy the provided Actors after the operation.

<a id="unreal.JoinStaticMeshActorsOptions.destroy_source_actors"></a>

#### destroy_source_actors

```python
@destroy_source_actors.setter
def destroy_source_actors(value: bool) -> None
```

<a id="unreal.JoinStaticMeshActorsOptions.new_actor_label"></a>

#### new_actor_label

```python
@property
def new_actor_label() -> str
```

(str):  [Read-Write] Name of the new spawned Actor to replace the provided Actors.

<a id="unreal.JoinStaticMeshActorsOptions.new_actor_label"></a>

#### new_actor_label

```python
@new_actor_label.setter
def new_actor_label(value: str) -> None
```

<a id="unreal.JoinStaticMeshActorsOptions.rename_components_from_source"></a>

#### rename_components_from_source

```python
@property
def rename_components_from_source() -> bool
```

(bool):  [Read-Write] Rename StaticMeshComponents based on source Actor's name.

<a id="unreal.JoinStaticMeshActorsOptions.rename_components_from_source"></a>

#### rename_components_from_source

```python
@rename_components_from_source.setter
def rename_components_from_source(value: bool) -> None
```

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions"></a>