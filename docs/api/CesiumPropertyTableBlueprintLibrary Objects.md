## CesiumPropertyTableBlueprintLibrary Objects

```python
class CesiumPropertyTableBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Property Table Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTable.h

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_property_table_status"></a>

#### get\_property\_table\_status

```python
@classmethod
def get_property_table_status(
        cls, property_table: CesiumPropertyTable) -> CesiumPropertyTableStatus
```

X.get_property_table_status(property_table) -> CesiumPropertyTableStatus
Gets the status of the property table. If an error occurred while parsing
the property table from the glTF extension, this briefly conveys why.

Args:
    property_table (CesiumPropertyTable): 

Returns:
    CesiumPropertyTableStatus:

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_property_table_name"></a>

#### get\_property\_table\_name

```python
@classmethod
def get_property_table_name(cls, property_table: CesiumPropertyTable) -> str
```

X.get_property_table_name(property_table) -> str
Gets the name of the property table. If no name was specified in the glTF
extension, this returns an empty string.

Args:
    property_table (CesiumPropertyTable): 

Returns:
    str:

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_property_table_count"></a>

#### get\_property\_table\_count

```python
@classmethod
def get_property_table_count(cls, property_table: CesiumPropertyTable) -> int
```

X.get_property_table_count(property_table) -> int64
Gets the number of values each property in the table is expected to have.
If an error occurred while parsing the property table, this returns zero.

Args:
    property_table (CesiumPropertyTable): 

Returns:
    int64:

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_number_of_features"></a>

#### get\_number\_of\_features

```python
@classmethod
def get_number_of_features(cls, property_table: CesiumPropertyTable) -> int
```

deprecated: 'get_number_of_features' was renamed to 'get_property_table_count'.

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_property_names"></a>

#### get\_property\_names

```python
@classmethod
def get_property_names(cls, property_table: CesiumPropertyTable) -> Array[str]
```

X.get_property_names(property_table) -> Array[str]
Gets the names of the properties in this property table.

Args:
    property_table (CesiumPropertyTable): 

Returns:
    Array[str]:

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_properties"></a>

#### get\_properties

```python
@classmethod
def get_properties(
    cls, property_table: CesiumPropertyTable
) -> Map[str, CesiumPropertyTableProperty]
```

X.get_properties(property_table) -> Map[str, CesiumPropertyTableProperty]
Gets all the properties of the property table, mapped by property name.

Args:
    property_table (CesiumPropertyTable): 

Returns:
    Map[str, CesiumPropertyTableProperty]:

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_metadata_values_for_feature_as_strings"></a>

#### get\_metadata\_values\_for\_feature\_as\_strings

```python
@classmethod
def get_metadata_values_for_feature_as_strings(
        cls, property_table: CesiumPropertyTable,
        feature_id: int) -> Map[str, str]
```

X.get_metadata_values_for_feature_as_strings(property_table, feature_id) -> Map[str, str]
Gets all of the property values for a given feature as strings, mapped by
property name. This will only include values from valid property table
properties.

Array properties cannot be converted to strings, so empty strings
will be returned for their values.

If the feature ID is out-of-bounds, the returned map will be empty.
deprecated: Use GetValuesAsStrings to convert the output of GetMetadataValuesForFeature instead.

Args:
    property_table (CesiumPropertyTable): 
    feature_id (int64): The ID of the feature.

Returns:
    Map[str, str]: The property values as strings mapped by property name.

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_metadata_values_as_string_for_feature_id"></a>

#### get\_metadata\_values\_as\_string\_for\_feature\_id

```python
@classmethod
def get_metadata_values_as_string_for_feature_id(
        cls, property_table: CesiumPropertyTable,
        feature_id: int) -> Map[str, str]
```

deprecated: 'get_metadata_values_as_string_for_feature_id' was renamed to 'get_metadata_values_for_feature_as_strings'.

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_metadata_values_for_feature"></a>

#### get\_metadata\_values\_for\_feature

```python
@classmethod
def get_metadata_values_for_feature(
        cls, property_table: CesiumPropertyTable,
        feature_id: int) -> Map[str, CesiumMetadataValue]
```

X.get_metadata_values_for_feature(property_table, feature_id) -> Map[str, CesiumMetadataValue]
Gets all of the property values for a given feature, mapped by property
name. This will only include values from valid property table properties.

If the feature ID is out-of-bounds, the returned map will be empty.

Args:
    property_table (CesiumPropertyTable): 
    feature_id (int64): The ID of the feature.

Returns:
    Map[str, CesiumMetadataValue]: The property values mapped by property name.

<a id="unreal.CesiumPropertyTableBlueprintLibrary.get_metadata_values_for_feature_id"></a>

#### get\_metadata\_values\_for\_feature\_id

```python
@classmethod
def get_metadata_values_for_feature_id(
        cls, property_table: CesiumPropertyTable,
        feature_id: int) -> Map[str, CesiumMetadataValue]
```

deprecated: 'get_metadata_values_for_feature_id' was renamed to 'get_metadata_values_for_feature'.

<a id="unreal.CesiumPropertyTableBlueprintLibrary.find_property"></a>

#### find\_property

```python
@classmethod
def find_property(cls, property_table: CesiumPropertyTable,
                  property_name: str) -> CesiumPropertyTableProperty
```

X.find_property(property_table, property_name) -> CesiumPropertyTableProperty
Retrieve a FCesiumPropertyTableProperty by name. If the property table
does not contain a property with that name, this returns an invalid
FCesiumPropertyTableProperty.

Args:
    property_table (CesiumPropertyTable): 
    property_name (str): 

Returns:
    CesiumPropertyTableProperty:

<a id="unreal.CesiumFeatureTableBlueprintLibrary"></a>