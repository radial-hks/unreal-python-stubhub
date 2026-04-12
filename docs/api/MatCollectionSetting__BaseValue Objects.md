## MatCollectionSetting\_BaseValue Objects

```python
class MatCollectionSetting_BaseValue(StructBase)
```

Mat Collection Setting Base Value

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: TOD_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scalar_para`` (Map[Name, float]):  [Read-Write]
- ``vector_para`` (Map[Name, LinearColor]):  [Read-Write]

<a id="unreal.MatCollectionSetting_BaseValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(scalar_para: Map[Name, float] = {},
             vector_para: Map[Name, LinearColor] = {}) -> None
```

<a id="unreal.MatCollectionSetting_BaseValue.scalar_para"></a>

#### scalar\_para

```python
@property
def scalar_para() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write]

<a id="unreal.MatCollectionSetting_BaseValue.scalar_para"></a>

#### scalar\_para

```python
@scalar_para.setter
def scalar_para(value: Map[Name, float]) -> None
```

<a id="unreal.MatCollectionSetting_BaseValue.vector_para"></a>

#### vector\_para

```python
@property
def vector_para() -> Map[Name, LinearColor]
```

(Map[Name, LinearColor]):  [Read-Write]

<a id="unreal.MatCollectionSetting_BaseValue.vector_para"></a>

#### vector\_para

```python
@vector_para.setter
def vector_para(value: Map[Name, LinearColor]) -> None
```

<a id="unreal.MatCollectionSetting"></a>