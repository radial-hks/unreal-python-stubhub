## CesiumPrimitiveMetadataBlueprintLibrary Objects

```python
class CesiumPrimitiveMetadataBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Primitive Metadata Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPrimitiveMetadata.h

<a id="unreal.CesiumPrimitiveMetadataBlueprintLibrary.get_property_texture_indices"></a>

#### get\_property\_texture\_indices

```python
@classmethod
def get_property_texture_indices(
        cls, primitive_metadata: CesiumPrimitiveMetadata) -> Array[int]
```

X.get_property_texture_indices(primitive_metadata) -> Array[int64]
Get the indices of the property textures that are associated with the
primitive. This can be used to retrieve the actual property textures from
the model's FCesiumModelMetadata.

Args:
    primitive_metadata (CesiumPrimitiveMetadata): 

Returns:
    Array[int64]:

<a id="unreal.CesiumPrimitiveMetadataBlueprintLibrary.get_property_attribute_indices"></a>

#### get\_property\_attribute\_indices

```python
@classmethod
def get_property_attribute_indices(
        cls, primitive_metadata: CesiumPrimitiveMetadata) -> Array[int]
```

X.get_property_attribute_indices(primitive_metadata) -> Array[int64]
Get the indices of the property attributes that are associated with the
primitive. This can be used to retrieve the actual property attributes from
the model's FCesiumModelMetadata.

Args:
    primitive_metadata (CesiumPrimitiveMetadata): 

Returns:
    Array[int64]:

<a id="unreal.CesiumPrimitiveMetadataBlueprintLibrary.get_primitive_metadata"></a>

#### get\_primitive\_metadata

```python
@classmethod
def get_primitive_metadata(
        cls, component: PrimitiveComponent) -> CesiumPrimitiveMetadata
```

X.get_primitive_metadata(component) -> CesiumPrimitiveMetadata
Gets the primitive metadata of a glTF primitive component. If component is
not a Cesium glTF primitive component, the returned metadata is empty.

Args:
    component (PrimitiveComponent): 

Returns:
    CesiumPrimitiveMetadata:

<a id="unreal.CesiumPropertyArrayBlueprintLibrary"></a>