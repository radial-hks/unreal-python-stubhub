## ControlRigShapeLibraryLink Objects

```python
class ControlRigShapeLibraryLink(NameSpacedUserData)
```

Namespaced user data which provides access to a linked shape library

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name_space`` (str):  [Read-Write] The namespace to use when looking up values inside of the user data.
- ``shape_library`` (ControlRigShapeLibrary):  [Read-Write] If assigned, the data asset link will provide access to the data asset's content.

<a id="unreal.ControlRigShapeLibraryLink.shape_library"></a>

#### shape_library

```python
@property
def shape_library() -> ControlRigShapeLibrary
```

(ControlRigShapeLibrary):  [Read-Write] If assigned, the data asset link will provide access to the data asset's content.

<a id="unreal.ControlRigShapeLibraryLink.shape_library"></a>

#### shape_library

```python
@shape_library.setter
def shape_library(value: ControlRigShapeLibrary) -> None
```

<a id="unreal.ControlRig"></a>