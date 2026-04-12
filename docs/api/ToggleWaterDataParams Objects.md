## ToggleWaterDataParams Objects

```python
class ToggleWaterDataParams(ParamsBase)
```

Toggle Water Data Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: WimDynamicWaterAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``refresh_scene`` (bool):  [Read-Write]
- ``show_water`` (bool):  [Read-Write]

<a id="unreal.ToggleWaterDataParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(show_water: bool = False, refresh_scene: bool = False) -> None
```

<a id="unreal.ToggleWaterDataParams.show_water"></a>

#### show\_water

```python
@property
def show_water() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToggleWaterDataParams.show_water"></a>

#### show\_water

```python
@show_water.setter
def show_water(value: bool) -> None
```

<a id="unreal.ToggleWaterDataParams.refresh_scene"></a>

#### refresh\_scene

```python
@property
def refresh_scene() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToggleWaterDataParams.refresh_scene"></a>

#### refresh\_scene

```python
@refresh_scene.setter
def refresh_scene(value: bool) -> None
```

<a id="unreal.MeshHeatMapPointData"></a>