## ARFilter Objects

```python
class ARFilter(StructBase)
```

A struct to serve as a filter for Asset Registry queries. (mirrored in ARFilter.h)

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_names`` (Array[Name]):  [Read-Write] [DEPRECATED] - Class names are now represented by path names. Please use ClassPaths instead.
  deprecated: Short asset class names must be converted to full asset pathnames. Use ClassPaths instead.
- ``class_paths`` (Array[TopLevelAssetPath]):  [Read-Write] The filter component for class path names. Instances of the specified classes, but not subclasses (by default), will be included. Derived classes will be included only if bRecursiveClasses is true.
- ``include_only_on_disk_assets`` (bool):  [Read-Write] If true, only on-disk assets will be returned. Be warned that this is rarely what you want and should only be used for performance reasons
- ``package_names`` (Array[Name]):  [Read-Write] The filter component for package names
- ``package_paths`` (Array[Name]):  [Read-Write] The filter component for package paths
- ``recursive_class_paths_exclusion_set`` (Set[TopLevelAssetPath]):  [Read-Write] Only if bRecursiveClasses is true, the results will exclude classes (and subclasses) in this list
- ``recursive_classes`` (bool):  [Read-Write] If true, subclasses of ClassNames will also be included and RecursiveClassesExclusionSet will be excluded.
- ``recursive_classes_exclusion_set`` (Set[Name]):  [Read-Write] [DEPRECATED] - Class names are now represented by path names. Please use RecursiveClassPathsExclusionSet instead.
  deprecated: Short asset class names must be converted to full asset pathnames. Use RecursiveClassPathsExclusionSet instead.
- ``recursive_paths`` (bool):  [Read-Write] If true, PackagePath components will be recursive
- ``soft_object_paths`` (Array[SoftObjectPath]):  [Read-Write] The filter component containing specific object paths

<a id="unreal.ARFilter.__init__"></a>

#### __init__

```python
def __init__(package_names: Array[Name] = [],
             package_paths: Array[Name] = [],
             soft_object_paths: Array[SoftObjectPath] = [],
             class_paths: Array[TopLevelAssetPath] = [],
             recursive_class_paths_exclusion_set: Set[TopLevelAssetPath] = [],
             class_names: Array[Name] = [],
             recursive_classes_exclusion_set: Set[Name] = [],
             recursive_paths: bool = False,
             recursive_classes: bool = False,
             include_only_on_disk_assets: bool = False) -> None
```

<a id="unreal.ARFilter.package_names"></a>

#### package_names

```python
@property
def package_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] The filter component for package names

<a id="unreal.ARFilter.package_names"></a>

#### package_names

```python
@package_names.setter
def package_names(value: Array[Name]) -> None
```

<a id="unreal.ARFilter.package_paths"></a>

#### package_paths

```python
@property
def package_paths() -> Array[Name]
```

(Array[Name]):  [Read-Write] The filter component for package paths

<a id="unreal.ARFilter.package_paths"></a>

#### package_paths

```python
@package_paths.setter
def package_paths(value: Array[Name]) -> None
```

<a id="unreal.ARFilter.soft_object_paths"></a>

#### soft_object_paths

```python
@property
def soft_object_paths() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] The filter component containing specific object paths

<a id="unreal.ARFilter.soft_object_paths"></a>

#### soft_object_paths

```python
@soft_object_paths.setter
def soft_object_paths(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.ARFilter.class_names"></a>

#### class_names

```python
@property
def class_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] [DEPRECATED] - Class names are now represented by path names. Please use ClassPaths instead.
deprecated: Short asset class names must be converted to full asset pathnames. Use ClassPaths instead.

<a id="unreal.ARFilter.class_names"></a>

#### class_names

```python
@class_names.setter
def class_names(value: Array[Name]) -> None
```

<a id="unreal.ARFilter.class_paths"></a>

#### class_paths

```python
@property
def class_paths() -> Array[TopLevelAssetPath]
```

(Array[TopLevelAssetPath]):  [Read-Write] The filter component for class path names. Instances of the specified classes, but not subclasses (by default), will be included. Derived classes will be included only if bRecursiveClasses is true.

<a id="unreal.ARFilter.class_paths"></a>

#### class_paths

```python
@class_paths.setter
def class_paths(value: Array[TopLevelAssetPath]) -> None
```

<a id="unreal.ARFilter.recursive_classes_exclusion_set"></a>

#### recursive_classes_exclusion_set

```python
@property
def recursive_classes_exclusion_set() -> Set[Name]
```

(Set[Name]):  [Read-Write] [DEPRECATED] - Class names are now represented by path names. Please use RecursiveClassPathsExclusionSet instead.
deprecated: Short asset class names must be converted to full asset pathnames. Use RecursiveClassPathsExclusionSet instead.

<a id="unreal.ARFilter.recursive_classes_exclusion_set"></a>

#### recursive_classes_exclusion_set

```python
@recursive_classes_exclusion_set.setter
def recursive_classes_exclusion_set(value: Set[Name]) -> None
```

<a id="unreal.ARFilter.recursive_class_paths_exclusion_set"></a>

#### recursive_class_paths_exclusion_set

```python
@property
def recursive_class_paths_exclusion_set() -> Set[TopLevelAssetPath]
```

(Set[TopLevelAssetPath]):  [Read-Write] Only if bRecursiveClasses is true, the results will exclude classes (and subclasses) in this list

<a id="unreal.ARFilter.recursive_class_paths_exclusion_set"></a>

#### recursive_class_paths_exclusion_set

```python
@recursive_class_paths_exclusion_set.setter
def recursive_class_paths_exclusion_set(value: Set[TopLevelAssetPath]) -> None
```

<a id="unreal.ARFilter.recursive_paths"></a>

#### recursive_paths

```python
@property
def recursive_paths() -> bool
```

(bool):  [Read-Write] If true, PackagePath components will be recursive

<a id="unreal.ARFilter.recursive_paths"></a>

#### recursive_paths

```python
@recursive_paths.setter
def recursive_paths(value: bool) -> None
```

<a id="unreal.ARFilter.recursive_classes"></a>

#### recursive_classes

```python
@property
def recursive_classes() -> bool
```

(bool):  [Read-Write] If true, subclasses of ClassNames will also be included and RecursiveClassesExclusionSet will be excluded.

<a id="unreal.ARFilter.recursive_classes"></a>

#### recursive_classes

```python
@recursive_classes.setter
def recursive_classes(value: bool) -> None
```

<a id="unreal.ARFilter.include_only_on_disk_assets"></a>

#### include_only_on_disk_assets

```python
@property
def include_only_on_disk_assets() -> bool
```

(bool):  [Read-Write] If true, only on-disk assets will be returned. Be warned that this is rarely what you want and should only be used for performance reasons

<a id="unreal.ARFilter.include_only_on_disk_assets"></a>

#### include_only_on_disk_assets

```python
@include_only_on_disk_assets.setter
def include_only_on_disk_assets(value: bool) -> None
```

<a id="unreal.ARFilter.get_blueprint_assets"></a>

#### get_blueprint_assets

```python
def get_blueprint_assets() -> Array[AssetData]
```

x.get_blueprint_assets() -> Array[AssetData]
Gets asset data for all blueprint assets that match the filter. ClassPaths in the filter specify the blueprint's parent class.

Returns:
    Array[AssetData]: 

    out_asset_data (Array[AssetData]):

<a id="unreal.TopLevelAssetPath"></a>