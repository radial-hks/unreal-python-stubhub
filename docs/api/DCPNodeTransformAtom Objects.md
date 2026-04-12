## DCPNodeTransformAtom Objects

```python
class DCPNodeTransformAtom(EntityAtomBase)
```

DCPNode Transform Atom

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPNodeTransformAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_node_transform_find`` (Map[int32, int32]):  [Read-Write]
- ``flip_coordinate_system`` (bool):  [Read-Write] 使用节点id索引对应绑定到的虚拟节点
- ``node_id_to_anchor`` (Map[int32, SceneComponent]):  [Read-Write] 使用节点id索引对应的mesh
- ``node_id_to_mesh`` (Map[int32, ProceduralMeshComponent]):  [Read-Write] 自定义节点捆绑的锚点，由于合并节点是后来计算的，轴心位置可能在某些情况下不能友好确定，所以提供一种方式可以指定轴心以谁为准

<a id="unreal.DCPNodeTransformAtom.custom_node_transform_find"></a>

#### custom\_node\_transform\_find

```python
@property
def custom_node_transform_find() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Only]

<a id="unreal.DCPNodeTransformAtom.node_id_to_mesh"></a>

#### node\_id\_to\_mesh

```python
@property
def node_id_to_mesh() -> Map[int, ProceduralMeshComponent]
```

(Map[int32, ProceduralMeshComponent]):  [Read-Only] 自定义节点捆绑的锚点，由于合并节点是后来计算的，轴心位置可能在某些情况下不能友好确定，所以提供一种方式可以指定轴心以谁为准

<a id="unreal.DCPNodeTransformAtom.node_id_to_anchor"></a>

#### node\_id\_to\_anchor

```python
@property
def node_id_to_anchor() -> Map[int, SceneComponent]
```

(Map[int32, SceneComponent]):  [Read-Only] 使用节点id索引对应的mesh

<a id="unreal.DCPNodeTransformAtom.flip_coordinate_system"></a>

#### flip\_coordinate\_system

```python
@property
def flip_coordinate_system() -> bool
```

(bool):  [Read-Only] 使用节点id索引对应绑定到的虚拟节点

<a id="unreal.DCPNodeTransformAtom.set_node_transform"></a>

#### set\_node\_transform

```python
def set_node_transform(node_ids_transform: Map[int, Transform]) -> None
```

x.set_node_transform(node_ids_transform) -> None
Set Node Transform

Args:
    node_ids_transform (Map[int32, Transform]):

<a id="unreal.DCPNodeTransformAtom.set_node_scale"></a>

#### set\_node\_scale

```python
def set_node_scale(node_ids_scale: Map[int, Vector]) -> None
```

x.set_node_scale(node_ids_scale) -> None
Set Node Scale

Args:
    node_ids_scale (Map[int32, Vector]):

<a id="unreal.DCPNodeTransformAtom.set_node_rotation"></a>

#### set\_node\_rotation

```python
def set_node_rotation(node_ids_rotation: Map[int, Rotator]) -> None
```

x.set_node_rotation(node_ids_rotation) -> None
Set Node Rotation

Args:
    node_ids_rotation (Map[int32, Rotator]):

<a id="unreal.DCPNodeTransformAtom.set_node_location"></a>

#### set\_node\_location

```python
def set_node_location(node_ids_location: Map[int, Vector]) -> None
```

x.set_node_location(node_ids_location) -> None
节点设置，进行设置的实际上是锚点的transform

Args:
    node_ids_location (Map[int32, Vector]):

<a id="unreal.DCPNodeTransformAtom.set_custom_node_transform_find"></a>

#### set\_custom\_node\_transform\_find

```python
def set_custom_node_transform_find(
        node_ids_transform_find: Map[int, int]) -> None
```

x.set_custom_node_transform_find(node_ids_transform_find) -> None
Set Custom Node Transform Find

Args:
    node_ids_transform_find (Map[int32, int32]):

<a id="unreal.DCPNodeTransformAtom.reset_transform_nodes"></a>

#### reset\_transform\_nodes

```python
def reset_transform_nodes() -> None
```

x.reset_transform_nodes() -> None
初始完整创建节点mesh链条

<a id="unreal.DCPNodeTransformAtom.debug_anchor_transform"></a>

#### debug\_anchor\_transform

```python
def debug_anchor_transform() -> None
```

x.debug_anchor_transform() -> None
Debug Anchor Transform

<a id="unreal.DCPNodeTransformAtom.create_transform_nodes_with_invisible"></a>

#### create\_transform\_nodes\_with\_invisible

```python
def create_transform_nodes_with_invisible(
        node_ids: Array[int], invisible_node_ids: Array[int]) -> bool
```

x.create_transform_nodes_with_invisible(node_ids, invisible_node_ids) -> bool
初始完整创建节点mesh链条

Args:
    node_ids (Array[int32]): 
    invisible_node_ids (Array[int32]): 

Returns:
    bool:

<a id="unreal.DCPNodeTransformAtom.create_transform_nodes"></a>

#### create\_transform\_nodes

```python
def create_transform_nodes(node_ids: Array[int]) -> bool
```

x.create_transform_nodes(node_ids) -> bool
Create Transform Nodes

Args:
    node_ids (Array[int32]): 

Returns:
    bool:

<a id="unreal.DCPSectionEntityAtom"></a>