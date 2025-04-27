## InterchangeMeshCollision Objects

```python
class InterchangeMeshCollision(EnumBase)
```

EInterchange Mesh Collision

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeMeshDefinitions.h

<a id="unreal.InterchangeMeshCollision.BOX"></a>

#### BOX

0: Generates a new box collision mesh encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.SPHERE"></a>

#### SPHERE

1: Generates a new sphere collision mesh encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.CAPSULE"></a>

#### CAPSULE

2: Generates a new capsule collision mesh encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.CONVEX10DOP_X"></a>

#### CONVEX10DOP_X

3: Generates a new axis-aligned box collision mesh with the 4 X-axis aligned edges beveled (10 total sides) encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.CONVEX10DOP_Y"></a>

#### CONVEX10DOP_Y

4: Generates a new axis-aligned box collision mesh with the 4 Y-axis aligned edges beveled (10 total sides) encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.CONVEX10DOP_Z"></a>

#### CONVEX10DOP_Z

5: Generates a new axis-aligned box collision mesh with the 4 Z-axis aligned edges beveled (10 total sides) encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.CONVEX18DOP"></a>

#### CONVEX18DOP

6: Generates a new axis-aligned box collision mesh with all edges beveled (18 total sides) encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.CONVEX26DOP"></a>

#### CONVEX26DOP

7: Generates a new axis-aligned box collision mesh with all edges and corners beveled (26 total sides) encompassing the static mesh

<a id="unreal.InterchangeMeshCollision.NONE"></a>

#### NONE

255: Generates no collisions, but continue to import custom collisions if the file has ones

<a id="unreal.InterchangeTextureWrapMode"></a>