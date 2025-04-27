## MergeStaticMeshActorsOptions Objects

```python
class MergeStaticMeshActorsOptions(JoinStaticMeshActorsOptions)
```

Merge Static Mesh Actors Options

**C++ Source:**

- **Module**: StaticMeshEditor
- **File**: StaticMeshEditorSubsystemHelpers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_package_name`` (str):  [Read-Write] The package path you want to save to. ie: /Game/MyFolder
- ``destroy_source_actors`` (bool):  [Read-Write] Destroy the provided Actors after the operation.
- ``mesh_merging_settings`` (MeshMergingSettings):  [Read-Write]
- ``new_actor_label`` (str):  [Read-Write] Name of the new spawned Actor to replace the provided Actors.
- ``rename_components_from_source`` (bool):  [Read-Write] Rename StaticMeshComponents based on source Actor's name.
- ``spawn_merged_actor`` (bool):  [Read-Write] Spawn the new merged actors

<a id="unreal.MergeStaticMeshActorsOptions.__init__"></a>

#### __init__

```python
def __init__(
    destroy_source_actors: bool = False,
    new_actor_label: str = "",
    rename_components_from_source: bool = False,
    spawn_merged_actor: bool = False,
    base_package_name: str = "",
    mesh_merging_settings: MeshMergingSettings = [
        256,
        [
            TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE,
            5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000,
            0.000000, 0.500000, 1.000000, 1.000000, 1.000000,
            BlendMode.BLEND_OPAQUE, True, True, False, False, False, False,
            False, False, False, False, False, [1024, 1024], [1024, 1024],
            [1024, 1024], [1024, 1024], [1024, 1024], [1024,
                                                       1024], [1024, 1024],
            [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]
        ], MeshLODSelectionType.CALCULATE_LOD, 0, True, False, False, False,
        False, False, False, True, False, False, True, True,
        [
            False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000,
            NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0
        ]
    ]
) -> None
```

<a id="unreal.MergeStaticMeshActorsOptions.spawn_merged_actor"></a>

#### spawn_merged_actor

```python
@property
def spawn_merged_actor() -> bool
```

(bool):  [Read-Write] Spawn the new merged actors

<a id="unreal.MergeStaticMeshActorsOptions.spawn_merged_actor"></a>

#### spawn_merged_actor

```python
@spawn_merged_actor.setter
def spawn_merged_actor(value: bool) -> None
```

<a id="unreal.MergeStaticMeshActorsOptions.base_package_name"></a>

#### base_package_name

```python
@property
def base_package_name() -> str
```

(str):  [Read-Write] The package path you want to save to. ie: /Game/MyFolder

<a id="unreal.MergeStaticMeshActorsOptions.base_package_name"></a>

#### base_package_name

```python
@base_package_name.setter
def base_package_name(value: str) -> None
```

<a id="unreal.MergeStaticMeshActorsOptions.mesh_merging_settings"></a>

#### mesh_merging_settings

```python
@property
def mesh_merging_settings() -> MeshMergingSettings
```

(MeshMergingSettings):  [Read-Write]

<a id="unreal.MergeStaticMeshActorsOptions.mesh_merging_settings"></a>

#### mesh_merging_settings

```python
@mesh_merging_settings.setter
def mesh_merging_settings(value: MeshMergingSettings) -> None
```

<a id="unreal.EditorScriptingMergeStaticMeshActorsOptions"></a>