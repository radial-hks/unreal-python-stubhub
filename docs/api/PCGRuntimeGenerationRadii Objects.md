## PCGRuntimeGenerationRadii Objects

```python
class PCGRuntimeGenerationRadii(StructBase)
```

PCGRuntime Generation Radii

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cleanup_radius_multiplier`` (double):  [Read-Write] Multiplier on the GenerationRadius to control the distance at which runtime generated components will be cleaned up. Applied per grid size.
- ``generation_radius`` (double):  [Read-Write] The distance (in centimeters) at which the component will be considered for generation by the RuntimeGenerationScheduler. For partitioned components, this also acts as the unbounded generation radius.
- ``generation_radius102400`` (double):  [Read-Write]
- ``generation_radius12800`` (double):  [Read-Write]
- ``generation_radius1600`` (double):  [Read-Write]
- ``generation_radius204800`` (double):  [Read-Write]
- ``generation_radius25600`` (double):  [Read-Write]
- ``generation_radius3200`` (double):  [Read-Write]
- ``generation_radius400`` (double):  [Read-Write]
- ``generation_radius51200`` (double):  [Read-Write]
- ``generation_radius6400`` (double):  [Read-Write]
- ``generation_radius800`` (double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.__init__"></a>

#### \_\_init\_\_

```python
def __init__(generation_radius: float = 0.000000,
             generation_radius400: float = 0.000000,
             generation_radius800: float = 0.000000,
             generation_radius1600: float = 0.000000,
             generation_radius3200: float = 0.000000,
             generation_radius6400: float = 0.000000,
             generation_radius12800: float = 0.000000,
             generation_radius25600: float = 0.000000,
             generation_radius51200: float = 0.000000,
             generation_radius102400: float = 0.000000,
             generation_radius204800: float = 0.000000,
             cleanup_radius_multiplier: float = 0.000000) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius"></a>

#### generation\_radius

```python
@property
def generation_radius() -> float
```

(double):  [Read-Write] The distance (in centimeters) at which the component will be considered for generation by the RuntimeGenerationScheduler. For partitioned components, this also acts as the unbounded generation radius.

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius"></a>

#### generation\_radius

```python
@generation_radius.setter
def generation_radius(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius400"></a>

#### generation\_radius400

```python
@property
def generation_radius400() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius400"></a>

#### generation\_radius400

```python
@generation_radius400.setter
def generation_radius400(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius800"></a>

#### generation\_radius800

```python
@property
def generation_radius800() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius800"></a>

#### generation\_radius800

```python
@generation_radius800.setter
def generation_radius800(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius1600"></a>

#### generation\_radius1600

```python
@property
def generation_radius1600() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius1600"></a>

#### generation\_radius1600

```python
@generation_radius1600.setter
def generation_radius1600(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius3200"></a>

#### generation\_radius3200

```python
@property
def generation_radius3200() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius3200"></a>

#### generation\_radius3200

```python
@generation_radius3200.setter
def generation_radius3200(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius6400"></a>

#### generation\_radius6400

```python
@property
def generation_radius6400() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius6400"></a>

#### generation\_radius6400

```python
@generation_radius6400.setter
def generation_radius6400(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius12800"></a>

#### generation\_radius12800

```python
@property
def generation_radius12800() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius12800"></a>

#### generation\_radius12800

```python
@generation_radius12800.setter
def generation_radius12800(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius25600"></a>

#### generation\_radius25600

```python
@property
def generation_radius25600() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius25600"></a>

#### generation\_radius25600

```python
@generation_radius25600.setter
def generation_radius25600(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius51200"></a>

#### generation\_radius51200

```python
@property
def generation_radius51200() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius51200"></a>

#### generation\_radius51200

```python
@generation_radius51200.setter
def generation_radius51200(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius102400"></a>

#### generation\_radius102400

```python
@property
def generation_radius102400() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius102400"></a>

#### generation\_radius102400

```python
@generation_radius102400.setter
def generation_radius102400(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius204800"></a>

#### generation\_radius204800

```python
@property
def generation_radius204800() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGRuntimeGenerationRadii.generation_radius204800"></a>

#### generation\_radius204800

```python
@generation_radius204800.setter
def generation_radius204800(value: float) -> None
```

<a id="unreal.PCGRuntimeGenerationRadii.cleanup_radius_multiplier"></a>

#### cleanup\_radius\_multiplier

```python
@property
def cleanup_radius_multiplier() -> float
```

(double):  [Read-Write] Multiplier on the GenerationRadius to control the distance at which runtime generated components will be cleaned up. Applied per grid size.

<a id="unreal.PCGRuntimeGenerationRadii.cleanup_radius_multiplier"></a>

#### cleanup\_radius\_multiplier

```python
@cleanup_radius_multiplier.setter
def cleanup_radius_multiplier(value: float) -> None
```

<a id="unreal.EnumSelector"></a>