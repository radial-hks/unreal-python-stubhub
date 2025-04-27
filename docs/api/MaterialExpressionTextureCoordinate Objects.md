## MaterialExpressionTextureCoordinate Objects

```python
class MaterialExpressionTextureCoordinate(MaterialExpression)
```

Material Expression Texture Coordinate

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTextureCoordinate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coordinate_index`` (int32):  [Read-Write] Texture coordinate index
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``u_tiling`` (float):  [Read-Write] Controls how much the texture tiles horizontally, by scaling the U component of the vertex UVs by the specified amount.
- ``un_mirror_u`` (bool):  [Read-Write] Would like to unmirror U or V
  - if the texture is mirrored and if you would like to undo mirroring for this texture sample, use this to unmirror
- ``un_mirror_v`` (bool):  [Read-Write]
- ``v_tiling`` (float):  [Read-Write] Controls how much the texture tiles vertically, by scaling the V component of the vertex UVs by the specified amount.

<a id="unreal.MaterialExpressionTextureCoordinate.coordinate_index"></a>

#### coordinate_index

```python
@property
def coordinate_index() -> int
```

(int32):  [Read-Write] Texture coordinate index

<a id="unreal.MaterialExpressionTextureCoordinate.coordinate_index"></a>

#### coordinate_index

```python
@coordinate_index.setter
def coordinate_index(value: int) -> None
```

<a id="unreal.MaterialExpressionTextureCoordinate.u_tiling"></a>

#### u_tiling

```python
@property
def u_tiling() -> float
```

(float):  [Read-Write] Controls how much the texture tiles horizontally, by scaling the U component of the vertex UVs by the specified amount.

<a id="unreal.MaterialExpressionTextureCoordinate.u_tiling"></a>

#### u_tiling

```python
@u_tiling.setter
def u_tiling(value: float) -> None
```

<a id="unreal.MaterialExpressionTextureCoordinate.v_tiling"></a>

#### v_tiling

```python
@property
def v_tiling() -> float
```

(float):  [Read-Write] Controls how much the texture tiles vertically, by scaling the V component of the vertex UVs by the specified amount.

<a id="unreal.MaterialExpressionTextureCoordinate.v_tiling"></a>

#### v_tiling

```python
@v_tiling.setter
def v_tiling(value: float) -> None
```

<a id="unreal.MaterialExpressionTextureObject"></a>