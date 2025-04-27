## AvaShape2DArrowDynamicMesh Objects

```python
class AvaShape2DArrowDynamicMesh(AvaShape2DDynMeshBase)
```

Ava Shape 2DArrow Dynamic Mesh

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShape2DArrowDynMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_edit_size`` (bool):  [Read-Write] enable mesh size property editing
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``both_side_arrows`` (bool):  [Read-Write] whether there should be an arrow on both side, arrows will have same ratio
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mesh_datas`` (Map[int32, AvaShapeMeshData]):  [Read-Write] Meshes used for the current shape sections
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``pixel_size2d`` (Vector2D):  [Read-Write] pixel size of the mesh, will only be available in editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``ratio_arrow_line`` (float):  [Read-Write] represents the ratio for the arrow and the line, 0.6 means 60% arrow and 40% line
- ``ratio_arrow_y`` (float):  [Read-Write] represents the ratio for the arrow end, 0 means arrow point will be at bottom, 1 means arrow point will be at top
- ``ratio_line_height`` (float):  [Read-Write] represents the ratio for the line height, 1 means 100% of the height available
- ``ratio_line_y`` (float):  [Read-Write] represents the ratio for the arrow end, 0 means arrow point will be at bottom, 1 means arrow point will be at top
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``size2d`` (Vector2D):  [Read-Write] total size in 2D from 0 to mesh size and not origin
- ``size_type`` (SizeType):  [Read-Write] the type of size you want to handle
- ``uniform_scaled_size`` (float):  [Read-Write] Uniform scaled size of the mesh
- ``use_primary_material_everywhere`` (bool):  [Read-Write] use primary material for every slot available
- ``vertex_color`` (LinearColor):  [Read-Write]

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_arrow_line"></a>

#### ratio_arrow_line

```python
@property
def ratio_arrow_line() -> float
```

(float):  [Read-Write] represents the ratio for the arrow and the line, 0.6 means 60% arrow and 40% line

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_arrow_line"></a>

#### ratio_arrow_line

```python
@ratio_arrow_line.setter
def ratio_arrow_line(value: float) -> None
```

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_line_height"></a>

#### ratio_line_height

```python
@property
def ratio_line_height() -> float
```

(float):  [Read-Write] represents the ratio for the line height, 1 means 100% of the height available

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_line_height"></a>

#### ratio_line_height

```python
@ratio_line_height.setter
def ratio_line_height(value: float) -> None
```

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_arrow_y"></a>

#### ratio_arrow_y

```python
@property
def ratio_arrow_y() -> float
```

(float):  [Read-Write] represents the ratio for the arrow end, 0 means arrow point will be at bottom, 1 means arrow point will be at top

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_arrow_y"></a>

#### ratio_arrow_y

```python
@ratio_arrow_y.setter
def ratio_arrow_y(value: float) -> None
```

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_line_y"></a>

#### ratio_line_y

```python
@property
def ratio_line_y() -> float
```

(float):  [Read-Write] represents the ratio for the arrow end, 0 means arrow point will be at bottom, 1 means arrow point will be at top

<a id="unreal.AvaShape2DArrowDynamicMesh.ratio_line_y"></a>

#### ratio_line_y

```python
@ratio_line_y.setter
def ratio_line_y(value: float) -> None
```

<a id="unreal.AvaShape2DArrowDynamicMesh.both_side_arrows"></a>

#### both_side_arrows

```python
@property
def both_side_arrows() -> bool
```

(bool):  [Read-Write] whether there should be an arrow on both side, arrows will have same ratio

<a id="unreal.AvaShape2DArrowDynamicMesh.both_side_arrows"></a>

#### both_side_arrows

```python
@both_side_arrows.setter
def both_side_arrows(value: bool) -> None
```

<a id="unreal.AvaToolbox2DArrowDynamicMesh"></a>