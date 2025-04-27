## MeshVertexPainterLibrary Objects

```python
class MeshVertexPainterLibrary(BlueprintFunctionLibrary)
```

Mesh Vertex Painter Kismet Library

**C++ Source:**

- **Module**: Engine
- **File**: MeshVertexPainterKismetLibrary.h

<a id="unreal.MeshVertexPainterLibrary.remove_painted_vertices"></a>

#### remove_painted_vertices

```python
@classmethod
def remove_painted_vertices(
        cls, static_mesh_component: StaticMeshComponent) -> None
```

X.remove_painted_vertices(static_mesh_component) -> None
Removes vertex colors on a mesh component

Args:
    static_mesh_component (StaticMeshComponent):

<a id="unreal.MeshVertexPainterLibrary.paint_vertices_single_color"></a>

#### paint_vertices_single_color

```python
@classmethod
def paint_vertices_single_color(cls,
                                static_mesh_component: StaticMeshComponent,
                                fill_color: LinearColor,
                                convert_to_srgb: bool = True) -> None
```

X.paint_vertices_single_color(static_mesh_component, fill_color, convert_to_srgb=True) -> None
Paints vertex colors on a mesh component in a specified color.

Args:
    static_mesh_component (StaticMeshComponent): 
    fill_color (LinearColor): 
    convert_to_srgb (bool):

<a id="unreal.MeshVertexPainterLibrary.paint_vertices_lerp_along_axis"></a>

#### paint_vertices_lerp_along_axis

```python
@classmethod
def paint_vertices_lerp_along_axis(cls,
                                   static_mesh_component: StaticMeshComponent,
                                   start_color: LinearColor,
                                   end_color: LinearColor,
                                   axis: VertexPaintAxis,
                                   convert_to_srgb: bool = True) -> None
```

X.paint_vertices_lerp_along_axis(static_mesh_component, start_color, end_color, axis, convert_to_srgb=True) -> None
Paints vertex colors on a mesh component lerping from the start to the end color along the specified axis.

Args:
    static_mesh_component (StaticMeshComponent): 
    start_color (LinearColor): 
    end_color (LinearColor): 
    axis (VertexPaintAxis): 
    convert_to_srgb (bool):

<a id="unreal.NavigationObjectBase"></a>