## VegetationCullRegion Objects

```python
class VegetationCullRegion(StructBase)
```

Vegetation Cull Region

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: WdpModelerEntity
- **File**: VegetationAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Only]
- ``loop_points`` (Array[Vector]):  [Read-Only]
- ``name`` (Name):  [Read-Only]

<a id="unreal.VegetationCullRegion.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None",
             enable: bool = False,
             loop_points: Array[Vector] = []) -> None
```

<a id="unreal.VegetationCullRegion.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.VegetationCullRegion.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Only]

<a id="unreal.VegetationCullRegion.loop_points"></a>

#### loop\_points

```python
@property
def loop_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.ModelerRegionName"></a>