## UrbanResourceStruct Objects

```python
class UrbanResourceStruct(StructBase)
```

Urban Resource Struct

**C++ Source:**

- **Plugin**: AesBuilderCommon
- **Module**: UrbanBuildDataAsset
- **File**: UrbanBuildDataAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_template`` (type(Class)):  [Read-Write]
- ``extern_data_float`` (Map[str, UrbanResourceDataStructFloat]):  [Read-Write]
- ``extern_data_int`` (Map[str, UrbanResourceDataStructInt]):  [Read-Write] UPROPERTY(EditAnywhere, Category = "Resource Data", meta = (AllowedClasses = "Blueprint" ))
         FSoftObjectPath DynamicExternDataObj;
- ``extern_data_string`` (Map[str, UrbanResourceDataStructString]):  [Read-Write]
- ``resource`` (SoftObjectPath):  [Read-Write] , meta = (AllowedClasses = "StaticMesh, Blueprint" )

<a id="unreal.UrbanResourceStruct.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ValidateAssetsDetails"></a>