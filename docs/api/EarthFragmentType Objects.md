## EarthFragmentType Objects

```python
class EarthFragmentType(EnumBase)
```

数据片段类型

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

<a id="unreal.EarthFragmentType.ENTITY"></a>

#### ENTITY

1: 实体片段类型：定义预制体的核心属性，与GIS数据源的要素关联，如地形、建筑、道路等
由外部传入时，会覆盖预制体内的实体片段的属性值

<a id="unreal.EarthFragmentType.SPATIAL"></a>

#### SPATIAL

2: 空间片段类型：定义预制体的几何形状或空间布局，可关联矢量、点云、栅格等数据
一般由外部数据传入，如果是静态预制体资产，则会存储一份在预制体资产中

<a id="unreal.EarthFragmentType.PROPERTY"></a>

#### PROPERTY

4: 属性片段类型：定义可传递给子资产或生成物的次要属性
预制体和外部皆可用

<a id="unreal.EarthFragmentType.OUTPUT"></a>

#### OUTPUT

8: 输出片段类型：定义预制体生成的最终产物
可被其他系统消费（如渲染系统或游戏玩法系统）

<a id="unreal.EarthFragmentType.EXTERNAL"></a>

#### EXTERNAL

16: 外部片段类型：定义驱动生成流程的控制指令或外部数据源标识
通常由外部系统（如GIS服务或生成子系统）注入，不建议预制体直接持有

<a id="unreal.EarthFragmentType.EXTENSION"></a>

#### EXTENSION

32: 扩展片段类型：预留给第三方工具或自定义生成算法的扩展类型

<a id="unreal.EarthFragmentType.ANY"></a>

#### ANY

63: 全类型掩码：支持所有类型组合的位掩码，用于快速匹配或配置
注意：仅在需要全类型兼容时使用（如编辑器选择器）

<a id="unreal.EarthLandCover"></a>