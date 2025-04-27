## GLTFMaterialVariantMode Objects

```python
class GLTFMaterialVariantMode(EnumBase)
```

EGLTFMaterial Variant Mode

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFExportOptions.h

<a id="unreal.GLTFMaterialVariantMode.NONE"></a>

#### NONE

0: Never export material variants.

<a id="unreal.GLTFMaterialVariantMode.SIMPLE"></a>

#### SIMPLE

1: Export material variants but only use a simple quad if a material input needs to be baked out.

<a id="unreal.GLTFMaterialVariantMode.USE_MESH_DATA"></a>

#### USE_MESH_DATA

2: Export material variants and allow usage of the mesh data if a material input needs to be baked out with vertex data.

<a id="unreal.GLTFMaterialBakeMode"></a>