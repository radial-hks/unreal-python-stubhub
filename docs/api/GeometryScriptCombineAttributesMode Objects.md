## GeometryScriptCombineAttributesMode Objects

```python
class GeometryScriptCombineAttributesMode(EnumBase)
```

Options for how attributes from a source and target mesh are combined into the target mesh

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBasicEditFunctions.h

<a id="unreal.GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING"></a>

#### ENABLE\_ALL\_MATCHING

0: Include attributes enabled on either the source or target mesh

<a id="unreal.GeometryScriptCombineAttributesMode.USE_TARGET"></a>

#### USE\_TARGET

1: Only include attributes that are already enabled on the target mesh

<a id="unreal.GeometryScriptCombineAttributesMode.USE_SOURCE"></a>

#### USE\_SOURCE

2: Make the target mesh have only the attributes that are enabled on the source mesh

<a id="unreal.GeometryScriptPruneBoneWeightsAssignmentType"></a>