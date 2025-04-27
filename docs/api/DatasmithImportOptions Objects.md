## DatasmithImportOptions Objects

```python
class DatasmithImportOptions(DatasmithOptionsBase)
```

Datasmith Import Options

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_options`` (DatasmithImportBaseOptions):  [Read-Write] Not displayed. Kept for future use
- ``file_name`` (str):  [Read-Write] Name of the imported file without its path
- ``file_path`` (str):  [Read-Write] Full path of the imported file
- ``reimport_options`` (DatasmithReimportOptions):  [Read-Write] Options specific to the reimport process
- ``source_uri`` (str):  [Read-Write]

<a id="unreal.DatasmithImportOptions.base_options"></a>

#### base_options

```python
@property
def base_options() -> DatasmithImportBaseOptions
```

(DatasmithImportBaseOptions):  [Read-Write] Not displayed. Kept for future use

<a id="unreal.DatasmithImportOptions.base_options"></a>

#### base_options

```python
@base_options.setter
def base_options(value: DatasmithImportBaseOptions) -> None
```

<a id="unreal.DatasmithImportOptions.reimport_options"></a>

#### reimport_options

```python
@property
def reimport_options() -> DatasmithReimportOptions
```

(DatasmithReimportOptions):  [Read-Write] Options specific to the reimport process

<a id="unreal.DatasmithImportOptions.reimport_options"></a>

#### reimport_options

```python
@reimport_options.setter
def reimport_options(value: DatasmithReimportOptions) -> None
```

<a id="unreal.DatasmithImportOptions.file_name"></a>

#### file_name

```python
@property
def file_name() -> str
```

(str):  [Read-Write] Name of the imported file without its path

<a id="unreal.DatasmithImportOptions.file_name"></a>

#### file_name

```python
@file_name.setter
def file_name(value: str) -> None
```

<a id="unreal.DatasmithImportOptions.file_path"></a>

#### file_path

```python
@property
def file_path() -> str
```

(str):  [Read-Write] Full path of the imported file

<a id="unreal.DatasmithImportOptions.file_path"></a>

#### file_path

```python
@file_path.setter
def file_path(value: str) -> None
```

<a id="unreal.DatasmithImportOptions.source_uri"></a>

#### source_uri

```python
@property
def source_uri() -> str
```

(str):  [Read-Write]

<a id="unreal.DatasmithImportOptions.source_uri"></a>

#### source_uri

```python
@source_uri.setter
def source_uri(value: str) -> None
```

<a id="unreal.DatasmithSceneActor"></a>