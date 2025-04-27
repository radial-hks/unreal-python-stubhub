## AddNewSubobjectParams Objects

```python
class AddNewSubobjectParams(StructBase)
```

Options when adding a new subobject

**C++ Source:**

- **Module**: SubobjectDataInterface
- **File**: SubobjectDataSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blueprint_context`` (Blueprint):  [Read-Write] Pointer to the blueprint context that this subobject is in. If this is null, it is assumed that
  this subobject is being added to an instance.
- ``conform_transform_to_parent`` (bool):  [Read-Write] Whether the newly created component should keep its transform, or conform it to its parent
- ``new_class`` (type(Class)):  [Read-Write] The class of the new subobject that will be added
- ``parent_handle`` (SubobjectDataHandle):  [Read-Write]
- ``skip_mark_blueprint_modified`` (bool):  [Read-Write] Optionally skip marking this blueprint as modified (e.g. if we're handling that externally

<a id="unreal.AddNewSubobjectParams.__init__"></a>

#### __init__

```python
def __init__(parent_handle: SubobjectDataHandle = [],
             new_class: Class = None,
             blueprint_context: Blueprint = None,
             skip_mark_blueprint_modified: bool = False,
             conform_transform_to_parent: bool = False) -> None
```

<a id="unreal.AddNewSubobjectParams.parent_handle"></a>

#### parent_handle

```python
@property
def parent_handle() -> SubobjectDataHandle
```

(SubobjectDataHandle):  [Read-Write]

<a id="unreal.AddNewSubobjectParams.parent_handle"></a>

#### parent_handle

```python
@parent_handle.setter
def parent_handle(value: SubobjectDataHandle) -> None
```

<a id="unreal.AddNewSubobjectParams.new_class"></a>

#### new_class

```python
@property
def new_class() -> Class
```

(type(Class)):  [Read-Write] The class of the new subobject that will be added

<a id="unreal.AddNewSubobjectParams.new_class"></a>

#### new_class

```python
@new_class.setter
def new_class(value: Class) -> None
```

<a id="unreal.AddNewSubobjectParams.blueprint_context"></a>

#### blueprint_context

```python
@property
def blueprint_context() -> Blueprint
```

(Blueprint):  [Read-Write] Pointer to the blueprint context that this subobject is in. If this is null, it is assumed that
this subobject is being added to an instance.

<a id="unreal.AddNewSubobjectParams.blueprint_context"></a>

#### blueprint_context

```python
@blueprint_context.setter
def blueprint_context(value: Blueprint) -> None
```

<a id="unreal.AddNewSubobjectParams.skip_mark_blueprint_modified"></a>

#### skip_mark_blueprint_modified

```python
@property
def skip_mark_blueprint_modified() -> bool
```

(bool):  [Read-Write] Optionally skip marking this blueprint as modified (e.g. if we're handling that externally

<a id="unreal.AddNewSubobjectParams.skip_mark_blueprint_modified"></a>

#### skip_mark_blueprint_modified

```python
@skip_mark_blueprint_modified.setter
def skip_mark_blueprint_modified(value: bool) -> None
```

<a id="unreal.AddNewSubobjectParams.conform_transform_to_parent"></a>

#### conform_transform_to_parent

```python
@property
def conform_transform_to_parent() -> bool
```

(bool):  [Read-Write] Whether the newly created component should keep its transform, or conform it to its parent

<a id="unreal.AddNewSubobjectParams.conform_transform_to_parent"></a>

#### conform_transform_to_parent

```python
@conform_transform_to_parent.setter
def conform_transform_to_parent(value: bool) -> None
```

<a id="unreal.ReparentSubobjectParams"></a>