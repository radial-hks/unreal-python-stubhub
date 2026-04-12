## MaterialFloatPrecisionMode Objects

```python
class MaterialFloatPrecisionMode(EnumBase)
```

The default float precision for material's pixel shaders on mobile devices

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.MaterialFloatPrecisionMode.MFPM_DEFAULT"></a>

#### MFPM\_DEFAULT

0: Uses project based precision mode setting

<a id="unreal.MaterialFloatPrecisionMode.MFPM_FULL_MATERIAL_EXPRESSION_ONLY"></a>

#### MFPM\_FULL\_MATERIAL\_EXPRESSION\_ONLY

1: Force full-precision for MaterialFloat only, no effect on shader codes in .ush/.usf

<a id="unreal.MaterialFloatPrecisionMode.MFPM_FULL"></a>

#### MFPM\_FULL

2: All the floats are full-precision

<a id="unreal.MaterialFloatPrecisionMode.MFPM_HALF"></a>

#### MFPM\_HALF

3: Half precision, except explict 'float' in .ush/.usf

<a id="unreal.MaterialShadingRate"></a>