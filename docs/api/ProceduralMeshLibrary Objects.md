## ProceduralMeshLibrary Objects

```python
class ProceduralMeshLibrary(BlueprintFunctionLibrary)
```

Kismet Procedural Mesh Library

**C++ Source:**

- **Plugin**: ProceduralMeshComponent
- **Module**: ProceduralMeshComponent
- **File**: KismetProceduralMeshLibrary.h

<a id="unreal.ProceduralMeshLibrary.slice_procedural_mesh"></a>

#### slice_procedural_mesh

```python
@classmethod
def slice_procedural_mesh(
        cls, proc_mesh: ProceduralMeshComponent, plane_position: Vector,
        plane_normal: Vector, create_other_half: bool,
        cap_option: ProcMeshSliceCapOption,
        cap_material: MaterialInterface) -> ProceduralMeshComponent
```

X.slice_procedural_mesh(proc_mesh, plane_position, plane_normal, create_other_half, cap_option, cap_material) -> ProceduralMeshComponent
Slice the ProceduralMeshComponent (including simple convex collision) using a plane. Optionally create 'cap' geometry.

Args:
    proc_mesh (ProceduralMeshComponent): ProceduralMeshComponent to slice
    plane_position (Vector): Point on the plane to use for slicing, in world space
    plane_normal (Vector): Normal of plane used for slicing. Geometry on the positive side of the plane will be kept.
    create_other_half (bool): If true, an additional ProceduralMeshComponent (OutOtherHalfProcMesh) will be created using the other half of the sliced geometry
    cap_option (ProcMeshSliceCapOption): If and how to create 'cap' geometry on the slicing plane
    cap_material (MaterialInterface): If creating a new section for the cap, assign this material to that section

Returns:
    ProceduralMeshComponent: 

    out_other_half_proc_mesh (ProceduralMeshComponent): If bCreateOtherHalf is set, this is the new component created. Its owner will be the same as the supplied InProcMesh.

<a id="unreal.ProceduralMeshLibrary.get_section_from_static_mesh"></a>

#### get_section_from_static_mesh

```python
@classmethod
def get_section_from_static_mesh(
    cls, mesh: StaticMesh, lod_index: int, section_index: int
) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector2D],
           Array[ProcMeshTangent]]
```

X.get_section_from_static_mesh(mesh, lod_index, section_index) -> (vertices=Array[Vector], triangles=Array[int32], normals=Array[Vector], u_vs=Array[Vector2D], tangents=Array[ProcMeshTangent])
Grab geometry data from a StaticMesh asset.

Args:
    mesh (StaticMesh): 
    lod_index (int32): 
    section_index (int32): 

Returns:
    tuple: 

    vertices (Array[Vector]): 

    triangles (Array[int32]): 

    normals (Array[Vector]): 

    u_vs (Array[Vector2D]): 

    tangents (Array[ProcMeshTangent]):

<a id="unreal.ProceduralMeshLibrary.get_section_from_procedural_mesh"></a>

#### get_section_from_procedural_mesh

```python
@classmethod
def get_section_from_procedural_mesh(
    cls, proc_mesh: ProceduralMeshComponent, section_index: int
) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector2D],
           Array[ProcMeshTangent]]
```

X.get_section_from_procedural_mesh(proc_mesh, section_index) -> (vertices=Array[Vector], triangles=Array[int32], normals=Array[Vector], u_vs=Array[Vector2D], tangents=Array[ProcMeshTangent])
Grab geometry data from a ProceduralMeshComponent.

Args:
    proc_mesh (ProceduralMeshComponent): 
    section_index (int32): 

Returns:
    tuple: 

    vertices (Array[Vector]): 

    triangles (Array[int32]): 

    normals (Array[Vector]): 

    u_vs (Array[Vector2D]): 

    tangents (Array[ProcMeshTangent]):

<a id="unreal.ProceduralMeshLibrary.generate_box_mesh"></a>

#### generate_box_mesh

```python
@classmethod
def generate_box_mesh(
    cls, box_radius: Vector
) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector2D],
           Array[ProcMeshTangent]]
```

X.generate_box_mesh(box_radius) -> (vertices=Array[Vector], triangles=Array[int32], normals=Array[Vector], u_vs=Array[Vector2D], tangents=Array[ProcMeshTangent])
Generate vertex and index buffer for a simple box, given the supplied dimensions. Normals, UVs and tangents are also generated for each vertex.

Args:
    box_radius (Vector): 

Returns:
    tuple: 

    vertices (Array[Vector]): 

    triangles (Array[int32]): 

    normals (Array[Vector]): 

    u_vs (Array[Vector2D]): 

    tangents (Array[ProcMeshTangent]):

<a id="unreal.ProceduralMeshLibrary.create_grid_mesh_welded"></a>

#### create_grid_mesh_welded

```python
@classmethod
def create_grid_mesh_welded(
    cls,
    num_x: int,
    num_y: int,
    grid_spacing: float = 16.000000
) -> Tuple[Array[int], Array[Vector], Array[Vector2D]]
```

