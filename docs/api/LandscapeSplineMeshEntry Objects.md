## LandscapeSplineMeshEntry Objects

```python
class LandscapeSplineMeshEntry(StructBase)
```

Landscape Spline Mesh Entry

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeSplineSegment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center_adjust`` (Vector2D):  [Read-Write] Tweak to center the mesh correctly on the spline
- ``center_h`` (bool):  [Read-Write] Whether to automatically center the mesh horizontally on the spline
- ``forward_axis`` (SplineMeshAxis):  [Read-Write] Chooses the forward axis for the spline mesh orientation
- ``material_overrides`` (Array[MaterialInterface]):  [Read-Write] Overrides mesh's materials
- ``mesh`` (StaticMesh):  [Read-Write] Mesh to use on the spline
- ``no_z_scaling`` (bool):  [Read-Write] Disables scale to width on the mesh Z coordinate
- ``scale`` (Vector):  [Read-Write] Scale of the spline mesh, (Z=Forwards)
- ``scale_to_width`` (bool):  [Read-Write] Whether to scale the mesh to fit the width of the spline
- ``up_axis`` (SplineMeshAxis):  [Read-Write] Chooses the up axis for the spline mesh orientation

<a id="unreal.LandscapeSplineMeshEntry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GrassInput"></a>