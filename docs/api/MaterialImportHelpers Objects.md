## MaterialImportHelpers Objects

```python
class MaterialImportHelpers(Object)
```

Material Import Helpers

**C++ Source:**

- **Module**: UnrealEd
- **File**: MaterialImportHelpers.h

<a id="unreal.MaterialImportHelpers.find_existing_material_from_search_location"></a>

#### find_existing_material_from_search_location

```python
@classmethod
def find_existing_material_from_search_location(
        cls, material_full_name: str, base_package_path: str,
        search_location: MaterialSearchLocation
) -> Tuple[MaterialInterface, Text]
```

X.find_existing_material_from_search_location(material_full_name, base_package_path, search_location) -> (MaterialInterface, out_error=Text)
Find Existing Material from Search Location

Args:
    material_full_name (str): 
    base_package_path (str): 
    search_location (MaterialSearchLocation): 

Returns:
    Text: 

    out_error (Text):

<a id="unreal.MaterialImportHelpers.find_existing_material"></a>

#### find_existing_material

```python
@classmethod
def find_existing_material(
        cls, base_path: str, material_full_name: str,
        recursive_paths: bool) -> Tuple[MaterialInterface, Text]
```

X.find_existing_material(base_path, material_full_name, recursive_paths) -> (MaterialInterface, out_error=Text)
Find Existing Material

Args:
    base_path (str): 
    material_full_name (str): 
    recursive_paths (bool): 

Returns:
    Text: 

    out_error (Text):

<a id="unreal.MaterialInstanceConstantFactoryNew"></a>