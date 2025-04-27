## AssetImportData Objects

```python
class AssetImportData(Object)
```

todo: Make this class better suited to multiple import paths - maybe have FAssetImportInfo use a map rather than array?

**C++ Source:**

- **Module**: Engine
- **File**: AssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.

<a id="unreal.AssetImportData.scripted_add_filename"></a>

#### scripted_add_filename

```python
def scripted_add_filename(path: str, index: int,
                          source_file_label: str) -> None
```

x.scripted_add_filename(path, index, source_file_label) -> None
Add or update a filename at the specified index. If the index is greater then the number of source file,
it will add empty filenames to fill up to the specified index. The timespan and MD5 will be computed.

Args:
    path (str): 
    index (int32): 
    source_file_label (str):

<a id="unreal.AssetImportData.get_first_filename"></a>

#### get_first_filename

```python
def get_first_filename() -> str
```

x.get_first_filename() -> str
Helper function to return the first filename stored in this data. The resulting filename will be absolute (ie, not relative to the asset).

Returns:
    str:

<a id="unreal.AssetImportData.extract_filenames"></a>

#### extract_filenames

```python
def extract_filenames() -> Array[str]
```

x.extract_filenames() -> Array[str]
K2 Extract Filenames

Returns:
    Array[str]:

<a id="unreal.InterchangeAssetImportData"></a>