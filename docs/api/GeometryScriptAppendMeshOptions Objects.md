## GeometryScriptAppendMeshOptions Objects

```python
class GeometryScriptAppendMeshOptions(StructBase)
```

Control how details like mesh attributes are handled when one mesh is appended to another

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBasicEditFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``combine_mode`` (GeometryScriptCombineAttributesMode):  [Read-Write] How attributes from each mesh are combined into the result

<a id="unreal.GeometryScriptAppendMeshOptions.__init__"></a>

#### __init__

```python
def __init__(
    combine_mode:
    GeometryScriptCombineAttributesMode = GeometryScriptCombineAttributesMode.
    ENABLE_ALL_MATCHING
) -> None
```

<a id="unreal.GeometryScriptAppendMeshOptions.combine_mode"></a>

#### combine_mode

```python
@property
def combine_mode() -> GeometryScriptCombineAttributesMode
```

(GeometryScriptCombineAttributesMode):  [Read-Write] How attributes from each mesh are combined into the result

<a id="unreal.GeometryScriptAppendMeshOptions.combine_mode"></a>

#### combine_mode

```python
@combine_mode.setter
def combine_mode(value: GeometryScriptCombineAttributesMode) -> None
```

<a id="unreal.GeometryScriptBoneWeight"></a>