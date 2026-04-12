## glTFRuntimeFunctionLibrary Objects

```python
class glTFRuntimeFunctionLibrary(BlueprintFunctionLibrary)
```

Gl TFRuntime Function Library

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeFunctionLibrary.h

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_runtime_path_item_array_from_json_path"></a>

#### gl\_tf\_runtime\_path\_item\_array\_from\_json\_path

```python
@classmethod
def gl_tf_runtime_path_item_array_from_json_path(
        cls, json_path: str) -> Array[glTFRuntimePathItem]
```

X.gl_tf_runtime_path_item_array_from_json_path(json_path) -> Array[glTFRuntimePathItem]
Gl TFRuntime Path Item Array from JSONPath

Args:
    json_path (str): 

Returns:
    Array[glTFRuntimePathItem]:

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_merge_runtime_lo_ds"></a>

#### gl\_tf\_merge\_runtime\_lo\_ds

```python
@classmethod
def gl_tf_merge_runtime_lo_ds(
        cls, runtime_lo_ds: Array[glTFRuntimeMeshLOD]) -> glTFRuntimeMeshLOD
```

X.gl_tf_merge_runtime_lo_ds(runtime_lo_ds) -> glTFRuntimeMeshLOD
Gl TFMerge Runtime LODs

Args:
    runtime_lo_ds (Array[glTFRuntimeMeshLOD]): 

Returns:
    glTFRuntimeMeshLOD:

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_url_with_progress"></a>

#### gl\_tf\_load\_asset\_from\_url\_with\_progress

```python
@classmethod
def gl_tf_load_asset_from_url_with_progress(
        cls, url: str, headers: Map[str, str],
        completed: glTFRuntimeHttpResponse, progress: glTFRuntimeHttpProgress,
        loader_config: glTFRuntimeConfig) -> None
```

X.gl_tf_load_asset_from_url_with_progress(url, headers, completed, progress, loader_config) -> None
Gl TFLoad Asset from Url with Progress

Args:
    url (str): 
    headers (Map[str, str]): 
    completed (glTFRuntimeHttpResponse): 
    progress (glTFRuntimeHttpProgress): 
    loader_config (glTFRuntimeConfig):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_url"></a>

#### gl\_tf\_load\_asset\_from\_url

```python
@classmethod
def gl_tf_load_asset_from_url(cls, url: str, headers: Map[str, str],
                              completed: glTFRuntimeHttpResponse,
                              loader_config: glTFRuntimeConfig) -> None
```

X.gl_tf_load_asset_from_url(url, headers, completed, loader_config) -> None
Gl TFLoad Asset from Url

Args:
    url (str): 
    headers (Map[str, str]): 
    completed (glTFRuntimeHttpResponse): 
    loader_config (glTFRuntimeConfig):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_string_async"></a>

#### gl\_tf\_load\_asset\_from\_string\_async

```python
@classmethod
def gl_tf_load_asset_from_string_async(
        cls, json_data: str, loader_config: glTFRuntimeConfig,
        completed: glTFRuntimeHttpResponse) -> None
```

X.gl_tf_load_asset_from_string_async(json_data, loader_config, completed) -> None
Gl TFLoad Asset from String Async

Args:
    json_data (str): 
    loader_config (glTFRuntimeConfig): 
    completed (glTFRuntimeHttpResponse):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_string"></a>

#### gl\_tf\_load\_asset\_from\_string

```python
@classmethod
def gl_tf_load_asset_from_string(
        cls, json_data: str,
        loader_config: glTFRuntimeConfig) -> glTFRuntimeAsset
```

X.gl_tf_load_asset_from_string(json_data, loader_config) -> glTFRuntimeAsset
Gl TFLoad Asset from String

Args:
    json_data (str): 
    loader_config (glTFRuntimeConfig): 

Returns:
    glTFRuntimeAsset:

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_filename_async"></a>

#### gl\_tf\_load\_asset\_from\_filename\_async

