## GeometryScriptCopySkinWeightProfileToAssetOptions Objects

```python
class GeometryScriptCopySkinWeightProfileToAssetOptions(StructBase)
```

Geometry Script Copy Skin Weight Profile to Asset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshAssetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``defer_mesh_post_edit_change`` (bool):  [Read-Write]
- ``emit_transaction`` (bool):  [Read-Write]
- ``overwrite_existing_profile`` (bool):  [Read-Write] If true and a skin weight profile with the given name exists, it will be overwritten.
  If false, will abort and print a console error.

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.__init__"></a>

#### __init__

```python
def __init__(overwrite_existing_profile: bool = False,
             emit_transaction: bool = False,
             defer_mesh_post_edit_change: bool = False) -> None
```

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.overwrite_existing_profile"></a>

#### overwrite_existing_profile

```python
@property
def overwrite_existing_profile() -> bool
```

(bool):  [Read-Write] If true and a skin weight profile with the given name exists, it will be overwritten.
If false, will abort and print a console error.

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.overwrite_existing_profile"></a>

#### overwrite_existing_profile

```python
@overwrite_existing_profile.setter
def overwrite_existing_profile(value: bool) -> None
```

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.emit_transaction"></a>

#### emit_transaction

```python
@property
def emit_transaction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.emit_transaction"></a>

#### emit_transaction

```python
@emit_transaction.setter
def emit_transaction(value: bool) -> None
```

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.defer_mesh_post_edit_change"></a>

#### defer_mesh_post_edit_change

```python
@property
def defer_mesh_post_edit_change() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.defer_mesh_post_edit_change"></a>

#### defer_mesh_post_edit_change

```python
@defer_mesh_post_edit_change.setter
def defer_mesh_post_edit_change(value: bool) -> None
```

<a id="unreal.GeometryScriptBakeTypeOptions"></a>