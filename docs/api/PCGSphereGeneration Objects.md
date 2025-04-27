## PCGSphereGeneration Objects

```python
class PCGSphereGeneration(EnumBase)
```

EPCGSphere Generation

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreatePointsSphere.h

<a id="unreal.PCGSphereGeneration.GEODESIC"></a>

#### GEODESIC

0: Points generated from subdivided equilateral triangles across the sphere's surface.

<a id="unreal.PCGSphereGeneration.ANGLE"></a>

#### ANGLE

1: Points generated radially along longitude and latitude lines to form a sphere with user defined angles.

<a id="unreal.PCGSphereGeneration.SEGMENTS"></a>

#### SEGMENTS

2: Points generated radially along longitude and latitude lines to form a sphere with user defined number of segments.

<a id="unreal.PCGSphereGeneration.RANDOM"></a>

#### RANDOM

3: Points are generated with a uniform distribution on the surface of the sphere.

<a id="unreal.PCGSphereGeneration.POISSON"></a>

#### POISSON

4: Sample points along the sphere's surface with a minimal distance between any given two points.

<a id="unreal.PCGSpherePointOrientation"></a>