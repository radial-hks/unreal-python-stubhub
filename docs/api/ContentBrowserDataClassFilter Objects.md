## ContentBrowserDataClassFilter Objects

```python
class ContentBrowserDataClassFilter(StructBase)
```

Data used to filter object instances by their class.
note: This will typically limit your query to returning assets.

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_names_to_exclude`` (Array[str]):  [Read-Write] Array of class names that should be excluded from this query
- ``class_names_to_include`` (Array[str]):  [Read-Write] Array of class names that should be included in this query
- ``recursive_class_names_to_exclude`` (bool):  [Read-Write] Whether we should include exclusive sub-classes in this query
- ``recursive_class_names_to_include`` (bool):  [Read-Write] Whether we should include inclusive sub-classes in this query

<a id="unreal.ContentBrowserDataClassFilter.__init__"></a>

#### __init__

```python
def __init__(class_names_to_include: Array[str] = [],
             class_names_to_exclude: Array[str] = [],
             recursive_class_names_to_include: bool = False,
             recursive_class_names_to_exclude: bool = False) -> None
```

<a id="unreal.ContentBrowserDataClassFilter.class_names_to_include"></a>

#### class_names_to_include

```python
@property
def class_names_to_include() -> Array[str]
```

(Array[str]):  [Read-Write] Array of class names that should be included in this query

<a id="unreal.ContentBrowserDataClassFilter.class_names_to_include"></a>

#### class_names_to_include

```python
@class_names_to_include.setter
def class_names_to_include(value: Array[str]) -> None
```

<a id="unreal.ContentBrowserDataClassFilter.class_names_to_exclude"></a>

#### class_names_to_exclude

```python
@property
def class_names_to_exclude() -> Array[str]
```

(Array[str]):  [Read-Write] Array of class names that should be excluded from this query

<a id="unreal.ContentBrowserDataClassFilter.class_names_to_exclude"></a>

#### class_names_to_exclude

```python
@class_names_to_exclude.setter
def class_names_to_exclude(value: Array[str]) -> None
```

<a id="unreal.ContentBrowserDataClassFilter.recursive_class_names_to_include"></a>

#### recursive_class_names_to_include

```python
@property
def recursive_class_names_to_include() -> bool
```

(bool):  [Read-Write] Whether we should include inclusive sub-classes in this query

<a id="unreal.ContentBrowserDataClassFilter.recursive_class_names_to_include"></a>

#### recursive_class_names_to_include

```python
@recursive_class_names_to_include.setter
def recursive_class_names_to_include(value: bool) -> None
```

<a id="unreal.ContentBrowserDataClassFilter.recursive_class_names_to_exclude"></a>

#### recursive_class_names_to_exclude

```python
@property
def recursive_class_names_to_exclude() -> bool
```

(bool):  [Read-Write] Whether we should include exclusive sub-classes in this query

<a id="unreal.ContentBrowserDataClassFilter.recursive_class_names_to_exclude"></a>

#### recursive_class_names_to_exclude

```python
@recursive_class_names_to_exclude.setter
def recursive_class_names_to_exclude(value: bool) -> None
```

<a id="unreal.ContentBrowserDataCollectionFilter"></a>