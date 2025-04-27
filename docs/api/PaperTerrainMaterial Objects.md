## PaperTerrainMaterial Objects

```python
class PaperTerrainMaterial(DataAsset)
```

Paper Terrain Material

'Material' setup for a 2D terrain spline (stores references to sprites that will be instanced along the spline path, not actually related to UMaterialInterface).

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTerrainMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``interior_fill`` (PaperSprite):  [Read-Write] The sprite to use for an interior region fill
- ``rules`` (Array[PaperTerrainMaterialRule]):  [Read-Write]

<a id="unreal.PaperTerrainSplineComponent"></a>