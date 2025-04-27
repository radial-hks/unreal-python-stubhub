## ContentBrowserDataMenuContext_AddNewMenu Objects

```python
class ContentBrowserDataMenuContext_AddNewMenu(Object)
```

Content Browser Data Menu Context Add New Menu

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataMenuContexts.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_modified`` (bool):  [Read-Write]
- ``contains_valid_package_path`` (bool):  [Read-Write] At least one of the selected paths maps to a mounted content root
- ``owner_domain`` (ContentBrowserDataMenuContext_AddNewMenuDomain):  [Read-Write]
- ``selected_paths`` (Array[Name]):  [Read-Write]

<a id="unreal.ContentBrowserDataMenuContext_AddNewMenu.selected_paths"></a>

#### selected_paths

```python
@property
def selected_paths() -> Array[Name]
```

(Array[Name]):  [Read-Only]

<a id="unreal.ContentBrowserDataMenuContext_AddNewMenu.contains_valid_package_path"></a>

#### contains_valid_package_path

```python
@property
def contains_valid_package_path() -> bool
```

(bool):  [Read-Only] At least one of the selected paths maps to a mounted content root

<a id="unreal.ContentBrowserDataMenuContext_AddNewMenu.can_be_modified"></a>

#### can_be_modified

```python
@property
def can_be_modified() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ContentBrowserDataMenuContext_AddNewMenu.owner_domain"></a>

#### owner_domain

```python
@property
def owner_domain() -> ContentBrowserDataMenuContext_AddNewMenuDomain
```

(ContentBrowserDataMenuContext_AddNewMenuDomain):  [Read-Only]

<a id="unreal.ContentBrowserDataMenuContext_FolderMenu"></a>