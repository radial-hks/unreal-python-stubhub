## ContentBrowserDataPackageFilter Objects

```python
class ContentBrowserDataPackageFilter(StructBase)
```

Data used to filter object instances by their package.
note: This will typically limit your query to returning assets.

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``package_names_to_exclude`` (Array[Name]):  [Read-Write] Array of package names that should be excluded from this query
- ``package_names_to_include`` (Array[Name]):  [Read-Write] Array of package names that should be included in this query
- ``package_paths_to_exclude`` (Array[Name]):  [Read-Write] Array of package paths that should be excluded from this query
- ``package_paths_to_include`` (Array[Name]):  [Read-Write] Array of package paths that should be included in this query
- ``recursive_package_paths_to_exclude`` (bool):  [Read-Write] Whether we should include exclusive package sub-paths in this query
- ``recursive_package_paths_to_include`` (bool):  [Read-Write] Whether we should include inclusive package sub-paths in this query

<a id="unreal.ContentBrowserDataPackageFilter.__init__"></a>

#### __init__

```python
def __init__(package_names_to_include: Array[Name] = [],
             package_names_to_exclude: Array[Name] = [],
             package_paths_to_include: Array[Name] = [],
             package_paths_to_exclude: Array[Name] = [],
             recursive_package_paths_to_include: bool = False,
             recursive_package_paths_to_exclude: bool = False) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter.package_names_to_include"></a>

#### package_names_to_include

```python
@property
def package_names_to_include() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of package names that should be included in this query

<a id="unreal.ContentBrowserDataPackageFilter.package_names_to_include"></a>

#### package_names_to_include

```python
@package_names_to_include.setter
def package_names_to_include(value: Array[Name]) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter.package_names_to_exclude"></a>

#### package_names_to_exclude

```python
@property
def package_names_to_exclude() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of package names that should be excluded from this query

<a id="unreal.ContentBrowserDataPackageFilter.package_names_to_exclude"></a>

#### package_names_to_exclude

```python
@package_names_to_exclude.setter
def package_names_to_exclude(value: Array[Name]) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter.package_paths_to_include"></a>

#### package_paths_to_include

```python
@property
def package_paths_to_include() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of package paths that should be included in this query

<a id="unreal.ContentBrowserDataPackageFilter.package_paths_to_include"></a>

#### package_paths_to_include

```python
@package_paths_to_include.setter
def package_paths_to_include(value: Array[Name]) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter.package_paths_to_exclude"></a>

#### package_paths_to_exclude

```python
@property
def package_paths_to_exclude() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of package paths that should be excluded from this query

<a id="unreal.ContentBrowserDataPackageFilter.package_paths_to_exclude"></a>

#### package_paths_to_exclude

```python
@package_paths_to_exclude.setter
def package_paths_to_exclude(value: Array[Name]) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter.recursive_package_paths_to_include"></a>

#### recursive_package_paths_to_include

```python
@property
def recursive_package_paths_to_include() -> bool
```

(bool):  [Read-Write] Whether we should include inclusive package sub-paths in this query

<a id="unreal.ContentBrowserDataPackageFilter.recursive_package_paths_to_include"></a>

#### recursive_package_paths_to_include

```python
@recursive_package_paths_to_include.setter
def recursive_package_paths_to_include(value: bool) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter.recursive_package_paths_to_exclude"></a>

#### recursive_package_paths_to_exclude

```python
@property
def recursive_package_paths_to_exclude() -> bool
```

(bool):  [Read-Write] Whether we should include exclusive package sub-paths in this query

<a id="unreal.ContentBrowserDataPackageFilter.recursive_package_paths_to_exclude"></a>

#### recursive_package_paths_to_exclude

```python
@recursive_package_paths_to_exclude.setter
def recursive_package_paths_to_exclude(value: bool) -> None
```

<a id="unreal.ContentBrowserDataClassFilter"></a>