## AvaShapeRectangleDynamicMesh Objects

```python
class AvaShapeRectangleDynamicMesh(AvaShape2DDynMeshBase)
```

Ava Shape Rectangle Dynamic Mesh

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeRectangleDynMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_edit_size`` (bool):  [Read-Write] enable mesh size property editing
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``bottom_left`` (AvaShapeRectangleCornerSettings):  [Read-Write]
- ``bottom_right`` (AvaShapeRectangleCornerSettings):  [Read-Write]
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``global_bevel_size`` (float):  [Read-Write]
- ``global_bevel_subdivisions`` (uint8):  [Read-Write]
- ``horizontal_alignment`` (AvaHorizontalAlignment):  [Read-Write]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``left_slant`` (float):  [Read-Write] Angle in degrees for the left slant of the rectangle
- ``mesh_datas`` (Map[int32, AvaShapeMeshData]):  [Read-Write] Meshes used for the current shape sections
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``pixel_size2d`` (Vector2D):  [Read-Write] pixel size of the mesh, will only be available in editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``right_slant`` (float):  [Read-Write] Angle in degrees for the right slant of the rectangle
- ``size2d`` (Vector2D):  [Read-Write] total size in 2D from 0 to mesh size and not origin
- ``size_type`` (SizeType):  [Read-Write] the type of size you want to handle
- ``top_left`` (AvaShapeRectangleCornerSettings):  [Read-Write]
- ``top_right`` (AvaShapeRectangleCornerSettings):  [Read-Write]
- ``uniform_scaled_size`` (float):  [Read-Write] Uniform scaled size of the mesh
- ``use_primary_material_everywhere`` (bool):  [Read-Write] use primary material for every slot available
- ``vertex_color`` (LinearColor):  [Read-Write]
- ``vertical_alignment`` (AvaVerticalAlignment):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> AvaHorizontalAlignment
```

(AvaHorizontalAlignment):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: AvaHorizontalAlignment) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> AvaVerticalAlignment
```

(AvaVerticalAlignment):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: AvaVerticalAlignment) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.left_slant"></a>

#### left_slant

```python
@property
def left_slant() -> float
```

(float):  [Read-Write] Angle in degrees for the left slant of the rectangle

<a id="unreal.AvaShapeRectangleDynamicMesh.left_slant"></a>

#### left_slant

```python
@left_slant.setter
def left_slant(value: float) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.right_slant"></a>

#### right_slant

```python
@property
def right_slant() -> float
```

(float):  [Read-Write] Angle in degrees for the right slant of the rectangle

<a id="unreal.AvaShapeRectangleDynamicMesh.right_slant"></a>

#### right_slant

```python
@right_slant.setter
def right_slant(value: float) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.global_bevel_size"></a>

#### global_bevel_size

```python
@property
def global_bevel_size() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.global_bevel_size"></a>

#### global_bevel_size

```python
@global_bevel_size.setter
def global_bevel_size(value: float) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.global_bevel_subdivisions"></a>

#### global_bevel_subdivisions

```python
@property
def global_bevel_subdivisions() -> int
```

(uint8):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.global_bevel_subdivisions"></a>

#### global_bevel_subdivisions

```python
@global_bevel_subdivisions.setter
def global_bevel_subdivisions(value: int) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.top_left"></a>

#### top_left

```python
@property
def top_left() -> AvaShapeRectangleCornerSettings
```

(AvaShapeRectangleCornerSettings):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.top_left"></a>

#### top_left

```python
@top_left.setter
def top_left(value: AvaShapeRectangleCornerSettings) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.top_right"></a>

#### top_right

```python
@property
def top_right() -> AvaShapeRectangleCornerSettings
```

(AvaShapeRectangleCornerSettings):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.top_right"></a>

#### top_right

```python
@top_right.setter
def top_right(value: AvaShapeRectangleCornerSettings) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.bottom_left"></a>

#### bottom_left

```python
@property
def bottom_left() -> AvaShapeRectangleCornerSettings
```

(AvaShapeRectangleCornerSettings):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.bottom_left"></a>

#### bottom_left

```python
@bottom_left.setter
def bottom_left(value: AvaShapeRectangleCornerSettings) -> None
```

<a id="unreal.AvaShapeRectangleDynamicMesh.bottom_right"></a>

#### bottom_right

```python
@property
def bottom_right() -> AvaShapeRectangleCornerSettings
```

(AvaShapeRectangleCornerSettings):  [Read-Write]

<a id="unreal.AvaShapeRectangleDynamicMesh.bottom_right"></a>

#### bottom_right

```python
@bottom_right.setter
def bottom_right(value: AvaShapeRectangleCornerSettings) -> None
```

<a id="unreal.AvaToolboxRectangleDynamicMesh"></a>