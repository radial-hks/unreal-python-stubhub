## GeometryScriptLODType Objects

```python
class GeometryScriptLODType(EnumBase)
```

The Type of LOD in a Mesh Asset (ie a StaticMesh Asset)

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptLODType.MAX_AVAILABLE"></a>

#### MAX_AVAILABLE

0: The Maximum-quality available SourceModel LOD (HiResSourceModel if it is available, otherwise SourceModel LOD0)

<a id="unreal.GeometryScriptLODType.HI_RES_SOURCE_MODEL"></a>

#### HI_RES_SOURCE_MODEL

1: The HiRes SourceModel. LOD Index is ignored. HiResSourceModel is not available at Runtime.

<a id="unreal.GeometryScriptLODType.SOURCE_MODEL"></a>

#### SOURCE_MODEL

2: The SourceModel mesh at a given LOD Index. Note that a StaticMesh Asset with Auto-Generated LODs may not have a valid SourceModel for every LOD Index
SourceModel meshes are not available at Runtime.

<a id="unreal.GeometryScriptLODType.RENDER_DATA"></a>

#### RENDER_DATA

3: The Render mesh at at given LOD Index.
A StaticMesh Asset derives its RenderData LODs from it's SourceModel LODs. RenderData LODs always exist for every valid LOD Index.
However the RenderData LODs are not identical to SourceModel LODs, in particular they will be split at UV seams, Hard Normal creases, etc.
RenderData LODs in a StaticMesh Asset are only available at Runtime if the bAllowCPUAccess flag was enabled on the Asset at Cook time.

<a id="unreal.GeometryScriptAxis"></a>