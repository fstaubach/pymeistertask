from .resource import Resource, ResourceAPI


class ChecklistItem(Resource):
    _repr_attrs = ("id", "checklist_id", "name")


class ChecklistItemsAPI(ResourceAPI):
    _resource = ChecklistItem

    def create(self, checklist_id, data):
        return self._create_object(
            url="/checklists/{checklist_id}/checklist_items".format(checklist_id=checklist_id), data=data
        )

    def get(self, id):
        return self._get_object(url="/checklist_items/{id}".format(id=id))

    def update(self, id, data):
        return self._update_object(url="/checklist_items/{id}".format(id=id), data=data)

    def delete(self, id):
        return self._delete_object(url="/checklist_items/{id}".format(id=id))

    def filter_by_task(self, task_id, **kwargs):
        return self._get_list(url="/tasks/{task_id}/checklist_items".format(task_id=task_id), **kwargs)

    def filter_by_checklist(self, checklist_id, **kwargs):
        return self._get_list(url="/checklists/{checklist_id}/checklist_items".format(checklist_id=checklist_id), **kwargs)
