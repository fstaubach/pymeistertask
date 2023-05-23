from .resource import Resource, ResourceAPI


class TaskRelationship(Resource):
    _repr_attrs = ("id", "owner_id", "target_id", "type")


class TaskRelationshipsAPI(ResourceAPI):
    _resource = TaskRelationship

    def create(self, task_id, data):
        return self._create_object(
            url="/tasks/{task_id}/task_relationships".format(task_id=task_id), data=data
        )

    def delete(self, id):
        return self._delete_object(url="/task_relationships/{id}".format(id=id))

    def filter_by_task(self, task_id):
        return self._get_list(url="/tasks/{task_id}/task_relationships".format(task_id=task_id))
