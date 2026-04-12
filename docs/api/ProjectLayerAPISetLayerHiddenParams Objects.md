## ProjectLayerAPISetLayerHiddenParams Objects

```python
class ProjectLayerAPISetLayerHiddenParams(ParamsBase)
```

Project Layer APISet Layer Hidden Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpProjectLayerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hidden`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``layer_names`` (Set[str]):  [Read-Write]

<a id="unreal.ProjectLayerAPISetLayerHiddenParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(layer_names: Set[str] = [], hidden: bool = False) -> None
```

<a id="unreal.ProjectLayerAPISetLayerHiddenParams.layer_names"></a>

#### layer\_names

```python
@property
def layer_names() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.ProjectLayerAPISetLayerHiddenParams.layer_names"></a>

#### layer\_names

```python
@layer_names.setter
def layer_names(value: Set[str]) -> None
```

<a id="unreal.ProjectLayerAPISetLayerHiddenParams.hidden"></a>

#### hidden

```python
@property
def hidden() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ProjectLayerAPISetLayerHiddenParams.hidden"></a>

#### hidden

```python
@hidden.setter
def hidden(value: bool) -> None
```

<a id="unreal.WDPScreenPosBoundAddParams"></a>