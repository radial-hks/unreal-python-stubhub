## EarthMaterialFragment Objects

```python
class EarthMaterialFragment(EarthPropertyFragment)
```

定义材质数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``overlay_material`` (MaterialInterface):  [Read-Write] 叠加材质
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] 覆盖材质列表
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] 运行时虚拟纹理列表
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthMaterialFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        override_materials: Array[MaterialInterface] = [],
        overlay_material: MaterialInterface = None,
        runtime_virtual_textures: Array[RuntimeVirtualTexture] = []) -> None
```

<a id="unreal.EarthMaterialFragment.override_materials"></a>

#### override\_materials

```python
@property
def override_materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write] 覆盖材质列表

<a id="unreal.EarthMaterialFragment.override_materials"></a>

#### override\_materials

```python
@override_materials.setter
def override_materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.EarthMaterialFragment.overlay_material"></a>

#### overlay\_material

```python
@property
def overlay_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] 叠加材质

<a id="unreal.EarthMaterialFragment.overlay_material"></a>

#### overlay\_material

```python
@overlay_material.setter
def overlay_material(value: MaterialInterface) -> None
```

<a id="unreal.EarthMaterialFragment.runtime_virtual_textures"></a>

#### runtime\_virtual\_textures

```python
@property
def runtime_virtual_textures() -> Array[RuntimeVirtualTexture]
```

(Array[RuntimeVirtualTexture]):  [Read-Write] 运行时虚拟纹理列表

<a id="unreal.EarthMaterialFragment.runtime_virtual_textures"></a>

#### runtime\_virtual\_textures

```python
@runtime_virtual_textures.setter
def runtime_virtual_textures(value: Array[RuntimeVirtualTexture]) -> None
```

<a id="unreal.EarthSubAssetsFragment"></a>