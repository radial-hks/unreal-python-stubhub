## InterchangeVertexColorImportOption Objects

```python
class InterchangeVertexColorImportOption(EnumBase)
```

EInterchange Vertex Color Import Option

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericAssetsPipelineSharedSettings.h

<a id="unreal.InterchangeVertexColorImportOption.IVCIO_REPLACE"></a>

#### IVCIO\_REPLACE

0: Import the mesh using the vertex colors from the translated source.

<a id="unreal.InterchangeVertexColorImportOption.IVCIO_IGNORE"></a>

#### IVCIO\_IGNORE

1: Ignore vertex colors from the translated source. In case of a reimport, keep the existing mesh vertex colors.

<a id="unreal.InterchangeVertexColorImportOption.IVCIO_OVERRIDE"></a>

#### IVCIO\_OVERRIDE

2: Override all vertex colors with the specified color.

<a id="unreal.InterchangeAnimationRange"></a>