## LightCollection Objects

```python
class LightCollection(StructBase)
```

Light Collection

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: TOD_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``light_actors`` (Array[Actor]):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "TOD", DisplayName = "灯光Actor")
  TMap<AActor*, FLightCompIntensity> LightActors;
- ``points_lights`` (Map[PointLight, float]):  [Read-Write]
- ``rect_lights`` (Map[RectLight, float]):  [Read-Write]
- ``spot_light`` (Map[SpotLight, float]):  [Read-Write]

<a id="unreal.LightCollection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(spot_light: Map[SpotLight, float] = {},
             points_lights: Map[PointLight, float] = {},
             rect_lights: Map[RectLight, float] = {},
             light_actors: Array[Actor] = []) -> None
```

<a id="unreal.LightCollection.spot_light"></a>

#### spot\_light

```python
@property
def spot_light() -> Map[SpotLight, float]
```

(Map[SpotLight, float]):  [Read-Write]

<a id="unreal.LightCollection.spot_light"></a>

#### spot\_light

```python
@spot_light.setter
def spot_light(value: Map[SpotLight, float]) -> None
```

<a id="unreal.LightCollection.points_lights"></a>

#### points\_lights

```python
@property
def points_lights() -> Map[PointLight, float]
```

(Map[PointLight, float]):  [Read-Write]

<a id="unreal.LightCollection.points_lights"></a>

#### points\_lights

```python
@points_lights.setter
def points_lights(value: Map[PointLight, float]) -> None
```

<a id="unreal.LightCollection.rect_lights"></a>

#### rect\_lights

```python
@property
def rect_lights() -> Map[RectLight, float]
```

(Map[RectLight, float]):  [Read-Write]

<a id="unreal.LightCollection.rect_lights"></a>

#### rect\_lights

```python
@rect_lights.setter
def rect_lights(value: Map[RectLight, float]) -> None
```

<a id="unreal.LightCollection.light_actors"></a>

#### light\_actors

```python
@property
def light_actors() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "TOD", DisplayName = "灯光Actor")
TMap<AActor*, FLightCompIntensity> LightActors;

<a id="unreal.LightCollection.light_actors"></a>

#### light\_actors

```python
@light_actors.setter
def light_actors(value: Array[Actor]) -> None
```

<a id="unreal.TimeSectionHideTag"></a>