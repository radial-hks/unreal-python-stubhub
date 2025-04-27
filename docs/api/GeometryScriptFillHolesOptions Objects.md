## GeometryScriptFillHolesOptions Objects

```python
class GeometryScriptFillHolesOptions(StructBase)
```

Geometry Script Fill Holes Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delete_isolated_triangles`` (bool):  [Read-Write] Delete floating, disconnected triangles, as they produce a "hole" that cannot be filled
- ``fill_method`` (GeometryScriptFillHolesMethod):  [Read-Write]

<a id="unreal.GeometryScriptFillHolesOptions.__init__"></a>

#### __init__

```python
def __init__(
        fill_method:
    GeometryScriptFillHolesMethod = GeometryScriptFillHolesMethod.AUTOMATIC,
        delete_isolated_triangles: bool = False) -> None
```

<a id="unreal.GeometryScriptFillHolesOptions.fill_method"></a>

#### fill_method

```python
@property
def fill_method() -> GeometryScriptFillHolesMethod
```

(GeometryScriptFillHolesMethod):  [Read-Write]

<a id="unreal.GeometryScriptFillHolesOptions.fill_method"></a>

#### fill_method

```python
@fill_method.setter
def fill_method(value: GeometryScriptFillHolesMethod) -> None
```

<a id="unreal.GeometryScriptFillHolesOptions.delete_isolated_triangles"></a>

#### delete_isolated_triangles

```python
@property
def delete_isolated_triangles() -> bool
```

(bool):  [Read-Write] Delete floating, disconnected triangles, as they produce a "hole" that cannot be filled

<a id="unreal.GeometryScriptFillHolesOptions.delete_isolated_triangles"></a>

#### delete_isolated_triangles

```python
@delete_isolated_triangles.setter
def delete_isolated_triangles(value: bool) -> None
```

<a id="unreal.GeometryScriptRemoveSmallComponentOptions"></a>