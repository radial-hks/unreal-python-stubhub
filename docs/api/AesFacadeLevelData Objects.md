## AesFacadeLevelData Objects

```python
class AesFacadeLevelData(StructBase)
```

立面层数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesFacadeAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``corners`` (str):  [Read-Write]
- ``height`` (float):  [Read-Write]
- ``module_grammar`` (str):  [Read-Write]
- ``variations`` (Map[Name, float]):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.AesFacadeLevelData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(module_grammar: str = "",
             height: float = 0.000000,
             weight: float = 0.000000,
             variations: Map[Name, float] = {}) -> None
```

<a id="unreal.AesFacadeLevelData.module_grammar"></a>

#### module\_grammar

```python
@property
def module_grammar() -> str
```

(str):  [Read-Write]

<a id="unreal.AesFacadeLevelData.module_grammar"></a>

#### module\_grammar

```python
@module_grammar.setter
def module_grammar(value: str) -> None
```

<a id="unreal.AesFacadeLevelData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write]

<a id="unreal.AesFacadeLevelData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesFacadeLevelData.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.AesFacadeLevelData.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.AesFacadeLevelData.variations"></a>

#### variations

```python
@property
def variations() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write]

<a id="unreal.AesFacadeLevelData.variations"></a>

#### variations

```python
@variations.setter
def variations(value: Map[Name, float]) -> None
```

<a id="unreal.AesFacadeShapeGrammar"></a>