## TilingConfig Objects

```python
class TilingConfig(StructBase)
```

Tiling configuration for fixed and dynamic size models

**C++ Source:**

- **Plugin**: NNEDenoiser
- **Module**: NNEDenoiser
- **File**: NNEDenoiserTilingConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (int32):  [Read-Write] Tile size alignment (applies only to dynamic size models)
- ``max_size`` (int32):  [Read-Write] Maximum tile size (applies only to dynamic size models)
- ``min_size`` (int32):  [Read-Write] Minimum tile size (applies only to dynamic size models)
- ``overlap`` (int32):  [Read-Write] Tile overlap

<a id="unreal.TilingConfig.__init__"></a>

#### __init__

```python
def __init__(alignment: int = 0,
             overlap: int = 0,
             max_size: int = 0,
             min_size: int = 0) -> None
```

<a id="unreal.TilingConfig.alignment"></a>

#### alignment

```python
@property
def alignment() -> int
```

(int32):  [Read-Write] Tile size alignment (applies only to dynamic size models)

<a id="unreal.TilingConfig.alignment"></a>

#### alignment

```python
@alignment.setter
def alignment(value: int) -> None
```

<a id="unreal.TilingConfig.overlap"></a>

#### overlap

```python
@property
def overlap() -> int
```

(int32):  [Read-Write] Tile overlap

<a id="unreal.TilingConfig.overlap"></a>

#### overlap

```python
@overlap.setter
def overlap(value: int) -> None
```

<a id="unreal.TilingConfig.max_size"></a>

#### max_size

```python
@property
def max_size() -> int
```

(int32):  [Read-Write] Maximum tile size (applies only to dynamic size models)

<a id="unreal.TilingConfig.max_size"></a>

#### max_size

```python
@max_size.setter
def max_size(value: int) -> None
```

<a id="unreal.TilingConfig.min_size"></a>

#### min_size

```python
@property
def min_size() -> int
```

(int32):  [Read-Write] Minimum tile size (applies only to dynamic size models)

<a id="unreal.TilingConfig.min_size"></a>

#### min_size

```python
@min_size.setter
def min_size(value: int) -> None
```

<a id="unreal.AbcCompressionSettings"></a>