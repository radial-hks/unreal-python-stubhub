## FbxMaterialBakeSize Objects

```python
class FbxMaterialBakeSize(StructBase)
```

Fbx Material Bake Size

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxExportOption.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_detect`` (bool):  [Read-Write] If enabled, bake size is based on the largest texture used in the material input's expression graph. If none found, bake size will fall back to the explicit dimensions.
- ``size`` (IntPoint):  [Read-Write]

<a id="unreal.FbxMaterialBakeSize.__init__"></a>

#### __init__

```python
def __init__(size: IntPoint = [0, 0], auto_detect: bool = False) -> None
```

<a id="unreal.FbxMaterialBakeSize.size"></a>

#### size

```python
@property
def size() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.FbxMaterialBakeSize.size"></a>

#### size

```python
@size.setter
def size(value: IntPoint) -> None
```

<a id="unreal.FbxMaterialBakeSize.auto_detect"></a>

#### auto_detect

```python
@property
def auto_detect() -> bool
```

(bool):  [Read-Write] If enabled, bake size is based on the largest texture used in the material input's expression graph. If none found, bake size will fall back to the explicit dimensions.

<a id="unreal.FbxMaterialBakeSize.auto_detect"></a>

#### auto_detect

```python
@auto_detect.setter
def auto_detect(value: bool) -> None
```

<a id="unreal.ImportMeshLodSectionsData"></a>