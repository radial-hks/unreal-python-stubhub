## EarthUpdateDependency Objects

```python
class EarthUpdateDependency(StructBase)
```

Earth Update Dependency

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthCore
- **File**: EarthEntityInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dependency_entity`` (int64):  [Read-Write]
- ``linked_atom_class`` (type(Class)):  [Read-Write]
- ``linked_atom_prop_name`` (Name):  [Read-Write]

<a id="unreal.EarthUpdateDependency.__init__"></a>

#### \_\_init\_\_

```python
def __init__(dependency_entity: int = 0,
             linked_atom_class: Class = None,
             linked_atom_prop_name: Name = "None") -> None
```

<a id="unreal.EarthUpdateDependency.dependency_entity"></a>

#### dependency\_entity

```python
@property
def dependency_entity() -> int
```

(int64):  [Read-Write]

<a id="unreal.EarthUpdateDependency.dependency_entity"></a>

#### dependency\_entity

```python
@dependency_entity.setter
def dependency_entity(value: int) -> None
```

<a id="unreal.EarthUpdateDependency.linked_atom_class"></a>

#### linked\_atom\_class

```python
@property
def linked_atom_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.EarthUpdateDependency.linked_atom_class"></a>

#### linked\_atom\_class

```python
@linked_atom_class.setter
def linked_atom_class(value: Class) -> None
```

<a id="unreal.EarthUpdateDependency.linked_atom_prop_name"></a>

#### linked\_atom\_prop\_name

```python
@property
def linked_atom_prop_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EarthUpdateDependency.linked_atom_prop_name"></a>

#### linked\_atom\_prop\_name

```python
@linked_atom_prop_name.setter
def linked_atom_prop_name(value: Name) -> None
```

<a id="unreal.EarthAtomChangedProperty"></a>