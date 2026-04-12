## CesiumMetadataBlueprintType Objects

```python
class CesiumMetadataBlueprintType(EnumBase)
```

The Blueprint type that can losslessly represent values of a given property.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataValueType.h

<a id="unreal.CesiumMetadataBlueprintType.NONE"></a>

#### NONE

0: Indicates a value cannot be represented in Blueprints.

<a id="unreal.CesiumMetadataBlueprintType.BOOLEAN"></a>

#### BOOLEAN

1: Indicates a value is best represented as a Boolean.

<a id="unreal.CesiumMetadataBlueprintType.BYTE"></a>

#### BYTE

2: Indicates a value is best represented as a Byte (8-bit unsigned integer).

<a id="unreal.CesiumMetadataBlueprintType.INTEGER"></a>

#### INTEGER

3: Indicates a value is best represented as a Integer (32-bit signed).

<a id="unreal.CesiumMetadataBlueprintType.INTEGER64"></a>

#### INTEGER64

4: Indicates a value is best represented as a Integer64 (64-bit signed).

<a id="unreal.CesiumMetadataBlueprintType.FLOAT"></a>

#### FLOAT

5: Indicates a value is best represented as a Float (32-bit).

<a id="unreal.CesiumMetadataBlueprintType.FLOAT64"></a>

#### FLOAT64

6: Indicates a value is best represented as a Float64 (64-bit).

<a id="unreal.CesiumMetadataBlueprintType.INT_POINT"></a>

#### INT\_POINT

7: Indicates a value is best represented as a FVector2D (2-dimensional
    integer vector).

<a id="unreal.CesiumMetadataBlueprintType.VECTOR2D"></a>

#### VECTOR2D

8: Indicates a value is best represented as a FVector2D (2-dimensional
    double-precision vector).

<a id="unreal.CesiumMetadataBlueprintType.INT_VECTOR"></a>

#### INT\_VECTOR

9: Indicates a value is best represented as a FIntVector (3-dimensional
    integer vector).

<a id="unreal.CesiumMetadataBlueprintType.VECTOR3F"></a>

#### VECTOR3F

10: Indicates a value is best represented as a FVector3f (3-dimensional
    single-precision vector).

<a id="unreal.CesiumMetadataBlueprintType.VECTOR3"></a>

#### VECTOR3

11: Indicates a value is best represented as a FVector3 (3-dimensional
    double-precision vector).

<a id="unreal.CesiumMetadataBlueprintType.VECTOR4"></a>

#### VECTOR4

12: Indicates a value is best represented as a FVector4 (4-dimensional
    double-precision vector).

<a id="unreal.CesiumMetadataBlueprintType.MATRIX"></a>

#### MATRIX

13: Indicates a value is best represented as a FMatrix (4-by-4 double-precision
    matrix).

<a id="unreal.CesiumMetadataBlueprintType.STRING"></a>

#### STRING

14: Indicates a value is best represented as a FString. This can be used as a
    fallback for types with no proper Blueprints representation.

<a id="unreal.CesiumMetadataBlueprintType.ARRAY"></a>

#### ARRAY

15: Indicates a value is best represented as a CesiumPropertyArray.

<a id="unreal.CesiumMetadataTrueType_DEPRECATED"></a>