X.create_grid_mesh_welded(num_x, num_y, grid_spacing=16.000000) -> (triangles=Array[int32], vertices=Array[Vector], u_vs=Array[Vector2D])
Generate a vertex buffer, index buffer and UVs for a tessellated grid mesh.
out: Triangles               Output index buffer
out: Vertices                Output vertex buffer
out: UVs                             Out UVs

Args:
    num_x (int32): Number of vertices in X direction (must be >= 2)
    num_y (int32): Number of vertices in y direction (must be >= 2)
    grid_spacing (float): Size of each quad in world units

Returns:
    tuple: 

    triangles (Array[int32]): 

    vertices (Array[Vector]): 

    u_vs (Array[Vector2D]):

<a id="unreal.ProceduralMeshLibrary.create_grid_mesh_triangles"></a>

#### create_grid_mesh_triangles

```python
@classmethod
def create_grid_mesh_triangles(cls, num_x: int, num_y: int,
                               winding: bool) -> Array[int]
```

X.create_grid_mesh_triangles(num_x, num_y, winding) -> Array[int32]
Generate an index buffer for a grid of quads.
out: Triangles               Output index buffer

Args:
    num_x (int32): Number of vertices in X direction (must be >= 2)
    num_y (int32): Number of vertices in y direction (must be >= 2)
    winding (bool): Reverses winding of indices generated for each quad

Returns:
    Array[int32]: 

    triangles (Array[int32]):

<a id="unreal.ProceduralMeshLibrary.create_grid_mesh_split"></a>

#### create_grid_mesh_split

```python
@classmethod
def create_grid_mesh_split(
    cls,
    num_x: int,
    num_y: int,
    grid_spacing: float = 16.000000
) -> Tuple[Array[int], Array[Vector], Array[Vector2D], Array[Vector2D]]
```

X.create_grid_mesh_split(num_x, num_y, grid_spacing=16.000000) -> (triangles=Array[int32], vertices=Array[Vector], u_vs=Array[Vector2D], uv1s=Array[Vector2D])
Generate a vertex buffer, index buffer and UVs for a grid mesh where each quad is split, with standard 0-1 UVs on UV0 and point sampled texel center UVs for UV1.
out: Triangles               Output index buffer
out: Vertices                Output vertex buffer
out: UVs                             Out UVs
out: UV1s                    Out UV1s

Args:
    num_x (int32): Number of vertices in X direction (must be >= 2)
    num_y (int32): Number of vertices in y direction (must be >= 2)
    grid_spacing (float): Size of each quad in world units

Returns:
    tuple: 

    triangles (Array[int32]): 

    vertices (Array[Vector]): 

    u_vs (Array[Vector2D]): 

    uv1s (Array[Vector2D]):

<a id="unreal.ProceduralMeshLibrary.copy_procedural_mesh_from_static_mesh_component"></a>

#### copy_procedural_mesh_from_static_mesh_component

```python
@classmethod
def copy_procedural_mesh_from_static_mesh_component(
        cls, static_mesh_component: StaticMeshComponent, lod_index: int,
        proc_mesh_component: ProceduralMeshComponent,
        create_collision: bool) -> None
```

X.copy_procedural_mesh_from_static_mesh_component(static_mesh_component, lod_index, proc_mesh_component, create_collision) -> None
Copy materials from StaticMeshComponent to ProceduralMeshComponent.

Args:
    static_mesh_component (StaticMeshComponent): 
    lod_index (int32): 
    proc_mesh_component (ProceduralMeshComponent): 
    create_collision (bool):

<a id="unreal.ProceduralMeshLibrary.convert_quad_to_triangles"></a>

#### convert_quad_to_triangles

```python
@classmethod
def convert_quad_to_triangles(cls, triangles: Array[int], vert0: int,
                              vert1: int, vert2: int,
                              vert3: int) -> Array[int]
```

X.convert_quad_to_triangles(triangles, vert0, vert1, vert2, vert3) -> Array[int32]
Add a quad, specified by four indices, to a triangle index buffer as two triangles.

Args:
    triangles (Array[int32]): 
    vert0 (int32): 
    vert1 (int32): 
    vert2 (int32): 
    vert3 (int32): 

Returns:
    Array[int32]: 

    triangles (Array[int32]):

<a id="unreal.ProceduralMeshLibrary.calculate_tangents_for_mesh"></a>

#### calculate_tangents_for_mesh

```python
@classmethod
def calculate_tangents_for_mesh(
        cls, vertices: Array[Vector], triangles: Array[int],
        u_vs: Array[Vector2D]) -> Tuple[Array[Vector], Array[ProcMeshTangent]]
```

X.calculate_tangents_for_mesh(vertices, triangles, u_vs) -> (normals=Array[Vector], tangents=Array[ProcMeshTangent])
Automatically generate normals and tangent vectors for a mesh
UVs are required for correct tangent generation.

Args:
    vertices (Array[Vector]): 
    triangles (Array[int32]): 
    u_vs (Array[Vector2D]): 

Returns:
    tuple: 

    normals (Array[Vector]): 

    tangents (Array[ProcMeshTangent]):

<a id="unreal.ProceduralMeshComponent"></a>