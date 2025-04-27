## SkinCacheUsage Objects

```python
class SkinCacheUsage(EnumBase)
```

ESkin Cache Usage

**C++ Source:**

- **Module**: Engine
- **File**: SkinnedAssetCommon.h

<a id="unreal.SkinCacheUsage.AUTO"></a>

#### AUTO

0: Auto will defer to child or global behavior based on context

<a id="unreal.SkinCacheUsage.DISABLED"></a>

#### DISABLED

255: Mesh will not use the skin cache. However, if Support Ray Tracing is enabled on the mesh, the skin cache will still be used for Ray Tracing updates

<a id="unreal.SkinCacheUsage.ENABLED"></a>

#### ENABLED

1: Mesh will use the skin cache

<a id="unreal.PhysBodyOp"></a>