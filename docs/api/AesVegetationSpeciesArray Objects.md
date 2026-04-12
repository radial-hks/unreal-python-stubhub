## AesVegetationSpeciesArray Objects

```python
class AesVegetationSpeciesArray(TableRowBase)
```

植被树种资产列表

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesVegetationAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_density`` (float):  [Read-Write] 种植密度
- ``species_list`` (Array[AesVegetationSpecie]):  [Read-Write] 树种列表

<a id="unreal.AesVegetationSpeciesArray.__init__"></a>

#### \_\_init\_\_

```python
def __init__(global_density: float = 0.000000,
             species_list: Array[AesVegetationSpecie] = []) -> None
```

<a id="unreal.AesVegetationSpeciesArray.global_density"></a>

#### global\_density

```python
@property
def global_density() -> float
```

(float):  [Read-Write] 种植密度

<a id="unreal.AesVegetationSpeciesArray.global_density"></a>

#### global\_density

```python
@global_density.setter
def global_density(value: float) -> None
```

<a id="unreal.AesVegetationSpeciesArray.species_list"></a>

#### species\_list

```python
@property
def species_list() -> Array[AesVegetationSpecie]
```

(Array[AesVegetationSpecie]):  [Read-Write] 树种列表

<a id="unreal.AesVegetationSpeciesArray.species_list"></a>

#### species\_list

```python
@species_list.setter
def species_list(value: Array[AesVegetationSpecie]) -> None
```

<a id="unreal.AesVegetationBiomeRule"></a>