## glTFRuntimeConfig Objects

```python
class glTFRuntimeConfig(StructBase)
```

Gl TFRuntime Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_external_files`` (bool):  [Read-Write]
- ``archive_auto_entry_point_extensions`` (str):  [Read-Write]
- ``archive_entry_point`` (str):  [Read-Write]
- ``as_blob`` (bool):  [Read-Write]
- ``base_transform`` (Transform):  [Read-Write]
- ``basis_matrix`` (Matrix):  [Read-Write]
- ``basis_vector_matrix`` (glTFRuntimeBasisMatrix):  [Read-Write]
- ``content_plugins_to_scan`` (Array[str]):  [Read-Write]
- ``encryption_key`` (str):  [Read-Write]
- ``override_base_directory`` (str):  [Read-Write]
- ``override_base_directory_from_content_dir`` (bool):  [Read-Write]
- ``prefix_for_unnamed_nodes`` (str):  [Read-Write]
- ``runtime_context_object`` (Object):  [Read-Write]
- ``runtime_context_string`` (str):  [Read-Write]
- ``scene_scale`` (float):  [Read-Write]
- ``transform_base_type`` (EglTFRuntimeTransformBaseType):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        transform_base_type:
    EglTFRuntimeTransformBaseType = EglTFRuntimeTransformBaseType.DEFAULT,
        basis_matrix: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000, 0.000000]],
        base_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
        basis_vector_matrix: glTFRuntimeBasisMatrix = [
            [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
        ],
        scene_scale: float = 0.000000,
        content_plugins_to_scan: Array[str] = [],
        allow_external_files: bool = False,
        override_base_directory: str = "",
        override_base_directory_from_content_dir: bool = False,
        archive_entry_point: str = "",
        archive_auto_entry_point_extensions: str = "",
        runtime_context_object: Object = None,
        runtime_context_string: str = "",
        as_blob: bool = False,
        prefix_for_unnamed_nodes: str = "",
        encryption_key: str = "") -> None
```

<a id="unreal.glTFRuntimeConfig.transform_base_type"></a>

#### transform\_base\_type

```python
@property
def transform_base_type() -> EglTFRuntimeTransformBaseType
```

(EglTFRuntimeTransformBaseType):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.transform_base_type"></a>

#### transform\_base\_type

```python
@transform_base_type.setter
def transform_base_type(value: EglTFRuntimeTransformBaseType) -> None
```

<a id="unreal.glTFRuntimeConfig.basis_matrix"></a>

#### basis\_matrix

```python
@property
def basis_matrix() -> Matrix
```

(Matrix):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.basis_matrix"></a>

#### basis\_matrix

```python
@basis_matrix.setter
def basis_matrix(value: Matrix) -> None
```

<a id="unreal.glTFRuntimeConfig.base_transform"></a>

#### base\_transform

```python
@property
def base_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.base_transform"></a>

#### base\_transform

```python
@base_transform.setter
def base_transform(value: Transform) -> None
```

<a id="unreal.glTFRuntimeConfig.basis_vector_matrix"></a>

#### basis\_vector\_matrix

```python
@property
def basis_vector_matrix() -> glTFRuntimeBasisMatrix
```

(glTFRuntimeBasisMatrix):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.basis_vector_matrix"></a>

#### basis\_vector\_matrix

```python
@basis_vector_matrix.setter
def basis_vector_matrix(value: glTFRuntimeBasisMatrix) -> None
```

<a id="unreal.glTFRuntimeConfig.scene_scale"></a>

#### scene\_scale

```python
@property
def scene_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.scene_scale"></a>

#### scene\_scale

```python
@scene_scale.setter
def scene_scale(value: float) -> None
```

<a id="unreal.glTFRuntimeConfig.content_plugins_to_scan"></a>

#### content\_plugins\_to\_scan

```python
@property
def content_plugins_to_scan() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.content_plugins_to_scan"></a>

#### content\_plugins\_to\_scan

```python
@content_plugins_to_scan.setter
def content_plugins_to_scan(value: Array[str]) -> None
```

<a id="unreal.glTFRuntimeConfig.allow_external_files"></a>

#### allow\_external\_files

```python
@property
def allow_external_files() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.allow_external_files"></a>

#### allow\_external\_files

```python
@allow_external_files.setter
def allow_external_files(value: bool) -> None
```

<a id="unreal.glTFRuntimeConfig.override_base_directory"></a>

#### override\_base\_directory

```python
@property
def override_base_directory() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.override_base_directory"></a>

#### override\_base\_directory

```python
@override_base_directory.setter
def override_base_directory(value: str) -> None
```

<a id="unreal.glTFRuntimeConfig.override_base_directory_from_content_dir"></a>

#### override\_base\_directory\_from\_content\_dir

```python
@property
def override_base_directory_from_content_dir() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.override_base_directory_from_content_dir"></a>

#### override\_base\_directory\_from\_content\_dir

```python
@override_base_directory_from_content_dir.setter
def override_base_directory_from_content_dir(value: bool) -> None
```

<a id="unreal.glTFRuntimeConfig.archive_entry_point"></a>

#### archive\_entry\_point

```python
@property
def archive_entry_point() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.archive_entry_point"></a>

#### archive\_entry\_point

```python
@archive_entry_point.setter
def archive_entry_point(value: str) -> None
```

<a id="unreal.glTFRuntimeConfig.archive_auto_entry_point_extensions"></a>

#### archive\_auto\_entry\_point\_extensions

```python
@property
def archive_auto_entry_point_extensions() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.archive_auto_entry_point_extensions"></a>

#### archive\_auto\_entry\_point\_extensions

```python
@archive_auto_entry_point_extensions.setter
def archive_auto_entry_point_extensions(value: str) -> None
```

<a id="unreal.glTFRuntimeConfig.runtime_context_object"></a>

#### runtime\_context\_object

```python
@property
def runtime_context_object() -> Object
```

(Object):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.runtime_context_object"></a>

#### runtime\_context\_object

```python
@runtime_context_object.setter
def runtime_context_object(value: Object) -> None
```

<a id="unreal.glTFRuntimeConfig.runtime_context_string"></a>

#### runtime\_context\_string

```python
@property
def runtime_context_string() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.runtime_context_string"></a>

#### runtime\_context\_string

```python
@runtime_context_string.setter
def runtime_context_string(value: str) -> None
```

<a id="unreal.glTFRuntimeConfig.as_blob"></a>

#### as\_blob

```python
@property
def as_blob() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.as_blob"></a>

#### as\_blob

```python
@as_blob.setter
def as_blob(value: bool) -> None
```

<a id="unreal.glTFRuntimeConfig.prefix_for_unnamed_nodes"></a>

#### prefix\_for\_unnamed\_nodes

```python
@property
def prefix_for_unnamed_nodes() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.prefix_for_unnamed_nodes"></a>

#### prefix\_for\_unnamed\_nodes

```python
@prefix_for_unnamed_nodes.setter
def prefix_for_unnamed_nodes(value: str) -> None
```

<a id="unreal.glTFRuntimeConfig.encryption_key"></a>

#### encryption\_key

```python
@property
def encryption_key() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeConfig.encryption_key"></a>

#### encryption\_key

```python
@encryption_key.setter
def encryption_key(value: str) -> None
```

<a id="unreal.glTFRuntimeBasisMatrix"></a>