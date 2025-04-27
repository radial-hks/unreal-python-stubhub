## PrimaryAssetCookRule Objects

```python
class PrimaryAssetCookRule(EnumBase)
```

Rule about when to cook/ship a primary asset

**C++ Source:**

- **Module**: Engine
- **File**: AssetManagerTypes.h

<a id="unreal.PrimaryAssetCookRule.UNKNOWN"></a>

#### UNKNOWN

0: Nothing is known about this asset specifically. It will cook in both Development and Production if something else depends on it.

<a id="unreal.PrimaryAssetCookRule.NEVER_COOK"></a>

#### NEVER_COOK

1: Asset should never be cooked/shipped in any situation. An error will be generated if something depends on it.

<a id="unreal.PrimaryAssetCookRule.PRODUCTION_NEVER_COOK"></a>

#### PRODUCTION_NEVER_COOK

2: Asset will be cooked in development if something else depends on it, but will never be cooked in a production build.

<a id="unreal.PrimaryAssetCookRule.DEVELOPMENT_COOK"></a>

#### DEVELOPMENT_COOK

2: Legacy name equivalent to Production Never Cook

<a id="unreal.PrimaryAssetCookRule.DEVELOPMENT_ALWAYS_PRODUCTION_NEVER_COOK"></a>

#### DEVELOPMENT_ALWAYS_PRODUCTION_NEVER_COOK

3: Asset will always be cooked in development, but should never be cooked in a production build.

<a id="unreal.PrimaryAssetCookRule.DEVELOPMENT_ALWAYS_COOK"></a>

#### DEVELOPMENT_ALWAYS_COOK

3: Legacy name equivalent to DevelopmentAlwaysProductionNeverCook

<a id="unreal.PrimaryAssetCookRule.DEVELOPMENT_ALWAYS_PRODUCTION_UNKNOWN_COOK"></a>

#### DEVELOPMENT_ALWAYS_PRODUCTION_UNKNOWN_COOK

4: Asset will always be cooked in development; nothing is known about whether it should cook in Production. It will cook
in production if something else depends on it.

<a id="unreal.PrimaryAssetCookRule.ALWAYS_COOK"></a>

#### ALWAYS_COOK

5: Asset will always be cooked, in both production and development.

<a id="unreal.BoneFilterActionOption"></a>