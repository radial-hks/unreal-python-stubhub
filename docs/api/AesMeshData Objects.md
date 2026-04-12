## AesMeshData Objects

```python
class AesMeshData(StructBase)
```

模型信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_ref`` (SoftObjectPath):  [Read-Write] 模型资产引用
- ``bounds`` (Box3f):  [Read-Write] 模型资产包围盒大小
- ``component_class`` (SoftClassPath):  [Read-Write] 组件引用
- ``materials`` (Array[SoftObjectPath]):  [Read-Write] 模型资产替换材质

<a id="unreal.AesMeshData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset_ref: SoftObjectPath = [""],
             component_class: SoftClassPath = [""],
             materials: Array[SoftObjectPath] = [],
             bounds: Box3f = []) -> None
```

<a id="unreal.AesMeshData.asset_ref"></a>

#### asset\_ref

```python
@property
def asset_ref() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 模型资产引用

<a id="unreal.AesMeshData.asset_ref"></a>

#### asset\_ref

```python
@asset_ref.setter
def asset_ref(value: SoftObjectPath) -> None
```

<a id="unreal.AesMeshData.component_class"></a>

#### component\_class

```python
@property
def component_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] 组件引用

<a id="unreal.AesMeshData.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: SoftClassPath) -> None
```

<a id="unreal.AesMeshData.materials"></a>

#### materials

```python
@property
def materials() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 模型资产替换材质

<a id="unreal.AesMeshData.materials"></a>

#### materials

```python
@materials.setter
def materials(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.AesMeshData.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box3f
```

(Box3f):  [Read-Write] 模型资产包围盒大小

<a id="unreal.AesMeshData.bounds"></a>

#### bounds

```python
@bounds.setter
def bounds(value: Box3f) -> None
```

<a id="unreal.AesMaterialData"></a>