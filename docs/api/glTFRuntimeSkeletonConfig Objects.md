## glTFRuntimeSkeletonConfig Objects

```python
class glTFRuntimeSkeletonConfig(StructBase)
```

Gl TFRuntime Skeleton Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_root_bone`` (bool):  [Read-Write]
- ``add_root_node_if_missing`` (bool):  [Read-Write]
- ``append_node_index_on_name_collision`` (bool):  [Read-Write]
- ``apply_parent_nodes_transforms_to_root`` (bool):  [Read-Write]
- ``apply_unmapped_bones_transforms`` (bool):  [Read-Write]
- ``assign_unmapped_bones_to_parent`` (bool):  [Read-Write]
- ``bone_remapper`` (glTFRuntimeSkeletonBoneRemapperHook):  [Read-Write]
- ``bones_delta_transform_map`` (Map[str, Transform]):  [Read-Write]
- ``bones_name_map`` (Map[str, str]):  [Read-Write]
- ``bones_transform_map`` (Map[str, Transform]):  [Read-Write]
- ``cache_mode`` (EglTFRuntimeCacheMode):  [Read-Write]
- ``clear_rotations`` (bool):  [Read-Write]
- ``copy_rotations_from`` (Skeleton):  [Read-Write]
- ``fallback_to_nodes_tree`` (bool):  [Read-Write]
- ``force_root_node`` (str):  [Read-Write]
- ``max_nodes_tree_depth`` (int32):  [Read-Write]
- ``node_bones_delta_transform_map`` (Map[str, Transform]):  [Read-Write]
- ``normalize_skeleton_scale`` (bool):  [Read-Write]
- ``root_bone_name`` (str):  [Read-Write]
- ``root_node_index`` (int32):  [Read-Write]
- ``skip_already_existent_bone_names`` (bool):  [Read-Write]
- ``sockets`` (Map[str, glTFRuntimeSocket]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE,
        add_root_bone: bool = False,
        root_bone_name: str = "",
        bones_name_map: Map[str, str] = {},
        assign_unmapped_bones_to_parent: bool = False,
        bones_transform_map: Map[str, Transform] = {},
        normalize_skeleton_scale: bool = False,
        root_node_index: int = 0,
        sockets: Map[str, glTFRuntimeSocket] = {},
        clear_rotations: bool = False,
        copy_rotations_from: Skeleton = None,
        skip_already_existent_bone_names: bool = False,
        force_root_node: str = "",
        bones_delta_transform_map: Map[str, Transform] = {},
        bone_remapper: glTFRuntimeSkeletonBoneRemapperHook = [
            glTFRuntimeBoneRemapper(), None
        ],
        append_node_index_on_name_collision: bool = False,
        fallback_to_nodes_tree: bool = False,
        apply_parent_nodes_transforms_to_root: bool = False,
        max_nodes_tree_depth: int = 0,
        apply_unmapped_bones_transforms: bool = False,
        node_bones_delta_transform_map: Map[str, Transform] = {},
        add_root_node_if_missing: bool = False) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.cache_mode"></a>

#### cache\_mode

```python
@property
def cache_mode() -> EglTFRuntimeCacheMode
```

(EglTFRuntimeCacheMode):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.cache_mode"></a>

#### cache\_mode

```python
@cache_mode.setter
def cache_mode(value: EglTFRuntimeCacheMode) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.add_root_bone"></a>

#### add\_root\_bone

```python
@property
def add_root_bone() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.add_root_bone"></a>

#### add\_root\_bone

```python
@add_root_bone.setter
def add_root_bone(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.root_bone_name"></a>

#### root\_bone\_name

```python
@property
def root_bone_name() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.root_bone_name"></a>

#### root\_bone\_name

```python
@root_bone_name.setter
def root_bone_name(value: str) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.bones_name_map"></a>

#### bones\_name\_map

```python
@property
def bones_name_map() -> Map[str, str]
```

(Map[str, str]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.bones_name_map"></a>

#### bones\_name\_map

```python
@bones_name_map.setter
def bones_name_map(value: Map[str, str]) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.assign_unmapped_bones_to_parent"></a>

#### assign\_unmapped\_bones\_to\_parent

