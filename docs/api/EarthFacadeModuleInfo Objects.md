## EarthFacadeModuleInfo Objects

```python
class EarthFacadeModuleInfo(StructBase)
```

用于立面拼装的模块信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_scale`` (bool):  [Read-Write] 模块是否在生成时使用缩放值，如果为“否”，则模块的缩放值为1
- ``asset`` (EarthPrefabAsset):  [Read-Write] 模块资产引用
- ``custom_length`` (float):  [Read-Write] 自定义的模块所占长度
- ``pivot_location`` (Vector):  [Read-Write] 基于模块的包围盒尺寸，设置归一化的轴心位置
  例：全0表示移动轴心到包围盒最小点，全0.5表示移动轴心到包围盒中心点，全1表示移动轴心到包围盒最大点
- ``scalable`` (bool):  [Read-Write] 模块所占长度是否可以缩放以适应剩余空间
- ``symbol`` (Name):  [Read-Write] 模块在形状语法中的符号表示
- ``transform`` (Transform):  [Read-Write] 模块的变换信息
- ``use_as_placeholder`` (bool):  [Read-Write] 模块是否作为占位符使用
- ``use_custom_length`` (bool):  [Read-Write] 是否使用自定义的模块所占长度
- ``use_custom_pivot_location`` (bool):  [Read-Write] 是否使用自定义的归一化的轴心位置

<a id="unreal.EarthFacadeModuleInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    symbol: Name = "None",
    asset: EarthPrefabAsset = None,
    use_custom_length: bool = False,
    custom_length: float = 0.000000,
    scalable: bool = False,
    apply_scale: bool = False,
    use_as_placeholder: bool = False,
    use_custom_pivot_location: bool = False,
    pivot_location: Vector = [0.000000, 0.000000, 0.000000],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.EarthFacadeModuleInfo.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] 模块在形状语法中的符号表示

<a id="unreal.EarthFacadeModuleInfo.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.EarthFacadeModuleInfo.asset"></a>

#### asset

```python
@property
def asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 模块资产引用

<a id="unreal.EarthFacadeModuleInfo.asset"></a>

#### asset

```python
@asset.setter
def asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthFacadeModuleInfo.use_custom_length"></a>

#### use\_custom\_length

```python
@property
def use_custom_length() -> bool
```

(bool):  [Read-Write] 是否使用自定义的模块所占长度

<a id="unreal.EarthFacadeModuleInfo.use_custom_length"></a>

#### use\_custom\_length

```python
@use_custom_length.setter
def use_custom_length(value: bool) -> None
```

<a id="unreal.EarthFacadeModuleInfo.custom_length"></a>

#### custom\_length

```python
@property
def custom_length() -> float
```

(float):  [Read-Write] 自定义的模块所占长度

<a id="unreal.EarthFacadeModuleInfo.custom_length"></a>

#### custom\_length

```python
@custom_length.setter
def custom_length(value: float) -> None
```

<a id="unreal.EarthFacadeModuleInfo.scalable"></a>

#### scalable

```python
@property
def scalable() -> bool
```

(bool):  [Read-Write] 模块所占长度是否可以缩放以适应剩余空间

<a id="unreal.EarthFacadeModuleInfo.scalable"></a>

#### scalable

```python
@scalable.setter
def scalable(value: bool) -> None
```

<a id="unreal.EarthFacadeModuleInfo.apply_scale"></a>

#### apply\_scale

```python
@property
def apply_scale() -> bool
```

(bool):  [Read-Write] 模块是否在生成时使用缩放值，如果为“否”，则模块的缩放值为1

<a id="unreal.EarthFacadeModuleInfo.apply_scale"></a>

#### apply\_scale

```python
@apply_scale.setter
def apply_scale(value: bool) -> None
```

<a id="unreal.EarthFacadeModuleInfo.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@property
def use_as_placeholder() -> bool
```

(bool):  [Read-Write] 模块是否作为占位符使用

<a id="unreal.EarthFacadeModuleInfo.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@use_as_placeholder.setter
def use_as_placeholder(value: bool) -> None
```

<a id="unreal.EarthFacadeModuleInfo.use_custom_pivot_location"></a>

#### use\_custom\_pivot\_location

```python
@property
def use_custom_pivot_location() -> bool
```

(bool):  [Read-Write] 是否使用自定义的归一化的轴心位置

<a id="unreal.EarthFacadeModuleInfo.use_custom_pivot_location"></a>

#### use\_custom\_pivot\_location

```python
@use_custom_pivot_location.setter
def use_custom_pivot_location(value: bool) -> None
```

<a id="unreal.EarthFacadeModuleInfo.pivot_location"></a>

#### pivot\_location

```python
@property
def pivot_location() -> Vector
```

(Vector):  [Read-Write] 基于模块的包围盒尺寸，设置归一化的轴心位置
例：全0表示移动轴心到包围盒最小点，全0.5表示移动轴心到包围盒中心点，全1表示移动轴心到包围盒最大点

<a id="unreal.EarthFacadeModuleInfo.pivot_location"></a>

#### pivot\_location

```python
@pivot_location.setter
def pivot_location(value: Vector) -> None
```

<a id="unreal.EarthFacadeModuleInfo.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] 模块的变换信息

<a id="unreal.EarthFacadeModuleInfo.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.EarthFacadeLevelInfo"></a>