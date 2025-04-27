## GameplayTask_ClaimResource Objects

```python
class GameplayTask_ClaimResource(GameplayTask)
```

Gameplay Task Claim Resource

**C++ Source:**

- **Module**: GameplayTasks
- **File**: GameplayTask_ClaimResource.h

<a id="unreal.GameplayTask_ClaimResource.claim_resources"></a>

#### claim_resources

```python
@classmethod
def claim_resources(
        cls,
        task_owner: GameplayTaskOwnerInterface,
        resource_classes: Array[Class],
        priority: int = 192,
        task_instance_name: Name = "None") -> GameplayTask_ClaimResource
```

X.claim_resources(task_owner, resource_classes, priority=192, task_instance_name="None") -> GameplayTask_ClaimResource
Claim Resources

Args:
    task_owner (GameplayTaskOwnerInterface): 
    resource_classes (Array[type(Class)]): 
    priority (uint8): 
    task_instance_name (Name): 

Returns:
    GameplayTask_ClaimResource:

<a id="unreal.GameplayTask_ClaimResource.claim_resource"></a>

#### claim_resource

```python
@classmethod
def claim_resource(
        cls,
        task_owner: GameplayTaskOwnerInterface,
        resource_class: Class,
        priority: int = 192,
        task_instance_name: Name = "None") -> GameplayTask_ClaimResource
```

X.claim_resource(task_owner, resource_class, priority=192, task_instance_name="None") -> GameplayTask_ClaimResource
Claim Resource

Args:
    task_owner (GameplayTaskOwnerInterface): 
    resource_class (type(Class)): 
    priority (uint8): 
    task_instance_name (Name): 

Returns:
    GameplayTask_ClaimResource:

<a id="unreal.GameplayTask_SpawnActor"></a>