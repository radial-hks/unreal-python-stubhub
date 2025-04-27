## RigUnit_SetupShapeLibraryFromUserData Objects

```python
class RigUnit_SetupShapeLibraryFromUserData(RigUnitMutable)
```

Allows to set / add a shape library on the running control rig from user data

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_UserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``library_name`` (str):  [Read-Write] * Optionally provide the namespace of the shape library to use.
  * This is only useful if you have multiple shape libraries and you
  * want to override a specific one.
- ``log_shape_libraries`` (bool):  [Read-Write] * If this is checked we'll output the resulting shape libraries to the log for debugging.
- ``name_space`` (str):  [Read-Write] * The name space of the user data to look the shape library up within
- ``path`` (str):  [Read-Write] * The path within the user data for the shape library

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             name_space: str = "",
             path: str = "",
             library_name: str = "",
             log_shape_libraries: bool = False) -> None
```

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.name_space"></a>

#### name_space

```python
@property
def name_space() -> str
```

(str):  [Read-Write] * The name space of the user data to look the shape library up within

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: str) -> None
```

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.path"></a>

#### path

```python
@property
def path() -> str
```

(str):  [Read-Write] * The path within the user data for the shape library

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.path"></a>

#### path

```python
@path.setter
def path(value: str) -> None
```

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.library_name"></a>

#### library_name

```python
@property
def library_name() -> str
```

(str):  [Read-Write] * Optionally provide the namespace of the shape library to use.
* This is only useful if you have multiple shape libraries and you
* want to override a specific one.

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.library_name"></a>

#### library_name

```python
@library_name.setter
def library_name(value: str) -> None
```

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.log_shape_libraries"></a>

#### log_shape_libraries

```python
@property
def log_shape_libraries() -> bool
```

(bool):  [Read-Write] * If this is checked we'll output the resulting shape libraries to the log for debugging.

<a id="unreal.RigUnit_SetupShapeLibraryFromUserData.log_shape_libraries"></a>

#### log_shape_libraries

```python
@log_shape_libraries.setter
def log_shape_libraries(value: bool) -> None
```

<a id="unreal.RigUnit_ShapeExists"></a>