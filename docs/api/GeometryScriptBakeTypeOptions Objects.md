## GeometryScriptBakeTypeOptions Objects

```python
class GeometryScriptBakeTypeOptions(StructBase)
```

Opaque struct for storing bake type options.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_type`` (GeometryScriptBakeTypes):  [Read-Write] The bake output type to generate

<a id="unreal.GeometryScriptBakeTypeOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        bake_type: GeometryScriptBakeTypes = GeometryScriptBakeTypes.NONE
) -> None
```

<a id="unreal.GeometryScriptBakeTypeOptions.bake_type"></a>

#### bake\_type

```python
@property
def bake_type() -> GeometryScriptBakeTypes
```

(GeometryScriptBakeTypes):  [Read-Only] The bake output type to generate

<a id="unreal.GeometryScriptBakeTextureOptions"></a>