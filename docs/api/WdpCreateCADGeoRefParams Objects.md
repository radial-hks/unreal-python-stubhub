## WdpCreateCADGeoRefParams Objects

```python
class WdpCreateCADGeoRefParams(ParamsBase)
```

Wdp Create CADGeo Ref Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cad_points`` (Array[Vector]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``world_points`` (Array[Vector]):  [Read-Write]

<a id="unreal.WdpCreateCADGeoRefParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cad_points: Array[Vector] = [],
             world_points: Array[Vector] = []) -> None
```

<a id="unreal.WdpCreateCADGeoRefParams.cad_points"></a>

#### cad\_points

```python
@property
def cad_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WdpCreateCADGeoRefParams.cad_points"></a>

#### cad\_points

```python
@cad_points.setter
def cad_points(value: Array[Vector]) -> None
```

<a id="unreal.WdpCreateCADGeoRefParams.world_points"></a>

#### world\_points

```python
@property
def world_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WdpCreateCADGeoRefParams.world_points"></a>

#### world\_points

```python
@world_points.setter
def world_points(value: Array[Vector]) -> None
```

<a id="unreal.NewMaterialsInfo"></a>