```python
@classmethod
def gl_tf_load_asset_from_filename_async(
        cls, filename: str, path_relative_to_content: bool,
        loader_config: glTFRuntimeConfig,
        completed: glTFRuntimeHttpResponse) -> None
```

X.gl_tf_load_asset_from_filename_async(filename, path_relative_to_content, loader_config, completed) -> None
Gl TFLoad Asset from Filename Async

Args:
    filename (str): 
    path_relative_to_content (bool): 
    loader_config (glTFRuntimeConfig): 
    completed (glTFRuntimeHttpResponse):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_filename"></a>

#### gl\_tf\_load\_asset\_from\_filename

```python
@classmethod
def gl_tf_load_asset_from_filename(
        cls, filename: str, path_relative_to_content: bool,
        loader_config: glTFRuntimeConfig) -> glTFRuntimeAsset
```

X.gl_tf_load_asset_from_filename(filename, path_relative_to_content, loader_config) -> glTFRuntimeAsset
Gl TFLoad Asset from Filename

Args:
    filename (str): 
    path_relative_to_content (bool): 
    loader_config (glTFRuntimeConfig): 

Returns:
    glTFRuntimeAsset:

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_file_map_async"></a>

#### gl\_tf\_load\_asset\_from\_file\_map\_async

```python
@classmethod
def gl_tf_load_asset_from_file_map_async(
        cls, file_map: Map[str, str], loader_config: glTFRuntimeConfig,
        completed: glTFRuntimeHttpResponse) -> None
```

X.gl_tf_load_asset_from_file_map_async(file_map, loader_config, completed) -> None
Gl TFLoad Asset from File Map Async

Args:
    file_map (Map[str, str]): 
    loader_config (glTFRuntimeConfig): 
    completed (glTFRuntimeHttpResponse):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_file_map"></a>

#### gl\_tf\_load\_asset\_from\_file\_map

```python
@classmethod
def gl_tf_load_asset_from_file_map(
        cls, file_map: Map[str, str],
        loader_config: glTFRuntimeConfig) -> glTFRuntimeAsset
```

X.gl_tf_load_asset_from_file_map(file_map, loader_config) -> glTFRuntimeAsset
Gl TFLoad Asset from File Map

Args:
    file_map (Map[str, str]): 
    loader_config (glTFRuntimeConfig): 

Returns:
    glTFRuntimeAsset:

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_data"></a>

#### gl\_tf\_load\_asset\_from\_data

```python
@classmethod
def gl_tf_load_asset_from_data(
        cls, data: Array[int],
        loader_config: glTFRuntimeConfig) -> glTFRuntimeAsset
```

X.gl_tf_load_asset_from_data(data, loader_config) -> glTFRuntimeAsset
Gl TFLoad Asset from Data

Args:
    data (Array[uint8]): 
    loader_config (glTFRuntimeConfig): 

Returns:
    glTFRuntimeAsset:

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_command"></a>

#### gl\_tf\_load\_asset\_from\_command

```python
@classmethod
def gl_tf_load_asset_from_command(cls,
                                  command: str,
                                  arguments: str,
                                  working_directory: str,
                                  completed: glTFRuntimeCommandResponse,
                                  loader_config: glTFRuntimeConfig,
                                  expected_exit_code: int = 0) -> None
```

X.gl_tf_load_asset_from_command(command, arguments, working_directory, completed, loader_config, expected_exit_code=0) -> None
Gl TFLoad Asset from Command

Args:
    command (str): 
    arguments (str): 
    working_directory (str): 
    completed (glTFRuntimeCommandResponse): 
    loader_config (glTFRuntimeConfig): 
    expected_exit_code (int32):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_clipboard"></a>

#### gl\_tf\_load\_asset\_from\_clipboard

```python
@classmethod
def gl_tf_load_asset_from_clipboard(
        cls, completed: glTFRuntimeHttpResponse,
        loader_config: glTFRuntimeConfig) -> Optional[str]
```

X.gl_tf_load_asset_from_clipboard(completed, loader_config) -> str or None
Gl TFLoad Asset from Clipboard

