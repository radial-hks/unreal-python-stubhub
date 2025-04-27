## SplineMeshParams Objects

```python
class SplineMeshParams(StructBase)
```

Structure that holds info about spline, passed to renderer to deform UStaticMesh.
Also used by Lightmass, so be sure to update Lightmass::FSplineMeshParams and the static lighting code if this changes!

**C++ Source:**

- **Module**: Engine
- **File**: SplineMeshComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_offset`` (Vector2D):  [Read-Write] Ending offset of the mesh from the spline, in component space.
- ``end_pos`` (Vector):  [Read-Write] End location of spline, in component space.
- ``end_roll`` (float):  [Read-Write] Roll around spline applied at end, in radians.
- ``end_scale`` (Vector2D):  [Read-Write] X and Y scale applied to mesh at end of spline.
- ``end_tangent`` (Vector):  [Read-Write] End tangent of spline, in component space.
- ``nanite_cluster_bounds_scale`` (float):  [Read-Write] How much to scale the calculated culling bounds of Nanite clusters after deformation.
  NOTE: This should only be set greater than 1.0 if it fixes visible issues with clusters being
  incorrectly culled.
- ``start_offset`` (Vector2D):  [Read-Write] Starting offset of the mesh from the spline, in component space.
- ``start_pos`` (Vector):  [Read-Write] Start location of spline, in component space.
- ``start_roll`` (float):  [Read-Write] Roll around spline applied at start, in radians.
- ``start_scale`` (Vector2D):  [Read-Write] X and Y scale applied to mesh at start of spline.
- ``start_tangent`` (Vector):  [Read-Write] Start tangent of spline, in component space.

<a id="unreal.SplineMeshParams.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.DialogueContextMapping"></a>