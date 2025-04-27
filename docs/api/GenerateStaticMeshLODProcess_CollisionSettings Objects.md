## GenerateStaticMeshLODProcess_CollisionSettings Objects

```python
class GenerateStaticMeshLODProcess_CollisionSettings(StructBase)
```

Generate Static Mesh LODProcess Collision Settings

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_type`` (GenerateStaticMeshLODSimpleCollisionGeometryType):  [Read-Write] Type of simple collision objects to produce
- ``convex_triangle_count`` (int32):  [Read-Write] Target triangle count for each convex hull after simplification
- ``hull_tolerance`` (float):  [Read-Write] Target minumum edge length for simplified swept convex hulls
- ``prefilter_grid_resolution`` (int32):  [Read-Write] Grid resolution (along the maximum-length axis) for subsampling before computing the convex hull
- ``prefilter_vertices`` (bool):  [Read-Write] Whether to subsample input vertices using a regular grid before computing the convex hull
- ``simplify_polygons`` (bool):  [Read-Write] Whether to simplify polygons used for swept convex hulls
- ``sweep_axis`` (GenerateStaticMeshLODProjectedHullAxisMode):  [Read-Write] Which axis to sweep along when computing swept convex hulls

<a id="unreal.GenerateStaticMeshLODProcess_CollisionSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MetaHumanCustomizableBodyPart"></a>