## TextureGroup Objects

```python
class TextureGroup(EnumBase)
```

warning:: if this is changed: update BaseEngine.ini [SystemSettings] you might have to update the update Game's DefaultEngine.ini [SystemSettings] order and actual name can never change (order is important!) TEXTUREGROUP_Cinematic: should be used for Cinematics which will be baked out and want to have the highest settings

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureGroup.TEXTUREGROUP_WORLD"></a>

#### TEXTUREGROUP\_WORLD

0

<a id="unreal.TextureGroup.TEXTUREGROUP_WORLD_NORMAL_MAP"></a>

#### TEXTUREGROUP\_WORLD\_NORMAL\_MAP

1

<a id="unreal.TextureGroup.TEXTUREGROUP_WORLD_SPECULAR"></a>

#### TEXTUREGROUP\_WORLD\_SPECULAR

2

<a id="unreal.TextureGroup.TEXTUREGROUP_CHARACTER"></a>

#### TEXTUREGROUP\_CHARACTER

3

<a id="unreal.TextureGroup.TEXTUREGROUP_CHARACTER_NORMAL_MAP"></a>

#### TEXTUREGROUP\_CHARACTER\_NORMAL\_MAP

4

<a id="unreal.TextureGroup.TEXTUREGROUP_CHARACTER_SPECULAR"></a>

#### TEXTUREGROUP\_CHARACTER\_SPECULAR

5

<a id="unreal.TextureGroup.TEXTUREGROUP_WEAPON"></a>

#### TEXTUREGROUP\_WEAPON

6

<a id="unreal.TextureGroup.TEXTUREGROUP_WEAPON_NORMAL_MAP"></a>

#### TEXTUREGROUP\_WEAPON\_NORMAL\_MAP

7

<a id="unreal.TextureGroup.TEXTUREGROUP_WEAPON_SPECULAR"></a>

#### TEXTUREGROUP\_WEAPON\_SPECULAR

8

<a id="unreal.TextureGroup.TEXTUREGROUP_VEHICLE"></a>

#### TEXTUREGROUP\_VEHICLE

9

<a id="unreal.TextureGroup.TEXTUREGROUP_VEHICLE_NORMAL_MAP"></a>

#### TEXTUREGROUP\_VEHICLE\_NORMAL\_MAP

10

<a id="unreal.TextureGroup.TEXTUREGROUP_VEHICLE_SPECULAR"></a>

#### TEXTUREGROUP\_VEHICLE\_SPECULAR

11

<a id="unreal.TextureGroup.TEXTUREGROUP_CINEMATIC"></a>

#### TEXTUREGROUP\_CINEMATIC

12

<a id="unreal.TextureGroup.TEXTUREGROUP_EFFECTS"></a>

#### TEXTUREGROUP\_EFFECTS

13

<a id="unreal.TextureGroup.TEXTUREGROUP_EFFECTS_NOT_FILTERED"></a>

#### TEXTUREGROUP\_EFFECTS\_NOT\_FILTERED

14

<a id="unreal.TextureGroup.TEXTUREGROUP_SKYBOX"></a>

#### TEXTUREGROUP\_SKYBOX

15

<a id="unreal.TextureGroup.TEXTUREGROUP_UI"></a>

#### TEXTUREGROUP\_UI

16

<a id="unreal.TextureGroup.TEXTUREGROUP_LIGHTMAP"></a>

#### TEXTUREGROUP\_LIGHTMAP

17

<a id="unreal.TextureGroup.TEXTUREGROUP_RENDER_TARGET"></a>

#### TEXTUREGROUP\_RENDER\_TARGET

18

<a id="unreal.TextureGroup.TEXTUREGROUP_MOBILE_FLATTENED"></a>

#### TEXTUREGROUP\_MOBILE\_FLATTENED

19

<a id="unreal.TextureGroup.TEXTUREGROUP_PROC_BUILDING_FACE"></a>

#### TEXTUREGROUP\_PROC\_BUILDING\_FACE

20: Obsolete - kept for backwards compatibility.

<a id="unreal.TextureGroup.TEXTUREGROUP_PROC_BUILDING_LIGHT_MAP"></a>

#### TEXTUREGROUP\_PROC\_BUILDING\_LIGHT\_MAP

21: Obsolete - kept for backwards compatibility.

<a id="unreal.TextureGroup.TEXTUREGROUP_SHADOWMAP"></a>

#### TEXTUREGROUP\_SHADOWMAP

22

<a id="unreal.TextureGroup.TEXTUREGROUP_COLOR_LOOKUP_TABLE"></a>

#### TEXTUREGROUP\_COLOR\_LOOKUP\_TABLE

23: No compression, no mips.

<a id="unreal.TextureGroup.TEXTUREGROUP_TERRAIN_HEIGHTMAP"></a>

