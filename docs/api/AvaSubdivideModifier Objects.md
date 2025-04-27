## AvaSubdivideModifier Objects

```python
class AvaSubdivideModifier(AvaGeometryBaseModifier)
```

Ava Subdivide Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaSubdivideModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cuts`` (int32):  [Read-Write]
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``recompute_normals`` (bool):  [Read-Write]
- ``type`` (AvaSubdivisionType):  [Read-Write]

<a id="unreal.AvaSubdivideModifier.set_type"></a>

#### set_type

```python
def set_type(type: AvaSubdivisionType) -> None
```

x.set_type(type) -> None
Set Type

Args:
    type (AvaSubdivisionType):

<a id="unreal.AvaSubdivideModifier.set_recompute_normals"></a>

#### set_recompute_normals

```python
def set_recompute_normals(recompute_normals: bool) -> None
```

x.set_recompute_normals(recompute_normals) -> None
Set Recompute Normals

Args:
    recompute_normals (bool):

<a id="unreal.AvaSubdivideModifier.set_cuts"></a>

#### set_cuts

```python
def set_cuts(cuts: int) -> None
```

x.set_cuts(cuts) -> None
Set Cuts

Args:
    cuts (int32):

<a id="unreal.AvaSubdivideModifier.get_type"></a>

#### get_type

```python
def get_type() -> AvaSubdivisionType
```

x.get_type() -> AvaSubdivisionType
Get Type

Returns:
    AvaSubdivisionType:

<a id="unreal.AvaSubdivideModifier.get_recompute_normals"></a>

#### get_recompute_normals

```python
def get_recompute_normals() -> bool
```

x.get_recompute_normals() -> bool
Get Recompute Normals

Returns:
    bool:

<a id="unreal.AvaSubdivideModifier.get_cuts"></a>

#### get_cuts

```python
def get_cuts() -> int
```

x.get_cuts() -> int32
Get Cuts

Returns:
    int32:

<a id="unreal.AvaTaperModifier"></a>