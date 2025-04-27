## AssetRegistryDependencyOptions Objects

```python
class AssetRegistryDependencyOptions(StructBase)
```

namespace UE::AssetRegistry

**C++ Source:**

- **Module**: AssetRegistry
- **File**: IAssetRegistry.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``include_hard_management_references`` (bool):  [Read-Write] Reference that says one object directly manages another object, set when Primary Assets manage things explicitly
- ``include_hard_package_references`` (bool):  [Read-Write] Dependencies which are required for correct usage of the source asset, and must be loaded at the same time
- ``include_searchable_names`` (bool):  [Read-Write] References to specific SearchableNames inside a package
- ``include_soft_management_references`` (bool):  [Read-Write] Indirect management references, these are set through recursion for Primary Assets that manage packages or other primary assets
- ``include_soft_package_references`` (bool):  [Read-Write] Dependencies which don't need to be loaded for the object to be used (i.e. soft object paths)

<a id="unreal.AssetRegistryDependencyOptions.__init__"></a>

#### __init__

```python
def __init__(include_soft_package_references: bool = False,
             include_hard_package_references: bool = False,
             include_searchable_names: bool = False,
             include_soft_management_references: bool = False,
             include_hard_management_references: bool = False) -> None
```

<a id="unreal.AssetRegistryDependencyOptions.include_soft_package_references"></a>

#### include_soft_package_references

```python
@property
def include_soft_package_references() -> bool
```

(bool):  [Read-Write] Dependencies which don't need to be loaded for the object to be used (i.e. soft object paths)

<a id="unreal.AssetRegistryDependencyOptions.include_soft_package_references"></a>

#### include_soft_package_references

```python
@include_soft_package_references.setter
def include_soft_package_references(value: bool) -> None
```

<a id="unreal.AssetRegistryDependencyOptions.include_hard_package_references"></a>

#### include_hard_package_references

```python
@property
def include_hard_package_references() -> bool
```

(bool):  [Read-Write] Dependencies which are required for correct usage of the source asset, and must be loaded at the same time

<a id="unreal.AssetRegistryDependencyOptions.include_hard_package_references"></a>

#### include_hard_package_references

```python
@include_hard_package_references.setter
def include_hard_package_references(value: bool) -> None
```

<a id="unreal.AssetRegistryDependencyOptions.include_searchable_names"></a>

#### include_searchable_names

```python
@property
def include_searchable_names() -> bool
```

(bool):  [Read-Write] References to specific SearchableNames inside a package

<a id="unreal.AssetRegistryDependencyOptions.include_searchable_names"></a>

#### include_searchable_names

```python
@include_searchable_names.setter
def include_searchable_names(value: bool) -> None
```

<a id="unreal.AssetRegistryDependencyOptions.include_soft_management_references"></a>

#### include_soft_management_references

```python
@property
def include_soft_management_references() -> bool
```

(bool):  [Read-Write] Indirect management references, these are set through recursion for Primary Assets that manage packages or other primary assets

<a id="unreal.AssetRegistryDependencyOptions.include_soft_management_references"></a>

#### include_soft_management_references

```python
@include_soft_management_references.setter
def include_soft_management_references(value: bool) -> None
```

<a id="unreal.AssetRegistryDependencyOptions.include_hard_management_references"></a>

#### include_hard_management_references

```python
@property
def include_hard_management_references() -> bool
```

(bool):  [Read-Write] Reference that says one object directly manages another object, set when Primary Assets manage things explicitly

<a id="unreal.AssetRegistryDependencyOptions.include_hard_management_references"></a>

#### include_hard_management_references

```python
@include_hard_management_references.setter
def include_hard_management_references(value: bool) -> None
```

<a id="unreal.ElementID"></a>