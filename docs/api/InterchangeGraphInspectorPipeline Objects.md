## InterchangeGraphInspectorPipeline Objects

```python
class InterchangeGraphInspectorPipeline(InterchangePipelineBase)
```

This pipeline is the generic pipeline option for all types of meshes. It should be called before specialized mesh pipelines like the generic static mesh or skeletal mesh pipelines.
All import options that are shared between mesh types should be added here.

UPROPERTY possible meta values:
meta: ImportOnly - Boolean. The property is used only for import, not for reimport. Cannot be mixed with ReimportOnly.
meta: ReimportOnly - Boolean. The property is used only for reimport, not for import. Cannot be mixed with ImportOnly.
meta: MeshType - String. The property is for static mesh or skeletal mesh or both. If not specified, it will apply to all mesh types.

**C++ Source:**

- **Plugin**: InterchangeEditor
- **Module**: InterchangeEditorPipelines
- **File**: InterchangeGraphInspectorPipeline.h

<a id="unreal.InterchangePipelineConfigurationGeneric"></a>