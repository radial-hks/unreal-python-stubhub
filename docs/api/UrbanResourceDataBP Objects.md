## UrbanResourceDataBP Objects

```python
class UrbanResourceDataBP(BlueprintFunctionLibrary)
```

Urban Resource Data BP

**C++ Source:**

- **Plugin**: AesBuilderCommon
- **Module**: UrbanComData
- **File**: UrbanResourceData.h

<a id="unreal.UrbanResourceDataBP.create_data_table_from_string_data"></a>

#### create\_data\_table\_from\_string\_data

```python
@classmethod
def create_data_table_from_string_data(cls,
                                       table: DataTable,
                                       type: StringDataType,
                                       string_data: str = "") -> None
```

X.create_data_table_from_string_data(table, type, string_data="") -> None
Create Data Table from String Data

Args:
    table (DataTable): 
    type (StringDataType): 
    string_data (str):

<a id="unreal.UrbanResourceDataBP.add_cache_data_from_spline"></a>

#### add\_cache\_data\_from\_spline

```python
@classmethod
def add_cache_data_from_spline(cls,
                               data_name: Name,
                               spline_component: SplineComponent,
                               extra_property_name: Name,
                               identity_name: str = "") -> None
```

X.add_cache_data_from_spline(data_name, spline_component, extra_property_name, identity_name="") -> None
Add Cache Data from Spline

Args:
    data_name (Name): 
    spline_component (SplineComponent): 
    extra_property_name (Name): 
    identity_name (str):

<a id="unreal.UrbanResourceDataBP.add_cache_data_from_data_table_with_title"></a>

#### add\_cache\_data\_from\_data\_table\_with\_title

```python
@classmethod
def add_cache_data_from_data_table_with_title(cls,
                                              table: DataTable,
                                              identity_name: str = "") -> None
```

X.add_cache_data_from_data_table_with_title(table, identity_name="") -> None
Add Cache Data from Data Table with Title

Args:
    table (DataTable): 
    identity_name (str):

<a id="unreal.UrbanResourceDataBP.add_cache_data_from_data_table"></a>

#### add\_cache\_data\_from\_data\_table

```python
@classmethod
def add_cache_data_from_data_table(cls,
                                   data_name: Name,
                                   table: DataTable,
                                   identity_name: str = "") -> None
```

X.add_cache_data_from_data_table(data_name, table, identity_name="") -> None
Add Cache Data from Data Table

Args:
    data_name (Name): 
    table (DataTable): 
    identity_name (str):

<a id="unreal.UrbanResourceDataBP.add_cache_data"></a>

#### add\_cache\_data

```python
@classmethod
def add_cache_data(cls,
                   data_name: Name,
                   provider_obj: Object,
                   property_name: Name,
                   identity_name: str = "") -> None
```

X.add_cache_data(data_name, provider_obj, property_name, identity_name="") -> None
Add Cache Data

Args:
    data_name (Name): 
    provider_obj (Object): 
    property_name (Name): 
    identity_name (str):

<a id="unreal.UrbanResourceDataBP.add_bgeo_cache_data_from_file_path"></a>

#### add\_bgeo\_cache\_data\_from\_file\_path

```python
@classmethod
def add_bgeo_cache_data_from_file_path(cls,
                                       data_name: Name,
                                       file_path: str,
                                       identity_name: str = "") -> None
```

X.add_bgeo_cache_data_from_file_path(data_name, file_path, identity_name="") -> None
Add Bgeo Cache Data from File Path

Args:
    data_name (Name): 
    file_path (str): 
    identity_name (str):

<a id="unreal.EditorUtilityObject"></a>