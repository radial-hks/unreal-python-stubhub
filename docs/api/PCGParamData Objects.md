## PCGParamData Objects

```python
class PCGParamData(PCGData)
```

Class to hold execution parameters that will be consumed in nodes of the graph

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGParamData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved

<a id="unreal.PCGParamData.mutable_metadata"></a>

#### mutable_metadata

```python
def mutable_metadata() -> PCGMetadata
```

x.mutable_metadata() -> PCGMetadata
Mutable Metadata

Returns:
    PCGMetadata:

<a id="unreal.PCGParamData.k2_filter_params_by_name"></a>

#### k2_filter_params_by_name

```python
def k2_filter_params_by_name(name: Name) -> PCGParamData
```

x.k2_filter_params_by_name(name) -> PCGParamData
Creates a new params that keeps only a given key/name

Args:
    name (Name): 

Returns:
    PCGParamData:

<a id="unreal.PCGParamData.filter_params_by_name"></a>

#### filter_params_by_name

```python
def filter_params_by_name(name: Name) -> PCGParamData
```

deprecated: 'filter_params_by_name' was renamed to 'k2_filter_params_by_name'.

<a id="unreal.PCGParamData.k2_filter_params_by_key"></a>

#### k2_filter_params_by_key

```python
def k2_filter_params_by_key(key: int) -> PCGParamData
```

x.k2_filter_params_by_key(key) -> PCGParamData
K2 Filter Params by Key

Args:
    key (int64): 

Returns:
    PCGParamData:

<a id="unreal.PCGParamData.filter_params_by_key"></a>

#### filter_params_by_key

```python
def filter_params_by_key(key: int) -> PCGParamData
```

deprecated: 'filter_params_by_key' was renamed to 'k2_filter_params_by_key'.

<a id="unreal.PCGParamData.find_or_add_metadata_key"></a>

#### find_or_add_metadata_key

```python
def find_or_add_metadata_key(name: Name) -> int
```

x.find_or_add_metadata_key(name) -> int64
Creates an entry for the given name, if not already added

Args:
    name (Name): 

Returns:
    int64:

<a id="unreal.PCGParamData.find_metadata_key"></a>

#### find_metadata_key

```python
def find_metadata_key(name: Name) -> int
```

x.find_metadata_key(name) -> int64
Returns the entry for the given name

Args:
    name (Name): 

Returns:
    int64:

<a id="unreal.PCGParamData.const_metadata"></a>

#### const_metadata

```python
def const_metadata() -> PCGMetadata
```

x.const_metadata() -> PCGMetadata
~End UPCGData interface

Returns:
    PCGMetadata:

<a id="unreal.PCGBlueprintPinHelpers"></a>