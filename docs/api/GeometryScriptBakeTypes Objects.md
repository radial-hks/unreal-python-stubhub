## GeometryScriptBakeTypes Objects

```python
class GeometryScriptBakeTypes(EnumBase)
```

EGeometry Script Bake Types

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

<a id="unreal.GeometryScriptBakeTypes.NONE"></a>

#### NONE

0

<a id="unreal.GeometryScriptBakeTypes.TANGENT_SPACE_NORMAL"></a>

#### TANGENT_SPACE_NORMAL

1: Normals in tangent space

<a id="unreal.GeometryScriptBakeTypes.OBJECT_SPACE_NORMAL"></a>

#### OBJECT_SPACE_NORMAL

2: Interpolated normals in object space

<a id="unreal.GeometryScriptBakeTypes.FACE_NORMAL"></a>

#### FACE_NORMAL

3: Geometric face normals in object space

<a id="unreal.GeometryScriptBakeTypes.BENT_NORMAL"></a>

#### BENT_NORMAL

4: Normals skewed towards the least occluded direction

<a id="unreal.GeometryScriptBakeTypes.POSITION"></a>

#### POSITION

5: Positions in object space

<a id="unreal.GeometryScriptBakeTypes.CURVATURE"></a>

#### CURVATURE

6: Local curvature of the mesh surface

<a id="unreal.GeometryScriptBakeTypes.AMBIENT_OCCLUSION"></a>

#### AMBIENT_OCCLUSION

7: Ambient occlusion sampled across the hemisphere

<a id="unreal.GeometryScriptBakeTypes.TEXTURE"></a>

#### TEXTURE

8: Transfer a given texture

<a id="unreal.GeometryScriptBakeTypes.MULTI_TEXTURE"></a>

#### MULTI_TEXTURE

9: Transfer a texture per material ID

<a id="unreal.GeometryScriptBakeTypes.VERTEX_COLOR"></a>

#### VERTEX_COLOR

10: Interpolated vertex colors

<a id="unreal.GeometryScriptBakeTypes.MATERIAL_ID"></a>

#### MATERIAL_ID

11: Material IDs as unique colors

<a id="unreal.GeometryScriptBakeTypes.CONSTANT"></a>

#### CONSTANT

12: Constant value

<a id="unreal.GeometryScriptBakeTypes.UV_SHELL"></a>

#### UV_SHELL

13: UV Shell

<a id="unreal.GeometryScriptBakeOutputMode"></a>