#### TEXTUREGROUP\_TERRAIN\_HEIGHTMAP

24

<a id="unreal.TextureGroup.TEXTUREGROUP_TERRAIN_WEIGHTMAP"></a>

#### TEXTUREGROUP\_TERRAIN\_WEIGHTMAP

25

<a id="unreal.TextureGroup.TEXTUREGROUP_BOKEH"></a>

#### TEXTUREGROUP\_BOKEH

26: Using this TextureGroup triggers special mip map generation code only useful for the BokehDOF post process.

<a id="unreal.TextureGroup.TEXTUREGROUP_IES_LIGHT_PROFILE"></a>

#### TEXTUREGROUP\_IES\_LIGHT\_PROFILE

27: No compression, created on import of a .IES file.

<a id="unreal.TextureGroup.TEXTUREGROUP_PIXELS2D"></a>

#### TEXTUREGROUP\_PIXELS2D

28: Non-filtered, useful for 2D rendering.

<a id="unreal.TextureGroup.TEXTUREGROUP_HIERARCHICAL_LOD"></a>

#### TEXTUREGROUP\_HIERARCHICAL\_LOD

29: Hierarchical LOD generated textures

<a id="unreal.TextureGroup.TEXTUREGROUP_IMPOSTOR"></a>

#### TEXTUREGROUP\_IMPOSTOR

30: Impostor Color Textures

<a id="unreal.TextureGroup.TEXTUREGROUP_IMPOSTOR_NORMAL_DEPTH"></a>

#### TEXTUREGROUP\_IMPOSTOR\_NORMAL\_DEPTH

31: Impostor Normal and Depth, use default compression

<a id="unreal.TextureGroup.TEXTUREGROUP_8_BIT_DATA"></a>

#### TEXTUREGROUP\_8\_BIT\_DATA

32: 8 bit data stored in textures

<a id="unreal.TextureGroup.TEXTUREGROUP_16_BIT_DATA"></a>

#### TEXTUREGROUP\_16\_BIT\_DATA

33: 16 bit data stored in textures

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT01"></a>

#### TEXTUREGROUP\_PROJECT01

34: Project specific group, rename in Engine.ini, [EnumRemap] TEXTUREGROUP_Project**.DisplayName=My Fun Group

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT02"></a>

#### TEXTUREGROUP\_PROJECT02

35

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT03"></a>

#### TEXTUREGROUP\_PROJECT03

36

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT04"></a>

#### TEXTUREGROUP\_PROJECT04

37

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT05"></a>

#### TEXTUREGROUP\_PROJECT05

38

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT06"></a>

#### TEXTUREGROUP\_PROJECT06

39

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT07"></a>

#### TEXTUREGROUP\_PROJECT07

40

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT08"></a>

#### TEXTUREGROUP\_PROJECT08

41

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT09"></a>

#### TEXTUREGROUP\_PROJECT09

42

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT10"></a>

#### TEXTUREGROUP\_PROJECT10

43

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT11"></a>

#### TEXTUREGROUP\_PROJECT11

44

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT12"></a>

#### TEXTUREGROUP\_PROJECT12

45

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT13"></a>

#### TEXTUREGROUP\_PROJECT13

46

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT14"></a>

#### TEXTUREGROUP\_PROJECT14

47

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT15"></a>

#### TEXTUREGROUP\_PROJECT15

48

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT16"></a>

#### TEXTUREGROUP\_PROJECT16

49

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT17"></a>

#### TEXTUREGROUP\_PROJECT17

50

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT18"></a>

#### TEXTUREGROUP\_PROJECT18

51

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT19"></a>

#### TEXTUREGROUP\_PROJECT19

52

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT20"></a>

#### TEXTUREGROUP\_PROJECT20

53

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT21"></a>

#### TEXTUREGROUP\_PROJECT21

54

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT22"></a>

#### TEXTUREGROUP\_PROJECT22

55

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT23"></a>

#### TEXTUREGROUP\_PROJECT23

56

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT24"></a>

#### TEXTUREGROUP\_PROJECT24

57

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT25"></a>

#### TEXTUREGROUP\_PROJECT25

58

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT26"></a>

#### TEXTUREGROUP\_PROJECT26

59

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT27"></a>

#### TEXTUREGROUP\_PROJECT27

60

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT28"></a>

#### TEXTUREGROUP\_PROJECT28

61

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT29"></a>

#### TEXTUREGROUP\_PROJECT29

62

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT30"></a>

#### TEXTUREGROUP\_PROJECT30

63

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT31"></a>

#### TEXTUREGROUP\_PROJECT31

64

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT32"></a>

#### TEXTUREGROUP\_PROJECT32

65

<a id="unreal.TextureAddress"></a>