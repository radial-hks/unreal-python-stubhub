## RigVMFunction_NoiseFloat Objects

```python
class RigVMFunction_NoiseFloat(RigVMFunction_MathBase)
```

Generates a float through a noise fluctuation process between a min and a max through speed

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Noise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency`` (float):  [Read-Write]
- ``maximum`` (float):  [Read-Write]
- ``minimum`` (float):  [Read-Write]
- ``result`` (float):  [Read-Write]
- ``speed`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseFloat.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             speed: float = 0.000000,
             frequency: float = 0.000000,
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_NoiseFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseFloat.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseFloat.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseFloat.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseFloat.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseFloat.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseFloat.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseFloat.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseFloat.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseFloat.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_NoiseFloat"></a>