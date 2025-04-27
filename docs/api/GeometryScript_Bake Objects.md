## GeometryScript_Bake Objects

```python
class GeometryScript_Bake(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Bake Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

<a id="unreal.GeometryScript_Bake.make_bake_type_vertex_color"></a>

#### make_bake_type_vertex_color

```python
@classmethod
def make_bake_type_vertex_color(cls) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_vertex_color() -> GeometryScriptBakeTypeOptions
Make Bake Type Vertex Color

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_uv_shell"></a>

#### make_bake_type_uv_shell

```python
@classmethod
def make_bake_type_uv_shell(
    cls,
    source_uv_layer: int = 0,
    wireframe_thickness: float = 1.000000,
    wireframe_color: LinearColor = [0.000000, 0.000000, 1.000000, 1.000000],
    shell_color: LinearColor = [0.500000, 0.500000, 0.500000, 1.000000],
    background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]
) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_uv_shell(source_uv_layer=0, wireframe_thickness=1.000000, wireframe_color=[0.000000, 0.000000, 1.000000, 1.000000], shell_color=[0.500000, 0.500000, 0.500000, 1.000000], background_color=[0.000000, 0.000000, 0.000000, 0.000000]) -> GeometryScriptBakeTypeOptions
Make Bake Type UVShell

Args:
    source_uv_layer (int32): 
    wireframe_thickness (float): 
    wireframe_color (LinearColor): 
    shell_color (LinearColor): 
    background_color (LinearColor): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_texture"></a>

#### make_bake_type_texture

```python
@classmethod
def make_bake_type_texture(
        cls,
        source_texture: Texture2D = None,
        source_uv_layer: int = 0) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_texture(source_texture=None, source_uv_layer=0) -> GeometryScriptBakeTypeOptions
Make Bake Type Texture

Args:
    source_texture (Texture2D): 
    source_uv_layer (int32): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_tangent_normal"></a>

#### make_bake_type_tangent_normal

```python
@classmethod
def make_bake_type_tangent_normal(cls) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_tangent_normal() -> GeometryScriptBakeTypeOptions
Make Bake Type Tangent Normal

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_position"></a>

#### make_bake_type_position

```python
@classmethod
def make_bake_type_position(cls) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_position() -> GeometryScriptBakeTypeOptions
Make Bake Type Position

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_object_normal"></a>

#### make_bake_type_object_normal

```python
@classmethod
def make_bake_type_object_normal(cls) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_object_normal() -> GeometryScriptBakeTypeOptions
Make Bake Type Object Normal

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_multi_texture"></a>

#### make_bake_type_multi_texture

```python
@classmethod
def make_bake_type_multi_texture(
        cls,
        material_id_source_textures: Array[Texture2D],
        source_uv_layer: int = 0) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_multi_texture(material_id_source_textures, source_uv_layer=0) -> GeometryScriptBakeTypeOptions
Make Bake Type Multi Texture

Args:
    material_id_source_textures (Array[Texture2D]): 
    source_uv_layer (int32): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_material_id"></a>

#### make_bake_type_material_id

```python
@classmethod
def make_bake_type_material_id(cls) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_material_id() -> GeometryScriptBakeTypeOptions
Make Bake Type Material ID

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_face_normal"></a>

#### make_bake_type_face_normal

```python
@classmethod
def make_bake_type_face_normal(cls) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_face_normal() -> GeometryScriptBakeTypeOptions
Make Bake Type Face Normal

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_curvature"></a>

#### make_bake_type_curvature

```python
@classmethod
def make_bake_type_curvature(
    cls,
    curvature_type:
    GeometryScriptBakeCurvatureTypeMode = GeometryScriptBakeCurvatureTypeMode.
    MEAN,
    color_mapping:
    GeometryScriptBakeCurvatureColorMode = GeometryScriptBakeCurvatureColorMode
    .GRAYSCALE,
    color_range_multiplier: float = 1.000000,
    min_range_multiplier: float = 0.000000,
    clamping:
    GeometryScriptBakeCurvatureClampMode = GeometryScriptBakeCurvatureClampMode
    .NONE
) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_curvature(curvature_type=GeometryScriptBakeCurvatureTypeMode.MEAN, color_mapping=GeometryScriptBakeCurvatureColorMode.GRAYSCALE, color_range_multiplier=1.000000, min_range_multiplier=0.000000, clamping=GeometryScriptBakeCurvatureClampMode.NONE) -> GeometryScriptBakeTypeOptions
Make Bake Type Curvature

Args:
    curvature_type (GeometryScriptBakeCurvatureTypeMode): 
    color_mapping (GeometryScriptBakeCurvatureColorMode): 
    color_range_multiplier (float): 
    min_range_multiplier (float): 
    clamping (GeometryScriptBakeCurvatureClampMode): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_constant"></a>

#### make_bake_type_constant

```python
@classmethod
def make_bake_type_constant(cls,
                            value: float = 0.000000
                            ) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_constant(value=0.000000) -> GeometryScriptBakeTypeOptions
Make Bake Type Constant

Args:
    value (float): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_bent_normal"></a>

#### make_bake_type_bent_normal

