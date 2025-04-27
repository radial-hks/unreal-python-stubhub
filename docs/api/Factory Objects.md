## Factory Objects

```python
class Factory(Object)
```

Base class for all factories
An object responsible for creating and importing new objects.

**C++ Source:**

- **Module**: UnrealEd
- **File**: Factory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.Factory.create_new"></a>

#### create_new

```python
@property
def create_new() -> bool
```

(bool):  [Read-Write] The default value to return from CanCreateNew()

<a id="unreal.Factory.create_new"></a>

#### create_new

```python
@create_new.setter
def create_new(value: bool) -> None
```

<a id="unreal.Factory.supported_class"></a>

#### supported_class

```python
@property
def supported_class() -> Class
```

(type(Class)):  [Read-Write] The class manufactured by this factory.

<a id="unreal.Factory.supported_class"></a>

#### supported_class

```python
@supported_class.setter
def supported_class(value: Class) -> None
```

<a id="unreal.Factory.context_class"></a>

#### context_class

```python
@property
def context_class() -> Class
```

(type(Class)):  [Read-Write] Class of the context object used to help create the object.

<a id="unreal.Factory.context_class"></a>

#### context_class

```python
@context_class.setter
def context_class(value: Class) -> None
```

<a id="unreal.Factory.formats"></a>

#### formats

```python
@property
def formats() -> Array[str]
```

(Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.

<a id="unreal.Factory.formats"></a>

#### formats

```python
@formats.setter
def formats(value: Array[str]) -> None
```

<a id="unreal.Factory.edit_after_new"></a>

#### edit_after_new

```python
@property
def edit_after_new() -> bool
```

(bool):  [Read-Write] true if the associated editor should be opened after creating a new object.

<a id="unreal.Factory.edit_after_new"></a>

#### edit_after_new

```python
@edit_after_new.setter
def edit_after_new(value: bool) -> None
```

<a id="unreal.Factory.editor_import"></a>

#### editor_import

```python
@property
def editor_import() -> bool
```

(bool):  [Read-Write] true if the factory imports objects from files.

<a id="unreal.Factory.editor_import"></a>

#### editor_import

```python
@editor_import.setter
def editor_import(value: bool) -> None
```

<a id="unreal.Factory.text"></a>

#### text

```python
@property
def text() -> bool
```

(bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.Factory.text"></a>

#### text

```python
@text.setter
def text(value: bool) -> None
```

<a id="unreal.Factory.automated_import_data"></a>

#### automated_import_data

```python
@property
def automated_import_data() -> AutomatedAssetImportData
```

(AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface

<a id="unreal.Factory.automated_import_data"></a>

#### automated_import_data

```python
@automated_import_data.setter
def automated_import_data(value: AutomatedAssetImportData) -> None
```

<a id="unreal.Factory.asset_import_task"></a>

#### asset_import_task

```python
@property
def asset_import_task() -> AssetImportTask
```

(AssetImportTask):  [Read-Write] Task for importing file via script interfaces

<a id="unreal.Factory.asset_import_task"></a>

#### asset_import_task

```python
@asset_import_task.setter
def asset_import_task(value: AssetImportTask) -> None
```

<a id="unreal.Factory.script_factory_create_file"></a>

#### script_factory_create_file

```python
def script_factory_create_file(task: AssetImportTask) -> bool
```

x.script_factory_create_file(task) -> bool
Import object(s) using a task via script

Args:
    task (AssetImportTask): 

Returns:
    bool: True if script implements

<a id="unreal.Factory.script_factory_can_import"></a>

#### script_factory_can_import

```python
def script_factory_can_import(filename: str) -> bool
```

x.script_factory_can_import(filename) -> bool
Whether the specified file can be imported by this factory. (Implemented in script)

Args:
    filename (str): 

Returns:
    bool: true if the file is supported, false otherwise.

<a id="unreal.FoliageType_InstancedStaticMeshFactory"></a>