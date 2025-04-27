## GeometryCollectionLibrary Objects

```python
class GeometryCollectionLibrary(BlueprintFunctionLibrary)
```

Blueprint library for Geometry Collections.

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionBlueprintLibrary.h

<a id="unreal.GeometryCollectionLibrary.set_ism_pool_custom_instance_data"></a>

#### set_ism_pool_custom_instance_data

```python
@classmethod
def set_ism_pool_custom_instance_data(
        cls, geometry_collection_component: GeometryCollectionComponent,
        custom_data_index: int, custom_data_value: float) -> None
```

X.set_ism_pool_custom_instance_data(geometry_collection_component, custom_data_index, custom_data_value) -> None
Set ISMPool Custom Instance Data
deprecated: Use SetCustomInstanceDataByIndex() instead

Args:
    geometry_collection_component (GeometryCollectionComponent): 
    custom_data_index (int32): 
    custom_data_value (float):

<a id="unreal.GeometryCollectionLibrary.set_custom_instance_data_by_name"></a>

#### set_custom_instance_data_by_name

```python
@classmethod
def set_custom_instance_data_by_name(
        cls, geometry_collection_component: GeometryCollectionComponent,
        custom_data_name: Name, custom_data_value: float) -> None
```

X.set_custom_instance_data_by_name(geometry_collection_component, custom_data_name, custom_data_value) -> None
Set a custom instance data value for all instances associated with a geometry collection.
This assumes that the geometry collection is using a custom renderer that supports IGeometryCollectionCustomDataInterface.

Args:
    geometry_collection_component (GeometryCollectionComponent): The Geometry Collection Component that we want to set custom instance data on.
    custom_data_name (Name): The name of the custom instance data slot that we want to set.
    custom_data_value (float): The value to set to the custom instance data slot.

<a id="unreal.GeometryCollectionLibrary.set_custom_instance_data_by_index"></a>

#### set_custom_instance_data_by_index

```python
@classmethod
def set_custom_instance_data_by_index(
        cls, geometry_collection_component: GeometryCollectionComponent,
        custom_data_index: int, custom_data_value: float) -> None
```

X.set_custom_instance_data_by_index(geometry_collection_component, custom_data_index, custom_data_value) -> None
Set a custom instance data value for all instances associated with a geometry collection.
This assumes that the geometry collection is using a custom renderer that supports IGeometryCollectionCustomDataInterface.

Args:
    geometry_collection_component (GeometryCollectionComponent): The Geometry Collection Component that we want to set custom instance data on.
    custom_data_index (int32): The index of the custom instance data slot that we want to set.
    custom_data_value (float): The value to set to the custom instance data slot.

<a id="unreal.ChaosDestructionListener"></a>