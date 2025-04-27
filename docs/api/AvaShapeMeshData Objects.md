## AvaShapeMeshData Objects

```python
class AvaShapeMeshData(StructBase)
```

Represents a mesh section with its material, uv data

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material`` (MaterialInterface):  [Read-Write] mesh material
- ``material_type`` (MaterialType):  [Read-Write] mesh material type
- ``material_uv_params`` (AvaShapeMaterialUVParameters):  [Read-Write] mesh material UV params
- ``mesh_visible`` (bool):  [Read-Write] whether the mesh is currently visible or not and should be editable
- ``override_primary_uv_params`` (bool):  [Read-Write] mesh uses same uv params as primary
- ``parametric_material`` (AvaShapeParametricMaterial):  [Read-Write] parametric material settings

<a id="unreal.AvaShapeMeshData.__init__"></a>

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

<a id="unreal.AvaShapeMeshData.mesh_visible"></a>

#### mesh_visible

```python
@property
def mesh_visible() -> bool
```

(bool):  [Read-Only] whether the mesh is currently visible or not and should be editable

<a id="unreal.AvaShapeMeshData.material_type"></a>

#### material_type

```python
@property
def material_type() -> MaterialType
```

(MaterialType):  [Read-Write] mesh material type

<a id="unreal.AvaShapeMeshData.material_type"></a>

#### material_type

```python
@material_type.setter
def material_type(value: MaterialType) -> None
```

<a id="unreal.AvaShapeMeshData.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] mesh material

<a id="unreal.AvaShapeMeshData.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.AvaShapeMeshData.parametric_material"></a>

#### parametric_material

```python
@property
def parametric_material() -> AvaShapeParametricMaterial
```

(AvaShapeParametricMaterial):  [Read-Write] parametric material settings

<a id="unreal.AvaShapeMeshData.parametric_material"></a>

#### parametric_material

```python
@parametric_material.setter
def parametric_material(value: AvaShapeParametricMaterial) -> None
```

<a id="unreal.AvaShapeMeshData.override_primary_uv_params"></a>

#### override_primary_uv_params

```python
@property
def override_primary_uv_params() -> bool
```

(bool):  [Read-Write] mesh uses same uv params as primary

<a id="unreal.AvaShapeMeshData.override_primary_uv_params"></a>

#### override_primary_uv_params

```python
@override_primary_uv_params.setter
def override_primary_uv_params(value: bool) -> None
```

<a id="unreal.AvaShapeMeshData.material_uv_params"></a>

#### material_uv_params

```python
@property
def material_uv_params() -> AvaShapeMaterialUVParameters
```

(AvaShapeMaterialUVParameters):  [Read-Write] mesh material UV params

<a id="unreal.AvaShapeMeshData.material_uv_params"></a>

#### material_uv_params

```python
@material_uv_params.setter
def material_uv_params(value: AvaShapeMaterialUVParameters) -> None
```

<a id="unreal.AvaToolboxMeshData"></a>