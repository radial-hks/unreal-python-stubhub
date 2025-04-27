## CreateMaterialObjectParams Objects

```python
class CreateMaterialObjectParams(StructBase)
```

FCreateMaterialObjectParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateMaterialObject().

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_name`` (str):  [Read-Write] The base name of the new Material object
- ``material_to_duplicate`` (MaterialInterface):  [Read-Write] The parent UMaterial of this material will be duplicated to create the new UMaterial Asset.
- ``store_relative_to_object`` (Object):  [Read-Write] An object to store the Material relative to.
- ``target_world`` (World):  [Read-Write] The World/Level the new Material object should be created in (if known).
  Note that Material generally do not exist as objects in a Level.
  However, it may be necessary to store the texture in a path relative to the
  level (for example if the level is in a Plugin, this would be necessary in-Editor)

<a id="unreal.CreateMaterialObjectParams.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CreateMaterialObjectResult"></a>