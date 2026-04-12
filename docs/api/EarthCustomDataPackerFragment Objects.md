## EarthCustomDataPackerFragment Objects

```python
class EarthCustomDataPackerFragment(EarthPropertyFragment)
```

自定义数据打包器片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthInstancedStaticMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_data_attributes`` (Map[Name, float]):  [Read-Write] 从数据片段中提取自定义数据的属性路径，键为属性路径，值为默认属性值
  --- 格式规则 ---
  1. 通用格式: "片段名称.属性名称.分量名称"，使用 "." 分隔嵌套结构体成员
    - 片段名称可省略前缀"Earth"和后缀"Fragment"
    - 示例: "Transform.Rotation" 等价于 "EarthTransformFragment.Rotation"
    - 当查找不到属性时，会直接添加默认属性值
  2. 简写规则:
    - 以"
  ": 开头表示引用片段的同名属性，自动补全片段名称 - 示例: "
  Color.R": 等价于 "EarthColorFragment.Color.R" 3. 支持常见结构体的分量，且不能不写分量来使用: - 向量: X/Y/Z/W, 颜色: R/G/B/A, 旋转: Pitch/Yaw/Roll - 示例: "
  Rotation.Yaw",: "
  Color.A": 4. 支持结构体连续嵌套: - 示例: 提取包围盒片段的包围盒的 Min 的 Z 坐标: "Bounds.Bounds.Min.Z"或"
  Bounds.Min.Z": 5. 特殊字段: - FeatureID: 自动将 64 位整数转换为 32 位浮点数 - FColor：将除255转FLinearColor后再提取数据
- ``packed_custom_data`` (Array[float]):  [Read-Only] 实例自定义数据
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthCustomDataPackerFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             custom_data_attributes: Map[Name, float] = {},
             packed_custom_data: Array[float] = []) -> None
```

<a id="unreal.EarthCustomDataPackerFragment.custom_data_attributes"></a>

#### custom\_data\_attributes

```python
@property
def custom_data_attributes() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 从数据片段中提取自定义数据的属性路径，键为属性路径，值为默认属性值
--- 格式规则 ---
1. 通用格式: "片段名称.属性名称.分量名称"，使用 "." 分隔嵌套结构体成员
  - 片段名称可省略前缀"Earth"和后缀"Fragment"
  - 示例: "Transform.Rotation" 等价于 "EarthTransformFragment.Rotation"
  - 当查找不到属性时，会直接添加默认属性值
2. 简写规则:
  - 以"
": 开头表示引用片段的同名属性，自动补全片段名称 - 示例: "
Color.R": 等价于 "EarthColorFragment.Color.R" 3. 支持常见结构体的分量，且不能不写分量来使用: - 向量: X/Y/Z/W, 颜色: R/G/B/A, 旋转: Pitch/Yaw/Roll - 示例: "
Rotation.Yaw",: "
Color.A": 4. 支持结构体连续嵌套: - 示例: 提取包围盒片段的包围盒的 Min 的 Z 坐标: "Bounds.Bounds.Min.Z"或"
Bounds.Min.Z": 5. 特殊字段: - FeatureID: 自动将 64 位整数转换为 32 位浮点数 - FColor：将除255转FLinearColor后再提取数据

<a id="unreal.EarthCustomDataPackerFragment.custom_data_attributes"></a>

#### custom\_data\_attributes

```python
@custom_data_attributes.setter
def custom_data_attributes(value: Map[Name, float]) -> None
```

<a id="unreal.EarthCustomDataPackerFragment.packed_custom_data"></a>

#### packed\_custom\_data

```python
@property
def packed_custom_data() -> Array[float]
```

(Array[float]):  [Read-Only] 实例自定义数据

<a id="unreal.EarthInstanceTransformsFragment"></a>