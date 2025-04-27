## GeometryScriptCopyMorphTargetToAssetOptions Objects

```python
class GeometryScriptCopyMorphTargetToAssetOptions(StructBase)
```

Geometry Script Copy Morph Target to Asset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshAssetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``defer_mesh_post_edit_change`` (bool):  [Read-Write]
- ``emit_transaction`` (bool):  [Read-Write]
- ``overwrite_existing_target`` (bool):  [Read-Write] If true and the morph target with the given name exists, it will be overwritten. If false, will abort and print a
  console error.

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.__init__"></a>

#### __init__

```python
def __init__(overwrite_existing_target: bool = False,
             emit_transaction: bool = False,
             defer_mesh_post_edit_change: bool = False) -> None
```

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.overwrite_existing_target"></a>

#### overwrite_existing_target

```python
@property
def overwrite_existing_target() -> bool
```

(bool):  [Read-Write] If true and the morph target with the given name exists, it will be overwritten. If false, will abort and print a
console error.

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.overwrite_existing_target"></a>

#### overwrite_existing_target

```python
@overwrite_existing_target.setter
def overwrite_existing_target(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.emit_transaction"></a>

#### emit_transaction

```python
@property
def emit_transaction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.emit_transaction"></a>

#### emit_transaction

```python
@emit_transaction.setter
def emit_transaction(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.defer_mesh_post_edit_change"></a>

#### defer_mesh_post_edit_change

```python
@property
def defer_mesh_post_edit_change() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions.defer_mesh_post_edit_change"></a>

#### defer_mesh_post_edit_change

```python
@defer_mesh_post_edit_change.setter
def defer_mesh_post_edit_change(value: bool) -> None
```

<a id="unreal.GeometryScriptCopySkinWeightProfileToAssetOptions"></a>