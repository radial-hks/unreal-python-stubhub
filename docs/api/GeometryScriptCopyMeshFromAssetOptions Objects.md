## GeometryScriptCopyMeshFromAssetOptions Objects

```python
class GeometryScriptCopyMeshFromAssetOptions(StructBase)
```

Geometry Script Copy Mesh from Asset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshAssetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_build_settings`` (bool):  [Read-Write] Whether to apply Build Settings during the mesh copy.
- ``ignore_remove_degenerates`` (bool):  [Read-Write] Whether to ignore the 'remove degenerates' option from Build Settings. Note: Only applies if 'Apply Build Settings' is enabled.
- ``request_tangents`` (bool):  [Read-Write] Whether to request tangents on the copied mesh. If tangents are not requested, tangent-related build settings will also be ignored.
- ``use_build_scale`` (bool):  [Read-Write] Whether to scale the copied mesh by the Build Setting's 'Build Scale'. Note: This is considered separately from the 'Apply Build Settings' option.

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.__init__"></a>

#### __init__

```python
def __init__(apply_build_settings: bool = False,
             request_tangents: bool = False,
             ignore_remove_degenerates: bool = False,
             use_build_scale: bool = False) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.apply_build_settings"></a>

#### apply_build_settings

```python
@property
def apply_build_settings() -> bool
```

(bool):  [Read-Write] Whether to apply Build Settings during the mesh copy.

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.apply_build_settings"></a>

#### apply_build_settings

```python
@apply_build_settings.setter
def apply_build_settings(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.request_tangents"></a>

#### request_tangents

```python
@property
def request_tangents() -> bool
```

(bool):  [Read-Write] Whether to request tangents on the copied mesh. If tangents are not requested, tangent-related build settings will also be ignored.

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.request_tangents"></a>

#### request_tangents

```python
@request_tangents.setter
def request_tangents(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.ignore_remove_degenerates"></a>

#### ignore_remove_degenerates

```python
@property
def ignore_remove_degenerates() -> bool
```

(bool):  [Read-Write] Whether to ignore the 'remove degenerates' option from Build Settings. Note: Only applies if 'Apply Build Settings' is enabled.

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.ignore_remove_degenerates"></a>

#### ignore_remove_degenerates

```python
@ignore_remove_degenerates.setter
def ignore_remove_degenerates(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.use_build_scale"></a>

#### use_build_scale

```python
@property
def use_build_scale() -> bool
```

(bool):  [Read-Write] Whether to scale the copied mesh by the Build Setting's 'Build Scale'. Note: This is considered separately from the 'Apply Build Settings' option.

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions.use_build_scale"></a>

#### use_build_scale

```python
@use_build_scale.setter
def use_build_scale(value: bool) -> None
```

<a id="unreal.GeometryScriptNaniteOptions"></a>