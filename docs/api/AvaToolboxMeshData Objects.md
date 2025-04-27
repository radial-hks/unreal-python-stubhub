## AvaToolboxMeshData Objects

```python
class AvaToolboxMeshData(AvaShapeMeshData)
```

deprecated: 'AvaToolboxMeshData' was renamed to 'AvaShapeMeshData'.

<a id="unreal.AvaToolboxMeshData.__init__"></a>

#### __init__

```python
def __init__(
    mesh_visible: bool = False,
    material_type: MaterialType = MaterialType.ASSET,
    material: MaterialInterface = None,
    parametric_material: AvaShapeParametricMaterial = [
        True, AvaShapeParametricMaterialStyle.SOLID,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000, 1.000000], 0.500000, False, True
    ],
    override_primary_uv_params: bool = False,
    material_uv_params: AvaShapeMaterialUVParameters = [
        AvaShapeUVMode.UNIFORM, AvaAnchors.CENTER, [0.500000, 0.500000],
        [1.000000, 1.000000], [0.000000, 0.000000], 0.000000, False, False
    ]
) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters"></a>