```python
@classmethod
def make_bake_type_bent_normal(
    cls,
    occlusion_rays: int = 16,
    max_distance: float = 0.000000,
    spread_angle: float = 180.000000,
    normal_space: GeometryScriptBakeNormalSpace = GeometryScriptBakeNormalSpace
    .TANGENT
) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_bent_normal(occlusion_rays=16, max_distance=0.000000, spread_angle=180.000000, normal_space=GeometryScriptBakeNormalSpace.TANGENT) -> GeometryScriptBakeTypeOptions
Make Bake Type Bent Normal

Args:
    occlusion_rays (int32): 
    max_distance (float): 
    spread_angle (float): 
    normal_space (GeometryScriptBakeNormalSpace): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.make_bake_type_ambient_occlusion"></a>

#### make_bake_type_ambient_occlusion

```python
@classmethod
def make_bake_type_ambient_occlusion(
        cls,
        occlusion_rays: int = 16,
        max_distance: float = 0.000000,
        spread_angle: float = 180.000000,
        bias_angle: float = 15.000000) -> GeometryScriptBakeTypeOptions
```

X.make_bake_type_ambient_occlusion(occlusion_rays=16, max_distance=0.000000, spread_angle=180.000000, bias_angle=15.000000) -> GeometryScriptBakeTypeOptions
Make Bake Type Ambient Occlusion

Args:
    occlusion_rays (int32): 
    max_distance (float): 
    spread_angle (float): 
    bias_angle (float): 

Returns:
    GeometryScriptBakeTypeOptions:

<a id="unreal.GeometryScript_Bake.convert_bake_resolution_to_int"></a>

#### convert_bake_resolution_to_int

```python
@classmethod
def convert_bake_resolution_to_int(
        cls, bake_resolution: GeometryScriptBakeResolution) -> int
```

X.convert_bake_resolution_to_int(bake_resolution) -> int32
Convert Bake Resolution to Int

Args:
    bake_resolution (GeometryScriptBakeResolution): 

Returns:
    int32:

<a id="unreal.GeometryScript_Bake.bake_vertex"></a>

#### bake_vertex

```python
@classmethod
def bake_vertex(cls,
                target_mesh: DynamicMesh,
                target_transform: Transform,
                target_options: GeometryScriptBakeTargetMeshOptions,
                source_mesh: DynamicMesh,
                source_transform: Transform,
                source_options: GeometryScriptBakeSourceMeshOptions,
                bake_types: GeometryScriptBakeOutputType,
                bake_options: GeometryScriptBakeVertexOptions,
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.bake_vertex(target_mesh, target_transform, target_options, source_mesh, source_transform, source_options, bake_types, bake_options, debug=None) -> DynamicMesh
Bake Vertex

Args:
    target_mesh (DynamicMesh): 
    target_transform (Transform): 
    target_options (GeometryScriptBakeTargetMeshOptions): 
    source_mesh (DynamicMesh): 
    source_transform (Transform): 
    source_options (GeometryScriptBakeSourceMeshOptions): 
    bake_types (GeometryScriptBakeOutputType): 
    bake_options (GeometryScriptBakeVertexOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Bake.bake_texture_from_render_captures"></a>

#### bake_texture_from_render_captures

```python
@classmethod
def bake_texture_from_render_captures(
        cls,
        target_mesh: DynamicMesh,
        target_local_to_world: Transform,
        target_options: GeometryScriptBakeTargetMeshOptions,
        source_actors: Array[Actor],
        bake_options: GeometryScriptBakeRenderCaptureOptions,
        debug: GeometryScriptDebug = None
) -> GeometryScriptRenderCaptureTextures
```

X.bake_texture_from_render_captures(target_mesh, target_local_to_world, target_options, source_actors, bake_options, debug=None) -> GeometryScriptRenderCaptureTextures
Bake Texture from Render Captures

Args:
    target_mesh (DynamicMesh): 
    target_local_to_world (Transform): 
    target_options (GeometryScriptBakeTargetMeshOptions): 
    source_actors (Array[Actor]): 
    bake_options (GeometryScriptBakeRenderCaptureOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptRenderCaptureTextures:

<a id="unreal.GeometryScript_Bake.bake_texture"></a>

#### bake_texture

```python
@classmethod
def bake_texture(cls,
                 target_mesh: DynamicMesh,
                 target_transform: Transform,
                 target_options: GeometryScriptBakeTargetMeshOptions,
                 source_mesh: DynamicMesh,
                 source_transform: Transform,
                 source_options: GeometryScriptBakeSourceMeshOptions,
                 bake_types: Array[GeometryScriptBakeTypeOptions],
                 bake_options: GeometryScriptBakeTextureOptions,
                 debug: GeometryScriptDebug = None) -> Array[Texture2D]
```

X.bake_texture(target_mesh, target_transform, target_options, source_mesh, source_transform, source_options, bake_types, bake_options, debug=None) -> Array[Texture2D]
Bake Texture

Args:
    target_mesh (DynamicMesh): 
    target_transform (Transform): 
    target_options (GeometryScriptBakeTargetMeshOptions): 
    source_mesh (DynamicMesh): 
    source_transform (Transform): 
    source_options (GeometryScriptBakeSourceMeshOptions): 
    bake_types (Array[GeometryScriptBakeTypeOptions]): 
    bake_options (GeometryScriptBakeTextureOptions): 
    debug (GeometryScriptDebug): 

Returns:
    Array[Texture2D]:

<a id="unreal.GeometryScript_MeshEdits"></a>