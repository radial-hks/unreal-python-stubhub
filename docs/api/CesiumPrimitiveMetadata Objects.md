## CesiumPrimitiveMetadata Objects

```python
class CesiumPrimitiveMetadata(StructBase)
```

A Blueprint-accessible wrapper for a glTF Primitive's EXT_structural_metadata
extension. It holds the indices of the property textures / attributes
associated with this primitive, which index into the respective arrays in the
model's EXT_structural_metadata extension.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPrimitiveMetadata.h

<a id="unreal.CesiumPrimitiveMetadata.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumPropertyArray"></a>