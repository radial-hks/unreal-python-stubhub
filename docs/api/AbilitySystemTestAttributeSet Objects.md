## AbilitySystemTestAttributeSet Objects

```python
class AbilitySystemTestAttributeSet(AttributeSet)
```

Ability System Test Attribute Set

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilitySystemTestAttributeSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``armor_damage_reduction`` (float):  [Read-Write]
- ``crit_chance`` (float):  [Read-Write]
- ``crit_multiplier`` (float):  [Read-Write]
- ``damage`` (float):  [Read-Write] This Damage is just used for applying negative health mods. Its not a 'persistent' attribute. // You can't make a GameplayEffect 'powered' by Damage (Its transient)
- ``dodge_chance`` (float):  [Read-Write]
- ``health`` (float):  [Read-Write] You can't make a GameplayEffect modify Health Directly (go through)
- ``life_steal`` (float):  [Read-Write]
- ``mana`` (GameplayAttributeData):  [Read-Write]
- ``max_health`` (float):  [Read-Write] NOTE ON MUTABLE:
  This is only done so that UAbilitySystemTestAttributeSet can be initialized directly in GameplayEffectsTest.cpp without doing a const_cast in 100+ places.
  Mutable is not required and should never be used on normal attribute sets.
     // You can't make a GameplayEffect modify Health Directly (go through)
- ``max_mana`` (float):  [Read-Write]
- ``no_stack_attribute`` (float):  [Read-Write]
- ``physical_damage`` (float):  [Read-Write] This Attribute is the actual physical damage for this actor. It will power physical based GameplayEffects
- ``spell_damage`` (float):  [Read-Write] This Attribute is the actual spell damage for this actor. It will power spell based GameplayEffects
- ``stacking_attribute1`` (float):  [Read-Write]
- ``stacking_attribute2`` (float):  [Read-Write]
- ``strength`` (float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.max_health"></a>

#### max\_health

```python
@property
def max_health() -> float
```

(float):  [Read-Write] NOTE ON MUTABLE:
This is only done so that UAbilitySystemTestAttributeSet can be initialized directly in GameplayEffectsTest.cpp without doing a const_cast in 100+ places.
Mutable is not required and should never be used on normal attribute sets.
   // You can't make a GameplayEffect modify Health Directly (go through)

<a id="unreal.AbilitySystemTestAttributeSet.max_health"></a>

#### max\_health

```python
@max_health.setter
def max_health(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.health"></a>

#### health

```python
@property
def health() -> float
```

(float):  [Read-Write] You can't make a GameplayEffect modify Health Directly (go through)

<a id="unreal.AbilitySystemTestAttributeSet.health"></a>

#### health

```python
@health.setter
def health(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.mana"></a>

#### mana

```python
@property
def mana() -> GameplayAttributeData
```

(GameplayAttributeData):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.mana"></a>

#### mana

```python
@mana.setter
def mana(value: GameplayAttributeData) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.max_mana"></a>

#### max\_mana

```python
@property
def max_mana() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.max_mana"></a>

#### max\_mana

```python
@max_mana.setter
def max_mana(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.damage"></a>

#### damage

```python
@property
def damage() -> float
```

(float):  [Read-Write] This Damage is just used for applying negative health mods. Its not a 'persistent' attribute. // You can't make a GameplayEffect 'powered' by Damage (Its transient)

<a id="unreal.AbilitySystemTestAttributeSet.damage"></a>

#### damage

```python
@damage.setter
def damage(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.spell_damage"></a>

#### spell\_damage

```python
@property
def spell_damage() -> float
```

(float):  [Read-Write] This Attribute is the actual spell damage for this actor. It will power spell based GameplayEffects

<a id="unreal.AbilitySystemTestAttributeSet.spell_damage"></a>

#### spell\_damage

```python
@spell_damage.setter
def spell_damage(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.physical_damage"></a>

#### physical\_damage

```python
@property
def physical_damage() -> float
```

(float):  [Read-Write] This Attribute is the actual physical damage for this actor. It will power physical based GameplayEffects

<a id="unreal.AbilitySystemTestAttributeSet.physical_damage"></a>

#### physical\_damage

```python
@physical_damage.setter
def physical_damage(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.crit_chance"></a>

#### crit\_chance

```python
@property
def crit_chance() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.crit_chance"></a>

#### crit\_chance

```python
@crit_chance.setter
def crit_chance(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.crit_multiplier"></a>

#### crit\_multiplier

```python
@property
def crit_multiplier() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.crit_multiplier"></a>

#### crit\_multiplier

```python
@crit_multiplier.setter
def crit_multiplier(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.armor_damage_reduction"></a>

#### armor\_damage\_reduction

```python
@property
def armor_damage_reduction() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.armor_damage_reduction"></a>

#### armor\_damage\_reduction

```python
@armor_damage_reduction.setter
def armor_damage_reduction(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.dodge_chance"></a>

#### dodge\_chance

```python
@property
def dodge_chance() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.dodge_chance"></a>

#### dodge\_chance

```python
@dodge_chance.setter
def dodge_chance(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.life_steal"></a>

#### life\_steal

```python
@property
def life_steal() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.life_steal"></a>

#### life\_steal

```python
@life_steal.setter
def life_steal(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.stacking_attribute1"></a>

#### stacking\_attribute1

```python
@property
def stacking_attribute1() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.stacking_attribute1"></a>

#### stacking\_attribute1

```python
@stacking_attribute1.setter
def stacking_attribute1(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.stacking_attribute2"></a>

#### stacking\_attribute2

```python
@property
def stacking_attribute2() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.stacking_attribute2"></a>

#### stacking\_attribute2

```python
@stacking_attribute2.setter
def stacking_attribute2(value: float) -> None
```

<a id="unreal.AbilitySystemTestAttributeSet.no_stack_attribute"></a>

#### no\_stack\_attribute

```python
@property
def no_stack_attribute() -> float
```

(float):  [Read-Write]

<a id="unreal.AbilitySystemTestAttributeSet.no_stack_attribute"></a>

#### no\_stack\_attribute

```python
@no_stack_attribute.setter
def no_stack_attribute(value: float) -> None
```

<a id="unreal.AbilitySystemTestPawn"></a>