## InterchangeFactoryBaseNode Objects

```python
class InterchangeFactoryBaseNode(InterchangeBaseNode)
```

This struct is used to store and retrieve key-value attributes. The attributes are stored in a generic FAttributeStorage that serializes the values in a TArray64<uint8>.
See UE::Interchange::EAttributeTypes to know the supported template types.
This is an abstract class. This is the base class of the Interchange node graph format; all classes in this format should derive from this class.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeFactoryBaseNode.h

<a id="unreal.InterchangeFactoryBaseNode.unset_skip_node_import"></a>

#### unset_skip_node_import

```python
def unset_skip_node_import() -> bool
```

x.unset_skip_node_import() -> bool
Remove the skip node attribute. See ShouldSkipNodeImport for more documentation.

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.unset_force_node_reimport"></a>

#### unset_force_node_reimport

```python
def unset_force_node_reimport() -> bool
```

x.unset_force_node_reimport() -> bool
Disallow the creation of the Unreal object if it has been previously deleted in the editor.

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.should_skip_node_import"></a>

#### should_skip_node_import

```python
def should_skip_node_import() -> bool
```

x.should_skip_node_import() -> bool
Return true if this node should skip the factory import process, or false otherwise.
Nodes can be in a situation where we have to skip the import process because we cannot import the associated asset for multiple reasons. For example:
- An asset can already exist and represents a different type (UClass).
- An asset can already exist and is being compiled.
- An asset can already exist and is being imported by another concurrent import task (such as a user importing multiple files at the same time in the same content folder).

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.should_force_node_reimport"></a>

#### should_force_node_reimport

```python
def should_force_node_reimport() -> bool
```

x.should_force_node_reimport() -> bool
Return whether or not an object should be created even if it has been deleted in the editor.
Return false by default.

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.set_skip_node_import"></a>

#### set_skip_node_import

```python
def set_skip_node_import() -> bool
```

x.set_skip_node_import() -> bool
Add the skip node attribute. Use this function to cancel the creation of the Unreal asset. See ShouldSkipNodeImport for more documentation.

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.set_reimport_strategy_flags"></a>

#### set_reimport_strategy_flags

```python
def set_reimport_strategy_flags(
        reimport_strategy_flags: ReimportStrategyFlags) -> bool
```

x.set_reimport_strategy_flags(reimport_strategy_flags) -> bool
Change the reimport strategy flags.

Args:
    reimport_strategy_flags (ReimportStrategyFlags): 

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.set_force_node_reimport"></a>

#### set_force_node_reimport

```python
def set_force_node_reimport() -> bool
```

x.set_force_node_reimport() -> bool
Allow the creation of the Unreal object even if it has been previously deleted in the editor.

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.set_custom_sub_path"></a>

#### set_custom_sub_path

```python
def set_custom_sub_path(attribute_value: str) -> bool
```

x.set_custom_sub_path(attribute_value) -> bool
Set the custom sub-path under PackageBasePath where the assets will be created.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.set_custom_reference_object"></a>

#### set_custom_reference_object

```python
def set_custom_reference_object(attribute_value: SoftObjectPath) -> bool
```

x.set_custom_reference_object(attribute_value) -> bool
Set the custom ReferenceObject: the UObject this factory node has created.

Args:
    attribute_value (SoftObjectPath): 

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.set_custom_level_uid"></a>

#### set_custom_level_uid

```python
def set_custom_level_uid(attribute_value: str) -> bool
```

x.set_custom_level_uid(attribute_value) -> bool
If this node represent a scene asset (actor), you can set a specific level in which we will create this scene asset.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.remove_factory_dependency_uid"></a>

#### remove_factory_dependency_uid

```python
def remove_factory_dependency_uid(dependency_uid: str) -> bool
```

x.remove_factory_dependency_uid(dependency_uid) -> bool
Remove one dependency from this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.is_runtime_import_allowed"></a>

#### is_runtime_import_allowed

```python
def is_runtime_import_allowed() -> bool
```

x.is_runtime_import_allowed() -> bool
Return if the import of the class is allowed at runtime.

Returns:
    bool:

<a id="unreal.InterchangeFactoryBaseNode.get_reimport_strategy_flags"></a>

#### get_reimport_strategy_flags

```python
def get_reimport_strategy_flags() -> ReimportStrategyFlags
```

x.get_reimport_strategy_flags() -> ReimportStrategyFlags
Return the reimport strategy flags.

Returns:
    ReimportStrategyFlags:

<a id="unreal.InterchangeFactoryBaseNode.get_factory_dependency"></a>

#### get_factory_dependency

```python
def get_factory_dependency(index: int) -> str
```

x.get_factory_dependency(index) -> str
Retrieve one dependency for this object.

Args:
    index (int32): 

Returns:
    str: 

    out_dependency (str):

<a id="unreal.InterchangeFactoryBaseNode.get_factory_dependencies_count"></a>

#### get_factory_dependencies_count

```python
def get_factory_dependencies_count() -> int
```

x.get_factory_dependencies_count() -> int32
Retrieve the number of factory dependencies for this object.

Returns:
    int32:

<a id="unreal.InterchangeFactoryBaseNode.get_factory_dependencies"></a>

#### get_factory_dependencies

```python
def get_factory_dependencies() -> Array[str]
```

x.get_factory_dependencies() -> Array[str]
Retrieve the dependencies for this object.

Returns:
    Array[str]: 

    out_dependencies (Array[str]):

<a id="unreal.InterchangeFactoryBaseNode.get_custom_sub_path"></a>

#### get_custom_sub_path

```python
def get_custom_sub_path() -> Optional[str]
```

x.get_custom_sub_path() -> str or None
Return the custom sub-path under PackageBasePath where the assets will be created.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeFactoryBaseNode.get_custom_reference_object"></a>

#### get_custom_reference_object

```python
def get_custom_reference_object() -> Optional[SoftObjectPath]
```

x.get_custom_reference_object() -> SoftObjectPath or None
Return the custom ReferenceObject: the UObject this factory node has created.

Returns:
    SoftObjectPath or None: 

    attribute_value (SoftObjectPath):

<a id="unreal.InterchangeFactoryBaseNode.get_custom_level_uid"></a>

#### get_custom_level_uid

```python
def get_custom_level_uid() -> Optional[str]
```

x.get_custom_level_uid() -> str or None
If this node represent a scene asset (actor), return a specific level in which we will create this scene asset.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeFactoryBaseNode.add_factory_dependency_uid"></a>

#### add_factory_dependency_uid

```python
def add_factory_dependency_uid(dependency_uid: str) -> bool
```

x.add_factory_dependency_uid(dependency_uid) -> bool
Add one dependency to this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode"></a>