Args:
    completed (glTFRuntimeHttpResponse): 
    loader_config (glTFRuntimeConfig): 

Returns:
    str or None: 

    clipboard_content (str):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_base64_async"></a>

#### gl\_tf\_load\_asset\_from\_base64\_async

```python
@classmethod
def gl_tf_load_asset_from_base64_async(
        cls, base64: str, loader_config: glTFRuntimeConfig,
        completed: glTFRuntimeHttpResponse) -> None
```

X.gl_tf_load_asset_from_base64_async(base64, loader_config, completed) -> None
Gl TFLoad Asset from Base 64Async

Args:
    base64 (str): 
    loader_config (glTFRuntimeConfig): 
    completed (glTFRuntimeHttpResponse):

<a id="unreal.glTFRuntimeFunctionLibrary.gl_tf_load_asset_from_base64"></a>

#### gl\_tf\_load\_asset\_from\_base64

```python
@classmethod
def gl_tf_load_asset_from_base64(
        cls, base64: str,
        loader_config: glTFRuntimeConfig) -> glTFRuntimeAsset
```

X.gl_tf_load_asset_from_base64(base64, loader_config) -> glTFRuntimeAsset
Gl TFLoad Asset from Base 64

Args:
    base64 (str): 
    loader_config (glTFRuntimeConfig): 

Returns:
    glTFRuntimeAsset:

<a id="unreal.glTFRuntimeFunctionLibrary.get_positions_as_bytes_fromgl_tf_runtime_lod_primitive"></a>

#### get\_positions\_as\_bytes\_fromgl\_tf\_runtime\_lod\_primitive

```python
@classmethod
def get_positions_as_bytes_fromgl_tf_runtime_lod_primitive(
        cls, runtime_lod: glTFRuntimeMeshLOD,
        primitive_index: int) -> Optional[Array[int]]
```

X.get_positions_as_bytes_fromgl_tf_runtime_lod_primitive(runtime_lod, primitive_index) -> Array[uint8] or None
Get Positions as Bytes Fromgl TFRuntime LODPrimitive

Args:
    runtime_lod (glTFRuntimeMeshLOD): 
    primitive_index (int32): 

Returns:
    Array[uint8] or None: 

    bytes (Array[uint8]):

<a id="unreal.glTFRuntimeFunctionLibrary.get_normals_as_bytes_fromgl_tf_runtime_lod_primitive"></a>

#### get\_normals\_as\_bytes\_fromgl\_tf\_runtime\_lod\_primitive

```python
@classmethod
def get_normals_as_bytes_fromgl_tf_runtime_lod_primitive(
        cls, runtime_lod: glTFRuntimeMeshLOD,
        primitive_index: int) -> Optional[Array[int]]
```

X.get_normals_as_bytes_fromgl_tf_runtime_lod_primitive(runtime_lod, primitive_index) -> Array[uint8] or None
Get Normals as Bytes Fromgl TFRuntime LODPrimitive

Args:
    runtime_lod (glTFRuntimeMeshLOD): 
    primitive_index (int32): 

Returns:
    Array[uint8] or None: 

    bytes (Array[uint8]):

<a id="unreal.glTFRuntimeFunctionLibrary.get_indices_as_bytes_fromgl_tf_runtime_lod_primitive"></a>

#### get\_indices\_as\_bytes\_fromgl\_tf\_runtime\_lod\_primitive

```python
@classmethod
def get_indices_as_bytes_fromgl_tf_runtime_lod_primitive(
        cls, runtime_lod: glTFRuntimeMeshLOD,
        primitive_index: int) -> Optional[Array[int]]
```

X.get_indices_as_bytes_fromgl_tf_runtime_lod_primitive(runtime_lod, primitive_index) -> Array[uint8] or None
Get Indices as Bytes Fromgl TFRuntime LODPrimitive

Args:
    runtime_lod (glTFRuntimeMeshLOD): 
    primitive_index (int32): 

Returns:
    Array[uint8] or None: 

    bytes (Array[uint8]):

<a id="unreal.glTFRuntimeSkeletalMeshComponent"></a>