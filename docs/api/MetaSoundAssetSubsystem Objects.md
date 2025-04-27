## MetaSoundAssetSubsystem Objects

```python
class MetaSoundAssetSubsystem(EngineSubsystem)
```

namespace Metasound::Engine

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundAssetSubsystem.h

<a id="unreal.MetaSoundAssetSubsystem.unregister_asset_classes_in_directories"></a>

#### unregister_asset_classes_in_directories

```python
def unregister_asset_classes_in_directories(
        directories: Array[MetaSoundAssetDirectory]) -> None
```

x.unregister_asset_classes_in_directories(directories) -> None
Unregister Asset Classes in Directories

Args:
    directories (Array[MetaSoundAssetDirectory]):

<a id="unreal.MetaSoundAssetSubsystem.replace_references_in_directory"></a>

#### replace_references_in_directory

```python
def replace_references_in_directory(
        directories: Array[MetaSoundAssetDirectory],
        old_class_name: MetasoundFrontendClassName,
        new_class_name: MetasoundFrontendClassName,
        old_version: MetasoundFrontendVersionNumber = [1, 0],
        new_version: MetasoundFrontendVersionNumber = [1, 0]) -> bool
```

x.replace_references_in_directory(directories, old_class_name, new_class_name, old_version=[1, 0], new_version=[1, 0]) -> bool
Replaces dependencies in a MetaSound with the given class name and version with another MetaSound with the given
class name and version.  Can be asset or code-defined.  It is up to the caller to validate the two classes have
matching interfaces (Swapping with classes of unmatched interfaces can leave MetaSound in non-executable state).

Args:
    directories (Array[MetaSoundAssetDirectory]): 
    old_class_name (MetasoundFrontendClassName): 
    new_class_name (MetasoundFrontendClassName): 
    old_version (MetasoundFrontendVersionNumber): 
    new_version (MetasoundFrontendVersionNumber): 

Returns:
    bool:

<a id="unreal.MetaSoundAssetSubsystem.register_asset_classes_in_directories"></a>

#### register_asset_classes_in_directories

```python
def register_asset_classes_in_directories(
        directories: Array[MetaSoundAssetDirectory]) -> None
```

x.register_asset_classes_in_directories(directories) -> None
Register Asset Classes in Directories

Args:
    directories (Array[MetaSoundAssetDirectory]):

<a id="unreal.MetaSoundAssetSubsystem.reassign_class_name"></a>

#### reassign_class_name

```python
def reassign_class_name(doc_interface: MetaSoundDocumentInterface) -> bool
```

x.reassign_class_name(doc_interface) -> bool
Reassign Class Name

Args:
    doc_interface (MetaSoundDocumentInterface): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase"></a>