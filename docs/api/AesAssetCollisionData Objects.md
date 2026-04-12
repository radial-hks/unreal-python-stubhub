## AesAssetCollisionData Objects

```python
class AesAssetCollisionData(StructBase)
```

资产碰撞数据基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_type`` (AesAssetCollisionType):  [Read-Write] 碰撞创建类型
- ``component_class`` (SoftClassPath):  [Read-Write] 组件引用

<a id="unreal.AesAssetCollisionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(collision_type: AesAssetCollisionType = AesAssetCollisionType.
             BOUNDS_NO_CAP,
             component_class: SoftClassPath = [""]) -> None
```

<a id="unreal.AesAssetCollisionData.collision_type"></a>

#### collision\_type

```python
@property
def collision_type() -> AesAssetCollisionType
```

(AesAssetCollisionType):  [Read-Write] 碰撞创建类型

<a id="unreal.AesAssetCollisionData.collision_type"></a>

#### collision\_type

```python
@collision_type.setter
def collision_type(value: AesAssetCollisionType) -> None
```

<a id="unreal.AesAssetCollisionData.component_class"></a>

#### component\_class

```python
@property
def component_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] 组件引用

<a id="unreal.AesAssetCollisionData.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: SoftClassPath) -> None
```

<a id="unreal.AesAssetChildMetaData"></a>