```python
@property
def assign_unmapped_bones_to_parent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.assign_unmapped_bones_to_parent"></a>

#### assign\_unmapped\_bones\_to\_parent

```python
@assign_unmapped_bones_to_parent.setter
def assign_unmapped_bones_to_parent(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.bones_transform_map"></a>

#### bones\_transform\_map

```python
@property
def bones_transform_map() -> Map[str, Transform]
```

(Map[str, Transform]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.bones_transform_map"></a>

#### bones\_transform\_map

```python
@bones_transform_map.setter
def bones_transform_map(value: Map[str, Transform]) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.normalize_skeleton_scale"></a>

#### normalize\_skeleton\_scale

```python
@property
def normalize_skeleton_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.normalize_skeleton_scale"></a>

#### normalize\_skeleton\_scale

```python
@normalize_skeleton_scale.setter
def normalize_skeleton_scale(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.root_node_index"></a>

#### root\_node\_index

```python
@property
def root_node_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.root_node_index"></a>

#### root\_node\_index

```python
@root_node_index.setter
def root_node_index(value: int) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.sockets"></a>

#### sockets

```python
@property
def sockets() -> Map[str, glTFRuntimeSocket]
```

(Map[str, glTFRuntimeSocket]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.sockets"></a>

#### sockets

```python
@sockets.setter
def sockets(value: Map[str, glTFRuntimeSocket]) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.clear_rotations"></a>

#### clear\_rotations

```python
@property
def clear_rotations() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.clear_rotations"></a>

#### clear\_rotations

```python
@clear_rotations.setter
def clear_rotations(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.copy_rotations_from"></a>

#### copy\_rotations\_from

```python
@property
def copy_rotations_from() -> Skeleton
```

(Skeleton):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.copy_rotations_from"></a>

#### copy\_rotations\_from

```python
@copy_rotations_from.setter
def copy_rotations_from(value: Skeleton) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.skip_already_existent_bone_names"></a>

#### skip\_already\_existent\_bone\_names

```python
@property
def skip_already_existent_bone_names() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.skip_already_existent_bone_names"></a>

#### skip\_already\_existent\_bone\_names

```python
@skip_already_existent_bone_names.setter
def skip_already_existent_bone_names(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.force_root_node"></a>

#### force\_root\_node

```python
@property
def force_root_node() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.force_root_node"></a>

#### force\_root\_node

```python
@force_root_node.setter
def force_root_node(value: str) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.bones_delta_transform_map"></a>

#### bones\_delta\_transform\_map

```python
@property
def bones_delta_transform_map() -> Map[str, Transform]
```

(Map[str, Transform]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.bones_delta_transform_map"></a>

#### bones\_delta\_transform\_map

```python
@bones_delta_transform_map.setter
def bones_delta_transform_map(value: Map[str, Transform]) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.bone_remapper"></a>

#### bone\_remapper

```python
@property
def bone_remapper() -> glTFRuntimeSkeletonBoneRemapperHook
```

(glTFRuntimeSkeletonBoneRemapperHook):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.bone_remapper"></a>

#### bone\_remapper

```python
@bone_remapper.setter
def bone_remapper(value: glTFRuntimeSkeletonBoneRemapperHook) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.append_node_index_on_name_collision"></a>

#### append\_node\_index\_on\_name\_collision

```python
@property
def append_node_index_on_name_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.append_node_index_on_name_collision"></a>

#### append\_node\_index\_on\_name\_collision

```python
@append_node_index_on_name_collision.setter
def append_node_index_on_name_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.fallback_to_nodes_tree"></a>

#### fallback\_to\_nodes\_tree

```python
@property
def fallback_to_nodes_tree() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.fallback_to_nodes_tree"></a>

#### fallback\_to\_nodes\_tree

```python
@fallback_to_nodes_tree.setter
def fallback_to_nodes_tree(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.apply_parent_nodes_transforms_to_root"></a>

#### apply\_parent\_nodes\_transforms\_to\_root

```python
@property
def apply_parent_nodes_transforms_to_root() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.apply_parent_nodes_transforms_to_root"></a>

#### apply\_parent\_nodes\_transforms\_to\_root

```python
@apply_parent_nodes_transforms_to_root.setter
def apply_parent_nodes_transforms_to_root(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.max_nodes_tree_depth"></a>

#### max\_nodes\_tree\_depth

```python
@property
def max_nodes_tree_depth() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.max_nodes_tree_depth"></a>

#### max\_nodes\_tree\_depth

```python
@max_nodes_tree_depth.setter
def max_nodes_tree_depth(value: int) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.apply_unmapped_bones_transforms"></a>

#### apply\_unmapped\_bones\_transforms

```python
@property
def apply_unmapped_bones_transforms() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.apply_unmapped_bones_transforms"></a>

#### apply\_unmapped\_bones\_transforms

```python
@apply_unmapped_bones_transforms.setter
def apply_unmapped_bones_transforms(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.node_bones_delta_transform_map"></a>

#### node\_bones\_delta\_transform\_map

```python
@property
def node_bones_delta_transform_map() -> Map[str, Transform]
```

(Map[str, Transform]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.node_bones_delta_transform_map"></a>

#### node\_bones\_delta\_transform\_map

```python
@node_bones_delta_transform_map.setter
def node_bones_delta_transform_map(value: Map[str, Transform]) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig.add_root_node_if_missing"></a>

#### add\_root\_node\_if\_missing

```python
@property
def add_root_node_if_missing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonConfig.add_root_node_if_missing"></a>

#### add\_root\_node\_if\_missing

```python
@add_root_node_if_missing.setter
def add_root_node_if_missing(value: bool) -> None
```

<a id="unreal.glTFRuntimeCapsule"></a>